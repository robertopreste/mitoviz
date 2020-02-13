#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
from typing import Union

import vcfpy

from mitoviz.classes.abstract_variant import _AbstractVariant
from mitoviz.utils import convert_hf, convert_nt


class _PolarVariant(_AbstractVariant):
    """ Class storing a given variant, used for polar plots.

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
        super().__init__(reference=reference,
                         position=position,
                         alternate=alternate,
                         hf=hf)

    @property
    def pos_x(self) -> float:
        """ The x position of the variant on the mitochondrial genome plot. """
        return convert_nt(self.position)

    @property
    def pos_y(self) -> float:
        """ The y position of the variant on the mitochondrial genome plot,
        based on its heteroplasmic fraction.
        """
        return 20 + convert_hf(self.hf)
