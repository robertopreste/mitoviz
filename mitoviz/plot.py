#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os
from typing import List, Optional

import matplotlib.pyplot as plt

from .classes import Locus, Variant, VcfParser
from .constants import NAMES
from .utils import parse_path


def plot_mito():
    """ Return an axes object with the base mitochondrial genome plot. """
    fig = plt.figure(figsize=(20, 10), dpi=300)
    ax = fig.add_subplot(111, polar=True)
    # ax = plt.axes([0.025, 0.025, 0.95, 0.95], polar=True)
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


def plot_variants(sample: str, variants: List[Variant]) -> None:
    """ Plot variants available in the given list.

    Parameters
    ----------
    sample : str
        Sample name, used for the title.
    variants : List[Variant]
        List of Variant instances to plot.
    """
    fig, ax = plot_mito()

    for variant in variants:
        ax.scatter(variant.pos_x, variant.pos_y, c="black", s=20, zorder=20)

    ax.set_title(sample)

    return None


def plot_vcf(in_vcf: str,
             sample: Optional[str] = None,
             save: bool = False,
             output: Optional[str] = None) -> None:
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
    """
    vcf = VcfParser(in_vcf)
    variants_per_sample = vcf.variants

    if sample:
        plot_variants(sample, variants_per_sample[sample])
        if save:
            dirname, name, ext = parse_path(output)
            if name == "":
                name = sample
            plt.savefig(os.path.join(dirname, f"{name}{ext}"))
            plt.close()
    else:
        for i, (sample, variants) in enumerate(variants_per_sample.items(),
                                               start=1):
            plot_variants(sample, variants)
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
