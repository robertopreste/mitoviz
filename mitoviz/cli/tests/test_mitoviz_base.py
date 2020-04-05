#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os
import unittest

import cv2
import numpy as np
from click.testing import CliRunner

from mitoviz.cli import mitoviz_base as cli
from mitoviz.tests.constants import (
    BASE_MITO_POLAR, BASE_MITO_POLAR_LEGEND, BASE_MITO_POLAR_SPLIT,
    BASE_MITO_LINEAR, BASE_MITO_LINEAR_LEGEND, BASE_MITO_LINEAR_SPLIT,
    BASE_MITO_PLOTLY, BASE_MITO_PLOTLY_LEGEND, BASE_MITO_PLOTLY_SPLIT,
    BASE_MITO_PLOTLY_LINEAR, BASE_MITO_PLOTLY_LINEAR_LEGEND,
    BASE_MITO_PLOTLY_LINEAR_SPLIT, OUTPUT_IMG, OUTPUT_HTML

)


class TestMitovizBase(unittest.TestCase):

    def setUp(self) -> None:
        self.runner = CliRunner()

    def test_cli_base_help(self):
        # Given/When
        result = self.runner.invoke(cli.main, ["--help"])

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertIn("Show this message and exit.", result.output)

    def test_cli_base_polar(self):
        # Given
        base_img = cv2.imread(BASE_MITO_POLAR)

        # When
        result = self.runner.invoke(cli.main)
        result_img = cv2.imread("base_mt.png")

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile("base_mt.png"))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove("base_mt.png")

    def test_cli_base_linear(self):
        # Given
        base_img = cv2.imread(BASE_MITO_LINEAR)

        # When
        result = self.runner.invoke(cli.main, ["--linear"])
        result_img = cv2.imread("base_mt.png")

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile("base_mt.png"))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove("base_mt.png")

    def test_cli_base_polar_plotly(self):
        # Given
        base_img = BASE_MITO_PLOTLY
        test_img = "base_mt.html"

        # When
        result = self.runner.invoke(cli.main, ["--interactive"])

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile(test_img))
        self.assertEqual(os.path.getsize(base_img), os.path.getsize(test_img))
        # Cleanup
        os.remove(test_img)

    def test_cli_base_linear_plotly(self):
        # Given
        base_img = BASE_MITO_PLOTLY_LINEAR
        test_img = "base_mt.html"

        # When
        result = self.runner.invoke(cli.main, ["--linear", "--interactive"])

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile(test_img))
        self.assertEqual(os.path.getsize(base_img), os.path.getsize(test_img))
        # Cleanup
        os.remove(test_img)

    def test_cli_plot_polar_legend(self):
        # Given
        base_img = cv2.imread(BASE_MITO_POLAR_LEGEND)

        # When
        result = self.runner.invoke(cli.main, ["--legend"])
        result_img = cv2.imread("base_mt.png")

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile("base_mt.png"))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove("base_mt.png")

    def test_cli_base_linear_legend(self):
        # Given
        base_img = cv2.imread(BASE_MITO_LINEAR_LEGEND)

        # When
        result = self.runner.invoke(cli.main, ["--legend", "--linear"])
        result_img = cv2.imread("base_mt.png")

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile("base_mt.png"))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove("base_mt.png")

    def test_cli_base_polar_plotly_legend(self):
        # Given
        base_img = BASE_MITO_PLOTLY_LEGEND
        test_img = "base_mt.html"

        # When
        result = self.runner.invoke(cli.main, ["--legend", "--interactive"])

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile(test_img))
        self.assertEqual(os.path.getsize(base_img), os.path.getsize(test_img))
        # Cleanup
        os.remove(test_img)

    def test_cli_base_linear_plotly_legend(self):
        # Given
        base_img = BASE_MITO_PLOTLY_LINEAR_LEGEND
        test_img = "base_mt.html"

        # When
        result = self.runner.invoke(cli.main,
                                    ["--legend", "--linear", "--interactive"])

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile(test_img))
        self.assertEqual(os.path.getsize(base_img), os.path.getsize(test_img))
        # Cleanup
        os.remove(test_img)

    def test_cli_base_output(self):
        # Given
        base_img = cv2.imread(BASE_MITO_POLAR)

        # When
        result = self.runner.invoke(cli.main, ["--output", OUTPUT_IMG])
        result_img = cv2.imread(OUTPUT_IMG)

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile(OUTPUT_IMG))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove(OUTPUT_IMG)

    def test_cli_base_plotly_output(self):
        # Given
        base_img = BASE_MITO_PLOTLY
        test_img = OUTPUT_HTML

        # When
        result = self.runner.invoke(cli.main,
                                    ["--interactive",
                                     "--output", test_img])

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile(test_img))
        self.assertEqual(os.path.getsize(base_img), os.path.getsize(test_img))
        # Cleanup
        os.remove(test_img)

    def test_cli_base_polar_split(self):
        # Given
        base_img = cv2.imread(BASE_MITO_POLAR_SPLIT)

        # When
        result = self.runner.invoke(cli.main, ["--split"])
        result_img = cv2.imread("base_mt.png")

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile("base_mt.png"))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove("base_mt.png")

    def test_cli_base_linear_split(self):
        # Given
        base_img = cv2.imread(BASE_MITO_LINEAR_SPLIT)

        # When
        result = self.runner.invoke(cli.main, ["--split", "--linear"])
        result_img = cv2.imread("base_mt.png")

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile("base_mt.png"))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove("base_mt.png")

    def test_cli_base_polar_plotly_split(self):
        # Given
        base_img = BASE_MITO_PLOTLY_SPLIT
        test_img = "base_mt.html"

        # When
        result = self.runner.invoke(cli.main, ["--split", "--interactive"])

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile(test_img))
        self.assertEqual(os.path.getsize(base_img), os.path.getsize(test_img))
        # Cleanup
        os.remove(test_img)

    def test_cli_base_linear_plotly_split(self):
        # Given
        base_img = BASE_MITO_PLOTLY_LINEAR_SPLIT
        test_img = "base_mt.html"

        # When
        result = self.runner.invoke(cli.main,
                                    ["--split", "--linear", "--interactive"])

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile(test_img))
        self.assertEqual(os.path.getsize(base_img), os.path.getsize(test_img))
        # Cleanup
        os.remove(test_img)
