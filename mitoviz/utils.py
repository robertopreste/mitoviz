#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste


def convert_nt(nt: int) -> float:
    """ Convert a nucleotide position/width to a relative value.

    Used to calculate relative values required for polar plots.

    Parameters
    ----------
    nt : int
        Position/width in nucleotides.

    Returns
    -------
    float
        Relative value.
    """
    return (nt * 6.29) / 16569


def convert_hf(hf: float) -> float:
    """ Convert a variant's HF value from the [0.0, 1.0] range to [0.0, 5.0].

    Used to plot the variant on a polar plot.

    Parameters
    ----------
    hf : float
        Heteroplasmic fraction of the variant.

    Returns
    -------
    float
        Adjusted HF value.
    """
    return hf * 5
