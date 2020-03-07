#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste

import unittest

from mitoviz.classes.base_locus import _BaseLocus


class TestBaseLocus(unittest.TestCase):

    def setUp(self) -> None:
        self.dloop = _BaseLocus(name="DLOOP", index=0)
        self.tf = _BaseLocus(name="TF", index=1)
        self.rnr1 = _BaseLocus(name="RNR1", index=2)
        self.nd1 = _BaseLocus(name="ND1", index=7)

    def test_strand(self):
        self.assertEqual("L", self.dloop.strand)
        self.assertEqual("H", self.tf.strand)
        self.assertEqual("H", self.rnr1.strand)
        self.assertEqual("H", self.nd1.strand)
