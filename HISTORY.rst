=======
History
=======

0.1.0 (2019-12-27)
==================

* First release.

0.2.0 (2019-12-29)
==================

* Add functionality to plot multiple samples.

0.2.1 (2020-01-06)
------------------

* Add legend to plots and update colors.

0.2.2 (2020-01-08)
------------------

* Add option to plot variant labels.

0.2.3 (2020-01-11)
------------------

* Make legend plotting optional.

0.3.0 (2020-01-15)
==================

* Add ``plot_df`` function to plot variants from a pandas DataFrame.

0.4.0 (2020-01-26)
==================

* Add ``plot_table`` function to plot variants from tabular files;
* add CLI functionality to plot variants from tabular files;
* refactor code.

0.4.1 (2020-02-13)
------------------

* Refactor to use abstract classes;
* Rename internal classes to _PolarLocus and _PolarVariant.

0.4.2 (2020-02-14)
------------------

* Fix bug with non coding loci not being shown in plots.

0.5.0 (2020-02-19)
==================

* Add ``split`` option to plot split strands on polar plots.

0.6.0 (2020-02-29)
==================

* ``_PolarVariant`` is deprecated and replaced by ``_Variant``;
* Add ``linear`` option to create linear plots.

0.6.1 (2020-03-02)
------------------

* Refactor and clean code;
* Add CI module for internal management.

0.6.2 (2020-03-03)
------------------

* Fix borders on linear plots.

0.6.3 (2020-03-04)
------------------

* Fix stemlines on split linear plots.

0.6.4 (2020-03-10)
------------------

* Fix loci label positions on polar plots.

0.7.0 (2020-03-15)
==================

* Add ``--interactive`` option to create interactive plots using plot.ly;
* Implement interactive basic polar plots;
* Implement interactive split polar plots.

0.7.1 (2020-03-28)
------------------

* Implement interactive basic linear plots;
* Implement interactive split linear plots.

0.8.0 (2020-04-05)
==================

* Add ``mitoviz-base`` command to create base mitochondrial plots.
