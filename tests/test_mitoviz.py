#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os
import pytest
import unittest

from click.testing import CliRunner
import cv2
import numpy as np

from mitoviz import mitoviz
from mitoviz import cli

DATADIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "data"
)
SAMPLE_VCF = os.path.join(DATADIR, "sample.vcf")
SAMPLE_HF_VCF = os.path.join(DATADIR, "sample_hf.vcf")
OUTPUT_IMG = os.path.join(DATADIR, "sample_plot.png")
OUTPUT_HF_IMG = os.path.join(DATADIR, "sample_hf_plot.png")


class TestCli(unittest.TestCase):

    def setUp(self) -> None:
        self.runner = CliRunner()

    def tearDown(self) -> None:
        try:
            os.remove("MITOVIZ001.png")
            os.remove(OUTPUT_IMG)
            os.remove(OUTPUT_HF_IMG)
        except FileNotFoundError:
            pass

    def test_cli_help(self):
        # Given/When
        result = self.runner.invoke(cli.main, ["--help"])

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertIn("Show this message and exit.", result.output)

    def test_cli_plot(self):
        # Given
        base_img = cv2.imread("images/sample.png")

        # When
        result = self.runner.invoke(cli.main, [SAMPLE_VCF])
        result_img = cv2.imread("MITOVIZ001.png")

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile("MITOVIZ001.png"))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))

    def test_cli_plot_hf(self):
        # Given
        base_img = cv2.imread("images/sample_hf.png")

        # When
        result = self.runner.invoke(cli.main, [SAMPLE_HF_VCF])
        result_img = cv2.imread("HG00420.png")

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile("HG00420.png"))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))

    def test_cli_plot_output(self):
        # Given
        base_img = cv2.imread("images/sample.png")

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

    def test_cli_plot_output_hf(self):
        # Given
        base_img = cv2.imread("images/sample_hf.png")

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
