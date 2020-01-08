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
