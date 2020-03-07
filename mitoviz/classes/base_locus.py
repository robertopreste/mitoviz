#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
from traits.api import Enum, HasTraits, Int, Property, Str

from mitoviz.constants import COLORS, STRANDS, TYPES


class _BaseLocus(HasTraits):
    """ Class referring to a single mitochondrial locus.

    Used to create the base mitochondrial plot, on which variants will
    be added using a separate layer.
    Polar plots and linear plots use a different flavor of this base
    class.
    """
    _colors = COLORS
    _strands = STRANDS
    _types = TYPES

    name = Str()
    index = Int()
    loc_type = Property(Enum("reg", "cds", "rrna", "trna", "nc"))
    color = Property(Enum("grey", "#2e8b57", "#ffa500", "#cd5c5c", "#4169e1"))
    strand = Property(Enum("", "H", "L"))

    def _get_loc_type(self):
        """ The locus type (regulatory, coding, rRNA, tRNA, non-coding). """
        return self._types[self.index]

    def _get_color(self):
        """ The locus-type-specific color. """
        return self._colors[self.loc_type]

    def _get_strand(self):
        """ The mitochondrial strand on which the locus is located. """
        return self._strands[self.index]

    def __repr__(self):
        return "{}(name={}, index={})".format(
            self.__class__.__name__, self.name, self.index
        )
