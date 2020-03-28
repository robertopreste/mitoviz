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

SAMPLE_HF_CSV = os.path.join(DATADIR, "sample_hf.csv")
SAMPLE_HF_TSV = os.path.join(DATADIR, "sample_hf.tsv")
SAMPLE_HF_TSV_COMM = os.path.join(DATADIR, "sample_hf_comment.tsv")

# Base

BASE_MITO_POLAR = os.path.join(IMGDIR, "base_mito_polar.png")
BASE_MITO_POLAR_LEGEND = os.path.join(IMGDIR, "base_mito_polar_legend.png")
BASE_MITO_POLAR_SPLIT = os.path.join(IMGDIR, "base_mito_polar_split.png")

BASE_MITO_LINEAR = os.path.join(IMGDIR, "base_mito_linear.png")
BASE_MITO_LINEAR_LEGEND = os.path.join(IMGDIR, "base_mito_linear_legend.png")
BASE_MITO_LINEAR_SPLIT = os.path.join(IMGDIR, "base_mito_linear_split.png")

BASE_MITO_PLOTLY = os.path.join(IMGDIR, "base_mito_plotly.html")
BASE_MITO_PLOTLY_LEGEND = os.path.join(IMGDIR, "base_mito_plotly_legend.html")
BASE_MITO_PLOTLY_SPLIT = os.path.join(IMGDIR, "base_mito_plotly_split.html")

BASE_MITO_PLOTLY_LINEAR = os.path.join(IMGDIR, "base_mito_plotly_linear.html")
BASE_MITO_PLOTLY_LINEAR_LEGEND = os.path.join(
    IMGDIR, "base_mito_plotly_linear_legend.html")
BASE_MITO_PLOTLY_LINEAR_SPLIT = os.path.join(
    IMGDIR, "base_mito_plotly_linear_split.html")

# No HF

BASE_IMG = os.path.join(IMGDIR, "sample.png")
BASE_IMG_LABELS = os.path.join(IMGDIR, "sample_labels.png")
BASE_IMG_LEGEND = os.path.join(IMGDIR, "sample_legend.png")
BASE_IMG_SPLIT = os.path.join(IMGDIR, "sample_split.png")

BASE_IMG_LINEAR = os.path.join(IMGDIR, "sample_linear.png")
BASE_IMG_LINEAR_LABELS = os.path.join(IMGDIR, "sample_linear_labels.png")
BASE_IMG_LINEAR_LEGEND = os.path.join(IMGDIR, "sample_linear_legend.png")
BASE_IMG_LINEAR_SPLIT = os.path.join(IMGDIR, "sample_linear_split.png")

BASE_IMG_PLOTLY = os.path.join(IMGDIR, "sample_plotly.html")
BASE_IMG_PLOTLY_LEGEND = os.path.join(IMGDIR, "sample_plotly_legend.html")
BASE_IMG_PLOTLY_SPLIT = os.path.join(IMGDIR, "sample_plotly_split.html")

BASE_IMG_PLOTLY_LINEAR = os.path.join(IMGDIR, "sample_plotly_linear.html")
BASE_IMG_PLOTLY_LINEAR_LEGEND = os.path.join(
    IMGDIR, "sample_plotly_linear_legend.html")
BASE_IMG_PLOTLY_LINEAR_SPLIT = os.path.join(
    IMGDIR, "sample_plotly_linear_split.html")

# Dataframe no HF

BASE_IMG_DF = os.path.join(IMGDIR, "sample_df.png")
BASE_IMG_LABELS_DF = os.path.join(IMGDIR, "sample_labels_df.png")
BASE_IMG_LEGEND_DF = os.path.join(IMGDIR, "sample_legend_df.png")
BASE_IMG_SPLIT_DF = os.path.join(IMGDIR, "sample_split_df.png")

BASE_IMG_LINEAR_DF = os.path.join(IMGDIR, "sample_linear_df.png")
BASE_IMG_LINEAR_LABELS_DF = os.path.join(IMGDIR, "sample_linear_labels_df.png")
BASE_IMG_LINEAR_LEGEND_DF = os.path.join(IMGDIR, "sample_linear_legend_df.png")
BASE_IMG_LINEAR_SPLIT_DF = os.path.join(IMGDIR, "sample_linear_split_df.png")

BASE_IMG_PLOTLY_DF = os.path.join(IMGDIR, "sample_plotly_df.html")
BASE_IMG_PLOTLY_LEGEND_DF = os.path.join(IMGDIR,
                                         "sample_plotly_legend_df.html")
BASE_IMG_PLOTLY_SPLIT_DF = os.path.join(IMGDIR, "sample_plotly_split_df.html")

BASE_IMG_PLOTLY_LINEAR_DF = os.path.join(
    IMGDIR, "sample_plotly_linear_df.html")
BASE_IMG_PLOTLY_LINEAR_LEGEND_DF = os.path.join(
    IMGDIR, "sample_plotly_linear_legend_df.html")
BASE_IMG_PLOTLY_LINEAR_SPLIT_DF = os.path.join(
    IMGDIR, "sample_plotly_linear_split_df.html")

BASE_HF_IMG = os.path.join(IMGDIR, "sample_hf.png")
BASE_HF_IMG_LABELS = os.path.join(IMGDIR, "sample_hf_labels.png")
BASE_HF_IMG_LEGEND = os.path.join(IMGDIR, "sample_hf_legend.png")
BASE_HF_IMG_SPLIT = os.path.join(IMGDIR, "sample_hf_split.png")

BASE_HF_IMG_LINEAR = os.path.join(IMGDIR, "sample_linear_hf.png")
BASE_HF_IMG_LINEAR_LABELS = os.path.join(IMGDIR, "sample_linear_hf_labels.png")
BASE_HF_IMG_LINEAR_LEGEND = os.path.join(IMGDIR, "sample_linear_hf_legend.png")
BASE_HF_IMG_LINEAR_SPLIT = os.path.join(IMGDIR, "sample_linear_hf_split.png")

BASE_HF_IMG_PLOTLY = os.path.join(IMGDIR, "sample_plotly_hf.html")
BASE_HF_IMG_PLOTLY_LEGEND = os.path.join(IMGDIR,
                                         "sample_plotly_hf_legend.html")
BASE_HF_IMG_PLOTLY_SPLIT = os.path.join(IMGDIR, "sample_plotly_hf_split.html")

BASE_HF_IMG_PLOTLY_LINEAR = os.path.join(
    IMGDIR, "sample_plotly_linear_hf.html")
BASE_HF_IMG_PLOTLY_LINEAR_LEGEND = os.path.join(
    IMGDIR, "sample_plotly_linear_hf_legend.html")
BASE_HF_IMG_PLOTLY_LINEAR_SPLIT = os.path.join(
    IMGDIR, "sample_plotly_linear_hf_split.html")

BASE_HF_IMG_DF = os.path.join(IMGDIR, "sample_hf_df.png")
BASE_HF_IMG_LABELS_DF = os.path.join(IMGDIR, "sample_hf_labels_df.png")
BASE_HF_IMG_LEGEND_DF = os.path.join(IMGDIR, "sample_hf_legend_df.png")
BASE_HF_IMG_SPLIT_DF = os.path.join(IMGDIR, "sample_hf_split_df.png")

BASE_HF_IMG_LINEAR_DF = os.path.join(IMGDIR, "sample_linear_hf_df.png")
BASE_HF_IMG_LINEAR_LABELS_DF = os.path.join(IMGDIR,
                                            "sample_linear_hf_labels_df.png")
BASE_HF_IMG_LINEAR_LEGEND_DF = os.path.join(IMGDIR,
                                            "sample_linear_hf_legend_df.png")
BASE_HF_IMG_LINEAR_SPLIT_DF = os.path.join(IMGDIR,
                                           "sample_linear_hf_split_df.png")

BASE_HF_IMG_PLOTLY_DF = os.path.join(IMGDIR, "sample_plotly_hf_df.html")
BASE_HF_IMG_PLOTLY_LEGEND_DF = os.path.join(IMGDIR,
                                            "sample_plotly_hf_legend_df.html")
BASE_HF_IMG_PLOTLY_SPLIT_DF = os.path.join(IMGDIR,
                                           "sample_plotly_hf_split_df.html")

BASE_HF_IMG_PLOTLY_LINEAR_DF = os.path.join(
    IMGDIR, "sample_plotly_linear_hf_df.html")
BASE_HF_IMG_PLOTLY_LINEAR_LEGEND_DF = os.path.join(
    IMGDIR, "sample_plotly_linear_hf_legend_df.html")
BASE_HF_IMG_PLOTLY_LINEAR_SPLIT_DF = os.path.join(
    IMGDIR, "sample_plotly_linear_hf_split_df.html")

BASE_MULTI_IMG = os.path.join(IMGDIR, "multisample_1.png")
BASE_MULTI_IMG_LABELS = os.path.join(IMGDIR, "multisample_labels_1.png")
BASE_MULTI_IMG_LEGEND = os.path.join(IMGDIR, "multisample_legend_1.png")
BASE_MULTI_IMG_SPLIT = os.path.join(IMGDIR, "multisample_split_1.png")

BASE_MULTI_IMG_LINEAR = os.path.join(IMGDIR, "multisample_linear_1.png")
BASE_MULTI_IMG_LINEAR_LABELS = os.path.join(IMGDIR,
                                            "multisample_linear_labels_1.png")
BASE_MULTI_IMG_LINEAR_LEGEND = os.path.join(IMGDIR,
                                            "multisample_linear_legend_1.png")
BASE_MULTI_IMG_LINEAR_SPLIT = os.path.join(IMGDIR,
                                           "multisample_linear_split_1.png")

BASE_MULTI_IMG_PLOTLY = os.path.join(IMGDIR, "multisample_plotly_1.html")
BASE_MULTI_IMG_PLOTLY_LEGEND = os.path.join(IMGDIR,
                                            "multisample_plotly_legend_1.html")
BASE_MULTI_IMG_PLOTLY_SPLIT = os.path.join(IMGDIR,
                                           "multisample_plotly_split_1.html")

BASE_MULTI_IMG_PLOTLY_LINEAR = os.path.join(
    IMGDIR, "multisample_plotly_linear_1.html")
BASE_MULTI_IMG_PLOTLY_LINEAR_LEGEND = os.path.join(
    IMGDIR, "multisample_plotly_linear_legend_1.html")
BASE_MULTI_IMG_PLOTLY_LINEAR_SPLIT = os.path.join(
    IMGDIR, "multisample_plotly_linear_split_1.html")

BASE_MULTI_IMG_DF = os.path.join(IMGDIR, "multisample_df_1.png")
BASE_MULTI_IMG_LABELS_DF = os.path.join(IMGDIR, "multisample_labels_df_1.png")
BASE_MULTI_IMG_LEGEND_DF = os.path.join(IMGDIR, "multisample_legend_df_1.png")
BASE_MULTI_IMG_SPLIT_DF = os.path.join(IMGDIR, "multisample_split_df_1.png")

BASE_MULTI_IMG_LINEAR_DF = os.path.join(IMGDIR, "multisample_linear_df_1.png")
BASE_MULTI_IMG_LINEAR_LABELS_DF = os.path.join(
    IMGDIR, "multisample_linear_labels_df_1.png")
BASE_MULTI_IMG_LINEAR_LEGEND_DF = os.path.join(
    IMGDIR, "multisample_linear_legend_df_1.png")
BASE_MULTI_IMG_LINEAR_SPLIT_DF = os.path.join(
    IMGDIR, "multisample_linear_split_df_1.png")

BASE_MULTI_IMG_PLOTLY_DF = os.path.join(IMGDIR, "multisample_plotly_df_1.html")
BASE_MULTI_IMG_PLOTLY_LEGEND_DF = os.path.join(
    IMGDIR, "multisample_plotly_legend_df_1.html")
BASE_MULTI_IMG_PLOTLY_SPLIT_DF = os.path.join(
    IMGDIR, "multisample_plotly_split_df_1.html")

BASE_MULTI_IMG_PLOTLY_LINEAR_DF = os.path.join(
    IMGDIR, "multisample_plotly_linear_df_1.html")
BASE_MULTI_IMG_PLOTLY_LINEAR_LEGEND_DF = os.path.join(
    IMGDIR, "multisample_plotly_linear_legend_df_1.html")
BASE_MULTI_IMG_PLOTLY_LINEAR_SPLIT_DF = os.path.join(
    IMGDIR, "multisample_plotly_linear_split_df_1.html")

OUTPUT_IMG = os.path.join(IMGDIR, "out_plot.png")
OUTPUT_HF_IMG = os.path.join(IMGDIR, "out_hf_plot.png")
OUTPUT_MULTI_IMG = os.path.join(IMGDIR, "out_multi_plot.png")

OUTPUT_HTML = os.path.join(IMGDIR, "out_plot.html")
OUTPUT_HF_HTML = os.path.join(IMGDIR, "out_hf_plot.html")
OUTPUT_MULTI_HTML = os.path.join(IMGDIR, "out_multi_plot.html")


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
     "het_frac": [0.998, 0.232, 0.015, 0.66, 1.0, 0.420, 0.899, 1.0, 0.999,
                  0.998],
     "samplename": ["HG00420"] * 10}
)
