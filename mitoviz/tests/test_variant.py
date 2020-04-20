#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import unittest

from vcfpy import Substitution

from mitoviz.variant import _Variant


class TestVariant(unittest.TestCase):

    def setUp(self) -> None:
        self.variant = _Variant(
            reference="C",
            position=3308,
            alternate=Substitution("SNV", "A"),
            hf=0.3
        )
        self.variant_del = _Variant(
            reference="CT",
            position=3308,
            alternate=Substitution("DEL", "C"),
            hf=0.3
        )
        self.variant_ins = _Variant(
            reference="C",
            position=3308,
            alternate=Substitution("INS", "CA"),
            hf=0.3
        )
        self.variant_raw = _Variant(
            reference="C",
            position=3308,
            alternate="A",
            hf=0.3
        )
        self.variant_del_raw = _Variant(
            reference="CT",
            position=3308,
            alternate="C",
            hf=0.3
        )
        self.variant_ins_raw = _Variant(
            reference="C",
            position=3308,
            alternate="CA",
            hf=0.3
        )

    def test__is_deletion_false(self):
        self.assertFalse(self.variant._is_deletion)
        self.assertFalse(self.variant_raw._is_deletion)

    def test__is_deletion_true(self):
        self.assertTrue(self.variant_del._is_deletion)
        self.assertTrue(self.variant_del_raw._is_deletion)

    def test__is_insertion_false(self):
        self.assertFalse(self.variant._is_insertion)
        self.assertFalse(self.variant_raw._is_insertion)

    def test__is_insertion_true(self):
        self.assertTrue(self.variant_ins._is_insertion)
        self.assertTrue(self.variant_ins_raw._is_insertion)

    def test_color(self):
        self.assertEqual("#2e8b57", self.variant.color)

    def test_label(self):
        self.assertEqual("3308C>A", self.variant.label)
        self.assertEqual("3308C>A", self.variant_raw.label)

    def test_label_deletion(self):
        self.assertEqual("3309d", self.variant_del.label)
        self.assertEqual("3309d", self.variant_del_raw.label)

    def test_label_insertion(self):
        self.assertEqual("3308.A", self.variant_ins.label)
        self.assertEqual("3308.A", self.variant_ins_raw.label)

    def test_label_hf(self):
        self.assertEqual("3308C>A\nHF: 0.3", self.variant.label_hf)
        self.assertEqual("3308C>A\nHF: 0.3", self.variant_raw.label_hf)

    def test_label_hf_plotly(self):
        self.assertEqual("3308C>A<br>HF: 0.3", self.variant.label_hf_plotly)
        self.assertEqual("3308C>A<br>HF: 0.3",
                         self.variant_raw.label_hf_plotly)

    def test_polar_x(self):
        self.assertEqual(1.2557981773190898, self.variant.polar_x)

    def test_polar_x_p(self):
        self.assertEqual(71.70607592492003, self.variant.polar_x_p)

    def test_polar_y(self):
        self.assertEqual(21.5, self.variant.polar_y)

    def test_linear_x(self):
        self.assertEqual(3308, self.variant.linear_x)

    def test_linear_y(self):
        self.assertEqual(0.3, self.variant.linear_y)

    def test_strand(self):
        # Given/When
        variant_h = self.variant
        variant_l = _Variant(
            reference="C",
            position=500,
            alternate=Substitution("SNV", "A"),
            hf=0.3
        )
        variant_nc = _Variant(
            reference="C",
            position=3305,
            alternate=Substitution("SNV", "A"),
            hf=0.3
        )

        # Then
        self.assertEqual("H", variant_h.strand)
        self.assertEqual("L", variant_l.strand)
        self.assertEqual("", variant_nc.strand)
