#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
from traits.api import Bool, Either, Enum, Float, HasTraits, Int, Property, Str
import vcfpy

from mitoviz.constants import COLOR_MAPS
from mitoviz.utils import convert_hf, convert_nt


class _Variant(HasTraits):
    """ Class storing a given variant, used for both linear and polar plots.

    Attributes:
        reference: reference allele of the variant
        position: position of the variant
        alternate: alternate allele of the variant
        hf: heteroplasmic fraction of the variant
    """

    reference = Str()
    position = Int()
    alternate = Either(Str, vcfpy.Substitution)
    hf = Float(0.5)
    color = Property(Enum("grey", "#2e8b57", "#ffa500", "#cd5c5c", "#4169e1"))
    label = Property(Str)
    linear_x = Property(Int)
    linear_y = Property(Float)
    polar_x = Property(Float)
    polar_y = Property(Float)
    strand = Property(Enum("", "H", "L"))
    _is_deletion = Property(Bool)
    _is_insertion = Property(Bool)

    def _get__is_deletion(self):
        """ Check whether the current variant refers to a deletion. """
        # e.g. ref CTG | alt C
        if isinstance(self.alternate, vcfpy.Substitution):
            return self.alternate.type == "DEL"
        return len(self.reference) > len(self.alternate)

    def _get__is_insertion(self):
        """ Check whether the current variant refers to an insertion. """
        # e.g. ref C | alt CTG
        if isinstance(self.alternate, vcfpy.Substitution):
            return self.alternate.type == "INS"
        return len(self.reference) < len(self.alternate)

    def _get_color(self):
        """ The color of the locus on which the variant is located. """
        for (start, stop), color in COLOR_MAPS.items():
            if self.position in range(start, stop + 1):
                return color

    def _get_label(self):
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

    def _get_linear_x(self):
        """ The x position of the variant on the linear mt genome plot. """
        return self.position

    def _get_linear_y(self):
        """ The y position of the variant on the linear mt genome plot. """
        return self.hf

    def _get_polar_x(self):
        """ The x position of the variant on the polar mt genome plot. """
        return convert_nt(self.position)

    def _get_polar_y(self):
        """ The y position of the variant on the polar mt genome plot. """
        return 20 + convert_hf(self.hf)

    def _get_strand(self):
        """ The mitochondrial strand on which the variant's locus is located.
        """
        if self.position in [*range(0, 576), *range(4331, 4400),
                             *range(5586, 5655), *range(5656, 5729),
                             *range(5729, 5761), *range(5760, 5826),
                             *range(5826, 5892), *range(7445, 7517),
                             *range(14148, 14673), *range(14673, 14742),
                             *range(15955, 16024), *range(16023, 16569)]:
            return "L"
        elif self.position in [*range(3304, 3306), *range(4400, 4401),
                               *range(5579, 5586), *range(5655, 5656),
                               *range(5891, 5903), *range(7514, 7517),
                               *range(8269, 8294), *range(8364, 8365),
                               *range(14742, 14746), *range(15953, 15955)]:
            return ""
        else:
            return "H"

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
