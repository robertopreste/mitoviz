#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os

from mitoviz import plot_vcf
from constants import (
    SAMPLE_VCF, SAMPLE_HF_VCF, BASE_IMG, BASE_IMG_LABELS,
    BASE_IMG_LEGEND, BASE_HF_IMG_LEGEND,
    BASE_HF_IMG, BASE_HF_IMG_LABELS, SAMPLE_MULTI_VCF, IMGDIR
)


def main():  # pragma: no cover
    """ Create the test files needed. """
    plot_vcf(in_vcf=SAMPLE_VCF, save=True, output=BASE_IMG)
    plot_vcf(in_vcf=SAMPLE_VCF, save=True, output=BASE_IMG_LABELS,
             labels=True)
    plot_vcf(in_vcf=SAMPLE_VCF, save=True, output=BASE_IMG_LEGEND,
             legend=True)

    plot_vcf(in_vcf=SAMPLE_HF_VCF, save=True, output=BASE_HF_IMG)
    plot_vcf(in_vcf=SAMPLE_HF_VCF, save=True,
             output=BASE_HF_IMG_LABELS, labels=True)
    plot_vcf(in_vcf=SAMPLE_HF_VCF, save=True,
             output=BASE_HF_IMG_LEGEND, legend=True)

    plot_vcf(in_vcf=SAMPLE_MULTI_VCF, save=True,
             output=os.path.join(IMGDIR, "multisample.png"))
    plot_vcf(in_vcf=SAMPLE_MULTI_VCF, save=True,
             output=os.path.join(IMGDIR, "multisample_labels.png"),
             labels=True)
    plot_vcf(in_vcf=SAMPLE_MULTI_VCF, save=True,
             output=os.path.join(IMGDIR, "multisample_legend.png"),
             legend=True)


if __name__ == '__main__':
    main()
