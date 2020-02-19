#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
from typing import List

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np

from mitoviz.constants import COLORS, NAMES
from mitoviz.locus import _PolarLocus, _PolarSplitLocus
from mitoviz.variant import _PolarVariant


def _label_variant(ax: plt.axes, variant: _PolarVariant):
    """ Annotate each variant with a label in the plot. """
    ax.annotate(variant.label,
                xy=(variant.pos_x, variant.pos_y),
                xytext=(variant.pos_x, variant.pos_y),
                textcoords="offset pixels",
                ha="center", va="bottom",
                bbox=dict(facecolor="w", alpha=0.8, boxstyle="round"))


def _plot_legend() -> List[mpatches.Patch]:
    """ Return a list of mpatches.Patch to create the loci legend. """
    cds = mpatches.Patch(color=COLORS["cds"], label="Coding")
    reg = mpatches.Patch(color=COLORS["reg"], label="Regulatory")
    rrna = mpatches.Patch(color=COLORS["rrna"], label="rRNA")
    trna = mpatches.Patch(color=COLORS["trna"], label="tRNA")
    nc = mpatches.Patch(color=COLORS["nc"], label="Non Coding")
    return [cds, reg, rrna, trna, nc]


def _plot_mito(legend: bool = False,
               split: bool = False):
    """ Return an axes object with the base mitochondrial genome plot.

    Args:
        legend: add a legend for loci colors in the plot [default: False]
        split: plot split H and L strands [default: False]
    """
    fig = plt.figure(figsize=(20, 10), dpi=300)
    ax = fig.add_subplot(111, polar=True)
    if split:
        names = NAMES + [""]
        loci = [_PolarSplitLocus(name=name, index=index)
                for index, name in enumerate(names)]
        radii = [el.radius for el in loci]
        bottoms = [el.bottom for el in loci]
    else:
        loci = [_PolarLocus(name=name, index=index)
                for index, name in enumerate(NAMES)]
        radii = [5.0] * 48
        bottoms = 20.0
    thetas = [el.theta for el in loci]
    widths = [el.width for el in loci]

    bars = plt.bar(thetas, radii, width=widths, bottom=bottoms)

    # Add black borders, useful for split plots
    ax.bar(0, 0.1, 2 * np.pi, 19.9, facecolor="black")
    ax.bar(0, 0.1, 2 * np.pi, 25.0, facecolor="black")

    for locus, bar in zip(loci, bars):
        bar.set_facecolor(locus.color)
        if locus.loc_type != "nc":
            ax.annotate(locus.name,
                        xy=(locus.theta, locus.text_y),
                        ha=locus.text_ha, va=locus.text_va)

    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.xaxis.grid(False)
    ax.yaxis.grid(False)
    ax.spines["polar"].set_visible(False)
    ax.set_theta_zero_location("N")

    if legend:
        handles = _plot_legend()
        plt.legend(handles=handles, loc="center")

    return fig, ax


def _plot_variants(sample: str,
                   variants: List[_PolarVariant],
                   labels: bool = False,
                   legend: bool = False,
                   split: bool = False) -> None:
    """ Plot variants available in the given list.

    Args:
        sample: sample name, used for the plot title
        variants: list of Variant instances to plot
        labels: add a label for each variant shown [default: False]
        legend: add a legend for loci colors in the plot [default: False]
        split: plot split H and L strands [default: False]
    """
    fig, ax = _plot_mito(legend, split)

    for variant in variants:
        ax.scatter(variant.pos_x, variant.pos_y, c="black", s=20, zorder=20)
        if labels:
            _label_variant(ax, variant)

    ax.set_title(sample)

    return None
