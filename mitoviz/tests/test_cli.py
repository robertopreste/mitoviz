#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os
import unittest

import cv2
import numpy as np
from click.testing import CliRunner

from mitoviz import cli
from mitoviz.tests.constants import (
    SAMPLE_VCF, SAMPLE_HF_VCF, SAMPLE_MULTI_VCF, SAMPLE_HF_CSV, SAMPLE_HF_TSV,
    SAMPLE_HF_TSV_COMM,
    BASE_IMG, BASE_IMG_LABELS, BASE_IMG_LEGEND, BASE_IMG_SPLIT,
    BASE_IMG_LINEAR, BASE_IMG_LINEAR_LABELS, BASE_IMG_LINEAR_LEGEND,
    BASE_IMG_LINEAR_SPLIT,
    BASE_HF_IMG, BASE_HF_IMG_LABELS, BASE_HF_IMG_LEGEND, BASE_HF_IMG_SPLIT,
    BASE_HF_IMG_LINEAR, BASE_HF_IMG_LINEAR_LABELS, BASE_HF_IMG_LINEAR_LEGEND,
    BASE_HF_IMG_LINEAR_SPLIT,
    BASE_HF_IMG_DF, BASE_HF_IMG_LABELS_DF, BASE_HF_IMG_LEGEND_DF,
    BASE_HF_IMG_SPLIT_DF,
    BASE_HF_IMG_LINEAR_DF, BASE_HF_IMG_LINEAR_LABELS_DF,
    BASE_HF_IMG_LINEAR_LEGEND_DF, BASE_HF_IMG_LINEAR_SPLIT_DF,
    BASE_MULTI_IMG, BASE_MULTI_IMG_LABELS, BASE_MULTI_IMG_LEGEND,
    BASE_MULTI_IMG_SPLIT,
    BASE_MULTI_IMG_LINEAR, BASE_MULTI_IMG_LINEAR_LABELS,
    BASE_MULTI_IMG_LINEAR_LEGEND, BASE_MULTI_IMG_LINEAR_SPLIT,
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
