#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os

import matplotlib.pyplot as plt

from mitoviz import plot_df, plot_vcf
from mitoviz.plot import _plot_mito
from mitoviz.tests.constants import (
    SAMPLE_VCF, SAMPLE_HF_VCF,
    SAMPLE_DF, SAMPLE_HF_DF,
    BASE_MITO, BASE_MITO_LEGEND, BASE_MITO_SPLIT,
    BASE_IMG, BASE_IMG_LABELS, BASE_IMG_LEGEND, BASE_IMG_SPLIT,
    BASE_IMG_DF, BASE_IMG_LABELS_DF, BASE_IMG_LEGEND_DF, BASE_IMG_SPLIT_DF,
    BASE_HF_IMG, BASE_HF_IMG_LABELS, BASE_HF_IMG_LEGEND, BASE_HF_IMG_SPLIT_DF,
    BASE_HF_IMG_DF, BASE_HF_IMG_LABELS_DF, BASE_HF_IMG_LEGEND_DF,
    BASE_HF_IMG_SPLIT,
    SAMPLE_MULTI_VCF, SAMPLE_MULTI_DF, IMGDIR
)


def main():  # pragma: no cover
    """ Create the test files needed. """
    fig, ax = _plot_mito()
    plt.savefig(BASE_MITO)
    plt.close()

    fig, ax = _plot_mito(legend=True)
    plt.savefig(BASE_MITO_LEGEND)
    plt.close()

    fig, ax = _plot_mito(split=True)
    plt.savefig(BASE_MITO_SPLIT)
    plt.close()

    plot_vcf(in_vcf=SAMPLE_VCF, save=True, output=BASE_IMG)
    plot_vcf(in_vcf=SAMPLE_VCF, save=True, output=BASE_IMG_LABELS,
             labels=True)
    plot_vcf(in_vcf=SAMPLE_VCF, save=True, output=BASE_IMG_LEGEND,
             legend=True)
    plot_vcf(in_vcf=SAMPLE_VCF, save=True, output=BASE_IMG_SPLIT,
             split=True)

    plot_df(in_df=SAMPLE_DF, save=True, output=BASE_IMG_DF)
    plot_df(in_df=SAMPLE_DF, save=True, output=BASE_IMG_LABELS_DF,
            labels=True)
    plot_df(in_df=SAMPLE_DF, save=True, output=BASE_IMG_LEGEND_DF,
            legend=True)
    plot_df(in_df=SAMPLE_DF, save=True, output=BASE_IMG_SPLIT_DF,
            split=True)

    plot_vcf(in_vcf=SAMPLE_HF_VCF, save=True, output=BASE_HF_IMG)
    plot_vcf(in_vcf=SAMPLE_HF_VCF, save=True,
             output=BASE_HF_IMG_LABELS, labels=True)
    plot_vcf(in_vcf=SAMPLE_HF_VCF, save=True,
             output=BASE_HF_IMG_LEGEND, legend=True)
    plot_vcf(in_vcf=SAMPLE_HF_VCF, save=True,
             output=BASE_HF_IMG_SPLIT, split=True)

    plot_df(in_df=SAMPLE_HF_DF, save=True, output=BASE_HF_IMG_DF)
    plot_df(in_df=SAMPLE_HF_DF, save=True,
            output=BASE_HF_IMG_LABELS_DF, labels=True)
    plot_df(in_df=SAMPLE_HF_DF, save=True,
            output=BASE_HF_IMG_LEGEND_DF, legend=True)
    plot_df(in_df=SAMPLE_HF_DF, save=True,
            output=BASE_HF_IMG_SPLIT_DF, split=True)

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


if __name__ == '__main__':
    main()
