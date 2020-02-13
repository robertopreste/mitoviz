#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import unittest

import pandas.testing as pt
from vcfpy import Call, Substitution

from mitoviz.tests.constants import (
    SAMPLE_DF, SAMPLE_HF_CSV, SAMPLE_HF_DF, SAMPLE_HF_TSV, SAMPLE_HF_VCF,
)
from mitoviz.parsers import _DataFrameParser, _TabularParser, _VcfParser
from mitoviz.variant import _PolarVariant


class TestVcfParser(unittest.TestCase):

    def setUp(self) -> None:
        self.vcf = _VcfParser(SAMPLE_HF_VCF)

    def test_samples(self):
        self.assertEqual(["HG00420"], self.vcf.samples)

    def test_variants(self):
        # Given/When
        variant = _PolarVariant(
            reference="C",
            position=8935,
            alternate=Substitution("SNV", "T"),
            hf=0.899
        )

        # Then
        self.assertIsInstance(self.vcf.variants, dict)
        self.assertIn(variant, list(self.vcf.variants.values())[0])

    def test_parse_call(self):
        # Given
        call = Call('HG00420', {'GT': '0/1',
                                'DP': [873],
                                'HF': [0.998],
                                'CILOW': [0.991],
                                'CIUP': [1.0]})
        expected = 0.998

        # When
        result = self.vcf.parse_call(call, 0)

        # Then
        self.assertEqual(expected, result)

    def test_parse_call_empty(self):
        # Given
        call = Call('HG00420', {})
        expected = 0.5

        # When
        result = self.vcf.parse_call(call, 0)

        # Then
        self.assertEqual(expected, result)


class TestDataFrameParser(unittest.TestCase):

    def setUp(self) -> None:
        self.df = _DataFrameParser(SAMPLE_DF)
        self.df_hf = _DataFrameParser(SAMPLE_HF_DF)

    def test_variants(self):
        # Given/When
        variant = _PolarVariant(
            reference="C",
            position=8935,
            alternate="T",
            hf=0.5
        )
        variant_hf = _PolarVariant(
            reference="C",
            position=8935,
            alternate="T",
            hf=0.899
        )

        # Then
        self.assertIsInstance(self.df.variants, dict)
        self.assertIn(variant, list(self.df.variants.values())[0])
        self.assertIn(variant_hf, list(self.df_hf.variants.values())[0])

    def test_has_sample_true(self):
        self.assertTrue(self.df_hf.has_sample)

    def test_has_sample_false(self):
        self.assertFalse(self.df.has_sample)

    def test_has_hf_true(self):
        self.assertTrue(self.df_hf.has_hf)

    def test_has_hf_false(self):
        self.assertFalse(self.df.has_hf)


class TestTabularParser(unittest.TestCase):

    def setUp(self) -> None:
        self.csv = _TabularParser(SAMPLE_HF_CSV)
        self.tsv = _TabularParser(SAMPLE_HF_TSV, sep="\t")

    def test_df(self):
        # Given/When
        df = SAMPLE_HF_DF

        # Then

        pt.assert_frame_equal(df, self.csv.df)
        pt.assert_frame_equal(df, self.tsv.df)
