#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os
from typing import List, Optional

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import pandas as pd

from .classes import Locus, Variant, VcfParser, DataFrameParser
from .constants import COLORS, NAMES
from .utils import parse_path


def label_variant(ax: plt.axes, variant: Variant):
    """ Annotate each variant with a label in the plot. """
    ax.annotate(variant.label,
                xy=(variant.pos_x, variant.pos_y),
                xytext=(variant.pos_x, variant.pos_y),
                textcoords="offset pixels",
                ha="center", va="bottom",
                bbox=dict(facecolor="w", alpha=0.8, boxstyle="round"))


def plot_legend() -> List[mpatches.Patch]:
    """ Return a list of mpatches.Patch to create the loci legend. """
    cds = mpatches.Patch(color=COLORS["cds"], label="Coding")
    reg = mpatches.Patch(color=COLORS["reg"], label="Regulatory")
    rrna = mpatches.Patch(color=COLORS["rrna"], label="rRNA")
    trna = mpatches.Patch(color=COLORS["trna"], label="tRNA")
    return [cds, reg, rrna, trna]


def plot_mito():
    """ Return an axes object with the base mitochondrial genome plot. """
    fig = plt.figure(figsize=(20, 10), dpi=300)
    ax = fig.add_subplot(111, polar=True)
    loci = [Locus(name=name, index=index)
            for name, index in zip(NAMES, range(len(NAMES)))]
    thetas = [el.theta for el in loci]
    radii = [5.0] * 38
    widths = [el.width for el in loci]

    bars = plt.bar(thetas, radii, width=widths, bottom=20.0)
    for locus, bar in zip(loci, bars):
        bar.set_facecolor(locus.color)
        ax.annotate(locus.name,
                    xy=(locus.theta, locus.text_y),
                    ha=locus.text_ha, va=locus.text_va)

    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.xaxis.grid(False)
    ax.yaxis.grid(False)
    ax.spines["polar"].set_visible(False)
    ax.set_theta_zero_location("N")

    return fig, ax


def plot_variants(sample: str,
                  variants: List[Variant],
                  labels: bool = False,
                  legend: bool = False) -> None:
    """ Plot variants available in the given list.

    Args:
        sample: sample name, used for the plot title
        variants: list of Variant instances to plot
        labels: add a label for each variant shown [default: False]
        legend: add a legend for loci colors in the plot [default: False]
    """
    fig, ax = plot_mito()

    for variant in variants:
        ax.scatter(variant.pos_x, variant.pos_y, c="black", s=20, zorder=20)
        if labels:
            label_variant(ax, variant)

    ax.set_title(sample)
    if legend:
        plt.legend(handles=plot_legend(), loc="center")

    return None


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
    vcf = VcfParser(in_vcf)
    variants_per_sample = vcf.variants

    if sample:
        plot_variants(sample, variants_per_sample[sample], labels, legend)
        if save:
            dirname, name, ext = parse_path(output)
            if name == "":
                name = sample
            plt.savefig(os.path.join(dirname, f"{name}{ext}"))
            plt.close()
    else:
        for i, (sample, variants) in enumerate(variants_per_sample.items(),
                                               start=1):
            plot_variants(sample, variants, labels, legend)
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
    df = DataFrameParser(in_df,
                         pos_col=pos_col,
                         ref_col=ref_col,
                         alt_col=alt_col,
                         sample_col=sample_col,
                         hf_col=hf_col)
    variants_per_sample = df.variants

    if sample:
        plot_variants(sample, variants_per_sample[sample], labels, legend)
        if save:
            dirname, name, ext = parse_path(output)
            if name == "":
                name = sample
            plt.savefig(os.path.join(dirname, f"{name}{ext}"))
            plt.close()
    else:
        for i, (sample, variants) in enumerate(variants_per_sample.items(),
                                               start=1):
            plot_variants(sample, variants, labels, legend)
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
