#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
from traits.api import Enum, Float, Int, Property, Tuple

from mitoviz.classes.base_locus import _BaseLocus
from mitoviz.constants import (
    NT_LENGTHS, STARTS, TEXT_HA, TEXT_VA, TEXT_Y, TYPES
)
from mitoviz.utils import convert_nt


class _PolarLocus(_BaseLocus):
    """ Class referring to a single mt locus, used in polar plots.

    Attributes:
        name: name of the locus
        index: index of the locus in the mt genome (dloop = 0, tf = 1, etc.)
    """

    _nt_lengths = NT_LENGTHS
    _text_ha = TEXT_HA
    _text_va = TEXT_VA
    _text_y = TEXT_Y

    text_ha = Property(Enum("center", "right", "left"))
    text_va = Property(Enum("center", "top", "bottom"))
    text_y = Property(Enum(19.2, 25.2))
    theta = Property(Float)
    width = Property(Float)

    def _get_text_ha(self):
        """ The horizontal alignment for the text label. """
        return self._text_ha[self.index]

    def _get_text_va(self):
        """ The vertical alignment for the text label. """
        return self._text_va[self.index]

    def _get_text_y(self):
        """ The y position for the text label. """
        return self._text_y[self.index]

    def _get_theta(self):
        """ The position at which the locus will be plotted. """
        if self.index == 0:
            return 0.0
        elif self.index == 1:
            return convert_nt(self._nt_lengths[0]) / 2 + self.width / 2
        return (convert_nt(self._nt_lengths[0]) / 2 + self.width / 2 + sum(
            map(convert_nt, self._nt_lengths[1:self.index])))

    def _get_width(self):
        """ The relative width of the locus from its length in nucleotides. """
        return convert_nt(self._nt_lengths[self.index])


class _PolarSplitLocus(_PolarLocus):
    """ Class referring to a single mt locus, used in polar plots with split
        strands.

    Attributes:
        name: name of the locus
        index: index of the locus in the mt genome (dloop = 0, tf = 1, etc.)
    """

    _nt_lengths = NT_LENGTHS + [546]
    _text_ha = TEXT_HA + ["center"]
    _text_va = TEXT_VA + ["center"]
    _text_y = TEXT_Y + [19.2]
    _types = TYPES + ["reg"]

    bottom = Property(Enum(20.0, 22.5))
    radius = Property(Enum(2.5, 5.0))

    def _get_bottom(self):
        """ The internal position of the locus, used to plot the locus on
        the H/L strand. """
        if self.strand == "H":
            return 22.5
        return 20.0

    def _get_radius(self):
        """ The radius of the locus, used to plot the locus on the H/L
        strand. """
        if self.strand == "":  # non coding
            return 5.0
        return 2.5


class _LinearLocus(_BaseLocus):
    """ Class referring to a single mt locus, used in linear plots.

    Attributes:
        name: name of the locus
        index: index of the locus in the mt genome (dloop = 0, tf = 1, etc.)
    """

    _nt_lengths = [576] + NT_LENGTHS[1:] + [546]
    _starts = STARTS
    _types = TYPES + ["reg"]

    loc_type = Property(Enum("reg", "cds", "rrna", "trna", "nc"))
    height = Property(Tuple(Float, Float))
    start = Property(Int)
    text_x = Property(Float)
    text_y = Property(Enum(-0.12, -0.13))
    width = Property(Float)

    def _get_loc_type(self):
        """ The locus type (regulatory, coding, rRNA, tRNA). """
        return self._types[self.index]

    def _get_height(self):
        """ The vertical position of the locus, if plotting split strands. """
        if self.strand == "H":
            return (-0.05, 0.05)
        elif self.strand == "L":
            return (-0.1, 0.05)
        return (-0.1, 0.1)

    def _get_start(self):
        """ Position on the mt genome where the locus starts. """
        return self._starts[self.index]

    def _get_text_x(self):
        """ The x position for the text label. """
        return self.start + (self.width / 2)

    def _get_text_y(self):
        """ The y position for the text label. """
        if self.name in ["TQ", "TA", "TC", "TD", "TK", "TS2", "TP"]:
            return -0.13
        return -0.12

    def _get_width(self):
        """ The width of the locus in nucleotides. """
        return self._nt_lengths[self.index]
