#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import unittest

from vcfpy import Substitution

from mitoviz.variant import _PolarVariant


class TestPolarVariant(unittest.TestCase):

    def setUp(self) -> None:
        self.variant = _PolarVariant(
            reference="C",
            position=3308,
            alternate=Substitution("SNV", "A"),
            hf=0.3
        )
        self.variant_del = _PolarVariant(
            reference="CT",
            position=3308,
            alternate=Substitution("DEL", "C"),
            hf=0.3
        )
        self.variant_ins = _PolarVariant(
            reference="C",
            position=3308,
            alternate=Substitution("INS", "CA"),
            hf=0.3
        )
        self.variant_raw = _PolarVariant(
            reference="C",
            position=3308,
            alternate="A",
            hf=0.3
        )
        self.variant_del_raw = _PolarVariant(
            reference="CT",
            position=3308,
            alternate="C",
            hf=0.3
        )
        self.variant_ins_raw = _PolarVariant(
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
