#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os
import unittest

import cv2
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np

from mitoviz.plot import _plot_legend, _plot_mito_linear, _plot_mito_polar
from mitoviz.tests.constants import (
    BASE_MITO_POLAR, BASE_MITO_POLAR_LEGEND, BASE_MITO_POLAR_SPLIT,
    BASE_MITO_LINEAR, BASE_MITO_LINEAR_LEGEND, BASE_MITO_LINEAR_SPLIT
)


class TestPlot(unittest.TestCase):

    def test__plot_legend(self):
        # Given
        expected = [
            mpatches.Patch(color="#2e8b57", label="Coding"),
            mpatches.Patch(color="#ffa500", label="Regulatory"),
            mpatches.Patch(color="#cd5c5c", label="rRNA"),
            mpatches.Patch(color="#4169e1", label="tRNA"),
            mpatches.Patch(color="grey", label="Non Coding")
        ]

        # When
        result = _plot_legend()

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

    @staticmethod
    def _compare_patches(expected, result):
        return expected._original_facecolor == result._original_facecolor
