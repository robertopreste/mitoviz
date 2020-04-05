#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os
from typing import Optional

import matplotlib.pyplot as plt
import pandas as pd

from mitoviz.parsers import _DataFrameParser, _TabularParser, _VcfParser
from mitoviz.plot import (
    _plot_variants_polar, _plot_variants_linear, _plotly_variants_polar,
    _plotly_variants_linear, _plot_mito_polar, _plot_mito_linear,
    _plotly_mito_polar, _plotly_mito_linear
)
from mitoviz.utils import parse_path


def plot_base(linear: bool = False,
              save: bool = False,
              output: Optional[str] = None,
              legend: bool = False,
              split: bool = False,
              interactive: bool = False) -> None:
    """ Plot the base mitochondrial representation.

    Args:
        linear: show a linear plot rather than a polar one [default: False]
        save: if true, the final plot will be saved to a file [default: False]
        output: path of the output file where the plot will be saved
        legend: if true, add a legend for loci colors in the plot
            [default: False]
        split: if true, plot split H and L strands [default: True]
        interactive: if true, create an interactive version of the plot
            [default: False]
    """
    if linear:
        if interactive:
            plot_mito = _plotly_mito_linear
        else:
            plot_mito = _plot_mito_linear
    else:
        if interactive:
            plot_mito = _plotly_mito_polar
        else:
            plot_mito = _plot_mito_polar

    fig = plot_mito(legend, split)

    if save:
        dirname, name, ext = parse_path(output)
        if name == "":
            name = "base_mt"
        if interactive:
            fig.write_html(os.path.join(dirname, f"{name}.html"),
                           auto_open=False)
        else:
            plt.savefig(os.path.join(dirname, f"{name}{ext}"))
            plt.close()


def plot_vcf(in_vcf: str,
             linear: bool = False,
             sample: Optional[str] = None,
             save: bool = False,
             output: Optional[str] = None,
             labels: bool = False,
             legend: bool = False,
             split: bool = False,
             interactive: bool = False) -> None:
    """ Plot variants from the given VCF file.

    Args:
        in_vcf: path of the input VCF file
        linear: plot variants on a linear plot rather than a polar one
            [default: False]
        sample: specific sample to plot (defaults to all available samples)
        save: if true, the final plot will be saved to a file [default: False]
        output: path of the output file where the plot will be saved
        labels: if true, add a label for each variant shown [default: False]
        legend: if true, add a legend for loci colors in the plot
            [default: False]
        split: if true, plot split H and L strands [default: False]
        interactive: if true, create an interactive version of the plot
            [default: False]
    """
    vcf = _VcfParser(in_vcf)
    variants_per_sample = vcf.variants

    if linear:
        if interactive:
            plot_variants = _plotly_variants_linear
        else:
            plot_variants = _plot_variants_linear
    else:
        if interactive:
            plot_variants = _plotly_variants_polar
        else:
            plot_variants = _plot_variants_polar

    if sample:
        fig = plot_variants(sample, variants_per_sample[sample], labels,
                            legend, split)

        if save:
            dirname, name, ext = parse_path(output)
            if name == "":
                name = sample
            if interactive:
                fig.write_html(os.path.join(dirname, f"{name}.html"),
                               auto_open=False)
            else:
                plt.savefig(os.path.join(dirname, f"{name}{ext}"))
                plt.close()
    else:
        for i, (sample, variants) in enumerate(variants_per_sample.items(),
                                               start=1):
            fig = plot_variants(sample, variants, labels, legend, split)

            if save:
                dirname, name, ext = parse_path(output)
                if name == "":
                    name = sample
                    if interactive:
                        fig.write_html(os.path.join(dirname, f"{name}.html"),
                                       auto_open=False)
                    else:
                        plt.savefig(os.path.join(dirname, f"{name}{ext}"))
                        plt.close()
                elif len(variants_per_sample) == 1:
                    if interactive:
                        fig.write_html(os.path.join(dirname, f"{name}.html"),
                                       auto_open=False)
                    else:
                        plt.savefig(os.path.join(dirname, f"{name}{ext}"))
                        plt.close()
                else:
                    if interactive:
                        fig.write_html(os.path.join(dirname,
                                                    f"{name}_{i}.html"),
                                       auto_open=False)
                    else:
                        plt.savefig(os.path.join(dirname, f"{name}_{i}{ext}"))
                        plt.close()


def plot_df(in_df: pd.DataFrame,
            linear: bool = False,
            sample: Optional[str] = None,
            save: bool = False,
            output: Optional[str] = None,
            labels: bool = False,
            legend: bool = False,
            split: bool = False,
            interactive: bool = False,
            pos_col: str = "POS",
            ref_col: str = "REF",
            alt_col: str = "ALT",
            sample_col: str = "SAMPLE",
            hf_col: str = "HF") -> None:
    """ Plot variant from the given pandas DataFrame.

    Args:
        in_df: input pandas DataFrame
        linear: plot variants on a linear plot rather than a polar one
            [default: False]
        sample: specific sample to plot (defaults to all available samples)
        save: if true, the final plot will be saved to a file [default: False]
        output: path of the output file where the plot will be saved
        labels: if true, add a label for each variant shown [default: False]
        legend: if true, add a legend for loci colors in the plot
            [default: False]
        split: if true, plot split H and L strands [default: False]
        interactive: if true, create an interactive version of the plot
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

    if linear:
        if interactive:
            plot_variants = _plotly_variants_linear
        else:
            plot_variants = _plot_variants_linear
    else:
        if interactive:
            plot_variants = _plotly_variants_polar
        else:
            plot_variants = _plot_variants_polar

    if sample:
        fig = plot_variants(sample, variants_per_sample[sample], labels,
                            legend, split)

        if save:
            dirname, name, ext = parse_path(output)
            if name == "":
                name = sample
            if interactive:
                fig.write_html(os.path.join(dirname, f"{name}.html"),
                               auto_open=False)
            else:
                plt.savefig(os.path.join(dirname, f"{name}{ext}"))
                plt.close()
    else:
        for i, (sample, variants) in enumerate(variants_per_sample.items(),
                                               start=1):
            fig = plot_variants(sample, variants, labels, legend, split)

            if save:
                dirname, name, ext = parse_path(output)
                if name == "":
                    name = sample
                    if interactive:
                        fig.write_html(os.path.join(dirname, f"{name}.html"),
                                       auto_open=False)
                    else:
                        plt.savefig(os.path.join(dirname, f"{name}{ext}"))
                        plt.close()
                elif len(variants_per_sample) == 1:
                    if interactive:
                        fig.write_html(os.path.join(dirname, f"{name}.html"),
                                       auto_open=False)
                    else:
                        plt.savefig(os.path.join(dirname, f"{name}{ext}"))
                        plt.close()
                else:
                    if interactive:
                        fig.write_html(os.path.join(dirname,
                                                    f"{name}_{i}.html"),
                                       auto_open=False)
                    else:
                        plt.savefig(os.path.join(dirname, f"{name}_{i}{ext}"))
                        plt.close()


def plot_table(in_table: str,
               sep: str = ",",
               linear: bool = False,
               sample: Optional[str] = None,
               save: bool = False,
               output: Optional[str] = None,
               labels: bool = False,
               legend: bool = False,
               split: bool = False,
               interactive: bool = False,
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
        linear: plot variants on a linear plot rather than a polar one
            [default: False]
        sample: specific sample to plot (defaults to all available samples)
        save: if true, the final plot will be saved to a file [default: False]
        output: path of the output file where the plot will be saved
        labels: if true, add a label for each variant shown [default: False]
        legend: if true, add a legend for loci colors in the plot
            [default: False]
        split: if true, plot split H and L strands [default: False]
        interactive: if true, create an interactive version of the plot
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
            linear=linear,
            sample=sample,
            save=save,
            output=output,
            labels=labels,
            legend=legend,
            split=split,
            interactive=interactive,
            pos_col=pos_col,
            ref_col=ref_col,
            alt_col=alt_col,
            sample_col=sample_col,
            hf_col=hf_col)
