#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os
import unittest

import cv2
import numpy as np
from click.testing import CliRunner

from mitoviz.cli import mitoviz_plot as cli
from mitoviz.tests.constants import (
    SAMPLE_VCF, SAMPLE_HF_VCF, SAMPLE_MULTI_VCF, SAMPLE_HF_CSV, SAMPLE_HF_TSV,
    SAMPLE_HF_TSV_COMM,
    BASE_IMG, BASE_IMG_LABELS, BASE_IMG_LEGEND, BASE_IMG_SPLIT,
    BASE_IMG_LINEAR, BASE_IMG_LINEAR_LABELS, BASE_IMG_LINEAR_LEGEND,
    BASE_IMG_LINEAR_SPLIT, BASE_IMG_LABELS_HF, BASE_IMG_LINEAR_LABELS_HF,
    BASE_IMG_PLOTLY, BASE_IMG_PLOTLY_LABELS_HF, BASE_IMG_PLOTLY_LEGEND,
    BASE_IMG_PLOTLY_SPLIT,
    BASE_IMG_PLOTLY_LINEAR, BASE_IMG_PLOTLY_LINEAR_LABELS_HF,
    BASE_IMG_PLOTLY_LINEAR_LEGEND, BASE_IMG_PLOTLY_LINEAR_SPLIT,
    BASE_HF_IMG, BASE_HF_IMG_LABELS, BASE_HF_IMG_LEGEND, BASE_HF_IMG_SPLIT,
    BASE_HF_IMG_LINEAR, BASE_HF_IMG_LINEAR_LABELS, BASE_HF_IMG_LINEAR_LEGEND,
    BASE_HF_IMG_LINEAR_SPLIT,
    BASE_HF_IMG_PLOTLY, BASE_HF_IMG_PLOTLY_LEGEND, BASE_HF_IMG_PLOTLY_SPLIT,
    BASE_HF_IMG_PLOTLY_LINEAR, BASE_HF_IMG_PLOTLY_LINEAR_LEGEND,
    BASE_HF_IMG_PLOTLY_LINEAR_SPLIT,
    BASE_HF_IMG_DF, BASE_HF_IMG_LABELS_DF, BASE_HF_IMG_LEGEND_DF,
    BASE_HF_IMG_SPLIT_DF,
    BASE_HF_IMG_LINEAR_DF, BASE_HF_IMG_LINEAR_LABELS_DF,
    BASE_HF_IMG_LINEAR_LEGEND_DF, BASE_HF_IMG_LINEAR_SPLIT_DF,
    BASE_HF_IMG_PLOTLY_DF, BASE_HF_IMG_PLOTLY_LEGEND_DF,
    BASE_HF_IMG_PLOTLY_SPLIT_DF,
    BASE_MULTI_IMG, BASE_MULTI_IMG_LABELS, BASE_MULTI_IMG_LEGEND,
    BASE_MULTI_IMG_SPLIT,
    BASE_MULTI_IMG_LINEAR, BASE_MULTI_IMG_LINEAR_LABELS,
    BASE_MULTI_IMG_LINEAR_LEGEND, BASE_MULTI_IMG_LINEAR_SPLIT,
    BASE_MULTI_IMG_PLOTLY, BASE_MULTI_IMG_PLOTLY_LEGEND,
    BASE_MULTI_IMG_PLOTLY_SPLIT,
    BASE_MULTI_IMG_PLOTLY_LINEAR, BASE_MULTI_IMG_PLOTLY_LINEAR_LEGEND,
    BASE_MULTI_IMG_PLOTLY_LINEAR_SPLIT,
    OUTPUT_IMG, OUTPUT_HF_IMG, OUTPUT_MULTI_IMG,
    OUTPUT_HTML, OUTPUT_HF_HTML, OUTPUT_MULTI_HTML
)


class TestCliVcf(unittest.TestCase):

    def setUp(self) -> None:
        self.runner = CliRunner()

    def test_cli_plot_help(self):
        # Given/When
        result = self.runner.invoke(cli.main, ["--help"])

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertIn("Show this message and exit.", result.output)

    def test_cli_plot_polar(self):
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

    def test_cli_plot_linear(self):
        # Given
        base_img = cv2.imread(BASE_IMG_LINEAR)

        # When
        result = self.runner.invoke(cli.main, [SAMPLE_VCF, "--linear"])
        result_img = cv2.imread("MITOVIZ001.png")

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile("MITOVIZ001.png"))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove("MITOVIZ001.png")

    def test_cli_plot_polar_plotly(self):
        # Given
        base_img = BASE_IMG_PLOTLY
        test_img = "MITOVIZ001.html"

        # When
        result = self.runner.invoke(cli.main, [SAMPLE_VCF, "--interactive"])

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile(test_img))
        self.assertEqual(os.path.getsize(base_img), os.path.getsize(test_img))
        # Cleanup
        os.remove(test_img)

    def test_cli_plot_linear_plotly(self):
        # Given
        base_img = BASE_IMG_PLOTLY_LINEAR
        test_img = "MITOVIZ001.html"

        # When
        result = self.runner.invoke(cli.main, [SAMPLE_VCF,
                                               "--linear", "--interactive"])

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile(test_img))
        self.assertEqual(os.path.getsize(base_img), os.path.getsize(test_img))
        # Cleanup
        os.remove(test_img)

    def test_cli_plot_polar_labels(self):
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

    def test_cli_plot_polar_labels_hf(self):
        # Given
        base_img = cv2.imread(BASE_IMG_LABELS_HF)

        # When
        result = self.runner.invoke(cli.main,
                                    [SAMPLE_VCF, "--labels", "--labels-hf"])
        result_img = cv2.imread("MITOVIZ001.png")

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile("MITOVIZ001.png"))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove("MITOVIZ001.png")

    def test_cli_plot_linear_labels(self):
        # Given
        base_img = cv2.imread(BASE_IMG_LINEAR_LABELS)

        # When
        result = self.runner.invoke(cli.main,
                                    [SAMPLE_VCF, "--labels", "--linear"])
        result_img = cv2.imread("MITOVIZ001.png")

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile("MITOVIZ001.png"))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove("MITOVIZ001.png")

    def test_cli_plot_linear_labels_hf(self):
        # Given
        base_img = cv2.imread(BASE_IMG_LINEAR_LABELS_HF)

        # When
        result = self.runner.invoke(cli.main,
                                    [SAMPLE_VCF, "--labels", "--labels-hf",
                                     "--linear"])
        result_img = cv2.imread("MITOVIZ001.png")

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile("MITOVIZ001.png"))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove("MITOVIZ001.png")

    def test_cli_plot_polar_legend(self):
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

    def test_cli_plot_linear_legend(self):
        # Given
        base_img = cv2.imread(BASE_IMG_LINEAR_LEGEND)

        # When
        result = self.runner.invoke(cli.main,
                                    [SAMPLE_VCF, "--legend", "--linear"])
        result_img = cv2.imread("MITOVIZ001.png")

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile("MITOVIZ001.png"))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove("MITOVIZ001.png")

    def test_cli_plot_polar_plotly_labels_hf(self):
        # Given
        base_img = BASE_IMG_PLOTLY_LABELS_HF
        test_img = "MITOVIZ001.html"

        # When
        result = self.runner.invoke(cli.main,
                                    [SAMPLE_VCF, "--labels-hf",
                                     "--interactive"])

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile(test_img))
        self.assertEqual(os.path.getsize(base_img), os.path.getsize(test_img))
        # Cleanup
        os.remove(test_img)

    def test_cli_plot_polar_plotly_legend(self):
        # Given
        base_img = BASE_IMG_PLOTLY_LEGEND
        test_img = "MITOVIZ001.html"

        # When
        result = self.runner.invoke(cli.main,
                                    [SAMPLE_VCF, "--legend", "--interactive"])

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile(test_img))
        self.assertEqual(os.path.getsize(base_img), os.path.getsize(test_img))
        # Cleanup
        os.remove(test_img)

    def test_cli_plot_linear_plotly_labels_hf(self):
        # Given
        base_img = BASE_IMG_PLOTLY_LINEAR_LABELS_HF
        test_img = "MITOVIZ001.html"

        # When
        result = self.runner.invoke(cli.main,
                                    [SAMPLE_VCF, "--labels-hf", "--linear",
                                     "--interactive"])

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile(test_img))
        self.assertEqual(os.path.getsize(base_img), os.path.getsize(test_img))
        # Cleanup
        os.remove(test_img)

    def test_cli_plot_linear_plotly_legend(self):
        # Given
        base_img = BASE_IMG_PLOTLY_LINEAR_LEGEND
        test_img = "MITOVIZ001.html"

        # When
        result = self.runner.invoke(cli.main,
                                    [SAMPLE_VCF,
                                     "--legend", "--linear", "--interactive"])

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile(test_img))
        self.assertEqual(os.path.getsize(base_img), os.path.getsize(test_img))
        # Cleanup
        os.remove(test_img)

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

    def test_cli_plotly_output(self):
        # Given
        base_img = BASE_IMG_PLOTLY
        test_img = OUTPUT_HTML

        # When
        result = self.runner.invoke(cli.main,
                                    [SAMPLE_VCF, "--interactive",
                                     "--output", test_img])

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile(test_img))
        self.assertEqual(os.path.getsize(base_img), os.path.getsize(test_img))
        # Cleanup
        os.remove(test_img)

    def test_cli_plot_polar_split(self):
        # Given
        base_img = cv2.imread(BASE_IMG_SPLIT)

        # When
        result = self.runner.invoke(cli.main,
                                    [SAMPLE_VCF, "--split"])
        result_img = cv2.imread("MITOVIZ001.png")

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile("MITOVIZ001.png"))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove("MITOVIZ001.png")

    def test_cli_plot_linear_split(self):
        # Given
        base_img = cv2.imread(BASE_IMG_LINEAR_SPLIT)

        # When
        result = self.runner.invoke(cli.main,
                                    [SAMPLE_VCF, "--split", "--linear"])
        result_img = cv2.imread("MITOVIZ001.png")

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile("MITOVIZ001.png"))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove("MITOVIZ001.png")

    def test_cli_plot_polar_plotly_split(self):
        # Given
        base_img = BASE_IMG_PLOTLY_SPLIT
        test_img = "MITOVIZ001.html"

        # When
        result = self.runner.invoke(cli.main,
                                    [SAMPLE_VCF, "--split", "--interactive"])

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile(test_img))
        self.assertEqual(os.path.getsize(base_img), os.path.getsize(test_img))
        # Cleanup
        os.remove(test_img)

    def test_cli_plot_linear_plotly_split(self):
        # Given
        base_img = BASE_IMG_PLOTLY_LINEAR_SPLIT
        test_img = "MITOVIZ001.html"

        # When
        result = self.runner.invoke(cli.main,
                                    [SAMPLE_VCF,
                                     "--split", "--linear", "--interactive"])

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile(test_img))
        self.assertEqual(os.path.getsize(base_img), os.path.getsize(test_img))
        # Cleanup
        os.remove(test_img)

    def test_cli_plot_hf_polar(self):
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

    def test_cli_plot_hf_linear(self):
        # Given
        base_img = cv2.imread(BASE_HF_IMG_LINEAR)

        # When
        result = self.runner.invoke(cli.main, [SAMPLE_HF_VCF, "--linear"])
        result_img = cv2.imread("HG00420.png")

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile("HG00420.png"))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove("HG00420.png")

    def test_cli_plot_hf_polar_plotly(self):
        # Given
        base_img = BASE_HF_IMG_PLOTLY
        test_img = "HG00420.html"

        # When
        result = self.runner.invoke(cli.main, [SAMPLE_HF_VCF, "--interactive"])

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile(test_img))
        self.assertEqual(os.path.getsize(base_img), os.path.getsize(test_img))
        # Cleanup
        os.remove(test_img)

    def test_cli_plot_hf_linear_plotly(self):
        # Given
        base_img = BASE_HF_IMG_PLOTLY_LINEAR
        test_img = "HG00420.html"

        # When
        result = self.runner.invoke(cli.main, [SAMPLE_HF_VCF,
                                               "--linear", "--interactive"])

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile(test_img))
        self.assertEqual(os.path.getsize(base_img), os.path.getsize(test_img))
        # Cleanup
        os.remove(test_img)

    def test_cli_plot_hf_polar_labels(self):
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

    def test_cli_plot_hf_linear_labels(self):
        # Given
        base_img = cv2.imread(BASE_HF_IMG_LINEAR_LABELS)

        # When
        result = self.runner.invoke(cli.main,
                                    [SAMPLE_HF_VCF, "--labels", "--linear"])
        result_img = cv2.imread("HG00420.png")

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile("HG00420.png"))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove("HG00420.png")

    def test_cli_plot_hf_polar_legend(self):
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

    def test_cli_plot_hf_linear_legend(self):
        # Given
        base_img = cv2.imread(BASE_HF_IMG_LINEAR_LEGEND)

        # When
        result = self.runner.invoke(cli.main,
                                    [SAMPLE_HF_VCF, "--legend", "--linear"])
        result_img = cv2.imread("HG00420.png")

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile("HG00420.png"))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove("HG00420.png")

    def test_cli_plot_hf_polar_plotly_legend(self):
        # Given
        base_img = BASE_HF_IMG_PLOTLY_LEGEND
        test_img = "HG00420.html"

        # When
        result = self.runner.invoke(cli.main,
                                    [SAMPLE_HF_VCF, "--legend",
                                     "--interactive"])

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile(test_img))
        self.assertEqual(os.path.getsize(base_img), os.path.getsize(test_img))
        # Cleanup
        os.remove(test_img)

    def test_cli_plot_hf_linear_plotly_legend(self):
        # Given
        base_img = BASE_HF_IMG_PLOTLY_LINEAR_LEGEND
        test_img = "HG00420.html"

        # When
        result = self.runner.invoke(cli.main,
                                    [SAMPLE_HF_VCF,
                                     "--linear", "--legend", "--interactive"])

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile(test_img))
        self.assertEqual(os.path.getsize(base_img), os.path.getsize(test_img))
        # Cleanup
        os.remove(test_img)

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

    def test_cli_plotly_hf_output(self):
        # Given
        base_img = BASE_HF_IMG_PLOTLY
        test_img = OUTPUT_HF_HTML

        # When
        result = self.runner.invoke(cli.main,
                                    [SAMPLE_HF_VCF, "--interactive",
                                     "--output", test_img])

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile(test_img))
        self.assertEqual(os.path.getsize(base_img), os.path.getsize(test_img))
        # Cleanup
        os.remove(test_img)

    def test_cli_plot_hf_polar_split(self):
        # Given
        base_img = cv2.imread(BASE_HF_IMG_SPLIT)

        # When
        result = self.runner.invoke(cli.main,
                                    [SAMPLE_HF_VCF, "--split"])
        result_img = cv2.imread("HG00420.png")

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile("HG00420.png"))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove("HG00420.png")

    def test_cli_plot_hf_linear_split(self):
        # Given
        base_img = cv2.imread(BASE_HF_IMG_LINEAR_SPLIT)

        # When
        result = self.runner.invoke(cli.main,
                                    [SAMPLE_HF_VCF, "--split", "--linear"])
        result_img = cv2.imread("HG00420.png")

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile("HG00420.png"))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove("HG00420.png")

    def test_cli_plot_hf_polar_plotly_split(self):
        # Given
        base_img = BASE_HF_IMG_PLOTLY_SPLIT
        test_img = "HG00420.html"

        # When
        result = self.runner.invoke(cli.main,
                                    [SAMPLE_HF_VCF, "--split",
                                     "--interactive"])

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile(test_img))
        self.assertEqual(os.path.getsize(base_img), os.path.getsize(test_img))
        # Cleanup
        os.remove(test_img)

    def test_cli_plot_hf_linear_plotly_split(self):
        # Given
        base_img = BASE_HF_IMG_PLOTLY_LINEAR_SPLIT
        test_img = "HG00420.html"

        # When
        result = self.runner.invoke(cli.main,
                                    [SAMPLE_HF_VCF,
                                     "--linear", "--split", "--interactive"])

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile(test_img))
        self.assertEqual(os.path.getsize(base_img), os.path.getsize(test_img))
        # Cleanup
        os.remove(test_img)

    def test_cli_plot_polar_sample_multi(self):
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

    def test_cli_plot_linear_sample_multi(self):
        # Given
        base_img = cv2.imread(BASE_MULTI_IMG_LINEAR)

        # When
        result = self.runner.invoke(cli.main,
                                    [SAMPLE_MULTI_VCF,
                                     "--sample", "SRR1777294",
                                     "--output", OUTPUT_MULTI_IMG,
                                     "--linear"])
        result_img = cv2.imread(OUTPUT_MULTI_IMG)

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile(OUTPUT_MULTI_IMG))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove(OUTPUT_MULTI_IMG)

    def test_cli_plot_polar_plotly_sample_multi(self):
        # Given
        base_img = BASE_MULTI_IMG_PLOTLY
        test_img = OUTPUT_MULTI_HTML

        # When
        result = self.runner.invoke(cli.main,
                                    [SAMPLE_MULTI_VCF,
                                     "--sample", "SRR1777294",
                                     "--output", test_img,
                                     "--interactive"])

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile(test_img))
        self.assertEqual(os.path.getsize(base_img), os.path.getsize(test_img))
        # Cleanup
        os.remove(test_img)

    def test_cli_plot_linear_plotly_sample_multi(self):
        # Given
        base_img = BASE_MULTI_IMG_PLOTLY_LINEAR
        test_img = OUTPUT_MULTI_HTML

        # When
        result = self.runner.invoke(cli.main,
                                    [SAMPLE_MULTI_VCF, "--linear",
                                     "--sample", "SRR1777294",
                                     "--output", test_img,
                                     "--interactive"])

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile(test_img))
        self.assertEqual(os.path.getsize(base_img), os.path.getsize(test_img))
        # Cleanup
        os.remove(test_img)

    def test_cli_plot_polar_sample_multi_labels(self):
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

    def test_cli_plot_linear_sample_multi_labels(self):
        # Given
        base_img = cv2.imread(BASE_MULTI_IMG_LINEAR_LABELS)

        # When
        result = self.runner.invoke(cli.main,
                                    [SAMPLE_MULTI_VCF,
                                     "--sample", "SRR1777294",
                                     "--output", OUTPUT_MULTI_IMG,
                                     "--labels", "--linear"])
        result_img = cv2.imread(OUTPUT_MULTI_IMG)

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile(OUTPUT_MULTI_IMG))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove(OUTPUT_MULTI_IMG)

    def test_cli_plot_polar_sample_multi_legend(self):
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

    def test_cli_plot_linear_sample_multi_legend(self):
        # Given
        base_img = cv2.imread(BASE_MULTI_IMG_LINEAR_LEGEND)

        # When
        result = self.runner.invoke(cli.main,
                                    [SAMPLE_MULTI_VCF,
                                     "--sample", "SRR1777294",
                                     "--output", OUTPUT_MULTI_IMG,
                                     "--legend", "--linear"])
        result_img = cv2.imread(OUTPUT_MULTI_IMG)

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile(OUTPUT_MULTI_IMG))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove(OUTPUT_MULTI_IMG)

    def test_cli_plot_polar_plotly_sample_multi_legend(self):
        # Given
        base_img = BASE_MULTI_IMG_PLOTLY_LEGEND
        test_img = OUTPUT_MULTI_HTML

        # When
        result = self.runner.invoke(cli.main,
                                    [SAMPLE_MULTI_VCF,
                                     "--sample", "SRR1777294",
                                     "--output", test_img,
                                     "--legend", "--interactive"])

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile(test_img))
        self.assertEqual(os.path.getsize(base_img), os.path.getsize(test_img))
        # Cleanup
        os.remove(test_img)

    def test_cli_plot_linear_plotly_sample_multi_legend(self):
        # Given
        base_img = BASE_MULTI_IMG_PLOTLY_LINEAR_LEGEND
        test_img = OUTPUT_MULTI_HTML

        # When
        result = self.runner.invoke(cli.main,
                                    [SAMPLE_MULTI_VCF, "--linear",
                                     "--sample", "SRR1777294",
                                     "--output", test_img,
                                     "--legend", "--interactive"])

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile(test_img))
        self.assertEqual(os.path.getsize(base_img), os.path.getsize(test_img))
        # Cleanup
        os.remove(test_img)

    def test_cli_plot_polar_sample_multi_split(self):
        # Given
        base_img = cv2.imread(BASE_MULTI_IMG_SPLIT)

        # When
        result = self.runner.invoke(cli.main,
                                    [SAMPLE_MULTI_VCF,
                                     "--sample", "SRR1777294",
                                     "--output", OUTPUT_MULTI_IMG,
                                     "--split"])
        result_img = cv2.imread(OUTPUT_MULTI_IMG)

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile(OUTPUT_MULTI_IMG))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove(OUTPUT_MULTI_IMG)

    def test_cli_plot_linear_sample_multi_split(self):
        # Given
        base_img = cv2.imread(BASE_MULTI_IMG_LINEAR_SPLIT)

        # When
        result = self.runner.invoke(cli.main,
                                    [SAMPLE_MULTI_VCF,
                                     "--sample", "SRR1777294",
                                     "--output", OUTPUT_MULTI_IMG,
                                     "--split", "--linear"])
        result_img = cv2.imread(OUTPUT_MULTI_IMG)

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile(OUTPUT_MULTI_IMG))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove(OUTPUT_MULTI_IMG)

    def test_cli_plot_polar_plotly_sample_multi_split(self):
        # Given
        base_img = BASE_MULTI_IMG_PLOTLY_SPLIT
        test_img = OUTPUT_MULTI_HTML

        # When
        result = self.runner.invoke(cli.main,
                                    [SAMPLE_MULTI_VCF,
                                     "--sample", "SRR1777294",
                                     "--output", test_img,
                                     "--split", "--interactive"])

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile(test_img))
        self.assertEqual(os.path.getsize(base_img), os.path.getsize(test_img))
        # Cleanup
        os.remove(test_img)

    def test_cli_plot_linear_plotly_sample_multi_split(self):
        # Given
        base_img = BASE_MULTI_IMG_PLOTLY_LINEAR_SPLIT
        test_img = OUTPUT_MULTI_HTML

        # When
        result = self.runner.invoke(cli.main,
                                    [SAMPLE_MULTI_VCF, "--linear",
                                     "--sample", "SRR1777294",
                                     "--output", test_img,
                                     "--split", "--interactive"])

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile(test_img))
        self.assertEqual(os.path.getsize(base_img), os.path.getsize(test_img))
        # Cleanup
        os.remove(test_img)


class TestCliCsv(unittest.TestCase):

    def setUp(self) -> None:
        self.runner = CliRunner()

    def test_cli_plot_polar_csv(self):
        # Given
        base_img = cv2.imread(BASE_HF_IMG_DF)

        # When
        result = self.runner.invoke(cli.main, [SAMPLE_HF_CSV])
        result_img = cv2.imread("HG00420.png")

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile("HG00420.png"))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove("HG00420.png")

    def test_cli_plot_linear_csv(self):
        # Given
        base_img = cv2.imread(BASE_HF_IMG_LINEAR_DF)

        # When
        result = self.runner.invoke(cli.main, [SAMPLE_HF_CSV, "--linear"])
        result_img = cv2.imread("HG00420.png")

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile("HG00420.png"))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove("HG00420.png")

    def test_cli_plot_polar_plotly_csv(self):
        # Given
        base_img = BASE_HF_IMG_PLOTLY_DF
        test_img = "HG00420.html"

        # When
        result = self.runner.invoke(cli.main, [SAMPLE_HF_CSV, "--interactive"])

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile(test_img))
        self.assertEqual(os.path.getsize(base_img), os.path.getsize(test_img))
        # Cleanup
        os.remove(test_img)

    def test_cli_plot_linear_plotly_csv(self):
        # Given
        test_img = "HG00420.html"

        # When
        result = self.runner.invoke(cli.main, [SAMPLE_HF_CSV,
                                               "--linear", "--interactive"])

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile(test_img))
        # Cleanup
        os.remove(test_img)

    def test_cli_plot_polar_csv_labels(self):
        # Given
        base_img = cv2.imread(BASE_HF_IMG_LABELS_DF)

        # When
        result = self.runner.invoke(cli.main,
                                    [SAMPLE_HF_CSV, "--labels"])
        result_img = cv2.imread("HG00420.png")

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile("HG00420.png"))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove("HG00420.png")

    def test_cli_plot_linear_csv_labels(self):
        # Given
        base_img = cv2.imread(BASE_HF_IMG_LINEAR_LABELS_DF)

        # When
        result = self.runner.invoke(cli.main,
                                    [SAMPLE_HF_CSV, "--labels", "--linear"])
        result_img = cv2.imread("HG00420.png")

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile("HG00420.png"))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove("HG00420.png")

    def test_cli_plot_polar_csv_legend(self):
        # Given
        base_img = cv2.imread(BASE_HF_IMG_LEGEND_DF)

        # When
        result = self.runner.invoke(cli.main,
                                    [SAMPLE_HF_CSV, "--legend"])
        result_img = cv2.imread("HG00420.png")

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile("HG00420.png"))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove("HG00420.png")

    def test_cli_plot_linear_csv_legend(self):
        # Given
        base_img = cv2.imread(BASE_HF_IMG_LINEAR_LEGEND_DF)

        # When
        result = self.runner.invoke(cli.main,
                                    [SAMPLE_HF_CSV, "--legend", "--linear"])
        result_img = cv2.imread("HG00420.png")

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile("HG00420.png"))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove("HG00420.png")

    def test_cli_plot_polar_plotly_csv_legend(self):
        # Given
        base_img = BASE_HF_IMG_PLOTLY_LEGEND_DF
        test_img = "HG00420.html"

        # When
        result = self.runner.invoke(cli.main,
                                    [SAMPLE_HF_CSV, "--legend",
                                     "--interactive"])

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile(test_img))
        self.assertEqual(os.path.getsize(base_img), os.path.getsize(test_img))
        # Cleanup
        os.remove(test_img)

    def test_cli_plot_linear_plotly_csv_legend(self):
        # Given
        test_img = "HG00420.html"

        # When
        result = self.runner.invoke(cli.main,
                                    [SAMPLE_HF_CSV,
                                     "--linear", "--legend", "--interactive"])

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile(test_img))
        # Cleanup
        os.remove(test_img)

    def test_cli_plot_polar_csv_split(self):
        # Given
        base_img = cv2.imread(BASE_HF_IMG_SPLIT_DF)

        # When
        result = self.runner.invoke(cli.main,
                                    [SAMPLE_HF_CSV, "--split"])
        result_img = cv2.imread("HG00420.png")

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile("HG00420.png"))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove("HG00420.png")

    def test_cli_plot_linear_csv_split(self):
        # Given
        base_img = cv2.imread(BASE_HF_IMG_LINEAR_SPLIT_DF)

        # When
        result = self.runner.invoke(cli.main,
                                    [SAMPLE_HF_CSV, "--split", "--linear"])
        result_img = cv2.imread("HG00420.png")

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile("HG00420.png"))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove("HG00420.png")

    def test_cli_plot_polar_plotly_csv_split(self):
        # Given
        base_img = BASE_HF_IMG_PLOTLY_SPLIT_DF
        test_img = "HG00420.html"

        # When
        result = self.runner.invoke(cli.main,
                                    [SAMPLE_HF_CSV, "--split",
                                     "--interactive"])

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile(test_img))
        self.assertEqual(os.path.getsize(base_img), os.path.getsize(test_img))
        # Cleanup
        os.remove(test_img)

    def test_cli_plot_linear_plotly_csv_split(self):
        # Given
        test_img = "HG00420.html"

        # When
        result = self.runner.invoke(cli.main,
                                    [SAMPLE_HF_CSV,
                                     "--linear", "--split", "--interactive"])

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile(test_img))
        # Cleanup
        os.remove(test_img)

    def test_cli_plot_csv_output(self):
        # Given
        base_img = cv2.imread(BASE_HF_IMG_DF)

        # When
        result = self.runner.invoke(cli.main,
                                    [SAMPLE_HF_CSV,
                                     "--output", OUTPUT_HF_IMG])
        result_img = cv2.imread(OUTPUT_HF_IMG)

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile(OUTPUT_HF_IMG))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove(OUTPUT_HF_IMG)


class TestCliTsv(unittest.TestCase):

    def setUp(self) -> None:
        self.runner = CliRunner()

    def test_cli_plot_tsv(self):
        # Given
        base_img = cv2.imread(BASE_HF_IMG_DF)

        # When
        result = self.runner.invoke(cli.main,
                                    [SAMPLE_HF_TSV, "--sep", "\t"])
        result_img = cv2.imread("HG00420.png")

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile("HG00420.png"))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove("HG00420.png")

    def test_cli_plot_tsv_labels(self):
        # Given
        base_img = cv2.imread(BASE_HF_IMG_LABELS_DF)

        # When
        result = self.runner.invoke(cli.main,
                                    [SAMPLE_HF_TSV, "--sep", "\t",
                                     "--labels"])
        result_img = cv2.imread("HG00420.png")

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile("HG00420.png"))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove("HG00420.png")

    def test_cli_plot_tsv_legend(self):
        # Given
        base_img = cv2.imread(BASE_HF_IMG_LEGEND_DF)

        # When
        result = self.runner.invoke(cli.main,
                                    [SAMPLE_HF_TSV, "--sep", "\t",
                                     "--legend"])
        result_img = cv2.imread("HG00420.png")

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile("HG00420.png"))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove("HG00420.png")

    def test_cli_plot_tsv_split(self):
        # Given
        base_img = cv2.imread(BASE_HF_IMG_SPLIT_DF)

        # When
        result = self.runner.invoke(cli.main,
                                    [SAMPLE_HF_TSV, "--sep", "\t",
                                     "--split"])
        result_img = cv2.imread("HG00420.png")

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile("HG00420.png"))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove("HG00420.png")

    def test_cli_plot_tsv_output(self):
        # Given
        base_img = cv2.imread(BASE_HF_IMG_DF)

        # When
        result = self.runner.invoke(cli.main,
                                    [SAMPLE_HF_TSV, "--sep", "\t",
                                     "--output", OUTPUT_HF_IMG])
        result_img = cv2.imread(OUTPUT_HF_IMG)

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile(OUTPUT_HF_IMG))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove(OUTPUT_HF_IMG)

    def test_cli_plot_tsv_comment(self):
        # Given
        base_img = cv2.imread(BASE_HF_IMG_DF)

        # When
        result = self.runner.invoke(cli.main,
                                    [SAMPLE_HF_TSV_COMM, "--sep", "\t",
                                     "comment=#"])
        result_img = cv2.imread("HG00420.png")

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile("HG00420.png"))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove("HG00420.png")
