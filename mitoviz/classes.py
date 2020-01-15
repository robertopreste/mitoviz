#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
from collections import defaultdict
from typing import List, Union

import pandas as pd
import vcfpy

from .constants import COLORS, NT_LENGTHS, TEXT_HA, TEXT_VA, TEXT_Y, TYPES
from .utils import convert_hf, convert_nt


class Locus:
    """ Class referring to a single mt locus.

    Used to create the base mitochondrial plot on which variants will
    be added on a separate layer.

    Attributes:
        name: name of the locus
        index: index of the locus in the mt genome (dloop = 0, tf = 1, etc.)
    """

    def __init__(self, name: str, index: int):
        self.name = name
        self.index = index

    @property
    def loc_type(self) -> str:
        """ The locus type (regulatory, coding, rRNA, tRNA). """
        return TYPES[self.index]

    @property
    def width(self) -> float:
        """ The relative width of the locus from its length in
        nucleotides.
        """
        return convert_nt(NT_LENGTHS[self.index])

    @property
    def theta(self) -> float:
        """ The position at which the locus will be plotted. """
        if self.index == 0:
            return 0.0
        elif self.index == 1:
            return convert_nt(NT_LENGTHS[0])/2 + self.width/2
        return (convert_nt(NT_LENGTHS[0])/2 + self.width/2
                + sum(map(convert_nt, NT_LENGTHS[1:self.index])))

    @property
    def color(self) -> str:
        """ The locus-type-specific color. """
        return COLORS[self.loc_type]

    @property
    def text_ha(self) -> str:
        """ The horizontal alignment for the text label. """
        return TEXT_HA[self.index]

    @property
    def text_va(self) -> str:
        """ The vertical alignment for the text label. """
        return TEXT_VA[self.index]

    @property
    def text_y(self) -> float:
        """ The y position for the text label. """
        return TEXT_Y[self.index]

    def __repr__(self):
        return "{}(name={}, index={})".format(
            self.__class__.__name__, self.name, self.index
        )


class Variant:
    """ Class used to store a given variant.

    Attributes:
        reference: reference allele of the variant
        position: position of the variant
        alternate: alternate allele of the variant
        hf: heteroplasmic fraction of the variant
    """

    def __init__(self,
                 reference: str,
                 position: int,
                 alternate: Union[str, vcfpy.Substitution],
                 hf: float):
        self.reference = reference
        self.position = position
        self.alternate = alternate
        self.hf = hf

    def _is_deletion(self) -> bool:
        """ Check whether the current variant refers to a deletion. """
        # e.g. ref CTG | alt C
        if isinstance(self.alternate, vcfpy.Substitution):
            return self.alternate.type == "DEL"
        return len(self.reference) > len(self.alternate)

    def _is_insertion(self) -> bool:
        """ Check whether the current variant refers to an insertion. """
        # e.g. ref C | alt CTG
        if isinstance(self.alternate, vcfpy.Substitution):
            return self.alternate.type == "INS"
        return len(self.reference) < len(self.alternate)

    @property
    def label(self) -> str:
        """ Create the variant label for deletions, insertions and SNPs. """
        alternate = (self.alternate.value
                     if isinstance(self.alternate, vcfpy.Substitution)
                     else self.alternate)
        if self._is_deletion():
            label = "{}d".format(int(self.position) + 1)
        elif self._is_insertion():
            label = "{}.{}".format(
                self.position, alternate[len(self.reference):]
            )
        else:
            label = "{}{}>{}".format(self.position, self.reference, alternate)

        return label

    @property
    def pos_x(self) -> float:
        """ The x position of the variant on the mitochondrial genome plot. """
        return convert_nt(self.position)

    @property
    def pos_y(self) -> float:
        """ The y position of the variant on the mitochondrial genome plot,
        based on its heteroplasmic fraction.
        """
        return 20 + convert_hf(self.hf)

    def __repr__(self):
        return "{}(reference={}, position={}, alternate={}, hf={})".format(
            self.__class__.__name__, self.reference, self.position,
            self.alternate, self.hf
        )


class VcfParser:
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
    def samples(self):
        return self._reader.header.samples.names

    @property
    def variants(self):
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
                    variants = [Variant(record.REF, record.POS, alt,
                                        self.parse_call(call, i))
                                for i, alt in enumerate(record.ALT)]
                    self._variants[sample].extend(variants)
            else:  # single sample without name
                sample = "MITOVIZ001"
                variants = [Variant(record.REF, record.POS, alt, 0.5)
                            for alt in record.ALT]
                self._variants[sample].extend(variants)

    def __repr__(self):
        return "{}(vcf_in={})".format(
            self.__class__.__name__, self.vcf_in
        )


class DataFrameParser:
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
    def has_sample(self):
        """ Return whether the SAMPLE column is available in the DataFrame. """
        return self.sample_col in self.df_in.columns

    @property
    def variants(self):
        return self._variants

    def parse_variants(self):
        """ Read the variants from the input DataFrame and parse them in the
        required format.

        Variants are stored in a per-sample fashion, in the self.variants
        dictionary.
        """
        for record in self.df_in.itertuples():
            rec = record._asdict()
            sample = rec[self.sample_col] if self.has_sample else "MITOVIZ001"
            hf = rec[self.hf_col] if self.has_hf else 0.5
            variant = Variant(rec[self.ref_col], rec[self.pos_col],
                              rec[self.alt_col], hf)
            self._variants[sample].append(variant)

    def __repr__(self):
        return ("{}(pos_col={}, ref_col={}, alt_col={}, "
                "sample_col={}, hf_col={})").format(
            self.__class__.__name__, self.pos_col, self.ref_col,
            self.alt_col, self.sample_col, self.hf_col
        )
