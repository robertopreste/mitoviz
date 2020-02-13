#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
from abc import ABC, abstractmethod
from typing import Union

import vcfpy


class _AbstractVariant(ABC):
    """ Class used to store a given variant.

    Polar plots and linear plots use a different flavor of this base
    class.
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
    @abstractmethod
    def pos_x(self):
        """ The x position of the variant on the mitochondrial plot. """
        pass

    @property
    @abstractmethod
    def pos_y(self):
        """ The y position of the variant on the mitochondrial plot. """
        pass

    def __key(self):
        return self.reference, self.position, self.alternate, self.hf

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        if isinstance(other, _AbstractVariant):
            return self.__key() == other.__key()
        return NotImplemented

    def __repr__(self):
        return "{}(reference={}, position={}, alternate={}, hf={})".format(
            self.__class__.__name__, self.reference, self.position,
            self.alternate, self.hf
        )
