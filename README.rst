=======
mitoviz
=======


.. image:: https://img.shields.io/pypi/v/mitoviz.svg
        :target: https://pypi.python.org/pypi/mitoviz

.. image:: https://www.repostatus.org/badges/latest/wip.svg
    :alt: Project Status: WIP – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.
    :target: https://www.repostatus.org/#wip

.. image:: https://travis-ci.com/robertopreste/mitoviz.svg?branch=master
        :target: https://travis-ci.com/robertopreste/mitoviz

.. image:: https://codecov.io/gh/robertopreste/mitoviz/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/robertopreste/mitoviz

.. image:: https://readthedocs.org/projects/mitoviz/badge/?version=latest
        :target: https://mitoviz.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/robertopreste/mitoviz/python-3-shield.svg
     :target: https://pyup.io/repos/github/robertopreste/mitoviz/
     :alt: Python 3


Plot variants on the human mitochondrial genome.


* Free software: MIT license
* Documentation: https://mitoviz.readthedocs.io
* GitHub repo: https://github.com/robertopreste/mitoviz


Features
========

mitoviz is a simple python package to plot human mitochondrial variants on a graphical
representation of the human mitochondrial genome. It currently supports plotting variants
stored in VCF and tabular files, as well as from general ``pandas`` dataframes when using
mitoviz from inside Python.

Variants are shown according to their heteroplasmic fraction (HF), plotting variants with
HF = 1.0 on the outer border of the mitochondrial circle, those with HF = 0.0 on the inner
border and all the others according to their actual HF value.

.. image:: /images/sample_hf.png
  :alt: Mitochondrial plot with HF

If the HF information is not available, variants will all be shown in the middle of the
mitochondrial circle.

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
of them; if you want to only plot a specific sample, use the ``--sample`` option::

    $ mitoviz multisample.vcf --sample SRR1777294

It is also possible to plot variants stored in a tabular file, such as CSV or TSV formats; mitoviz
will automatically recognise them, treating the file as comma-separated by default. If a different
separator is used (as in the case of TSV files), just specify it with the ``--sep`` option::

    $ mitoviz sample.tsv --sep "\t"

Python Module
-------------

Import mitoviz and use its ``plot_vcf`` function to use it in your own script::

    from mitoviz import plot_vcf

    my_plot = plot_vcf("sample.vcf")

In this case, no plot will be shown until a call to ``plt.show()`` is made. It is possible to
save the resulting plot using the ``save`` option and to provide a specific file where the plot will be
saved using the ``output`` option::

    plot_vcf("sample.vcf", save=True, output="my_mt_plot.png")

If the provided VCF file contains more than one sample, a separate plot will be created for each
of them; if you want to only plot a specific sample, use the ``sample`` option::

    plot_vcf("multisample.vcf", save=True, sample="SRR1777294")

A similar function to plot variants contained in a pandas DataFrame is available as ``plot_df``.
Supposing you have a pandas DataFrame with human mitochondrial variants named ``variants_df``, it
is possible to plot them as follows::

    from mitoviz import plot_df

    plot_df(variants_df)

Variants stored in tabular files can be plotted using ``plot_table``, which accepts the same
options available for ``plot_vcf`` and ``plot_df``, with the addition of ``sep``, which is used to
specify the column separator. By default, the comma is used as column delimiter::

    from mitoviz import plot_table

    # plotting a CSV file
    plot_table("sample.csv")
    # plotting a TSV (tab-separated) file
    plot_table("sample.tsv", sep="\t")

``plot_table`` also accept additional keyword options, which will be passed to ``pandas.read_table``
when processing the given input file::

    plot_table("sample.tsv", sep="\t", comment="#", skiprows=0)

Please refer to the Usage_ section of the documentation for further information.

Installation
============

**PLEASE NOTE: HmtNote only supports Python >= 3.6!**

The preferred installation method for mitoviz is using ``pip``::

    $ pip install mitoviz

Please refer to the Installation_ section of the documentation for further information.

Credits
=======

This package was created with Cookiecutter_ and the `cc-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cc-pypackage`: https://github.com/robertopreste/cc-pypackage
.. _Usage: https://mitoviz.readthedocs.io/en/latest/usage.html
.. _Installation: https://mitoviz.readthedocs.io/en/latest/installation.html
