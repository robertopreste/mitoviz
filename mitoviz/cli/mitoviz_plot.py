#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os
import sys

import click

from mitoviz.mitoviz import plot_table, plot_vcf


@click.command("mitoviz", context_settings=dict(ignore_unknown_options=True,
                                                allow_extra_args=True))
@click.version_option()
@click.argument("input_file", type=click.Path(exists=True))
@click.option("--linear", "-r", default=False, is_flag=True, show_default=True,
              help="Plot variants on a linear plot rather than a polar one.")
@click.option("--sample", "-s", default=None, show_default=True,
              help="Specific sample to plot.")
@click.option("--output", "-o", default=None, show_default=True,
              help="Output filename.")
@click.option("--labels", "-l", default=False, is_flag=True, show_default=True,
              help="Add variant labels.")
@click.option("--labels-hf", default=False, is_flag=True, show_default=True,
              help="Show HF value in each variant's label")
@click.option("--legend", "-L", default=False, is_flag=True, show_default=True,
              help="Add legend to the plot.")
@click.option("--split", "-p", default=False, is_flag=True, show_default=True,
              help="Plot split H and L strands.")
@click.option("--interactive", "-i", default=False, is_flag=True,
              show_default=True,
              help="Create an interactive version of the plot.")
@click.option("--sep", "-S", default=",", show_default=True,
              help="Column delimiter used (if INPUT_FILE is not a VCF file)")
@click.pass_context
def main(ctx, input_file, linear, sample, output, labels, labels_hf, legend,
         split, interactive, sep):
    """ Plot human mitochondrial variants available in INPUT_FILE. """
    ext = os.path.splitext(os.path.basename(input_file))[-1]
    if ext.casefold() == ".vcf":
        plot_vcf(in_vcf=input_file, linear=linear, sample=sample, save=True,
                 output=output, labels=labels, labels_hf=labels_hf,
                 legend=legend, split=split, interactive=interactive)
    else:
        pandas_opts = dict()
        if ctx.args:
            pandas_opts.update([el.split("=") for el in ctx.args])
        plot_table(in_table=input_file, sep=sep, linear=linear, sample=sample,
                   save=True, output=output, labels=labels,
                   labels_hf=labels_hf,  legend=legend, split=split,
                   interactive=interactive,
                   **pandas_opts)

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
