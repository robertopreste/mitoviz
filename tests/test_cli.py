#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os
import unittest

import cv2
import numpy as np
from click.testing import CliRunner

from mitoviz import cli
from .constants import (
    SAMPLE_VCF, SAMPLE_HF_VCF, SAMPLE_MULTI_VCF,
    BASE_IMG, BASE_IMG_LABELS, BASE_IMG_LEGEND,
    BASE_HF_IMG, BASE_HF_IMG_LABELS, BASE_HF_IMG_LEGEND,
    BASE_MULTI_IMG, BASE_MULTI_IMG_LABELS, BASE_MULTI_IMG_LEGEND,
    OUTPUT_IMG, OUTPUT_HF_IMG, OUTPUT_MULTI_IMG
)


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

    def test_cli_plot_labels(self):
        # Given
        base_img = cv2.imread(BASE_IMG_LABELS)

        # When
        result = self.runner.invoke(cli.main,
                                    [SAMPLE_VCF, "--labels"])
        result_img = cv2.imread("MITOVIZ001.png")

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile("MITOVIZ001.png"))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove("MITOVIZ001.png")

    def test_cli_plot_legend(self):
        # Given
        base_img = cv2.imread(BASE_IMG_LEGEND)

        # When
        result = self.runner.invoke(cli.main,
                                    [SAMPLE_VCF, "--legend"])
        result_img = cv2.imread("MITOVIZ001.png")

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile("MITOVIZ001.png"))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove("MITOVIZ001.png")

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

    def test_cli_plot_hf_labels(self):
        # Given
        base_img = cv2.imread(BASE_HF_IMG_LABELS)

        # When
        result = self.runner.invoke(cli.main,
                                    [SAMPLE_HF_VCF, "--labels"])
        result_img = cv2.imread("HG00420.png")

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile("HG00420.png"))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove("HG00420.png")

    def test_cli_plot_hf_legend(self):
        # Given
        base_img = cv2.imread(BASE_HF_IMG_LEGEND)

        # When
        result = self.runner.invoke(cli.main,
                                    [SAMPLE_HF_VCF, "--legend"])
        result_img = cv2.imread("HG00420.png")

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile("HG00420.png"))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove("HG00420.png")

    def test_cli_plot_hf_output(self):
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

    def test_cli_plot_sample_multi_labels(self):
        # Given
        base_img = cv2.imread(BASE_MULTI_IMG_LABELS)

        # When
        result = self.runner.invoke(cli.main,
                                    [SAMPLE_MULTI_VCF,
                                     "--sample", "SRR1777294",
                                     "--output", OUTPUT_MULTI_IMG,
                                     "--labels"])
        result_img = cv2.imread(OUTPUT_MULTI_IMG)

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile(OUTPUT_MULTI_IMG))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove(OUTPUT_MULTI_IMG)

    def test_cli_plot_sample_multi_legend(self):
        # Given
        base_img = cv2.imread(BASE_MULTI_IMG_LEGEND)

        # When
        result = self.runner.invoke(cli.main,
                                    [SAMPLE_MULTI_VCF,
                                     "--sample", "SRR1777294",
                                     "--output", OUTPUT_MULTI_IMG,
                                     "--legend"])
        result_img = cv2.imread(OUTPUT_MULTI_IMG)

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile(OUTPUT_MULTI_IMG))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove(OUTPUT_MULTI_IMG)
