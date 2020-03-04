#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
from typing import List

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np

from mitoviz.constants import COLORS, NAMES
from mitoviz.locus import _LinearLocus, _PolarLocus, _PolarSplitLocus
from mitoviz.variant import _Variant


def _label_variant(ax: plt.axes, variant: _Variant, linear: bool = False):
    """ Annotate each variant with a label in the polar or linear plot.

    Args:
        ax: axis element on which the label will be added
        variant: variant to annotate
        linear: whether the resulting is a linear or polar plot
            [default: False]
    """
    if linear:
        ax.annotate(variant.label,
                    xy=(variant.linear_x, variant.linear_y + 0.02),
                    xytext=(variant.linear_x, variant.linear_y + 0.02),
                    ha="center", va="bottom",
                    bbox=dict(facecolor="w",
                              alpha=0.8,
                              boxstyle="round"))
    else:
        ax.annotate(variant.label,
                    xy=(variant.polar_x, variant.polar_y),
                    xytext=(variant.polar_x, variant.polar_y),
                    textcoords="offset pixels",
                    ha="center", va="bottom",
                    bbox=dict(facecolor="w",
                              alpha=0.8,
                              boxstyle="round"))


def _legend_patches() -> List[mpatches.Patch]:
    """ Return a list of mpatches.Patch to create the loci legend. """
    cds = mpatches.Patch(color=COLORS["cds"], label="Coding")
    reg = mpatches.Patch(color=COLORS["reg"], label="Regulatory")
    rrna = mpatches.Patch(color=COLORS["rrna"], label="rRNA")
    trna = mpatches.Patch(color=COLORS["trna"], label="tRNA")
    nc = mpatches.Patch(color=COLORS["nc"], label="Non Coding")
    return [cds, reg, rrna, trna, nc]


def _plot_mito_linear(legend: bool = False,
                      split: bool = False):
    """ Return an axes object with the base mt genome linear plot.

    Args:
        legend: add a legend for loci colors in the plot [default: False]
        split: plot split H and L strands [default: False]
    """
    fig = plt.figure(figsize=(20, 10), dpi=300)
    ax = fig.add_subplot(111)
    names = NAMES + ["DLOOP"]
    loci = [_LinearLocus(name=name, index=index)
            for index, name in enumerate(names)]

    if split:
        h_loci = [locus for locus in loci if locus.strand == "H"]
        l_loci = [locus for locus in loci if locus.strand == "L"]
        nc_loci = [locus for locus in loci if locus.strand == ""]
        ax.broken_barh([(locus.start, locus.width) for locus in h_loci],
                       (-0.05, 0.05),
                       facecolors=[locus.color for locus in h_loci])
        ax.broken_barh([(locus.start, locus.width) for locus in l_loci],
                       (-0.1, 0.05),
                       facecolors=[locus.color for locus in l_loci])
        ax.broken_barh([(locus.start, locus.width) for locus in nc_loci],
                       (-0.1, 0.1),
                       facecolors=[locus.color for locus in nc_loci])
    else:
        ax.broken_barh([(locus.start, locus.width) for locus in loci],
                       (-0.1, 0.1),
                       facecolors=[f"{locus.color}" for locus in loci])
    ax.set_xticks([0, 4000, 8000, 12000, 16000])
    ax.set_yticks([0.0, 0.25, 0.50, 0.75, 1.00])
    ax.set_ylim(-0.15, 1.10)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    for locus in loci:
        if locus.name == "OLR":
            ax.annotate(locus.name,
                        xy=(locus.text_x, -0.11),
                        ha="center",
                        fontsize=4)
            continue
        if locus.loc_type != "nc":
            ax.annotate(locus.name,
                        xy=(locus.text_x, locus.text_y),
                        ha="center",
                        fontsize=5)

    if legend:
        handles = _legend_patches()
        plt.legend(handles=handles, loc="upper right")
        ax.set_xlim([-500, 18000])

    return fig, ax


def _plot_mito_polar(legend: bool = False,
                     split: bool = False):
    """ Return an axes object with the base mt genome polar plot.

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
        radii = 5.0
        bottoms = 20.0
    thetas = [el.theta for el in loci]
    widths = [el.width for el in loci]

    bars = plt.bar(thetas, radii, width=widths, bottom=bottoms)

    # Add black borders, useful for split plots
    ax.bar(0, 0.1, 2 * np.pi, 19.9, facecolor="black")
    ax.bar(0, 0.1, 2 * np.pi, 25.0, facecolor="black")

    for locus, bar in zip(loci, bars):
        bar.set_facecolor(locus.color)
        if locus.name == "OLR":
            ax.annotate(locus.name,
                        xy=(locus.theta, locus.text_y),
                        ha=locus.text_ha, va=locus.text_va,
                        fontsize=6)
            continue
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
        handles = _legend_patches()
        plt.legend(handles=handles, loc="center")

    return fig, ax


def _plot_variants_polar(sample: str,
                         variants: List[_Variant],
                         labels: bool = False,
                         legend: bool = False,
                         split: bool = False) -> None:
    """ Plot variants available in the given list onto a polar plot.

    Args:
        sample: sample name, used for the plot title
        variants: list of _PolarVariant instances to plot
        labels: add a label for each variant shown [default: False]
        legend: add a legend for loci colors in the plot [default: False]
        split: plot split H and L strands [default: False]
    """
    fig, ax = _plot_mito_polar(legend, split)

    for variant in variants:
        ax.scatter(variant.polar_x, variant.polar_y,
                   c="black", s=20, zorder=20)
        if labels:
            _label_variant(ax, variant, linear=False)

    ax.set_title(sample)


def _plot_variants_linear(sample: str,
                          variants: List[_Variant],
                          labels: bool = False,
                          legend: bool = False,
                          split: bool = False) -> None:
    """ Plot variant available in a given list onto a linear plot.

    Args:
        sample: sample name, used for the plot title
        variants: list of _LinearVariant instances to plot
        labels: add a label for each variant shown [default: False]
        legend: add a legend for loci colors in the plot [default: False]
        split: plot split H and L strands [default: False]
    """
    fig, ax = _plot_mito_linear(legend, split)

    for variant in variants:
        if split:
            bottom = -0.05 if variant.strand == "L" else 0.0
        else:
            bottom = 0.0
        marker, stem, base = plt.stem([variant.linear_x], [variant.linear_y],
                                      "-.", bottom=bottom,
                                      use_line_collection=True)
        plt.setp(marker, "color", variant.color)
        plt.setp(stem, "color", variant.color)
        plt.setp(base, "linestyle", "None")

        if labels:
            _label_variant(ax, variant, linear=True)

    ax.set_title(sample)
