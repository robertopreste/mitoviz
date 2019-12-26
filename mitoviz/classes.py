#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import vcfpy

from .constants import COLORS, NT_LENGTHS, TEXT_HA, TEXT_VA, TEXT_Y, TYPES
from .utils import convert_hf, convert_nt


class Locus:
    """ Class referring to a single mt locus.

    Used to create the base mitochondrial plot on which variants will
    be added on a separate layer.

    Attributes:
        name: name of the locus
        index: index of the locus in the mt genome (dloop = 0, tf = 1, etc.)
    """

    def __init__(self, name: str, index: int):
        self.name = name
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


class Variant:
    """ Class used to store a given variant.

    Attributes:
        reference: reference allele of the variant
        position: position of the variant
        alternate: alternate allele of the variant
        hf: heteroplasmic fraction of the variant
    """

    def __init__(self,
                 reference: str,
                 position: int,
                 alternate: vcfpy.Substitution,
                 hf: float):
        self.reference = reference
        self.position = position
        self.alternate = alternate
        self.hf = hf

    def _is_deletion(self) -> bool:
        """ Check whether the current variant refers to a deletion. """
        # e.g. ref CTG | alt C
        return self.alternate.type == "DEL"

    def _is_insertion(self) -> bool:
        """ Check whether the current variant refers to an insertion. """
        # e.g. ref C | alt CTG
        return self.alternate.type == "INS"

    @property
    def label(self) -> str:
        """ Create the variant label for deletions, insertions and SNPs. """
        if self._is_deletion():
            label = "{}d".format(int(self.position) + 1)
        elif self._is_insertion():
            label = "{}.{}".format(
                self.position, self.alternate.value[len(self.reference):]
            )
        else:
            label = "{}{}>{}".format(self.position, self.reference,
                                     self.alternate.value)

        return label

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

    def __repr__(self):
        return "{}(reference={}, position={}, alternate={}, hf={})".format(
            self.__class__.__name__, self.reference, self.position,
            self.alternate, self.hf
        )


class VcfParser:
    """ Class to read and parse the given VCF file.

    Attributes
        vcf_in: path of the input VCF file
    """

    def __init__(self, vcf_in: str):
        self.vcf_in = vcf_in
        self._variants = []
        self._reader = vcfpy.Reader.from_path(vcf_in)
        self.parse_variants()

    @property
    def variants(self):
        return self._variants

    @variants.setter
    def variants(self, value):
        if isinstance(value, list):
            self._variants.extend(value)
        elif isinstance(float, value):
            self._variants.append(value)
        else:
            raise ValueError("not allowed")

    def parse_variants(self):
        """ Read the variants from the input VCF file and parse them in the
            required format.
        """
        for record in self._reader:
            if "HF" in record.FORMAT:
                variants = [
                    Variant(record.REF, record.POS, alt,
                            record.calls[0].data["HF"][i])
                    for i, alt in enumerate(record.ALT)
                ]
            else:
                variants = [
                    Variant(record.REF, record.POS, alt, 0.5)
                    for alt in record.ALT
                ]
            self.variants = variants

    def __repr__(self):
        return "{}(vcf_in={})".format(
            self.__class__.__name__, self.vcf_in
        )
