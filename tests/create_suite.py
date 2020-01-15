#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os

from mitoviz import plot_df, plot_vcf
from constants import (
    SAMPLE_VCF, SAMPLE_HF_VCF,
    SAMPLE_DF, SAMPLE_HF_DF,
    BASE_IMG, BASE_IMG_LABELS, BASE_IMG_LEGEND,
    BASE_IMG_DF, BASE_IMG_LABELS_DF, BASE_IMG_LEGEND_DF,
    BASE_HF_IMG, BASE_HF_IMG_LEGEND, BASE_HF_IMG_LABELS,
    BASE_HF_IMG_DF, BASE_HF_IMG_LEGEND_DF, BASE_HF_IMG_LABELS_DF,
    SAMPLE_MULTI_VCF, SAMPLE_MULTI_DF, IMGDIR
)


def main():  # pragma: no cover
    """ Create the test files needed. """
    plot_vcf(in_vcf=SAMPLE_VCF, save=True, output=BASE_IMG)
    plot_vcf(in_vcf=SAMPLE_VCF, save=True, output=BASE_IMG_LABELS,
             labels=True)
    plot_vcf(in_vcf=SAMPLE_VCF, save=True, output=BASE_IMG_LEGEND,
             legend=True)

    plot_df(in_df=SAMPLE_DF, save=True, output=BASE_IMG_DF)
    plot_df(in_df=SAMPLE_DF, save=True, output=BASE_IMG_LABELS_DF,
            labels=True)
    plot_df(in_df=SAMPLE_DF, save=True, output=BASE_IMG_LEGEND_DF,
            legend=True)

    plot_vcf(in_vcf=SAMPLE_HF_VCF, save=True, output=BASE_HF_IMG)
    plot_vcf(in_vcf=SAMPLE_HF_VCF, save=True,
             output=BASE_HF_IMG_LABELS, labels=True)
    plot_vcf(in_vcf=SAMPLE_HF_VCF, save=True,
             output=BASE_HF_IMG_LEGEND, legend=True)

    plot_df(in_df=SAMPLE_HF_DF, save=True, output=BASE_HF_IMG_DF)
    plot_df(in_df=SAMPLE_HF_DF, save=True,
            output=BASE_HF_IMG_LABELS_DF, labels=True)
    plot_df(in_df=SAMPLE_HF_DF, save=True,
            output=BASE_HF_IMG_LEGEND_DF, legend=True)

    plot_vcf(in_vcf=SAMPLE_MULTI_VCF, save=True,
             output=os.path.join(IMGDIR, "multisample.png"))
    plot_vcf(in_vcf=SAMPLE_MULTI_VCF, save=True,
             output=os.path.join(IMGDIR, "multisample_labels.png"),
             labels=True)
    plot_vcf(in_vcf=SAMPLE_MULTI_VCF, save=True,
             output=os.path.join(IMGDIR, "multisample_legend.png"),
             legend=True)

    plot_df(in_df=SAMPLE_MULTI_DF, save=True,
            output=os.path.join(IMGDIR, "multisample_df.png"))
    plot_df(in_df=SAMPLE_MULTI_DF, save=True,
            output=os.path.join(IMGDIR, "multisample_labels_df.png"),
            labels=True)
    plot_df(in_df=SAMPLE_MULTI_DF, save=True,
            output=os.path.join(IMGDIR, "multisample_legend_df.png"),
            legend=True)


if __name__ == '__main__':
    main()
