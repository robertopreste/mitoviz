#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
from abc import ABC, abstractmethod


class _AbstractLocus(ABC):
    """ Class referring to a single mitochondrial locus.

    Used to create the base mitochondrial plot, on which variants will
    be added using a separate layes.
    Polar plots and linear plots use a different flavor of this base
    class.
    """

    def __init__(self, name: str):
        self.name = name
        super().__init__()

    @property
    @abstractmethod
    def loc_type(self):
        """ The locus type (regulatory, coding, rRNA, tRNA). """
        pass

    @property
    @abstractmethod
    def width(self):
        """ The width of the locus. """
        pass

    @property
    @abstractmethod
    def color(self):
        """ The locus-type-specific color. """
        pass

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name})"
