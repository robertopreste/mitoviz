#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import matplotlib.pyplot as plt

from .classes import Locus, VcfParser
from .constants import NAMES


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


def plot_vcf(in_vcf: str,
             save: bool = False,
             output: str = "mitoviz.png") -> None:
    """ Plot variants from the given VCF file.

    Parameters
    ----------
    in_vcf : str
        Path of the input VCF file.
    save : bool
        If true, the final plot will be saved to a file.
    output : str
        Path of the output file where the plot will be saved
        (default: ./mitoviz.png).
    """
    fig, ax = plot_mito()

    vcf = VcfParser(in_vcf)
    for variant in vcf.variants:
        ax.scatter(variant.pos_x, variant.pos_y, c="black", s=20, zorder=20)

    if save:
        plt.savefig(output)

    return None
