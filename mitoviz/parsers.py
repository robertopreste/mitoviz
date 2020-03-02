#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
from collections import defaultdict
from typing import List

import pandas as pd
import vcfpy

from mitoviz.variant import _Variant


class _VcfParser:
    """ Class to read and parse the given VCF file.

    Attributes
        vcf_in: path of the input VCF file
    """

    def __init__(self, vcf_in: str):
        self.vcf_in = vcf_in
        self._variants = defaultdict(list)
        self._reader = vcfpy.Reader.from_path(vcf_in)
        self.parse_variants()

    @property
    def samples(self) -> List[str]:
        return self._reader.header.samples.names

    @property
    def variants(self) -> dict:
        return self._variants

    @staticmethod
    def parse_call(call: vcfpy.Call, i: int) -> float:
        """ Parse the vcfpy.Call to get the i-th value for HF; if not present,
        return 0.5.

        Args:
            call: input call to parse
            i: i-th element of HF to get

        Returns:
            either the required i-th element of HF or 0.5
        """
        hf_list = call.data.get("HF", [])
        if hf_list:
            return hf_list[i]
        return 0.5

    def parse_variants(self):
        """ Read the variants from the input VCF file and parse them in the
        required format.

        Variants are stored in a per-sample fashion, in the self.variants
        dictionary.
        """
        for record in self._reader:
            if self.samples:  # sample name is specified
                for sample, call in record.call_for_sample.items():
                    variants = [_Variant(record.REF, record.POS, alt,
                                         self.parse_call(call, i))
                                for i, alt in enumerate(record.ALT)]
                    self._variants[sample].extend(variants)
            else:  # single sample without name
                sample = "MITOVIZ001"
                variants = [_Variant(record.REF, record.POS, alt, 0.5)
                            for alt in record.ALT]
                self._variants[sample].extend(variants)

    def __repr__(self):
        return "{}(vcf_in={})".format(
            self.__class__.__name__, self.vcf_in
        )


class _DataFrameParser:
    """ Class to read and parse a given pandas DataFrame.

    Attributes:
        df_in: path of the input pandas DataFrame
        pos_col: column name for the variant position
        ref_col: column name for the variant reference allele
        alt_col: column name for the variant alternate allele
        sample_col: column name for the variant sample
        hf_col: column name for the variant heteroplasmic fraction
    """

    def __init__(self,
                 df_in: pd.DataFrame,
                 pos_col: str = "POS",
                 ref_col: str = "REF",
                 alt_col: str = "ALT",
                 sample_col: str = "SAMPLE",
                 hf_col: str = "HF"):
        self.df_in = df_in
        self.pos_col = pos_col
        self.ref_col = ref_col
        self.alt_col = alt_col
        self.sample_col = sample_col
        self.hf_col = hf_col
        self._variants = defaultdict(list)
        self.parse_variants()

    @property
    def has_hf(self) -> bool:
        """ Return whether the HF column is available in the DataFrame. """
        return self.hf_col in self.df_in.columns

    @property
    def has_sample(self) -> bool:
        """ Return whether the SAMPLE column is available in the DataFrame. """
        return self.sample_col in self.df_in.columns

    @property
    def variants(self) -> dict:
        return self._variants

    def parse_variants(self):
        """ Read the variants from the input DataFrame and parse them in the
        required format.

        Variants are stored in a per-sample fashion, in the self.variants
        dictionary.
        """
        if self.has_hf:
            self.df_in[self.hf_col] = self.df_in[self.hf_col].astype(float)
        for record in self.df_in.itertuples():
            rec = record._asdict()
            sample = rec[self.sample_col] if self.has_sample else "MITOVIZ001"
            hf = rec[self.hf_col] if self.has_hf else 0.5
            variant = _Variant(rec[self.ref_col], rec[self.pos_col],
                               rec[self.alt_col], hf)
            self._variants[sample].append(variant)

    def __repr__(self):
        return ("{}(pos_col={}, ref_col={}, alt_col={}, "
                "sample_col={}, hf_col={})").format(
            self.__class__.__name__, self.pos_col, self.ref_col,
            self.alt_col, self.sample_col, self.hf_col
        )


class _TabularParser:
    """ Class to read and parse a given tabular generic file.

    Attributes:
        table_in: path of the input tabular file
        sep: column delimiter used
        **kwargs: additional arguments passed to pandas.read_table()
    """

    def __init__(self,
                 table_in: str,
                 sep: str = ",",
                 **kwargs):
        self.table_in = table_in
        self.sep = sep
        self.kwargs = kwargs

    @property
    def df(self) -> pd.DataFrame:
        try:
            df_in = pd.read_table(self.table_in, sep=self.sep, engine="python",
                                  **self.kwargs)
        except TypeError as e:
            raise TypeError(e)
        return df_in

    def __repr__(self):
        return "{}(table_in={}, sep={!r})".format(self.__class__.__name__,
                                                  self.table_in, self.sep)
