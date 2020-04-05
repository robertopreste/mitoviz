#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os
import unittest

import cv2
import numpy as np

from mitoviz.mitoviz import plot_base, plot_df, plot_table, plot_vcf
from mitoviz.tests.constants import (
    SAMPLE_VCF, SAMPLE_HF_VCF, SAMPLE_MULTI_VCF, SAMPLE_CUSTOM_DF,
    SAMPLE_DF, SAMPLE_HF_DF, SAMPLE_MULTI_DF,
    SAMPLE_HF_CSV, SAMPLE_HF_TSV, SAMPLE_HF_TSV_COMM,
    BASE_IMG, BASE_IMG_LABELS, BASE_IMG_LEGEND,
    BASE_IMG_DF, BASE_IMG_LABELS_DF, BASE_IMG_LEGEND_DF,
    BASE_HF_IMG, BASE_HF_IMG_LABELS, BASE_HF_IMG_LEGEND,
    BASE_HF_IMG_DF, BASE_HF_IMG_LABELS_DF, BASE_HF_IMG_LEGEND_DF,
    BASE_MULTI_IMG, BASE_MULTI_IMG_LABELS, BASE_MULTI_IMG_LEGEND,
    BASE_MULTI_IMG_DF, BASE_MULTI_IMG_LABELS_DF, BASE_MULTI_IMG_LEGEND_DF,
    BASE_MITO_POLAR, BASE_MITO_POLAR_LEGEND, BASE_MITO_POLAR_SPLIT,
    BASE_MITO_LINEAR, BASE_MITO_LINEAR_LEGEND, BASE_MITO_LINEAR_SPLIT,
    BASE_MITO_PLOTLY, BASE_MITO_PLOTLY_LEGEND, BASE_MITO_PLOTLY_SPLIT,
    BASE_MITO_PLOTLY_LINEAR, BASE_MITO_PLOTLY_LINEAR_LEGEND,
    BASE_MITO_PLOTLY_LINEAR_SPLIT, OUTPUT_IMG, OUTPUT_HF_IMG, OUTPUT_MULTI_IMG,
    OUTPUT_HTML
)


class TestModuleBase(unittest.TestCase):

    def test_module_base_polar(self):
        # Given
        base_img = cv2.imread(BASE_MITO_POLAR)

        # When
        plot_base(save=True)
        result_img = cv2.imread("base_mt.png")

        # Then
        self.assertTrue(os.path.isfile("base_mt.png"))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove("base_mt.png")

    def test_module_base_linear(self):
        # Given
        base_img = cv2.imread(BASE_MITO_LINEAR)

        # When
        plot_base(linear=True, save=True)
        result_img = cv2.imread("base_mt.png")

        # Then
        self.assertTrue(os.path.isfile("base_mt.png"))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove("base_mt.png")

    def test_module_base_polar_plotly(self):
        # Given
        base_img = BASE_MITO_PLOTLY
        test_img = "base_mt.html"

        # When
        plot_base(interactive=True, save=True)

        # Then
        self.assertTrue(os.path.isfile(test_img))
        self.assertEqual(os.path.getsize(base_img), os.path.getsize(test_img))
        # Cleanup
        os.remove(test_img)

    def test_module_base_linear_plotly(self):
        # Given
        base_img = BASE_MITO_PLOTLY_LINEAR
        test_img = "base_mt.html"

        # When
        plot_base(linear=True, interactive=True, save=True)

        # Then
        self.assertTrue(os.path.isfile(test_img))
        self.assertEqual(os.path.getsize(base_img), os.path.getsize(test_img))
        # Cleanup
        os.remove(test_img)

    def test_module_plot_polar_legend(self):
        # Given
        base_img = cv2.imread(BASE_MITO_POLAR_LEGEND)

        # When
        plot_base(legend=True, save=True)
        result_img = cv2.imread("base_mt.png")

        # Then
        self.assertTrue(os.path.isfile("base_mt.png"))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove("base_mt.png")

    def test_module_base_linear_legend(self):
        # Given
        base_img = cv2.imread(BASE_MITO_LINEAR_LEGEND)

        # When
        plot_base(legend=True, linear=True, save=True)
        result_img = cv2.imread("base_mt.png")

        # Then
        self.assertTrue(os.path.isfile("base_mt.png"))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove("base_mt.png")

    def test_module_base_polar_plotly_legend(self):
        # Given
        base_img = BASE_MITO_PLOTLY_LEGEND
        test_img = "base_mt.html"

        # When
        plot_base(legend=True, interactive=True, save=True)

        # Then
        self.assertTrue(os.path.isfile(test_img))
        self.assertEqual(os.path.getsize(base_img), os.path.getsize(test_img))
        # Cleanup
        os.remove(test_img)

    def test_module_base_linear_plotly_legend(self):
        # Given
        base_img = BASE_MITO_PLOTLY_LINEAR_LEGEND
        test_img = "base_mt.html"

        # When
        plot_base(legend=True, linear=True, interactive=True, save=True)

        # Then
        self.assertTrue(os.path.isfile(test_img))
        self.assertEqual(os.path.getsize(base_img), os.path.getsize(test_img))
        # Cleanup
        os.remove(test_img)

    def test_module_base_output(self):
        # Given
        base_img = cv2.imread(BASE_MITO_POLAR)

        # When
        plot_base(output=OUTPUT_IMG, save=True)
        result_img = cv2.imread(OUTPUT_IMG)

        # Then
        self.assertTrue(os.path.isfile(OUTPUT_IMG))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove(OUTPUT_IMG)

    def test_module_base_plotly_output(self):
        # Given
        base_img = BASE_MITO_PLOTLY
        test_img = OUTPUT_HTML

        # When
        plot_base(interactive=True, output=test_img, save=True)

        # Then
        self.assertTrue(os.path.isfile(test_img))
        self.assertEqual(os.path.getsize(base_img), os.path.getsize(test_img))
        # Cleanup
        os.remove(test_img)

    def test_module_base_polar_split(self):
        # Given
        base_img = cv2.imread(BASE_MITO_POLAR_SPLIT)

        # When
        plot_base(split=True, save=True)
        result_img = cv2.imread("base_mt.png")

        # Then
        self.assertTrue(os.path.isfile("base_mt.png"))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove("base_mt.png")

    def test_module_base_linear_split(self):
        # Given
        base_img = cv2.imread(BASE_MITO_LINEAR_SPLIT)

        # When
        plot_base(split=True, linear=True, save=True)
        result_img = cv2.imread("base_mt.png")

        # Then
        self.assertTrue(os.path.isfile("base_mt.png"))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove("base_mt.png")

    def test_module_base_polar_plotly_split(self):
        # Given
        base_img = BASE_MITO_PLOTLY_SPLIT
        test_img = "base_mt.html"

        # When
        plot_base(split=True, interactive=True, save=True)

        # Then
        self.assertTrue(os.path.isfile(test_img))
        self.assertEqual(os.path.getsize(base_img), os.path.getsize(test_img))
        # Cleanup
        os.remove(test_img)

    def test_module_base_linear_plotly_split(self):
        # Given
        base_img = BASE_MITO_PLOTLY_LINEAR_SPLIT
        test_img = "base_mt.html"

        # When
        plot_base(split=True, linear=True, interactive=True, save=True)

        # Then
        self.assertTrue(os.path.isfile(test_img))
        self.assertEqual(os.path.getsize(base_img), os.path.getsize(test_img))
        # Cleanup
        os.remove(test_img)


class TestModuleVcf(unittest.TestCase):

    def test_module_plot(self):
        # Given
        base_img = cv2.imread(BASE_IMG)

        # When
        plot_vcf(SAMPLE_VCF, save=True)
        result_img = cv2.imread("MITOVIZ001.png")

        # Then
        self.assertTrue(os.path.isfile("MITOVIZ001.png"))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove("MITOVIZ001.png")

    def test_module_plot_labels(self):
        # Given
        base_img = cv2.imread(BASE_IMG_LABELS)

        # When
        plot_vcf(SAMPLE_VCF, save=True, labels=True)
        result_img = cv2.imread("MITOVIZ001.png")

        # Then
        self.assertTrue(os.path.isfile("MITOVIZ001.png"))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove("MITOVIZ001.png")

    def test_module_plot_legend(self):
        # Given
        base_img = cv2.imread(BASE_IMG_LEGEND)

        # When
        plot_vcf(SAMPLE_VCF, save=True, legend=True)
        result_img = cv2.imread("MITOVIZ001.png")

        # Then
        self.assertTrue(os.path.isfile("MITOVIZ001.png"))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove("MITOVIZ001.png")

    def test_module_plot_output(self):
        # Given
        base_img = cv2.imread(BASE_IMG)

        # When
        plot_vcf(SAMPLE_VCF, save=True, output=OUTPUT_IMG)
        result_img = cv2.imread(OUTPUT_IMG)

        # Then
        self.assertTrue(os.path.isfile(OUTPUT_IMG))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove(OUTPUT_IMG)

    def test_module_plot_hf(self):
        # Given
        base_img = cv2.imread(BASE_HF_IMG)

        # When
        plot_vcf(SAMPLE_HF_VCF, save=True)
        result_img = cv2.imread("HG00420.png")

        # Then
        self.assertTrue(os.path.isfile("HG00420.png"))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove("HG00420.png")

    def test_module_plot_hf_labels(self):
        # Given
        base_img = cv2.imread(BASE_HF_IMG_LABELS)

        # When
        plot_vcf(SAMPLE_HF_VCF, save=True, labels=True)
        result_img = cv2.imread("HG00420.png")

        # Then
        self.assertTrue(os.path.isfile("HG00420.png"))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove("HG00420.png")

    def test_module_plot_hf_legend(self):
        # Given
        base_img = cv2.imread(BASE_HF_IMG_LEGEND)

        # When
        plot_vcf(SAMPLE_HF_VCF, save=True, legend=True)
        result_img = cv2.imread("HG00420.png")

        # Then
        self.assertTrue(os.path.isfile("HG00420.png"))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove("HG00420.png")

    def test_module_plot_hf_output(self):
        # Given
        base_img = cv2.imread(BASE_HF_IMG)

        # When
        plot_vcf(SAMPLE_HF_VCF, save=True, output=OUTPUT_HF_IMG)
        result_img = cv2.imread(OUTPUT_HF_IMG)

        # Then
        self.assertTrue(os.path.isfile(OUTPUT_HF_IMG))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove(OUTPUT_HF_IMG)

    def test_module_plot_sample_multi(self):
        # Given
        base_img = cv2.imread(BASE_MULTI_IMG)

        # When
        plot_vcf(SAMPLE_MULTI_VCF, sample="SRR1777294",
                 save=True, output=OUTPUT_MULTI_IMG)
        result_img = cv2.imread(OUTPUT_MULTI_IMG)

        # Then
        self.assertTrue(os.path.isfile(OUTPUT_MULTI_IMG))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove(OUTPUT_MULTI_IMG)

    def test_module_plot_sample_multi_labels(self):
        # Given
        base_img = cv2.imread(BASE_MULTI_IMG_LABELS)

        # When
        plot_vcf(SAMPLE_MULTI_VCF, sample="SRR1777294",
                 save=True, output=OUTPUT_MULTI_IMG, labels=True)
        result_img = cv2.imread(OUTPUT_MULTI_IMG)

        # Then
        self.assertTrue(os.path.isfile(OUTPUT_MULTI_IMG))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove(OUTPUT_MULTI_IMG)

    def test_module_plot_sample_multi_legend(self):
        # Given
        base_img = cv2.imread(BASE_MULTI_IMG_LEGEND)

        # When
        plot_vcf(SAMPLE_MULTI_VCF, sample="SRR1777294",
                 save=True, output=OUTPUT_MULTI_IMG, legend=True)
        result_img = cv2.imread(OUTPUT_MULTI_IMG)

        # Then
        self.assertTrue(os.path.isfile(OUTPUT_MULTI_IMG))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove(OUTPUT_MULTI_IMG)


class TestModuleDataFrame(unittest.TestCase):

    def test_module_plot(self):
        # Given
        base_img = cv2.imread(BASE_IMG_DF)

        # When
        plot_df(SAMPLE_DF, save=True)
        result_img = cv2.imread("MITOVIZ001.png")

        # Then
        self.assertTrue(os.path.isfile("MITOVIZ001.png"))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove("MITOVIZ001.png")

    def test_module_plot_labels(self):
        # Given
        base_img = cv2.imread(BASE_IMG_LABELS_DF)

        # When
        plot_df(SAMPLE_DF, save=True, labels=True)
        result_img = cv2.imread("MITOVIZ001.png")

        # Then
        self.assertTrue(os.path.isfile("MITOVIZ001.png"))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove("MITOVIZ001.png")

    def test_module_plot_legend(self):
        # Given
        base_img = cv2.imread(BASE_IMG_LEGEND_DF)

        # When
        plot_df(SAMPLE_DF, save=True, legend=True)
        result_img = cv2.imread("MITOVIZ001.png")

        # Then
        self.assertTrue(os.path.isfile("MITOVIZ001.png"))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove("MITOVIZ001.png")

    def test_module_plot_output(self):
        # Given
        base_img = cv2.imread(BASE_IMG_DF)

        # When
        plot_df(SAMPLE_DF, save=True, output=OUTPUT_IMG)
        result_img = cv2.imread(OUTPUT_IMG)

        # Then
        self.assertTrue(os.path.isfile(OUTPUT_IMG))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove(OUTPUT_IMG)

    def test_module_plot_hf(self):
        # Given
        base_img = cv2.imread(BASE_HF_IMG_DF)

        # When
        plot_df(SAMPLE_HF_DF, save=True)
        result_img = cv2.imread("HG00420.png")

        # Then
        self.assertTrue(os.path.isfile("HG00420.png"))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove("HG00420.png")

    def test_module_plot_hf_labels(self):
        # Given
        base_img = cv2.imread(BASE_HF_IMG_LABELS_DF)

        # When
        plot_df(SAMPLE_HF_DF, save=True, labels=True)
        result_img = cv2.imread("HG00420.png")

        # Then
        self.assertTrue(os.path.isfile("HG00420.png"))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove("HG00420.png")

    def test_module_plot_hf_legend(self):
        # Given
        base_img = cv2.imread(BASE_HF_IMG_LEGEND_DF)

        # When
        plot_df(SAMPLE_HF_DF, save=True, legend=True)
        result_img = cv2.imread("HG00420.png")

        # Then
        self.assertTrue(os.path.isfile("HG00420.png"))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove("HG00420.png")

    def test_module_plot_hf_output(self):
        # Given
        base_img = cv2.imread(BASE_HF_IMG_DF)

        # When
        plot_df(SAMPLE_HF_DF, save=True, output=OUTPUT_HF_IMG)
        result_img = cv2.imread(OUTPUT_HF_IMG)

        # Then
        self.assertTrue(os.path.isfile(OUTPUT_HF_IMG))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove(OUTPUT_HF_IMG)

    def test_module_plot_custom(self):
        # Given
        base_img = cv2.imread(BASE_HF_IMG_DF)

        # When
        plot_df(SAMPLE_CUSTOM_DF, save=True,
                pos_col="position",
                ref_col="reference",
                alt_col="alternate",
                sample_col="samplename",
                hf_col="het_frac")
        result_img = cv2.imread("HG00420.png")

        # Then
        self.assertTrue(os.path.isfile("HG00420.png"))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove("HG00420.png")

    def test_module_plot_sample_multi(self):
        # Given
        base_img = cv2.imread(BASE_MULTI_IMG_DF)

        # When
        plot_df(SAMPLE_MULTI_DF, sample="SRR1777294",
                save=True, output=OUTPUT_MULTI_IMG)
        result_img = cv2.imread(OUTPUT_MULTI_IMG)

        # Then
        self.assertTrue(os.path.isfile(OUTPUT_MULTI_IMG))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove(OUTPUT_MULTI_IMG)

    def test_module_plot_sample_multi_labels(self):
        # Given
        base_img = cv2.imread(BASE_MULTI_IMG_LABELS_DF)

        # When
        plot_df(SAMPLE_MULTI_DF, sample="SRR1777294",
                save=True, output=OUTPUT_MULTI_IMG, labels=True)
        result_img = cv2.imread(OUTPUT_MULTI_IMG)

        # Then
        self.assertTrue(os.path.isfile(OUTPUT_MULTI_IMG))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove(OUTPUT_MULTI_IMG)

    def test_module_plot_sample_multi_legend(self):
        # Given
        base_img = cv2.imread(BASE_MULTI_IMG_LEGEND_DF)

        # When
        plot_df(SAMPLE_MULTI_DF, sample="SRR1777294",
                save=True, output=OUTPUT_MULTI_IMG, legend=True)
        result_img = cv2.imread(OUTPUT_MULTI_IMG)

        # Then
        self.assertTrue(os.path.isfile(OUTPUT_MULTI_IMG))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove(OUTPUT_MULTI_IMG)


class TestModuleTabular(unittest.TestCase):

    def test_module_plot_csv(self):
        # Given
        base_img = cv2.imread(BASE_HF_IMG_DF)

        # When
        plot_table(SAMPLE_HF_CSV, save=True)
        result_img = cv2.imread("HG00420.png")

        # Then
        self.assertTrue(os.path.isfile("HG00420.png"))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove("HG00420.png")

    def test_module_plot_csv_labels(self):
        # Given
        base_img = cv2.imread(BASE_HF_IMG_LABELS_DF)

        # When
        plot_table(SAMPLE_HF_CSV, save=True, labels=True)
        result_img = cv2.imread("HG00420.png")

        # Then
        self.assertTrue(os.path.isfile("HG00420.png"))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove("HG00420.png")

    def test_module_plot_csv_legend(self):
        # Given
        base_img = cv2.imread(BASE_HF_IMG_LEGEND_DF)

        # When
        plot_table(SAMPLE_HF_CSV, save=True, legend=True)
        result_img = cv2.imread("HG00420.png")

        # Then
        self.assertTrue(os.path.isfile("HG00420.png"))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove("HG00420.png")

    def test_module_plot_csv_output(self):
        # Given
        base_img = cv2.imread(BASE_HF_IMG_DF)

        # When
        plot_table(SAMPLE_HF_CSV, save=True, output=OUTPUT_HF_IMG)
        result_img = cv2.imread(OUTPUT_HF_IMG)

        # Then
        self.assertTrue(os.path.isfile(OUTPUT_HF_IMG))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove(OUTPUT_HF_IMG)

    def test_module_plot_tsv(self):
        # Given
        base_img = cv2.imread(BASE_HF_IMG_DF)

        # When
        plot_table(SAMPLE_HF_TSV, sep="\t", save=True)
        result_img = cv2.imread("HG00420.png")

        # Then
        self.assertTrue(os.path.isfile("HG00420.png"))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove("HG00420.png")

    def test_module_plot_tsv_labels(self):
        # Given
        base_img = cv2.imread(BASE_HF_IMG_LABELS_DF)

        # When
        plot_table(SAMPLE_HF_TSV, sep="\t", save=True, labels=True)
        result_img = cv2.imread("HG00420.png")

        # Then
        self.assertTrue(os.path.isfile("HG00420.png"))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove("HG00420.png")

    def test_module_plot_tsv_legend(self):
        # Given
        base_img = cv2.imread(BASE_HF_IMG_LEGEND_DF)

        # When
        plot_table(SAMPLE_HF_TSV, sep="\t", save=True, legend=True)
        result_img = cv2.imread("HG00420.png")

        # Then
        self.assertTrue(os.path.isfile("HG00420.png"))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove("HG00420.png")

    def test_module_plot_tsv_output(self):
        # Given
        base_img = cv2.imread(BASE_HF_IMG_DF)

        # When
        plot_table(SAMPLE_HF_TSV, sep="\t", save=True, output=OUTPUT_HF_IMG)
        result_img = cv2.imread(OUTPUT_HF_IMG)

        # Then
        self.assertTrue(os.path.isfile(OUTPUT_HF_IMG))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove(OUTPUT_HF_IMG)

    def test_module_plot_tsv_comment(self):
        # Given
        base_img = cv2.imread(BASE_HF_IMG_DF)

        # When
        plot_table(SAMPLE_HF_TSV_COMM, sep="\t", save=True, comment="#")
        result_img = cv2.imread("HG00420.png")

        # Then
        self.assertTrue(os.path.isfile("HG00420.png"))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove("HG00420.png")
