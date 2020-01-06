#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import unittest

import matplotlib.patches as mpatches

from mitoviz.plot import plot_legend


class TestPlot(unittest.TestCase):

    def test_plot_legend(self):
        # Given
        expected = [
            mpatches.Patch(color="#2e8b57", label="Coding"),
            mpatches.Patch(color="#ffa500", label="Regulatory"),
            mpatches.Patch(color="#cd5c5c", label="rRNA"),
            mpatches.Patch(color="#4169e1", label="tRNA"),
        ]

        # When
        result = plot_legend()

        # Then
        for n in range(len(result)):
            self.assertTrue(self._compare_patches(expected[n], result[n]))

    @staticmethod
    def _compare_patches(expected, result):
        return expected._original_facecolor == result._original_facecolor
