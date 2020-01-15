#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os
import unittest

from vcfpy import Call, Substitution

from mitoviz.classes import Locus, Variant, VcfParser, DataFrameParser
from .constants import SAMPLE_HF_VCF, SAMPLE_DF, SAMPLE_HF_DF


class TestLocus(unittest.TestCase):

    def setUp(self) -> None:
        self.dloop = Locus("DLOOP", 0)
        self.tf = Locus("TF", 1)
        self.rnr1 = Locus("RNR1", 2)
        self.nd1 = Locus("ND1", 6)

    def test_loc_type(self):
        self.assertEqual("reg", self.dloop.loc_type)
        self.assertEqual("trna", self.tf.loc_type)
        self.assertEqual("rrna", self.rnr1.loc_type)
        self.assertEqual("cds", self.nd1.loc_type)

    def test_width(self):
        self.assertEqual(0.4259388013760637, self.dloop.width)
        self.assertEqual(0.026953346611141286, self.tf.width)
        self.assertEqual(0.3621618685497012, self.rnr1.width)
        self.assertEqual(0.36292111775001507, self.nd1.width)

    def test_theta(self):
        self.assertEqual(0.0, self.dloop.theta)
        self.assertEqual(0.2264460739936025, self.tf.theta)
        self.assertEqual(0.42100368157402374, self.rnr1.theta)
        self.assertEqual(1.430045868791116, self.nd1.theta)

    def test_color(self):
        self.assertEqual("#ffa500", self.dloop.color)
        self.assertEqual("#4169e1", self.tf.color)
        self.assertEqual("#cd5c5c", self.rnr1.color)
        self.assertEqual("#2e8b57", self.nd1.color)

    def test_text_ha(self):
        self.assertEqual("center", self.dloop.text_ha)
        self.assertEqual("center", self.tf.text_ha)
        self.assertEqual("right", self.rnr1.text_ha)
        self.assertEqual("right", self.nd1.text_ha)

    def test_text_va(self):
        self.assertEqual("bottom", self.dloop.text_va)
        self.assertEqual("bottom", self.tf.text_va)
        self.assertEqual("bottom", self.rnr1.text_va)
        self.assertEqual("bottom", self.nd1.text_va)

    def test_text_y(self):
        self.assertEqual(25.2, self.dloop.text_y)
        self.assertEqual(25.2, self.tf.text_y)
        self.assertEqual(25.2, self.rnr1.text_y)
        self.assertEqual(25.2, self.nd1.text_y)


class TestVariant(unittest.TestCase):

    def setUp(self) -> None:
        self.variant = Variant(
            reference="C",
            position=3308,
            alternate=Substitution("SNV", "A"),
            hf=0.3
        )
        self.variant_del = Variant(
            reference="CT",
            position=3308,
            alternate=Substitution("DEL", "C"),
            hf=0.3
        )
        self.variant_ins = Variant(
            reference="C",
            position=3308,
            alternate=Substitution("INS", "CA"),
            hf=0.3
        )
        self.variant_raw = Variant(
            reference="C",
            position=3308,
            alternate="A",
            hf=0.3
        )
        self.variant_del_raw = Variant(
            reference="CT",
            position=3308,
            alternate="C",
            hf=0.3
        )
        self.variant_ins_raw = Variant(
            reference="C",
            position=3308,
            alternate="CA",
            hf=0.3
        )

    def test__is_deletion_false(self):
        self.assertFalse(self.variant._is_deletion())
        self.assertFalse(self.variant_raw._is_deletion())

    def test__is_deletion_true(self):
        self.assertTrue(self.variant_del._is_deletion())
        self.assertTrue(self.variant_del_raw._is_deletion())

    def test__is_insertion_false(self):
        self.assertFalse(self.variant._is_insertion())
        self.assertFalse(self.variant_raw._is_insertion())

    def test__is_insertion_true(self):
        self.assertTrue(self.variant_ins._is_insertion())
        self.assertTrue(self.variant_ins_raw._is_insertion())

    def test_label(self):
        self.assertEqual("3308C>A", self.variant.label)
        self.assertEqual("3308C>A", self.variant_raw.label)

    def test_label_deletion(self):
        self.assertEqual("3309d", self.variant_del.label)
        self.assertEqual("3309d", self.variant_del_raw.label)

    def test_label_insertion(self):
        self.assertEqual("3308.A", self.variant_ins.label)
        self.assertEqual("3308.A", self.variant_ins_raw.label)

    def test_pos_x(self):
        self.assertEqual(1.2557981773190898, self.variant.pos_x)

    def test_pos_y(self):
        self.assertEqual(21.5, self.variant.pos_y)


class TestVcfParser(unittest.TestCase):

    def setUp(self) -> None:
        self.vcf = VcfParser(SAMPLE_HF_VCF)

    def test_samples(self):
        self.assertEqual(["HG00420"], self.vcf.samples)

    def test_variants(self):
        # Given/When
        variant = Variant(
            reference="C",
            position=8935,
            alternate=Substitution("SNV", "T"),
            hf=0.899
        )

        # Then
        self.assertIsInstance(self.vcf.variants, dict)
        # self.assertIn(variant, self.vcf.variants)

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


class TestDfParser(unittest.TestCase):

    def setUp(self) -> None:
        self.df = DataFrameParser(SAMPLE_DF)
        self.df_hf = DataFrameParser(SAMPLE_HF_DF)

    def test_variants(self):
        # Given/When
        variant = Variant(
            reference="C",
            position=8935,
            alternate=Substitution("SNV", "T"),
            hf=0.899
        )

        # Then
        self.assertIsInstance(self.df.variants, dict)
        # self.assertIn(variant, self.vcf.variants)

    def test_has_sample_true(self):
        self.assertTrue(self.df_hf.has_sample)

    def test_has_sample_false(self):
        self.assertFalse(self.df.has_sample)

    def test_has_hf_true(self):
        self.assertTrue(self.df_hf.has_hf)

    def test_has_hf_false(self):
        self.assertFalse(self.df.has_hf)
