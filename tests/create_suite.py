#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os

from mitoviz import plot_vcf


DATADIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")
IMGDIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")


def main():
    """ Create the test files needed. """
    plot_vcf(in_vcf=os.path.join(DATADIR, "sample.vcf"),
             save=True, output=os.path.join(IMGDIR, "sample.png"))
    plot_vcf(in_vcf=os.path.join(DATADIR, "sample.vcf"),
             save=True, output=os.path.join(IMGDIR, "sample_labels.png"),
             labels=True)
    plot_vcf(in_vcf=os.path.join(DATADIR, "sample_hf.vcf"),
             save=True, output=os.path.join(IMGDIR, "sample_hf.png"))
    plot_vcf(in_vcf=os.path.join(DATADIR, "sample_hf.vcf"),
             save=True, output=os.path.join(IMGDIR, "sample_hf_labels.png"),
             labels=True)
    plot_vcf(in_vcf=os.path.join(DATADIR, "multisample.vcf"),
             save=True, output=os.path.join(IMGDIR, "multisample.png"))
    plot_vcf(in_vcf=os.path.join(DATADIR, "multisample.vcf"),
             save=True, output=os.path.join(IMGDIR, "multisample_labels.png"),
             labels=True)


if __name__ == '__main__':
    main()
