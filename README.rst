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


Plot variants on the human mitochondrial genome.


* Free software: MIT license
* Documentation: https://mitoviz.readthedocs.io
* GitHub repo: https://github.com/robertopreste/mitoviz


Features
========

mitoviz is a simple python package to plot human mitochondrial variants on a graphical
representation of the human mitochondrial genome. It currently supports plotting variants
stored in VCF and tabular files, as well as from general ``pandas`` dataframes when importing
mitoviz in Python.

Variants are shown according to their heteroplasmic fraction (HF), plotting variants with
HF = 1.0 on the outer border of the mitochondrial circle, those with HF = 0.0 on the inner
border and all the others in between, according to their actual HF value.

.. image:: https://github.com/robertopreste/mitoviz/raw/master/mitoviz/tests/images/sample_hf.png
  :alt: Mitochondrial plot with HF

If the HF information is not available, variants will all be shown in the middle of the
mitochondrial circle.

A linear representation of the mitochondrial genome can also be plotted; in this case,
variants are shown using a *lollipop plot* style, with the height of the marker reflecting
their HF.

.. image:: https://github.com/robertopreste/mitoviz/raw/master/mitoviz/tests/images/sample_linear_hf.png
  :alt: Mitochondrial linear plot with HF

Variants with no HF information will be shown as if their HF was 0.5.

Usage
=====

mitoviz can be used both from the command line and as a python module.

Command Line
------------

Given a VCF file with human mitochondrial variants (``sample.vcf``), plotting them is fairly
simple:

.. code-block:: console

    $ mitoviz sample.vcf

An image named ``mitoviz.png`` will be created in the current directory; if you want to provide a
specific filename where the plot will be saved, just add the ``--output`` option with the desired
path:

.. code-block:: console

    $ mitoviz sample.vcf --output my_mt_plot.png

Linear plots can be created using the ``--linear`` option:

.. code-block:: console

    $ mitoviz sample.vcf --linear

Polar and linear interactive plots can also be created by adding the ``--interactive`` option, and
will be saved to an HTML file:

.. code-block:: console

    $ mitoviz sample.vcf --interactive

It is also possible to plot variants stored in a tabular file, such as CSV or TSV formats; mitoviz
will automatically recognise them, treating the file as comma-separated by default. If a different
separator is used (as in the case of TSV files), just specify it with the ``--sep`` option:

.. code-block:: console

    $ mitoviz sample.tsv --sep "\t"

If you just need to create an empty mitochondrial plot, we've got you covered: use the
``mitoviz-base`` command and provide one or more options like ``--linear``, ``--interactive``,
``--legend``, ``--split``, ``--output``, based on your needs.

Python Module
-------------

Import mitoviz and use its ``plot_vcf`` function to use it in your own script:

.. code-block:: python

    from mitoviz import plot_vcf

    my_plot = plot_vcf("sample.vcf")

In this case, no plot will be shown until a call to ``plt.show()`` is made. It is possible to
save the resulting plot using the ``save`` option and to provide a specific file where the plot
will be saved using the ``output`` option:

.. code-block:: python

    plot_vcf("sample.vcf", save=True, output="my_mt_plot.png")

By default, a polar plot is returned; linear plots are easily created using the ``linear`` option:

.. code-block:: python

    plot_vcf("sample.vcf", save=True, linear=True)

Interactive plots can be created with the ``interactive`` option, and can be either saved to an
HTML file or inspected in a Jupyter notebook:

.. code-block:: python

    # Show the interactive plot (works in a Jupyter notebook)
    plot_vcf("sample.vcf", interactive=True)
    # Save the interactive plot to an HTML file
    plot_vcf("sample.vcf", interactive=True, save=True)

A similar function to plot variants contained in a pandas DataFrame is available as ``plot_df``.
Supposing you have a pandas DataFrame with human mitochondrial variants named ``variants_df``, it
is possible to plot them as follows:

.. code-block:: python

    from mitoviz import plot_df

    plot_df(variants_df)

Variants stored in tabular files can be plotted using ``plot_table``, which accepts the same
options available for ``plot_vcf`` and ``plot_df``, with the addition of ``sep``, which is used to
specify the column separator. By default, the comma is used as column delimiter:

.. code-block:: python

    from mitoviz import plot_table

    # plotting a CSV file
    plot_table("sample.csv")
    # plotting a TSV (tab-separated) file
    plot_table("sample.tsv", sep="\t")

``plot_table`` also accept additional keyword options, which will be passed to ``pandas.read_table``
when processing the given input file:

.. code-block:: python

    plot_table("sample.tsv", sep="\t", comment="#", skiprows=0)

If you just need to create an empty mitochondrial plot, the ``plot_base`` function allows to do so,
and accepts the ``linear``, ``interactive``, ``legend``, ``split``, ``output`` and ``save``
arguments to further tweak its behaviour.

Please refer to the Usage_ section of the documentation for further information.

Installation
============

**PLEASE NOTE: HmtNote only supports Python >= 3.6!**

The preferred installation method for mitoviz is using ``pip``:

.. code-block:: console

    $ pip install mitoviz

Please refer to the Installation_ section of the documentation for further information.

Credits
=======

This package was created with Cookiecutter_ and the `cc-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cc-pypackage`: https://github.com/robertopreste/cc-pypackage
.. _Usage: https://mitoviz.readthedocs.io/en/latest/usage.html
.. _Installation: https://mitoviz.readthedocs.io/en/latest/installation.html
