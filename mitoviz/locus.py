#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
from mitoviz.classes.abstract_locus import _AbstractLocus
from mitoviz.constants import (
    COLORS, NT_LENGTHS, TEXT_HA, TEXT_VA, TEXT_Y, TYPES
)
from mitoviz.utils import convert_nt


class _PolarLocus(_AbstractLocus):
    """ Class referring to a single mt locus, used in polar plots.

    Attributes:
        name: name of the locus
        index: index of the locus in the mt genome (dloop = 0, tf = 1, etc.)
    """

    def __init__(self, name: str, index: int):
        super().__init__(name=name)
        self.index = index

    @property
    def loc_type(self) -> str:
        """ The locus type (regulatory, coding, rRNA, tRNA). """
        return TYPES[self.index]

    @property
    def width(self) -> float:
        """ The relative width of the locus from its length in
        nucleotides.
        """
        return convert_nt(NT_LENGTHS[self.index])

    @property
    def theta(self) -> float:
        """ The position at which the locus will be plotted. """
        if self.index == 0:
            return 0.0
        elif self.index == 1:
            return convert_nt(NT_LENGTHS[0])/2 + self.width/2
        return (convert_nt(NT_LENGTHS[0])/2 + self.width/2
                + sum(map(convert_nt, NT_LENGTHS[1:self.index])))

    @property
    def color(self) -> str:
        """ The locus-type-specific color. """
        return COLORS[self.loc_type]

    @property
    def text_ha(self) -> str:
        """ The horizontal alignment for the text label. """
        return TEXT_HA[self.index]

    @property
    def text_va(self) -> str:
        """ The vertical alignment for the text label. """
        return TEXT_VA[self.index]

    @property
    def text_y(self) -> float:
        """ The y position for the text label. """
        return TEXT_Y[self.index]

    def __repr__(self):
        return "{}(name={}, index={})".format(
            self.__class__.__name__, self.name, self.index
        )
