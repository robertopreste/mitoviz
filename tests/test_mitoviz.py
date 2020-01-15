#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os
import unittest

import cv2
import numpy as np

from mitoviz import plot_df, plot_vcf
from .constants import (
    SAMPLE_VCF, SAMPLE_HF_VCF, SAMPLE_MULTI_VCF, SAMPLE_CUSTOM_DF,
    SAMPLE_DF, SAMPLE_HF_DF, SAMPLE_MULTI_DF,
    BASE_IMG, BASE_IMG_LABELS, BASE_IMG_LEGEND,
    BASE_IMG_DF, BASE_IMG_LABELS_DF, BASE_IMG_LEGEND_DF,
    BASE_HF_IMG, BASE_HF_IMG_LABELS, BASE_HF_IMG_LEGEND,
    BASE_HF_IMG_DF, BASE_HF_IMG_LABELS_DF, BASE_HF_IMG_LEGEND_DF,
    BASE_MULTI_IMG, BASE_MULTI_IMG_LABELS, BASE_MULTI_IMG_LEGEND,
    BASE_MULTI_IMG_DF, BASE_MULTI_IMG_LABELS_DF, BASE_MULTI_IMG_LEGEND_DF,
    OUTPUT_IMG, OUTPUT_HF_IMG, OUTPUT_MULTI_IMG
)


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
