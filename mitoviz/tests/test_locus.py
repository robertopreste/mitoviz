#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import unittest

from mitoviz.locus import _LinearLocus, _PolarLocus, _PolarSplitLocus


class TestPolarLocus(unittest.TestCase):

    def setUp(self) -> None:
        self.dloop = _PolarLocus(name="DLOOP", index=0)
        self.tf = _PolarLocus(name="TF", index=1)
        self.rnr1 = _PolarLocus(name="RNR1", index=2)
        self.nd1 = _PolarLocus(name="ND1", index=7)

    def test_loc_type(self):
        self.assertEqual("reg", self.dloop.loc_type)
        self.assertEqual("trna", self.tf.loc_type)
        self.assertEqual("rrna", self.rnr1.loc_type)
        self.assertEqual("cds", self.nd1.loc_type)

    def test_color(self):
        self.assertEqual("#ffa500", self.dloop.color)
        self.assertEqual("#4169e1", self.tf.color)
        self.assertEqual("#cd5c5c", self.rnr1.color)
        self.assertEqual("#2e8b57", self.nd1.color)

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


class TestPolarSplitLocus(unittest.TestCase):

    def setUp(self) -> None:
        self.dloop = _PolarSplitLocus(name="DLOOP", index=0)
        self.tf = _PolarSplitLocus(name="TF", index=1)
        self.nc1 = _PolarSplitLocus(name="NC1", index=6)

    def test_color(self):
        self.assertEqual("#ffa500", self.dloop.color)
        self.assertEqual("#4169e1", self.tf.color)
        self.assertEqual("grey", self.nc1.color)

    def test_strand(self):
        self.assertEqual("L", self.dloop.strand)
        self.assertEqual("H", self.tf.strand)
        self.assertEqual("", self.nc1.strand)

    def test_bottom(self):
        self.assertEqual(20.0, self.dloop.bottom)
        self.assertEqual(22.5, self.tf.bottom)
        self.assertEqual(20.0, self.nc1.bottom)

    def test_radius(self):
        self.assertEqual(2.5, self.dloop.radius)
        self.assertEqual(2.5, self.tf.radius)
        self.assertEqual(5.0, self.nc1.radius)


class TestLinearLocus(unittest.TestCase):

    def setUp(self) -> None:
        self.dloop = _LinearLocus(name="DLOOP", index=0)
        self.nc1 = _LinearLocus(name="NC1", index=6)
        self.nd1 = _LinearLocus(name="ND1", index=7)
        self.tq = _LinearLocus(name="TQ", index=9)

    def test_loc_type(self):
        self.assertEqual("reg", self.dloop.loc_type)
        self.assertEqual("nc", self.nc1.loc_type)
        self.assertEqual("cds", self.nd1.loc_type)
        self.assertEqual("trna", self.tq.loc_type)

    def test_color(self):
        self.assertEqual("#ffa500", self.dloop.color)
        self.assertEqual("grey", self.nc1.color)
        self.assertEqual("#2e8b57", self.nd1.color)
        self.assertEqual("#4169e1", self.tq.color)

    def test_width(self):
        self.assertEqual(576, self.dloop.width)
        self.assertEqual(2, self.nc1.width)
        self.assertEqual(956, self.nd1.width)
        self.assertEqual(69, self.tq.width)

    def test_height(self):
        self.assertEqual((-0.1, 0.05), self.dloop.height)
        self.assertEqual((-0.1, 0.1), self.nc1.height)
        self.assertEqual((-0.05, 0.05), self.nd1.height)
        self.assertEqual((-0.1, 0.05), self.tq.height)

    def test_start(self):
        self.assertEqual(0, self.dloop.start)
        self.assertEqual(3304, self.nc1.start)
        self.assertEqual(3306, self.nd1.start)
        self.assertEqual(4331, self.tq.start)

    def test_text_x(self):
        self.assertEqual(288.0, self.dloop.text_x)
        self.assertEqual(3305.0, self.nc1.text_x)
        self.assertEqual(3784.0, self.nd1.text_x)
        self.assertEqual(4365.5, self.tq.text_x)

    def test_text_y(self):
        self.assertEqual(-0.12, self.dloop.text_y)
        self.assertEqual(-0.12, self.nc1.text_y)
        self.assertEqual(-0.12, self.nd1.text_y)
        self.assertEqual(-0.13, self.tq.text_y)
