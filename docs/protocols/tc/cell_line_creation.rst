==================
Cell Line Creation
==================


.. time:: 1 month

    While the intial transfection does not take very long, the selection
    process takes a long time!

.. note::
    Except for day 0, all steps are the same for the creation of PiggyBac, Crispr,
    or TALEN cell lines

    This protocol is still in development! In particular, for PiggyBacs, the ratio of
    transposase to integration plasmid is a key variable that must be tuned!

    An efficient selection method has also not been fully tested.

Day -1
~~~~~~
Seed your cells such that they will be around 30-40% confluent on the next day. There is an
extended selection outgrowth period required, which means we should start with lower confluence.

Day 0
~~~~~~
Follow the step for the cell line type to generate
    - PiggyBac
        - Co-transfect the PiggyBac plasmid alongside your plasmid containing PB recognition sites at a 1:1 mass ratio.
    - Crispr
        - Co-transfect the Crispr/guide plasmid alongside your plasmid containing locus-specific recognition sites at a 1:1 mass ratio.
    - TALEN
        - Co-transfect the TALEN-R and TALEN-L plasmids alongside your plasmid containing locus-specific recognition sites at a 1:1:1 mass ratio.
Day 1 - 4
~~~~~~~~~
Media change into selection media. Continue dilution until decent cell death occurs, or the cells are too dense.

Week 2
~~~~~~
Dilute the cells roughly 5 to 1 (~20% confluence), using non-selection media.

Week 2 + 1 day
~~~~~~~~~~~~~~
One day later, switch back into selection media. Continue selecting until you have roughly 25% of the
cells showing successful reporter output.

Week n, Day 1
~~~~~~~~~~~~~
Dilute to 1000 cells per mL, then seed 1-3 96-well plates with 100 uL in each well (e.g. 1 cell per well on average). Make sure to replace media roughly every 3-4 days to ensure that wells do not fully evaporate.


.. figure:: /img/post_pb_dilution.png
    :width: 50%
    :align: center

    Example of what outgrowth looks like when grown out from a single-cell dilution.
    This is one well in a 96-well dilution plate.
