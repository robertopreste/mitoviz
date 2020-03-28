#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os
import unittest

import cv2
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np

from mitoviz.plot import (
    _legend_patches, _plot_mito_linear, _plot_mito_polar, _plotly_mito_linear,
    _plotly_mito_polar
)
from mitoviz.tests.constants import (
    BASE_MITO_POLAR, BASE_MITO_POLAR_LEGEND, BASE_MITO_POLAR_SPLIT,
    BASE_MITO_LINEAR, BASE_MITO_LINEAR_LEGEND, BASE_MITO_LINEAR_SPLIT,
    BASE_MITO_PLOTLY, BASE_MITO_PLOTLY_LEGEND, BASE_MITO_PLOTLY_SPLIT,
    BASE_MITO_PLOTLY_LINEAR, BASE_MITO_PLOTLY_LINEAR_LEGEND,
    BASE_MITO_PLOTLY_LINEAR_SPLIT
)


class TestPlot(unittest.TestCase):

    def test__legend_patches(self):
        # Given
        expected = [
            mpatches.Patch(color="#2e8b57", label="Coding"),
            mpatches.Patch(color="#ffa500", label="Regulatory"),
            mpatches.Patch(color="#cd5c5c", label="rRNA"),
            mpatches.Patch(color="#4169e1", label="tRNA"),
            mpatches.Patch(color="grey", label="Non Coding")
        ]

        # When
        result = _legend_patches()

        # Then
        for n in range(len(result)):
            self.assertTrue(self._compare_patches(expected[n], result[n]))

    def test__plot_mito_polar(self):
        # Given
        base_img = cv2.imread(BASE_MITO_POLAR)
        result_img_path = "test_base_mito.png"

        # When
        fig, ax = _plot_mito_polar()
        plt.savefig(result_img_path)
        plt.close()
        result_img = cv2.imread(result_img_path)

        # Then
        self.assertTrue(os.path.isfile(result_img_path))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove(result_img_path)

    def test__plot_mito_polar_legend(self):
        # Given
        base_img = cv2.imread(BASE_MITO_POLAR_LEGEND)
        result_img_path = "test_base_mito_legend.png"

        # When
        fig, ax = _plot_mito_polar(legend=True)
        plt.savefig(result_img_path)
        plt.close()
        result_img = cv2.imread(result_img_path)

        # Then
        self.assertTrue(os.path.isfile(result_img_path))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove(result_img_path)

    def test__plot_mito_polar_split(self):
        # Given
        base_img = cv2.imread(BASE_MITO_POLAR_SPLIT)
        result_img_path = "test_base_mito_split.png"

        # When
        fig, ax = _plot_mito_polar(split=True)
        plt.savefig(result_img_path)
        plt.close()
        result_img = cv2.imread(result_img_path)

        # Then
        self.assertTrue(os.path.isfile(result_img_path))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove(result_img_path)

    def test__plot_mito_linear(self):
        # Given
        base_img = cv2.imread(BASE_MITO_LINEAR)
        result_img_path = "test_base_mito.png"

        # When
        fig, ax = _plot_mito_linear()
        plt.savefig(result_img_path)
        plt.close()
        result_img = cv2.imread(result_img_path)

        # Then
        self.assertTrue(os.path.isfile(result_img_path))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove(result_img_path)

    def test__plot_mito_linear_legend(self):
        # Given
        base_img = cv2.imread(BASE_MITO_LINEAR_LEGEND)
        result_img_path = "test_base_mito_legend.png"

        # When
        fig, ax = _plot_mito_linear(legend=True)
        plt.savefig(result_img_path)
        plt.close()
        result_img = cv2.imread(result_img_path)

        # Then
        self.assertTrue(os.path.isfile(result_img_path))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove(result_img_path)

    def test__plot_mito_linear_split(self):
        # Given
        base_img = cv2.imread(BASE_MITO_LINEAR_SPLIT)
        result_img_path = "test_base_mito_split.png"

        # When
        fig, ax = _plot_mito_linear(split=True)
        plt.savefig(result_img_path)
        plt.close()
        result_img = cv2.imread(result_img_path)

        # Then
        self.assertTrue(os.path.isfile(result_img_path))
        diff = cv2.subtract(base_img, result_img)
        self.assertFalse(np.any(diff))
        # Cleanup
        os.remove(result_img_path)

    def test__plotly_mito_polar(self):
        # Given
        base_img = BASE_MITO_PLOTLY
        result_img = "test_base_mito.html"

        # When
        fig = _plotly_mito_polar()
        fig.write_html(result_img)

        # Then
        self.assertTrue(os.path.isfile(result_img))
        self.assertEqual(os.path.getsize(base_img),
                         os.path.getsize(result_img))
        # Cleanup
        os.remove(result_img)

    def test__plotly_mito_polar_legend(self):
        # Given
        base_img = BASE_MITO_PLOTLY_LEGEND
        result_img = "test_base_mito_legend.html"

        # When
        fig = _plotly_mito_polar(legend=True)
        fig.write_html(result_img)

        # Then
        self.assertTrue(os.path.isfile(result_img))
        self.assertEqual(os.path.getsize(base_img),
                         os.path.getsize(result_img))
        # Cleanup
        os.remove(result_img)

    def test__plotly_mito_polar_split(self):
        # Given
        base_img = BASE_MITO_PLOTLY_SPLIT
        result_img = "test_base_mito_split.html"

        # When
        fig = _plotly_mito_polar(split=True)
        fig.write_html(result_img)

        # Then
        self.assertTrue(os.path.isfile(result_img))
        self.assertEqual(os.path.getsize(base_img),
                         os.path.getsize(result_img))
        # Cleanup
        os.remove(result_img)

    def test__plotly_mito_linear(self):
        # Given
        base_img = BASE_MITO_PLOTLY_LINEAR
        result_img = "test_base_mito_linear.html"

        # When
        fig = _plotly_mito_linear()
        fig.write_html(result_img)

        # Then
        self.assertTrue(os.path.isfile(result_img))
        self.assertEqual(os.path.getsize(base_img),
                         os.path.getsize(result_img))
        # Cleanup
        os.remove(result_img)

    def test__plotly_mito_linear_legend(self):
        # Given
        base_img = BASE_MITO_PLOTLY_LINEAR_LEGEND
        result_img = "test_base_mito_legend_linear.html"

        # When
        fig = _plotly_mito_linear(legend=True)
        fig.write_html(result_img)

        # Then
        self.assertTrue(os.path.isfile(result_img))
        self.assertEqual(os.path.getsize(base_img),
                         os.path.getsize(result_img))
        # Cleanup
        os.remove(result_img)

    def test__plotly_mito_linear_split(self):
        # Given
        base_img = BASE_MITO_PLOTLY_LINEAR_SPLIT
        result_img = "test_base_mito_split_linear.html"

        # When
        fig = _plotly_mito_linear(split=True)
        fig.write_html(result_img)

        # Then
        self.assertTrue(os.path.isfile(result_img))
        self.assertEqual(os.path.getsize(base_img),
                         os.path.getsize(result_img))
        # Cleanup
        os.remove(result_img)

    @staticmethod
    def _compare_patches(expected, result):
        return expected._original_facecolor == result._original_facecolor
