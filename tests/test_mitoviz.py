#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os
import unittest

from click.testing import CliRunner
import cv2
import numpy as np

from mitoviz import cli

TESTDIR = os.path.dirname(os.path.realpath(__file__))
DATADIR = os.path.join(TESTDIR, "data")
IMGDIR = os.path.join(TESTDIR, "images")
SAMPLE_VCF = os.path.join(DATADIR, "sample.vcf")
SAMPLE_HF_VCF = os.path.join(DATADIR, "sample_hf.vcf")
SAMPLE_MULTI_VCF = os.path.join(DATADIR, "multisample.vcf")
BASE_IMG = os.path.join(IMGDIR, "sample.png")
BASE_HF_IMG = os.path.join(IMGDIR, "sample_hf.png")
BASE_MULTI_IMG = os.path.join(IMGDIR, "multisample_1.png")
OUTPUT_IMG = os.path.join(IMGDIR, "out_plot.png")
OUTPUT_HF_IMG = os.path.join(IMGDIR, "out_hf_plot.png")
OUTPUT_MULTI_IMG = os.path.join(IMGDIR, "out_multi_plot.png")


class TestCli(unittest.TestCase):

    def setUp(self) -> None:
        self.runner = CliRunner()

    def test_cli_help(self):
        # Given/When
        result = self.runner.invoke(cli.main, ["--help"])

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertIn("Show this message and exit.", result.output)

    def test_cli_plot(self):
        # Given
        base_img = cv2.imread(BASE_IMG)

        # When
        result = self.runner.invoke(cli.main, [SAMPLE_VCF])
        result_img = cv2.imread("MITOVIZ001.png")

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile("MITOVIZ001.png"))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove("MITOVIZ001.png")

    def test_cli_plot_hf(self):
        # Given
        base_img = cv2.imread(BASE_HF_IMG)

        # When
        result = self.runner.invoke(cli.main, [SAMPLE_HF_VCF])
        result_img = cv2.imread("HG00420.png")

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile("HG00420.png"))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove("HG00420.png")

    def test_cli_plot_output(self):
        # Given
        base_img = cv2.imread(BASE_IMG)

        # When
        result = self.runner.invoke(cli.main,
                                    [SAMPLE_VCF,
                                     "--output", OUTPUT_IMG])
        result_img = cv2.imread(OUTPUT_IMG)

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile(OUTPUT_IMG))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove(OUTPUT_IMG)

    def test_cli_plot_output_hf(self):
        # Given
        base_img = cv2.imread(BASE_HF_IMG)

        # When
        result = self.runner.invoke(cli.main,
                                    [SAMPLE_HF_VCF,
                                     "--output", OUTPUT_HF_IMG])
        result_img = cv2.imread(OUTPUT_HF_IMG)

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile(OUTPUT_HF_IMG))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove(OUTPUT_HF_IMG)

    def test_cli_plot_sample_multi(self):
        # Given
        base_img = cv2.imread(BASE_MULTI_IMG)

        # When
        result = self.runner.invoke(cli.main,
                                    [SAMPLE_MULTI_VCF,
                                     "--sample", "SRR1777294",
                                     "--output", OUTPUT_MULTI_IMG])
        result_img = cv2.imread(OUTPUT_MULTI_IMG)

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile(OUTPUT_MULTI_IMG))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove(OUTPUT_MULTI_IMG)
