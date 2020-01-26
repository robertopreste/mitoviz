#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os
import unittest

from mitoviz.utils import convert_hf, convert_nt, parse_path


class TestUtils(unittest.TestCase):

    def test_convert_nt(self):
        # Given
        nt = 3308
        expected = 1.2557981773190898

        # When
        result = convert_nt(nt)

        # Then
        self.assertEqual(expected, result)

    def test_convert_hf(self):
        # Given
        hf = 0.3
        expected = 1.5

        # When
        result = convert_hf(hf)

        # Then
        self.assertEqual(expected, result)

    def test_parse_path(self):
        # Given
        path = "test/dir/tester.py"
        expected = ("test/dir", "tester", ".py")

        # When
        result = parse_path(path)

        # Then
        self.assertEqual(expected, result)

    def test_parse_path_empty(self):
        # Given
        path = ""
        expected = (os.getcwd(), "", ".png")

        # When
        result = parse_path(path)

        # Then
        self.assertEqual(expected, result)
