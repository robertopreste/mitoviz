#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
from typing import List, Optional

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go

from mitoviz.constants import COLORS, LABELS, NAMES
from mitoviz.locus import _LinearLocus, _PolarLocus, _PolarSplitLocus
from mitoviz.variant import _Variant


class Legend:
    """ Class dealing with the creation of different legend flavors. """

    def __init__(self):
        self.colors = COLORS
        self.labels = LABELS

    def patches(self) -> List[mpatches.Patch]:
        """ Return a list of mpatches.Patch to create the loci legend. """
        patches = [mpatches.Patch(color=self.colors[loc],
                                  label=self.labels[loc])
                   for loc in self.colors]
        return patches

    def plotly_polar(self) -> List[go.Scatterpolar]:
        """ Return a list of plotly Scatterpolar elements to create the loci
        legend on a polar plot. """
        patches = [go.Scatterpolar(r=[None], theta=[None], mode="markers",
                                   marker=dict(size=10,
                                               color=self.colors[loc]),
                                   showlegend=True, name=self.labels[loc])
                   for loc in self.colors]
        return patches

    def plotly_linear(self) -> List[go.Scatter]:
        """ Return a list of plotly Scatter elements to create the loci
        legend on a linear plot. """
        patches = [go.Scatter(x=[None], y=[None], mode="markers",
                              marker=dict(size=10, color=self.colors[loc]),
                              showlegend=True, name=self.labels[loc])
                   for loc in self.colors]
        return patches


class PlotBase:
    """ Class dealing with the creation of the different base plots. """

    def __init__(self):
        self.legend = Legend()

    def linear(self,
               legend: bool = False,
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
            handles = self.legend.patches()
            plt.legend(handles=handles, loc="upper right")
            ax.set_xlim([-500, 18000])

        return fig, ax

    def linear_plotly(self,
                      legend: bool = False,
                      split: bool = False) -> go.Figure:
        """Return a plotly figure with the base mt genome linear plot.

        Args:
            legend: add a legend for loci colors in the plot [default: False]
            split: plot split H and L strand [default: False]
        """
        names = NAMES + ["DLOOP"]
        loci = [_LinearLocus(name=name, index=index)
                for index, name in enumerate(names)]

        if split:
            shapes = []
            for locus in loci:
                if locus.strand == "H":
                    y0 = -0.1
                    y1 = 0.0
                elif locus.strand == "L":
                    y0 = -0.2
                    y1 = -0.1
                else:
                    y0 = -0.2
                    y1 = 0.0
                shape = dict(type="rect",
                             x0=locus.start,
                             y0=y0,
                             x1=(locus.start + locus.width),
                             y1=y1,
                             fillcolor=locus.color,
                             line_color=locus.color)
                shapes.append(shape)
        else:
            shapes = [dict(type="rect",
                           x0=locus.start,
                           y0=-0.2,
                           x1=(locus.start + locus.width),
                           y1=0.0,
                           fillcolor=locus.color,
                           line_color=locus.color) for locus in loci]

        scatters = go.Scatter(
            x=[locus.text_x for locus in loci],
            y=[-0.1 for _ in loci],
            text=[locus.name for locus in loci],
            hovertemplate="%{text}<extra></extra>",
            mode="markers",
            marker=dict(symbol="square", opacity=0),
            showlegend=False,
        )
        fig = go.Figure()
        fig.add_trace(scatters)

        if legend:
            legend = self.legend.plotly_linear()
            for el in legend:
                fig.add_trace(el)

        fig.update_layout(width=1000, height=800, template="none",
                          legend=dict(x=0.0, y=1.0,
                                      xanchor="right", yanchor="middle"),
                          xaxis=dict(showgrid=False,
                                     showline=False,
                                     zeroline=False),
                          yaxis=dict(showgrid=False,
                                     showline=False,
                                     zeroline=False),
                          yaxis_range=[-0.3, 1.2],
                          hovermode="closest",
                          shapes=shapes)
        fig.update_xaxes(tickvals=[0, 4000, 8000, 12000, 16000])
        fig.update_yaxes(tickvals=[0, 0.25, 0.5, 0.75, 1.0])

        return fig

    def polar(self,
              legend: bool = False,
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
            handles = self.legend.patches()
            plt.legend(handles=handles, loc="center")

        return fig, ax

    def polar_plotly(self,
                     legend: bool = False,
                     split: bool = False) -> go.Figure:
        """ Return a plotly figure with the base mt genome polar plot.

        Args:
            legend: add a legend for loci colors in the plot [default: False]
            split: plot split H and L strand [default: False]
        """
        fig = go.Figure()

        if split:
            names = NAMES + [""]
            loci = [_PolarSplitLocus(name=name, index=index)
                    for index, name in enumerate(names)]
            radii = [el.radius for el in loci]
            bottoms = [el.bottom for el in loci]
        else:
            loci = [_PolarLocus(name=name, index=index)
                    for index, name in enumerate(NAMES)]
            radii = [5.0 for _ in loci]
            bottoms = [20.0 for _ in loci]
        names = [el.name for el in loci]
        thetas = [el.theta_p for el in loci]
        widths = [el.width_p for el in loci]
        colors = [el.color for el in loci]

        mito_trace = go.Barpolar(r=radii, theta=thetas,
                                 width=widths, base=bottoms,
                                 marker_color=colors, meta=names,
                                 hovertemplate="%{meta}<extra></extra>",
                                 showlegend=False)

        fig.add_trace(mito_trace)

        border_trace = go.Barpolar(r=[0.1, 0.1], theta=[0, 0],
                                   width=[360, 360], base=[19.9, 25.0],
                                   marker_color="black",
                                   hoverinfo="none", showlegend=False)

        fig.add_trace(border_trace)

        if legend:
            legend = self.legend.plotly_polar()
            for el in legend:
                fig.add_trace(el)

        fig.update_layout(width=900, height=800, template="none",
                          legend=dict(x=0.5, y=0.5,
                                      xanchor="center", yanchor="middle"),
                          polar=dict(
                              radialaxis=dict(showticklabels=False,
                                              ticks="",
                                              showgrid=False,
                                              showline=False),
                              angularaxis=dict(rotation=90,
                                               showticklabels=False,
                                               ticks="",
                                               showgrid=False,
                                               showline=False)))

        return fig


class PlotVariants:
    """ Class dealing with the creation of the different variant plots.

    Args:
         sample: sample name, used for the plot title
    """

    def __init__(self, sample: Optional[str] = None):
        self.base_plot = PlotBase()
        self.sample = sample

    def polar(self,
              variants: List[_Variant],
              labels: bool = False,
              labels_hf: bool = False,
              legend: bool = False,
              split: bool = False):
        """ Plot variants available in the given list onto a polar plot.

        Args:
            variants: list of _PolarVariant instances to plot
            labels: add a label for each variant shown [default: False]
            labels_hf: show HF value in each variant's label [default: False]
            legend: add a legend for loci colors in the plot [default: False]
            split: plot split H and L strands [default: False]
        """
        fig, ax = self.base_plot.polar(legend, split)

        for variant in variants:
            ax.scatter(variant.polar_x, variant.polar_y,
                       c="black", s=20, zorder=20)
            if labels:
                self.label_variant(ax, variant,
                                   linear=False, show_hf=labels_hf)

        ax.set_title(self.sample)

        return fig, ax

    def polar_plotly(self,
                     variants: List[_Variant],
                     labels: bool = False,
                     labels_hf: bool = False,
                     legend: bool = False,
                     split: bool = False) -> go.Figure:
        """ Plot variants available in the given list onto a plotly polar plot.

        Args:
            variants: list of _PolarVariant instances to plot
            labels: add a label for each variant shown [default: False]
            labels_hf: show HF value in each variant's label [default: False]
            legend: add a legend for loci colors in the plot [default: False]
            split: plot split H and L strands [default: False]
        """
        fig = self.base_plot.polar_plotly(legend, split)

        radii = [el.polar_y for el in variants]
        theta = [el.polar_x_p for el in variants]
        if labels_hf:
            meta = [el.label_hf_plotly for el in variants]
        else:
            meta = [el.label for el in variants]

        var_trace = go.Scatterpolar(r=radii, theta=theta, mode="markers",
                                    marker=dict(color="black"), meta=meta,
                                    hovertemplate="%{meta}<extra></extra>",
                                    showlegend=False)

        fig.add_trace(var_trace)
        fig.update_layout(title=self.sample)

        # Returning go.Figure to allow saving the html image
        return fig

    def linear(self,
               variants: List[_Variant],
               labels: bool = False,
               labels_hf: bool = False,
               legend: bool = False,
               split: bool = False):
        """ Plot variant available in a given list onto a linear plot.

        Args:
            variants: list of _LinearVariant instances to plot
            labels: add a label for each variant shown [default: False]
            labels_hf: show HF value in each variant's label [default: False]
            legend: add a legend for loci colors in the plot [default: False]
            split: plot split H and L strands [default: False]
        """
        fig, ax = self.base_plot.linear(legend, split)

        for variant in variants:
            if split:
                bottom = -0.05 if variant.strand == "L" else 0.0
            else:
                bottom = 0.0
            marker, stem, base = plt.stem([variant.linear_x],
                                          [variant.linear_y],
                                          "-.", bottom=bottom,
                                          use_line_collection=True)
            plt.setp(marker, "color", variant.color)
            plt.setp(stem, "color", variant.color)
            plt.setp(base, "linestyle", "None")

            if labels:
                self.label_variant(ax, variant,
                                   linear=True, show_hf=labels_hf)

        ax.set_title(self.sample)

        return fig, ax

    def linear_plotly(self,
                      variants: List[_Variant],
                      labels: bool = False,
                      labels_hf: bool = False,
                      legend: bool = False,
                      split: bool = False) -> go.Figure:
        """ Plot variant available in a given list onto a plotly linear plot.

        Args:
            variants: list of _LinearVariant instances to plot
            labels: add a label for each variant shown [default: False]
            labels_hf: show HF value in each variant's label [default: False]
            legend: add a legend for loci colors in the plot [default: False]
            split: plot split H and L strands [default: False]
        """
        fig = self.base_plot.linear_plotly(legend, split)

        xs = [variant.linear_x for variant in variants]
        ys = [variant.linear_y for variant in variants]
        if labels_hf:
            meta = [el.label_hf_plotly for el in variants]
        else:
            meta = [el.label for el in variants]

        var_trace = go.Scatter(x=xs, y=ys, mode="markers",
                               marker=dict(color="black"), meta=meta,
                               hovertemplate="%{meta}<extra></extra>",
                               showlegend=False)
        lines = [dict(type="line",
                      xref="x",
                      yref="y",
                      x0=variant.linear_x,
                      y0=-0.1,
                      x1=variant.linear_x,
                      y1=(variant.linear_y - 0.006),
                      layer="below",
                      line=dict(color="grey", width=1))
                 for variant in variants]

        fig.add_trace(var_trace)
        base_shapes = list(fig.layout.shapes)
        fig.update_layout(shapes=[*base_shapes, *lines], title=self.sample)

        # Returning go.Figure to allow saving the html image
        return fig

    @staticmethod
    def label_variant(ax: plt.axes,
                      variant: _Variant,
                      linear: bool = False,
                      show_hf: bool = False):
        """ Annotate each variant with a label in the polar or linear plot.

        Args:
            ax: axis element on which the label will be added
            variant: variant to annotate
            linear: whether the resulting is a linear or polar plot
                [default: False]
            show_hf: show HF value in each variant's label [default: False]
        """
        if show_hf:
            label = variant.label_hf
        else:
            label = variant.label
        if linear:
            ax.annotate(label,
                        xy=(variant.linear_x, variant.linear_y + 0.02),
                        xytext=(variant.linear_x, variant.linear_y + 0.02),
                        ha="center", va="bottom",
                        bbox=dict(facecolor="w",
                                  alpha=0.8,
                                  boxstyle="round"))
        else:
            ax.annotate(label,
                        xy=(variant.polar_x, variant.polar_y),
                        xytext=(variant.polar_x, variant.polar_y),
                        textcoords="offset pixels",
                        ha="center", va="bottom",
                        bbox=dict(facecolor="w",
                                  alpha=0.8,
                                  boxstyle="round"))
