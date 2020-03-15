#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
from typing import Tuple

from mitoviz.classes.base_locus import _BaseLocus
from mitoviz.constants import (
    NT_LENGTHS, STARTS, TEXT_HA, TEXT_VA, TEXT_Y, TYPES
)
from mitoviz.utils import convert_nt, convert_plotly


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
    _types = TYPES

    def __init__(self, name: str, index: int):
        super().__init__(name=name, index=index)

    @property
    def loc_type(self) -> str:
        """ The locus type (regulatory, coding, rRNA, tRNA, non-coding). """
        return self._types[self.index]

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
    def theta_p(self) -> float:
        """ The position at which the locus will be plotted when using plotly.
        """
        return convert_plotly(self.theta)

    @property
    def width(self) -> float:
        """ The relative width of the locus from its length in
        nucleotides. """
        return convert_nt(self._nt_lengths[self.index])

    @property
    def width_p(self) -> float:
        """ The relative width of the locus from its length in
        nucleotides when using plotly. """
        return convert_plotly(self.width)


class _PolarSplitLocus(_PolarLocus):
    """ Class referring to a single mt locus, used in polar plots with
    split strands.

    Attributes:
        name: name of the locus
        index: index of the locus in the mt genome (dloop = 0, tf = 1, etc.)
    """
    _nt_lengths = NT_LENGTHS + [546]
    _text_ha = TEXT_HA + ["center"]
    _text_va = TEXT_VA + ["center"]
    _text_y = TEXT_Y + [19.2]
    _types = TYPES + ["reg"]

    def __init__(self, name: str, index: int):
        super().__init__(name=name, index=index)

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


class _LinearLocus(_BaseLocus):
    """ Class referring to a single mt locus, used in linear plots.

    Attributes:
        name: name of the locus
        index: index of the locus in the mt genome (dloop = 0, tf = 1, etc.)
    """
    _nt_lengths = [576] + NT_LENGTHS[1:] + [546]
    _starts = STARTS
    _types = TYPES + ["reg"]

    def __init__(self, name: str, index: int):
        super().__init__(name=name, index=index)

    @property
    def height(self) -> Tuple[float, float]:
        """ The vertical position of the locus, if plotting split strands. """
        if self.strand == "H":
            return (-0.05, 0.05)
        elif self.strand == "L":
            return (-0.1, 0.05)
        return (-0.1, 0.1)

    @property
    def loc_type(self) -> str:
        """ The locus type (regulatory, coding, rRNA, tRNA). """
        return self._types[self.index]

    @property
    def start(self) -> int:
        """ Position on the mt genome where the locus starts. """
        return self._starts[self.index]

    @property
    def text_x(self) -> float:
        """ The x position for the text label. """
        return self.start + (self.width / 2)

    @property
    def text_y(self) -> float:
        """ The y position for the text label. """
        if self.name in ["TQ", "TA", "TC", "TD", "TK", "TS2", "TP"]:
            return -0.13
        return -0.12

    @property
    def width(self) -> float:
        """ The width of the locus in nucleotides. """
        return self._nt_lengths[self.index]
