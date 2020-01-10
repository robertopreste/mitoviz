#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import sys
import click

from .plot import plot_vcf


@click.command()
@click.version_option()
@click.argument("input_vcf")
@click.option("--sample", "-s", default=None, help="Specific sample to plot.")
@click.option("--output", "-o", default=None, help="Output filename.")
@click.option("--labels", "-l", default=False, is_flag=True,
              help="Add variant labels.")
@click.option("--legend", "-L", default=False, is_flag=True,
              help="Add legend to the plot.")
def main(input_vcf, sample, output, labels, legend):
    """ Plot variants on the human mitochondrial genome. """
    plot_vcf(in_vcf=input_vcf, sample=sample, save=True, output=output,
             labels=labels, legend=legend)

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
