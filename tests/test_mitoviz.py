#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os
import pytest
import unittest

from click.testing import CliRunner

from mitoviz import mitoviz
from mitoviz import cli

DATADIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "data"
)
SAMPLE_HF_VCF = os.path.join(DATADIR, "sample_hf.vcf")
OUTPUT = os.path.join(DATADIR, "sample_hf_plot.png")


class TestCli(unittest.TestCase):

    def setUp(self) -> None:
        self.runner = CliRunner()

    def tearDown(self) -> None:
        try:
            os.remove("mitoviz.png")
            os.remove(OUTPUT)
        except FileNotFoundError:
            pass

    def test_cli_help(self):
        # Given/When
        result = self.runner.invoke(cli.main, ["--help"])

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertIn("Show this message and exit.", result.output)

    def test_cli_plot(self):
        # Given/When
        result = self.runner.invoke(cli.main, [SAMPLE_HF_VCF])

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile("mitoviz.png"))

    def test_cli_plot_output(self):
        # Given/When
        result = self.runner.invoke(cli.main,
                                    [SAMPLE_HF_VCF,
                                     "--output", OUTPUT])

        # Then
        self.assertEqual(0, result.exit_code)
        self.assertTrue(os.path.isfile(OUTPUT))
