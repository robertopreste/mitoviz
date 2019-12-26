#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import sys
import click

from .plot import plot_vcf


@click.command()
@click.version_option()
@click.argument("input_vcf")
@click.option("--output", "-o", default="mitoviz.png",
              help="Output filename.")
def main(input_vcf, output):
    """ Plot variants on the human mitochondrial genome. """
    plot_vcf(in_vcf=input_vcf, save=True, output=output)

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
