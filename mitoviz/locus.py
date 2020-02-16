#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
from mitoviz.classes.abstract_locus import _AbstractLocus
from mitoviz.constants import (
    COLORS, NT_LENGTHS, STRANDS, TEXT_HA, TEXT_VA, TEXT_Y, TYPES
)
from mitoviz.utils import convert_nt


class _PolarLocus(_AbstractLocus):
    """ Class referring to a single mt locus, used in polar plots.

    Attributes:
        name: name of the locus
        index: index of the locus in the mt genome (dloop = 0, tf = 1, etc.)
    """
    _types = TYPES
    _nt_lengths = NT_LENGTHS
    _text_ha = TEXT_HA
    _text_va = TEXT_VA
    _text_y = TEXT_Y

    def __init__(self, name: str, index: int):
        super().__init__(name=name)
        self.index = index

    @property
    def loc_type(self) -> str:
        """ The locus type (regulatory, coding, rRNA, tRNA). """
        return self._types[self.index]

    @property
    def width(self) -> float:
        """ The relative width of the locus from its length in
        nucleotides.
        """
        return convert_nt(self._nt_lengths[self.index])

    @property
    def theta(self) -> float:
        """ The position at which the locus will be plotted. """
        if self.index == 0:
            return 0.0
        elif self.index == 1:
            return convert_nt(self._nt_lengths[0])/2 + self.width/2
        return (convert_nt(self._nt_lengths[0])/2 + self.width/2
                + sum(map(convert_nt, self._nt_lengths[1:self.index])))

    @property
    def color(self) -> str:
        """ The locus-type-specific color. """
        return COLORS[self.loc_type]

    @property
    def text_ha(self) -> str:
        """ The horizontal alignment for the text label. """
        return self._text_ha[self.index]

    @property
    def text_va(self) -> str:
        """ The vertical alignment for the text label. """
        return self._text_va[self.index]

    @property
    def text_y(self) -> float:
        """ The y position for the text label. """
        return self._text_y[self.index]

    def __repr__(self):
        return "{}(name={}, index={})".format(
            self.__class__.__name__, self.name, self.index
        )


class _PolarSplitLocus(_PolarLocus):
    """ Class referring to a single mt locus, used in polar plots with
    split strands.

    Attributes:
        name: name of the locus
        index: index of the locus in the mt genome (dloop = 0, tf = 1, etc.)
    """
    _types = TYPES + ["reg"]
    _nt_lengths = NT_LENGTHS + [546]
    _text_ha = TEXT_HA + ["center"]
    _text_va = TEXT_VA + ["center"]
    _text_y = TEXT_Y + [19.2]

    def __init__(self, name: str, index: int):
        super().__init__(name=name, index=index)

    @property
    def strand(self) -> str:
        """ The mitochondrial strand on which the locus is located. """
        return STRANDS[self.index]

    @property
    def bottom(self) -> float:
        """ The internal position of the locus, used to plot the locus on
        the H/L strand. """
        if self.strand == "H":
            return 22.5
        return 20.0

    @property
    def radius(self) -> float:
        """ The radius of the locus, used to plot the locus on the H/L
        strand. """
        if self.strand == "":  # non coding
            return 5.0
        return 2.5
