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
