#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
from typing import Union

import vcfpy

from mitoviz.constants import COLOR_MAPS
from mitoviz.utils import convert_hf, convert_nt


class _Variant:
    """ Class storing a given variant, used for both linear and polar plots.

    Attributes:
        reference: reference allele of the variant
        position: position of the variant
        alternate: alternate allele of the variant
        hf: heteroplasmic fraction of the variant
    """

    def __init__(self,
                 reference: str,
                 position: int,
                 alternate: Union[str, vcfpy.Substitution],
                 hf: float):
        self.reference = reference
        self.position = position
        self.alternate = alternate
        self.hf = hf

    @property
    def _is_deletion(self) -> bool:
        """ Check whether the current variant refers to a deletion. """
        # e.g. ref CTG | alt C
        if isinstance(self.alternate, vcfpy.Substitution):
            return self.alternate.type == "DEL"
        return len(self.reference) > len(self.alternate)

    @property
    def _is_insertion(self) -> bool:
        """ Check whether the current variant refers to an insertion. """
        # e.g. ref C | alt CTG
        if isinstance(self.alternate, vcfpy.Substitution):
            return self.alternate.type == "INS"
        return len(self.reference) < len(self.alternate)

    @property
    def color(self) -> str:
        """ The color of the locus on which the variant is located. """
        for (start, stop), color in COLOR_MAPS.items():
            if self.position in range(start, stop + 1):
                return color

    @property
    def label(self) -> str:
        """ Create the variant label for deletions, insertions and SNPs. """
        alternate = (self.alternate.value
                     if isinstance(self.alternate, vcfpy.Substitution)
                     else self.alternate)
        if self._is_deletion:
            label = "{}d".format(int(self.position) + 1)
        elif self._is_insertion:
            label = "{}.{}".format(
                self.position, alternate[len(self.reference):]
            )
        else:
            label = "{}{}>{}".format(self.position, self.reference, alternate)

        return label

    @property
    def linear_x(self) -> int:
        """ The x position of the variant on the linear mt genome plot. """
        return self.position

    @property
    def linear_y(self) -> float:
        """ The y position of the variant on the linear mt genome plot. """
        return self.hf

    @property
    def polar_x(self) -> float:
        """ The x position of the variant on the polar mt genome plot. """
        return convert_nt(self.position)

    @property
    def polar_y(self) -> float:
        """ The y position of the variant on the polar mt genome plot. """
        return 20 + convert_hf(self.hf)

    def __key(self):
        return self.reference, self.position, self.alternate, self.hf

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        if isinstance(other, _Variant):
            return self.__key() == other.__key()
        return NotImplemented

    def __repr__(self):
        return "{}(reference={}, position={}, alternate={}, hf={})".format(
            self.__class__.__name__, self.reference, self.position,
            self.alternate, self.hf
        )
