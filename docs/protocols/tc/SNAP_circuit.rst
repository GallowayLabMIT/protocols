============================================================
SNAP circuit (Transient expression in 96-well plate version)
============================================================


Materials
=========

- Cells
- Plates
- DMEM supplemented with 10% FBS
- PEI
- Small molecule inducer such as guanine or O6-benzylguanine (check the concentration that you will need)
- Output construct: plasmid expressing reporter gene-ribozyme switch cassette (e.g, pHAGE-UBC-mGreenLantern-p2g6)
- Input construct: plasmid expressing SNAPtag conjugated with target protein (e.g, pHAGE-SNAP-tagBFP)


Procedure
=========

Day 1: Seed cells
-----------------------------------

1. Seed the cells at a density of 2.5-4k cells/well in a 96-well plate
2. Incubate the cells at 37C overnight

Day 2. Transfection
-------------------

1. Transfect 100μg of the input and output plasmids per well with PEI by following the :doc:`general transfection protocol <./tc-basics/transient_transfection>`. If your small molecule or the solvent has cytotoxicity, using a lower PEI:DNA ratio of 3:1 is recommended.
2. Incubate the cells overnight

Day 3: Small molecule treatment
-------------------------------

1. Remove the media from the wells, being careful not to detach the cells, and add 100μl of fresh media that contains the small molecule inducer such as O6-benzylguanine or the solvent.
2. Incubate the cells for 48-72 hours at 37℃

.. note::
  Be careful when changing the media for 293T cells—they easily detach, especially in a 96-well plate.

Day 5-6
---------------

Analyze the cells via microscopy or flow cytometry.