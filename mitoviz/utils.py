#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os
from typing import Optional, Tuple


def convert_nt(nt: int) -> float:
    """ Convert a nucleotide position/width to a relative value.

    Used to calculate relative values required for polar plots.

    Args:
        nt: position/width in nucleotides

    Returns:
        relative value
    """
    return (nt * 6.29) / 16569


def convert_hf(hf: float) -> float:
    """ Convert a variant's HF value from the [0.0, 1.0] range to [0.0, 5.0].

    Used to plot the variant on a polar plot.

    Args:
        hf: heteroplasmic fraction of the variant

    Returns:
        adjusted HF value
    """
    return hf * 5


def convert_plotly(value: float) -> float:
    """ Convert the given element to the proper value used in plotly polar
    plots.

    Works with _Variant.polar_x, _PolarLocus.theta, _PolarLocus.width, using
    the somehow magic number 57.1.

    Args:
        value: input value to convert

    Returns:
        adjusted value
    """
    return value * 57.1


def parse_path(path: Optional[str]) -> Tuple[str, str, str]:
    """ Parse the given path into directory name, file name and extension.

    Args:
        path: output path to parse; if None, returns the current directory
            and an empty file name

    Returns:
        tuple with directory name, file name and extension
    """
    if path:
        dirname = os.path.dirname(path)
        filename = os.path.basename(path)
        name, ext = os.path.splitext(filename)
    else:
        dirname = os.getcwd()
        name = ""
        ext = ".png"

    return dirname, name, ext
