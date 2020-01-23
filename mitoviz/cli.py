#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os
import sys

import click

from mitoviz.mitoviz import plot_table, plot_vcf


@click.command(context_settings=dict(ignore_unknown_options=True,
                                     allow_extra_args=True))
@click.version_option()
@click.argument("input_file", type=click.Path(exists=True))
@click.option("--sample", "-s", default=None, help="Specific sample to plot.")
@click.option("--output", "-o", default=None, help="Output filename.")
@click.option("--labels", "-l", default=False, is_flag=True,
              help="Add variant labels.")
@click.option("--legend", "-L", default=False, is_flag=True,
              help="Add legend to the plot.")
@click.option("--sep", "-S", default=",",
              help="Column delimiter used (if INPUT_FILE is not a VCF file)")
@click.pass_context
def main(ctx, input_file, sample, output, labels, legend, sep):
    """ Plot variants on the human mitochondrial genome. """
    ext = os.path.splitext(os.path.basename(input_file))[-1]
    if ext.casefold() == ".vcf":
        plot_vcf(in_vcf=input_file, sample=sample, save=True, output=output,
                 labels=labels, legend=legend)
    else:
        pandas_opts = dict()
        if ctx.args:
            pandas_opts.update([el.split("=") for el in ctx.args])
        plot_table(in_table=input_file, sep=sep, sample=sample, save=True,
                   output=output, labels=labels, legend=legend, **pandas_opts)

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
