=====
Usage
=====

mitoviz can be used both from the command line and as a python module.

Command Line
------------

Given a VCF file with human mitochondrial variants (``sample.vcf``), plotting them is fairly
simple::

    $ mitoviz sample.vcf

An image named ``mitoviz.png`` will be created in the current directory.

If you want to provide a specific filename where the plot will be saved, just add the ``--output``
option with the desired path::

    $ mitoviz sample.vcf --output my_mt_plot.png

If the provided VCF file contains more than one sample, a separate plot will be created for each
of them; if you want to plot only a specific sample, use the ``--sample`` option::

    $ mitoviz multisample.vcf --sample SRR1777294

It is possible to show labels above each variant using the ``--labels`` flag::

    $ mitoviz sample.vcf --labels

Mitochondrial loci on mitoviz plots are drawn using a green color for protein-coding, blue for
tRNAs, red for rRNAs and orange for regulatory (D-Loop). It is possible to include a legend in the
resulting plot, using the ``--legend`` option::

    $ mitoviz sample.vcf --legend

Comprehensive help about the mitoviz CLI can be found with ``mitoviz --help``.

Python Module
-------------

Import mitoviz and use its ``plot_vcf`` function to use it in your own script::

    from mitoviz import plot_vcf

    my_plot = plot_vcf("sample.vcf")

In this case, no plot will be shown until a call to ``plt.show()`` is made. It is possible to
save the resulting plot using the ``save`` option and to provide a specific file where the plot will be
saved using the ``output`` option::

    from mitoviz import plot_vcf

    plot_vcf("sample.vcf", save=True, output="my_mt_plot.png")

If the provided VCF file contains more than one sample, a separate plot will be created for each
of them; if you want to plot only a specific sample, use the ``sample`` option::

    from mitoviz import plot_vcf

    plot_vcf("multisample.vcf", save=True, sample="SRR1777294")

If you want to show labels for each variant plotted, add the ``labels=True`` option::

    from mitoviz import plot_vcf

    plot_vcf("sample.vcf", labels=True)

It is possible to include a legend for loci colors in the output plot, using the ``legend=True``
option::

    from mitoviz import plot_vcf

    plot_vcf("sample.vcf", legend=True)

Comprehensive help about the ``plot_vcf`` function can be found with ``help(mitoviz.plot_vcf)``.

A similar function to plot variants contained in a pandas DataFrame is available as ``plot_df``.
Supposing you have a pandas DataFrame with human mitochondrial variants named ``variants_df``, it
is possible to plot them as follows::

    from mitoviz import plot_df

    plot_df(variants_df)

This function expects a DataFrame with at least a reference allele, position and alternate allele
columns; these are respectively called "REF", "POS" and "ALT" by default, but it is possible to
use custom column names::

    from mitoviz import plot_df

    plot_df(variants_df, ref_col="position", ref_col="reference", alt_col="alternate")

It is possible to provide optional sample and hf (heteroplasmic fraction) columns, which are called
"SAMPLE" and "HF" by default but can be customised using the ``sample_col`` and ``hf_col`` options.

Apart from this, ``plot_df`` accepts the same set of options available for ``plot_vcf``; more
comprehensive help about the ``plot_df`` function can be found with ``help(mitoviz.plot_df)``.
