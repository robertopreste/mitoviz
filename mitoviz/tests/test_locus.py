#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import unittest

from mitoviz.locus import _PolarLocus


class TestPolarLocus(unittest.TestCase):

    def setUp(self) -> None:
        self.dloop = _PolarLocus("DLOOP", 0)
        self.tf = _PolarLocus("TF", 1)
        self.rnr1 = _PolarLocus("RNR1", 2)
        self.nd1 = _PolarLocus("ND1", 7)

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
        self.assertEqual(1.4308051179914298, self.nd1.theta)

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
        self.assertEqual("top", self.dloop.text_va)
        self.assertEqual("bottom", self.tf.text_va)
        self.assertEqual("bottom", self.rnr1.text_va)
        self.assertEqual("bottom", self.nd1.text_va)

    def test_text_y(self):
        self.assertEqual(19.2, self.dloop.text_y)
        self.assertEqual(25.2, self.tf.text_y)
        self.assertEqual(25.2, self.rnr1.text_y)
        self.assertEqual(25.2, self.nd1.text_y)
