=====
Usage
=====

mitoviz can be used both from the command line and as a python module.

Command Line
------------

Given a VCF file with human mitochondrial variants (``sample.vcf``), plotting them is fairly
simple:

.. code-block:: console

    $ mitoviz sample.vcf

An image named ``mitoviz.png`` will be created in the current directory.

If you want to provide a specific filename where the plot will be saved, just add the ``--output``
option with the desired path:

.. code-block:: console

    $ mitoviz sample.vcf --output my_mt_plot.png

If the provided VCF file contains more than one sample, a separate plot will be created for each
of them; if you want to plot only a specific sample, use the ``--sample`` option:

.. code-block:: console

    $ mitoviz multisample.vcf --sample SRR1777294

It is possible to show labels above each variant using the ``--labels`` flag:

.. code-block:: console

    $ mitoviz sample.vcf --labels

Mitochondrial loci on mitoviz plots are drawn using a green color for protein-coding, blue for
tRNAs, red for rRNAs, orange for regulatory (D-Loop and L-strand origin) and grey for non-coding
loci. It is possible to include a legend in the
resulting plot, using the ``--legend`` option:

.. code-block:: console

    $ mitoviz sample.vcf --legend

The plot can draw loci located on H and L strands on two different levels, using the ``--split``
option:

.. code-block:: console

    $ mitoviz sample.vcf --split

mitoviz can create linear plots as well, where variants are shown using a *lollipop plot* style,
using the ``--linear`` option:

.. code-block:: console

    $ mitoviz sample.vcf --linear

Linear plots can be managed and customised using the ``--output``, ``--sample``, ``--labels``,
``--legend`` and ``--split`` options.

Polar and linear interactive plots can also be created by adding the ``--interactive`` option, and
will be saved to an HTML file:

.. code-block:: console

    $ mitoviz sample.vcf --interactive

It is also possible to plot variants stored in a tabular file, such as CSV or TSV formats; mitoviz
will automatically recognise them, treating the file as comma-separated by default. If a different
separator is used (as in the case of TSV files), just specify it with the ``--sep`` option:

.. code-block:: console

    $ mitoviz sample.tsv --sep "\t"

Additional keyword options can be specified in the format ``option=value``, and will be passed to
``pandas.read_table`` when processing the given input file:

.. code-block:: console

    $ mitoviz sample.tsv --sep "\t" comment=#

If you just need to create an empty mitochondrial plot, we've got you covered: use the
``mitoviz-base`` command and provide one or more options like ``--linear``, ``--interactive``,
``--legend``, ``--split``, ``--output``, based on your needs:

.. code-block:: console

    # Create a base polar plot
    $ mitoviz-base

    # Create a base linear plot and save it as "base_linear.png"
    $ mitoviz-base --linear --output "base_linear.png"

    # Create an interactive linear plot with split loci
    $ mitoviz-base --linear --interactive --split


Comprehensive help about the mitoviz CLI can be found with ``mitoviz --help`` and
``mitoviz-base --help``.

Python Module
-------------

Import mitoviz and use its ``plot_vcf`` function to use it in your own script:

.. code-block:: python

    from mitoviz import plot_vcf

    my_plot = plot_vcf("sample.vcf")

In this case, no plot will be shown until a call to ``plt.show()`` is made. It is possible to
save the resulting plot using the ``save`` option and to provide a specific file where the plot will be
saved using the ``output`` option:

.. code-block:: python

    from mitoviz import plot_vcf

    plot_vcf("sample.vcf", save=True, output="my_mt_plot.png")

If the provided VCF file contains more than one sample, a separate plot will be created for each
of them; if you want to plot only a specific sample, use the ``sample`` option:

.. code-block:: python

    from mitoviz import plot_vcf

    plot_vcf("multisample.vcf", save=True, sample="SRR1777294")

If you want to show labels for each variant plotted, add the ``labels=True`` option:

.. code-block:: python

    from mitoviz import plot_vcf

    plot_vcf("sample.vcf", labels=True)

It is possible to include a legend for loci colors in the output plot, using the ``legend=True``
option:

.. code-block:: python

    from mitoviz import plot_vcf

    plot_vcf("sample.vcf", legend=True)

Loci located on the H and L strands can be shown on two separate levels, using the ``split=True``
option:

.. code-block:: python

    from mitoviz import plot_vcf

    plot_vcf("sample.vcf", split=True)

Linear plots can be also created (instead of the default polar plot), using the ``linear=True``
option:

.. code-block:: python

    from mitoviz import plot_vcf

    plot_vcf("sample.vcf", linear=True)

The ``linear=True`` option can be combined with previously described options as well.

Interactive plots can be created with the ``interactive`` option, and can be either saved to an
HTML file or inspected in a Jupyter notebook:

.. code-block:: python

    # Show the interactive plot (works in a Jupyter notebook)
    plot_vcf("sample.vcf", interactive=True)
    # Save the interactive plot to an HTML file
    plot_vcf("sample.vcf", interactive=True, save=True)

Comprehensive help about the ``plot_vcf`` function can be found with ``help(mitoviz.plot_vcf)``.

A similar function to plot variants contained in a pandas DataFrame is available as ``plot_df``.
Supposing you have a pandas DataFrame with human mitochondrial variants named ``variants_df``, it
is possible to plot them as follows:

.. code-block:: python

    from mitoviz import plot_df

    plot_df(variants_df)

This function expects a DataFrame with at least a reference allele, position and alternate allele
columns; these are respectively called "REF", "POS" and "ALT" by default, but it is possible to
use custom column names:

.. code-block:: python

    from mitoviz import plot_df

    plot_df(variants_df, ref_col="position", ref_col="reference", alt_col="alternate")

It is possible to provide optional sample and hf (heteroplasmic fraction) columns, which are called
"SAMPLE" and "HF" by default but can be customised using the ``sample_col`` and ``hf_col`` options.

Apart from this, ``plot_df`` accepts the same set of options available for ``plot_vcf``.
Comprehensive help about the ``plot_df`` function can be found with ``help(mitoviz.plot_df)``.

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

    from mitoviz import plot_table

    plot_table("sample.tsv", sep="\t", comment="#", skiprows=0)


Comprehensive help about the ``plot_table`` function can be found with ``help(mitoviz.plot_table)``.

If you just need to create an empty mitochondrial plot, the ``plot_base`` function allows to do so,
and accepts the ``linear``, ``interactive``, ``legend``, ``split``, ``output`` and ``save``
arguments to further tweak its behaviour:

.. code-block:: python

    from mitoviz import plot_base

    # Create a base polar plot
    plot_base()
    # Create a base linear plot and save it as "base_linear.png"
    plot_base(linear=True, save=True, output="base_linear.png)
    # Create an interactive linear plot with split loci
    plot_base(linear=True, interactive=True, split=True)
