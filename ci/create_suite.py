#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os

import matplotlib.pyplot as plt

from mitoviz import plot_df, plot_vcf
from mitoviz.plot import (
    _plot_mito_linear, _plot_mito_polar, _plotly_mito_polar
)
from mitoviz.tests.constants import (
    SAMPLE_VCF, SAMPLE_HF_VCF,
    SAMPLE_DF, SAMPLE_HF_DF,
    BASE_MITO_POLAR, BASE_MITO_POLAR_LEGEND, BASE_MITO_POLAR_SPLIT,
    BASE_MITO_LINEAR, BASE_MITO_LINEAR_LEGEND, BASE_MITO_LINEAR_SPLIT,
    BASE_MITO_PLOTLY, BASE_MITO_PLOTLY_LEGEND, BASE_MITO_PLOTLY_SPLIT,
    BASE_IMG, BASE_IMG_LABELS, BASE_IMG_LEGEND, BASE_IMG_SPLIT,
    BASE_IMG_LINEAR, BASE_IMG_LINEAR_LABELS, BASE_IMG_LINEAR_LEGEND,
    BASE_IMG_LINEAR_SPLIT,
    BASE_IMG_PLOTLY, BASE_IMG_PLOTLY_LEGEND, BASE_IMG_PLOTLY_SPLIT,
    BASE_IMG_DF, BASE_IMG_LABELS_DF, BASE_IMG_LEGEND_DF, BASE_IMG_SPLIT_DF,
    BASE_IMG_LINEAR_DF, BASE_IMG_LINEAR_LABELS_DF, BASE_IMG_LINEAR_LEGEND_DF,
    BASE_IMG_LINEAR_SPLIT_DF,
    BASE_IMG_PLOTLY_DF, BASE_IMG_PLOTLY_LEGEND_DF, BASE_IMG_PLOTLY_SPLIT_DF,
    BASE_HF_IMG, BASE_HF_IMG_LABELS, BASE_HF_IMG_LEGEND, BASE_HF_IMG_SPLIT,
    BASE_HF_IMG_LINEAR, BASE_HF_IMG_LINEAR_LABELS, BASE_HF_IMG_LINEAR_LEGEND,
    BASE_HF_IMG_LINEAR_SPLIT,
    BASE_HF_IMG_PLOTLY, BASE_HF_IMG_PLOTLY_LEGEND, BASE_HF_IMG_PLOTLY_SPLIT,
    BASE_HF_IMG_DF, BASE_HF_IMG_LABELS_DF, BASE_HF_IMG_LEGEND_DF,
    BASE_HF_IMG_SPLIT_DF,
    BASE_HF_IMG_LINEAR_DF, BASE_HF_IMG_LINEAR_LABELS_DF,
    BASE_HF_IMG_LINEAR_LEGEND_DF, BASE_HF_IMG_LINEAR_SPLIT_DF,
    BASE_HF_IMG_PLOTLY_DF, BASE_HF_IMG_PLOTLY_LEGEND_DF,
    BASE_HF_IMG_PLOTLY_SPLIT_DF,
    SAMPLE_MULTI_VCF, SAMPLE_MULTI_DF, IMGDIR
)


def create_mito_polar():
    """ Create base mitochondrial polar plots. """
    fig, ax = _plot_mito_polar()
    plt.savefig(BASE_MITO_POLAR)
    plt.close()

    fig, ax = _plot_mito_polar(legend=True)
    plt.savefig(BASE_MITO_POLAR_LEGEND)
    plt.close()

    fig, ax = _plot_mito_polar(split=True)
    plt.savefig(BASE_MITO_POLAR_SPLIT)
    plt.close()


def create_mito_linear():
    """ Create base mitochondrial linear plots. """
    fig, ax = _plot_mito_linear()
    plt.savefig(BASE_MITO_LINEAR)
    plt.close()

    fig, ax = _plot_mito_linear(legend=True)
    plt.savefig(BASE_MITO_LINEAR_LEGEND)
    plt.close()

    fig, ax = _plot_mito_linear(split=True)
    plt.savefig(BASE_MITO_LINEAR_SPLIT)
    plt.close()


def create_mito_polar_plotly():
    """ Create base mitochondrial polar plots with plotly. """
    fig = _plotly_mito_polar()
    fig.write_html(BASE_MITO_PLOTLY)

    fig = _plotly_mito_polar(legend=True)
    fig.write_html(BASE_MITO_PLOTLY_LEGEND)

    fig = _plotly_mito_polar(split=True)
    fig.write_html(BASE_MITO_PLOTLY_SPLIT)


def create_sample_vcf_polar():
    """ Create polar plots from sample.vcf. """
    plot_vcf(in_vcf=SAMPLE_VCF, save=True, output=BASE_IMG)
    plot_vcf(in_vcf=SAMPLE_VCF, save=True, output=BASE_IMG_LABELS,
             labels=True)
    plot_vcf(in_vcf=SAMPLE_VCF, save=True, output=BASE_IMG_LEGEND,
             legend=True)
    plot_vcf(in_vcf=SAMPLE_VCF, save=True, output=BASE_IMG_SPLIT,
             split=True)


def create_sample_vcf_linear():
    """ Create linear plots from sample.vcf. """
    plot_vcf(in_vcf=SAMPLE_VCF, linear=True, save=True, output=BASE_IMG_LINEAR)
    plot_vcf(in_vcf=SAMPLE_VCF, linear=True, save=True,
             output=BASE_IMG_LINEAR_LABELS, labels=True)
    plot_vcf(in_vcf=SAMPLE_VCF, linear=True, save=True,
             output=BASE_IMG_LINEAR_LEGEND, legend=True)
    plot_vcf(in_vcf=SAMPLE_VCF, linear=True, save=True,
             output=BASE_IMG_LINEAR_SPLIT, split=True)


def create_sample_vcf_polar_plotly():
    """ Create polar plots from sample.vcf with plotly. """
    plot_vcf(in_vcf=SAMPLE_VCF, save=True, interactive=True,
             output=BASE_IMG_PLOTLY)
    plot_vcf(in_vcf=SAMPLE_VCF, save=True, interactive=True,
             output=BASE_IMG_PLOTLY_LEGEND, legend=True)
    plot_vcf(in_vcf=SAMPLE_VCF, save=True, interactive=True,
             output=BASE_IMG_PLOTLY_SPLIT, split=True)


def create_sample_df_polar():
    """ Create polar plots from the sample dataframe. """
    plot_df(in_df=SAMPLE_DF, save=True, output=BASE_IMG_DF)
    plot_df(in_df=SAMPLE_DF, save=True, output=BASE_IMG_LABELS_DF,
            labels=True)
    plot_df(in_df=SAMPLE_DF, save=True, output=BASE_IMG_LEGEND_DF,
            legend=True)
    plot_df(in_df=SAMPLE_DF, save=True, output=BASE_IMG_SPLIT_DF,
            split=True)


def create_sample_df_linear():
    """ Create linear plots from the sample dataframe. """
    plot_df(in_df=SAMPLE_DF, linear=True, save=True,
            output=BASE_IMG_LINEAR_DF)
    plot_df(in_df=SAMPLE_DF, linear=True, save=True,
            output=BASE_IMG_LINEAR_LABELS_DF, labels=True)
    plot_df(in_df=SAMPLE_DF, linear=True, save=True,
            output=BASE_IMG_LINEAR_LEGEND_DF, legend=True)
    plot_df(in_df=SAMPLE_DF, linear=True, save=True,
            output=BASE_IMG_LINEAR_SPLIT_DF, split=True)


def create_sample_df_polar_plotly():
    """ Create polar plots from the sample dataframe with plotly. """
    plot_df(in_df=SAMPLE_DF, save=True, interactive=True,
            output=BASE_IMG_PLOTLY_DF)
    plot_df(in_df=SAMPLE_DF, save=True, interactive=True,
            output=BASE_IMG_PLOTLY_LEGEND_DF, legend=True)
    plot_df(in_df=SAMPLE_DF, save=True, interactive=True,
            output=BASE_IMG_PLOTLY_SPLIT_DF, split=True)


def create_sample_vcf_hf_polar():
    """ Create polar plots from sample_hf.vcf. """
    plot_vcf(in_vcf=SAMPLE_HF_VCF, save=True, output=BASE_HF_IMG)
    plot_vcf(in_vcf=SAMPLE_HF_VCF, save=True,
             output=BASE_HF_IMG_LABELS, labels=True)
    plot_vcf(in_vcf=SAMPLE_HF_VCF, save=True,
             output=BASE_HF_IMG_LEGEND, legend=True)
    plot_vcf(in_vcf=SAMPLE_HF_VCF, save=True,
             output=BASE_HF_IMG_SPLIT, split=True)


def create_sample_vcf_hf_linear():
    """ Create linear plots from sample_hf.vcf. """
    plot_vcf(in_vcf=SAMPLE_HF_VCF, linear=True, save=True,
             output=BASE_HF_IMG_LINEAR)
    plot_vcf(in_vcf=SAMPLE_HF_VCF, linear=True, save=True,
             output=BASE_HF_IMG_LINEAR_LABELS, labels=True)
    plot_vcf(in_vcf=SAMPLE_HF_VCF, linear=True, save=True,
             output=BASE_HF_IMG_LINEAR_LEGEND, legend=True)
    plot_vcf(in_vcf=SAMPLE_HF_VCF, linear=True, save=True,
             output=BASE_HF_IMG_LINEAR_SPLIT, split=True)


def create_sample_vcf_hf_polar_plotly():
    """ Create polar plots from sample_hf.vcf with plotly. """
    plot_vcf(in_vcf=SAMPLE_HF_VCF, save=True, interactive=True,
             output=BASE_HF_IMG_PLOTLY)
    plot_vcf(in_vcf=SAMPLE_HF_VCF, save=True, interactive=True,
             output=BASE_HF_IMG_PLOTLY_LEGEND, legend=True)
    plot_vcf(in_vcf=SAMPLE_HF_VCF, save=True, interactive=True,
             output=BASE_HF_IMG_PLOTLY_SPLIT, split=True)


def create_sample_df_hf_polar():
    """ Create polar plots from the sample dataframe with hf. """
    plot_df(in_df=SAMPLE_HF_DF, save=True, output=BASE_HF_IMG_DF)
    plot_df(in_df=SAMPLE_HF_DF, save=True,
            output=BASE_HF_IMG_LABELS_DF, labels=True)
    plot_df(in_df=SAMPLE_HF_DF, save=True,
            output=BASE_HF_IMG_LEGEND_DF, legend=True)
    plot_df(in_df=SAMPLE_HF_DF, save=True,
            output=BASE_HF_IMG_SPLIT_DF, split=True)


def create_sample_df_hf_linear():
    """ Create linear plots from the sample dataframe with hf. """
    plot_df(in_df=SAMPLE_HF_DF, linear=True, save=True,
            output=BASE_HF_IMG_LINEAR_DF)
    plot_df(in_df=SAMPLE_HF_DF, linear=True, save=True,
            output=BASE_HF_IMG_LINEAR_LABELS_DF, labels=True)
    plot_df(in_df=SAMPLE_HF_DF, linear=True, save=True,
            output=BASE_HF_IMG_LINEAR_LEGEND_DF, legend=True)
    plot_df(in_df=SAMPLE_HF_DF, linear=True, save=True,
            output=BASE_HF_IMG_LINEAR_SPLIT_DF, split=True)


def create_sample_df_hf_polar_plotly():
    """ Create polar plots from the sample dataframe with hf with plotly. """
    plot_df(in_df=SAMPLE_HF_DF, save=True, interactive=True,
            output=BASE_HF_IMG_PLOTLY_DF)
    plot_df(in_df=SAMPLE_HF_DF, save=True, interactive=True,
            output=BASE_HF_IMG_PLOTLY_LEGEND_DF, legend=True)
    plot_df(in_df=SAMPLE_HF_DF, save=True, interactive=True,
            output=BASE_HF_IMG_PLOTLY_SPLIT_DF, split=True)


def create_multisample_vcf_polar():
    """ Create polar plots from multisample.vcf. """
    plot_vcf(in_vcf=SAMPLE_MULTI_VCF, save=True,
             output=os.path.join(IMGDIR, "multisample.png"))
    plot_vcf(in_vcf=SAMPLE_MULTI_VCF, save=True,
             output=os.path.join(IMGDIR, "multisample_labels.png"),
             labels=True)
    plot_vcf(in_vcf=SAMPLE_MULTI_VCF, save=True,
             output=os.path.join(IMGDIR, "multisample_legend.png"),
             legend=True)
    plot_vcf(in_vcf=SAMPLE_MULTI_VCF, save=True,
             output=os.path.join(IMGDIR, "multisample_split.png"),
             split=True)


def create_multisample_vcf_linear():
    """ Create linear plots from multisample.vcf. """
    plot_vcf(in_vcf=SAMPLE_MULTI_VCF, linear=True, save=True,
             output=os.path.join(IMGDIR, "multisample_linear.png"))
    plot_vcf(in_vcf=SAMPLE_MULTI_VCF, linear=True, save=True,
             output=os.path.join(IMGDIR, "multisample_linear_labels.png"),
             labels=True)
    plot_vcf(in_vcf=SAMPLE_MULTI_VCF, linear=True, save=True,
             output=os.path.join(IMGDIR, "multisample_linear_legend.png"),
             legend=True)
    plot_vcf(in_vcf=SAMPLE_MULTI_VCF, linear=True, save=True,
             output=os.path.join(IMGDIR, "multisample_linear_split.png"),
             split=True)


def create_multisample_vcf_polar_plotly():
    """ Create polar plots from multisample.vcf with plotly. """
    plot_vcf(in_vcf=SAMPLE_MULTI_VCF, save=True, interactive=True,
             output=os.path.join(IMGDIR, "multisample_plotly.html"))
    plot_vcf(in_vcf=SAMPLE_MULTI_VCF, save=True, interactive=True,
             output=os.path.join(IMGDIR, "multisample_plotly_legend.html"),
             legend=True)
    plot_vcf(in_vcf=SAMPLE_MULTI_VCF, save=True, interactive=True,
             output=os.path.join(IMGDIR, "multisample_plotly_split.png"),
             split=True)


def create_multisample_df_polar():
    """ Create polar plots from the multisample dataframe. """
    plot_df(in_df=SAMPLE_MULTI_DF, save=True,
            output=os.path.join(IMGDIR, "multisample_df.png"))
    plot_df(in_df=SAMPLE_MULTI_DF, save=True,
            output=os.path.join(IMGDIR, "multisample_labels_df.png"),
            labels=True)
    plot_df(in_df=SAMPLE_MULTI_DF, save=True,
            output=os.path.join(IMGDIR, "multisample_legend_df.png"),
            legend=True)
    plot_df(in_df=SAMPLE_MULTI_DF, save=True,
            output=os.path.join(IMGDIR, "multisample_split_df.png"),
            split=True)


def create_multisample_df_linear():
    """ Create linear plots from the multisample dataframe. """
    plot_df(in_df=SAMPLE_MULTI_DF, linear=True, save=True,
            output=os.path.join(IMGDIR, "multisample_linear_df.png"))
    plot_df(in_df=SAMPLE_MULTI_DF, linear=True, save=True,
            output=os.path.join(IMGDIR, "multisample_linear_labels_df.png"),
            labels=True)
    plot_df(in_df=SAMPLE_MULTI_DF, linear=True, save=True,
            output=os.path.join(IMGDIR, "multisample_linear_legend_df.png"),
            legend=True)
    plot_df(in_df=SAMPLE_MULTI_DF, linear=True, save=True,
            output=os.path.join(IMGDIR, "multisample_linear_split_df.png"),
            split=True)


def create_multisample_df_polar_plotly():
    """ Create polar plots from the multisample dataframe with plotly. """
    plot_df(in_df=SAMPLE_MULTI_DF, save=True, interactive=True,
            output=os.path.join(IMGDIR, "multisample_plotly_df.html"))
    plot_df(in_df=SAMPLE_MULTI_DF, save=True, interactive=True,
            output=os.path.join(IMGDIR, "multisample_plotly_legend_df.html"),
            legend=True)
    plot_df(in_df=SAMPLE_MULTI_DF, save=True, interactive=True,
            output=os.path.join(IMGDIR, "multisample_plotly_split_df.png"),
            split=True)


def create_all():
    """ Create all the test files needed. """
    create_mito_polar()
    create_mito_linear()
    create_mito_polar_plotly()

    create_sample_vcf_polar()
    create_sample_vcf_linear()
    create_sample_vcf_polar_plotly()

    create_sample_df_polar()
    create_sample_df_linear()
    create_sample_df_polar_plotly()

    create_sample_vcf_hf_polar()
    create_sample_vcf_hf_linear()
    create_sample_vcf_hf_polar_plotly()

    create_sample_df_hf_polar()
    create_sample_df_hf_linear()
    create_sample_df_hf_polar_plotly()

    create_multisample_vcf_polar()
    create_multisample_vcf_linear()
    create_multisample_vcf_polar_plotly()

    create_multisample_df_polar()
    create_multisample_df_linear()
    create_multisample_df_polar_plotly()
