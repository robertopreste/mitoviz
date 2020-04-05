#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import sys

import click

from mitoviz.mitoviz import plot_base


@click.command("mitoviz-base")
@click.version_option()
@click.option("--linear", "-r", default=False, is_flag=True,
              help="Show a linear plot rather than a polar one.")
@click.option("--output", "-o", default=None, help="Output filename.")
@click.option("--legend", "-L", default=False, is_flag=True,
              help="Add legend to the plot.")
@click.option("--split", "-p", default=False, is_flag=True,
              help="Plot split H and L strands.")
@click.option("--interactive", "-i", default=False, is_flag=True,
              help="Create an interactive version of the plot.")
def main(linear, output, legend, split, interactive):
    """ Plot an empty base mitochondrial representation. """
    plot_base(linear=linear, save=True, output=output, legend=legend,
              split=split, interactive=interactive)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
