#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os  # pragma: no cover

TESTDIR = os.path.dirname(os.path.realpath(__file__))
DATADIR = os.path.join(TESTDIR, "data")
IMGDIR = os.path.join(TESTDIR, "images")

SAMPLE_VCF = os.path.join(DATADIR, "sample.vcf")
SAMPLE_HF_VCF = os.path.join(DATADIR, "sample_hf.vcf")
SAMPLE_MULTI_VCF = os.path.join(DATADIR, "multisample.vcf")

BASE_IMG = os.path.join(IMGDIR, "sample.png")
BASE_IMG_LABELS = os.path.join(IMGDIR, "sample_labels.png")
BASE_IMG_LEGEND = os.path.join(IMGDIR, "sample_legend.png")

BASE_HF_IMG = os.path.join(IMGDIR, "sample_hf.png")
BASE_HF_IMG_LABELS = os.path.join(IMGDIR, "sample_hf_labels.png")
BASE_HF_IMG_LEGEND = os.path.join(IMGDIR, "sample_hf_legend.png")

BASE_MULTI_IMG = os.path.join(IMGDIR, "multisample_1.png")
BASE_MULTI_IMG_LABELS = os.path.join(IMGDIR, "multisample_labels_1.png")
BASE_MULTI_IMG_LEGEND = os.path.join(IMGDIR, "multisample_legend_1.png")

OUTPUT_IMG = os.path.join(IMGDIR, "out_plot.png")
OUTPUT_HF_IMG = os.path.join(IMGDIR, "out_hf_plot.png")
OUTPUT_MULTI_IMG = os.path.join(IMGDIR, "out_multi_plot.png")
