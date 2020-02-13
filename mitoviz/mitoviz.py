#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os
from typing import Optional

import matplotlib.pyplot as plt
import pandas as pd

from mitoviz.parsers import _DataFrameParser, _TabularParser, _VcfParser
from mitoviz.plot import _plot_variants
from mitoviz.utils import parse_path


def plot_vcf(in_vcf: str,
             sample: Optional[str] = None,
             save: bool = False,
             output: Optional[str] = None,
             labels: bool = False,
             legend: bool = False) -> None:
    """ Plot variants from the given VCF file.

    Args:
        in_vcf: path of the input VCF file
        sample: specific sample to plot (defaults to all available samples)
        save: if true, the final plot will be saved to a file [default: False]
        output: path of the output file where the plot will be saved
        labels: if true, add a label for each variant shown [default: False]
        legend: if true, add a legend for loci colors in the plot
            [default: False]
    """
    vcf = _VcfParser(in_vcf)
    variants_per_sample = vcf.variants

    if sample:
        _plot_variants(sample, variants_per_sample[sample], labels, legend)
        if save:
            dirname, name, ext = parse_path(output)
            if name == "":
                name = sample
            plt.savefig(os.path.join(dirname, f"{name}{ext}"))
            plt.close()
    else:
        for i, (sample, variants) in enumerate(variants_per_sample.items(),
                                               start=1):
            _plot_variants(sample, variants, labels, legend)
            if save:
                dirname, name, ext = parse_path(output)
                if name == "":
                    name = sample
                    plt.savefig(os.path.join(dirname, f"{name}{ext}"))
                elif len(variants_per_sample) == 1:
                    plt.savefig(os.path.join(dirname, f"{name}{ext}"))
                else:
                    plt.savefig(os.path.join(dirname, f"{name}_{i}{ext}"))
                plt.close()

    return None


def plot_df(in_df: pd.DataFrame,
            sample: Optional[str] = None,
            save: bool = False,
            output: Optional[str] = None,
            labels: bool = False,
            legend: bool = False,
            pos_col: str = "POS",
            ref_col: str = "REF",
            alt_col: str = "ALT",
            sample_col: str = "SAMPLE",
            hf_col: str = "HF") -> None:
    """ Plot variant from the given pandas DataFrame.

    Args:
        in_df: input pandas DataFrame
        sample: specific sample to plot (defaults to all available samples)
        save: if true, the final plot will be saved to a file [default: False]
        output: path of the output file where the plot will be saved
        labels: if true, add a label for each variant shown [default: False]
        legend: if true, add a legend for loci colors in the plot
            [default: False]
        pos_col: column name for the variant position
        ref_col: column name for the variant reference allele
        alt_col: column name for the variant alternate allele
        sample_col: column name for the variant sample
        hf_col: column name for the variant heteroplasmic fraction
    """
    df = _DataFrameParser(in_df,
                          pos_col=pos_col,
                          ref_col=ref_col,
                          alt_col=alt_col,
                          sample_col=sample_col,
                          hf_col=hf_col)
    variants_per_sample = df.variants

    if sample:
        _plot_variants(sample, variants_per_sample[sample], labels, legend)
        if save:
            dirname, name, ext = parse_path(output)
            if name == "":
                name = sample
            plt.savefig(os.path.join(dirname, f"{name}{ext}"))
            plt.close()
    else:
        for i, (sample, variants) in enumerate(variants_per_sample.items(),
                                               start=1):
            _plot_variants(sample, variants, labels, legend)
            if save:
                dirname, name, ext = parse_path(output)
                if name == "":
                    name = sample
                    plt.savefig(os.path.join(dirname, f"{name}{ext}"))
                elif len(variants_per_sample) == 1:
                    plt.savefig(os.path.join(dirname, f"{name}{ext}"))
                else:
                    plt.savefig(os.path.join(dirname, f"{name}_{i}{ext}"))
                plt.close()

    return None


def plot_table(in_table: str,
               sep: str = ",",
               sample: Optional[str] = None,
               save: bool = False,
               output: Optional[str] = None,
               labels: bool = False,
               legend: bool = False,
               pos_col: str = "POS",
               ref_col: str = "REF",
               alt_col: str = "ALT",
               sample_col: str = "SAMPLE",
               hf_col: str = "HF",
               **kwargs) -> None:
    """ Plot variants from the given tabular file.

    Args:
        in_table: path of the input tabular file
        sep: column delimiter used [default: ',']
        sample: specific sample to plot (defaults to all available samples)
        save: if true, the final plot will be saved to a file [default: False]
        output: path of the output file where the plot will be saved
        labels: if true, add a label for each variant shown [default: False]
        legend: if true, add a legend for loci colors in the plot
            [default: False]
        pos_col: column name for the variant position
        ref_col: column name for the variant reference allele
        alt_col: column name for the variant alternate allele
        sample_col: column name for the variant sample
        hf_col: column name for the variant heteroplasmic fraction
        **kwargs: additional arguments passed to pandas.read_table()
    """
    table = _TabularParser(in_table, sep=sep, **kwargs)
    plot_df(table.df,
            sample=sample,
            save=save,
            output=output,
            labels=labels,
            legend=legend,
            pos_col=pos_col,
            ref_col=ref_col,
            alt_col=alt_col,
            sample_col=sample_col,
            hf_col=hf_col)

    return None
