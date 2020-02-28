#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
from mitoviz.constants import COLORS, STRANDS


class _BaseLocus:
    """ Class referring to a single mitochondrial locus.

    Used to create the base mitochondrial plot, on which variants will
    be added using a separate layer.
    Polar plots and linear plots use a different flavor of this base
    class.
    """
    _colors = COLORS
    _strands = STRANDS

    def __init__(self, name: str, index: int):
        self.name = name
        self.index = index

    @property
    def loc_type(self):
        """ The locus type (regulatory, coding, rRNA, tRNA, non-coding). """
        return NotImplemented

    @property
    def width(self):
        """ The width of the locus. """
        return NotImplemented

    @property
    def strand(self) -> str:
        """ The mitochondrial strand on which the locus is located. """
        return self._strands[self.index]

    def __repr__(self):
        return "{}(name={}, index={})".format(
            self.__class__.__name__, self.name, self.index
        )
