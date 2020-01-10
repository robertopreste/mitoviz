#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os
from typing import List, Optional

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

from .classes import Locus, Variant, VcfParser
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

    Parameters
    ----------
    sample : str
        Sample name, used for the title.
    variants : List[Variant]
        List of Variant instances to plot.
    labels : bool
        Add a label for each variant shown. [default: False]
    legend : bool
        Add a legend for loci colors in the plot. [default: False]
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

    Parameters
    ----------
    in_vcf : str
        Path of the input VCF file.
    sample : Optional[str]
        Specific sample to plot (defaults to all available samples).
    save : bool
        If true, the final plot will be saved to a file.
    output : Optional[str]
        Path of the output file where the plot will be saved.
    labels : bool
        If true, add a label for each variant shown.
    legend : bool
        If true, add a legend for loci colors in the plot.
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
