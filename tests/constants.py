#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os  # pragma: no cover

import pandas as pd

TESTDIR = os.path.dirname(os.path.realpath(__file__))
DATADIR = os.path.join(TESTDIR, "data")
IMGDIR = os.path.join(TESTDIR, "images")

SAMPLE_VCF = os.path.join(DATADIR, "sample.vcf")
SAMPLE_HF_VCF = os.path.join(DATADIR, "sample_hf.vcf")
SAMPLE_MULTI_VCF = os.path.join(DATADIR, "multisample.vcf")

BASE_IMG = os.path.join(IMGDIR, "sample.png")
BASE_IMG_LABELS = os.path.join(IMGDIR, "sample_labels.png")
BASE_IMG_LEGEND = os.path.join(IMGDIR, "sample_legend.png")

BASE_IMG_DF = os.path.join(IMGDIR, "sample_df.png")
BASE_IMG_LABELS_DF = os.path.join(IMGDIR, "sample_labels_df.png")
BASE_IMG_LEGEND_DF = os.path.join(IMGDIR, "sample_legend_df.png")

BASE_HF_IMG = os.path.join(IMGDIR, "sample_hf.png")
BASE_HF_IMG_LABELS = os.path.join(IMGDIR, "sample_hf_labels.png")
BASE_HF_IMG_LEGEND = os.path.join(IMGDIR, "sample_hf_legend.png")

BASE_HF_IMG_DF = os.path.join(IMGDIR, "sample_hf_df.png")
BASE_HF_IMG_LABELS_DF = os.path.join(IMGDIR, "sample_hf_labels_df.png")
BASE_HF_IMG_LEGEND_DF = os.path.join(IMGDIR, "sample_hf_legend_df.png")

BASE_MULTI_IMG = os.path.join(IMGDIR, "multisample_1.png")
BASE_MULTI_IMG_LABELS = os.path.join(IMGDIR, "multisample_labels_1.png")
BASE_MULTI_IMG_LEGEND = os.path.join(IMGDIR, "multisample_legend_1.png")

BASE_MULTI_IMG_DF = os.path.join(IMGDIR, "multisample_df_1.png")
BASE_MULTI_IMG_LABELS_DF = os.path.join(IMGDIR, "multisample_labels_df_1.png")
BASE_MULTI_IMG_LEGEND_DF = os.path.join(IMGDIR, "multisample_legend_df_1.png")

OUTPUT_IMG = os.path.join(IMGDIR, "out_plot.png")
OUTPUT_HF_IMG = os.path.join(IMGDIR, "out_hf_plot.png")
OUTPUT_MULTI_IMG = os.path.join(IMGDIR, "out_multi_plot.png")


SAMPLE_DF = pd.DataFrame(
    {"POS": [750, 1438, 2706, 3270, 4216, 7028, 8935, 9389, 11251, 12633],
     "REF": ["A", "A", "A", "CT", "T", "C", "C", "A", "A", "C"],
     "ALT": ["G", "G", "G", "C", "C", "T", "T", "G", "G", "A"]}
)

SAMPLE_HF_DF = pd.DataFrame(
    {"POS": [750, 1438, 2706, 3270, 4216, 7028, 8935, 9389, 11251, 12633],
     "REF": ["A", "A", "A", "CT", "T", "C", "C", "A", "A", "C"],
     "ALT": ["G", "G", "G", "C", "C", "T", "T", "G", "G", "A"],
     "HF": [0.998, 0.232, 0.015, 0.66, 1.0, 0.420, 0.899, 1.0, 0.999, 0.998],
     "SAMPLE": ["HG00420"] * 10}
)

SAMPLE_MULTI_DF = pd.DataFrame(
    {"POS": [750, 1438, 2706, 3270, 4216, 7028, 8935, 9389, 11251, 12633],
     "REF": ["A", "A", "A", "CT", "T", "C", "C", "A", "A", "C"],
     "ALT": ["G", "G", "G", "C", "C", "T", "T", "G", "G", "A"],
     "HF": [0.998, 0.232, 0.015, 0.66, 1.0, 0.420, 0.899, 1.0, 0.999, 0.998],
     "SAMPLE": ["SRR1777294", "SRR1777290", "SRR1777294", "SRR1777290",
                "SRR1777294", "SRR1777290", "SRR1777294", "SRR1777290",
                "SRR1777294", "SRR1777290"]}
)

SAMPLE_CUSTOM_DF = pd.DataFrame(
    {"position": [750, 1438, 2706, 3270, 4216, 7028, 8935, 9389, 11251, 12633],
     "reference": ["A", "A", "A", "CT", "T", "C", "C", "A", "A", "C"],
     "alternate": ["G", "G", "G", "C", "C", "T", "T", "G", "G", "A"],
     "het_frac": [0.998, 0.232, 0.015, 0.66, 1.0, 0.420, 0.899, 1.0, 0.999, 0.998],
     "samplename": ["HG00420"] * 10}
)
