==============
SNAP circuit
==============

This protocol describes the induction of the SNAP circuit in transient transfection in a 96-well plate.

Materials
=========

- Cells
- Plates
- DMEM supplemented with 10% FBS
- PEI
- **Small molecule inducers:**
  
   - Guanine (:ref:`25 mM stock <guanine_stock>`)
   - O6-benzylguanine (:ref:`50 mM stock <O6-BG_stock>`)
   - Solvent controls (e.g., 0.2N NaOH for guanine or DMSO for O6-benzylguanine)
  
- **Input plasmid:** plasmid expressing SNAPtag conjugated with target protein (e.g., pHAGE-SNAP-tagBFP)
- **Output plasmid:** plasmid expressing reporter gene-ribozyme switch cassette (e.g., pHAGE-UBC-mGreenLantern-p2g6)


Protocol
=========

Day 1: Seed cells
-----------------------------------

1. Seed the cells at a density of 2.5-4e4 cells/well in a gelatin-coated 96-well plate.
2. Incubate the cells at 37ºC overnight.

Day 2: Transfection
-------------------

1. Transfect 100 μg each of the input and output plasmids per well with PEI by following the 
   :doc:`general transfection protocol <./tc-basics/transient_transfection>`. To avoid cell death due to toxicity of 
   the small-molecule inducers, reduce cell stress from transfection by using a lower PEI:DNA ratio of 3:1.
2. Incubate the cells at 37ºC overnight.

Day 3: Small molecule treatment
-------------------------------

1. Dilute the small molecule inducers to the appropriate concentrations in the appropriate culture medium. 
   
   - For both O6-benzylguanine and guanine, no greater than 100 µM should be used to minimize cytotoxicity.
   - Include conditions containing only the inducer solvent as a control (e.g., the same percent volume of DMSO only as 
     in the O6-benzylguanine condition).

2. Remove the media from the wells, being careful not to detach the cells.
3. Add 100 μL/well of the inducer-containing media to the cells.
4. Incubate the cells for 48-72 hours at 37ºC.

.. note::
  Be careful when changing the media for HEK293T cells---they easily detach, especially in a 96-well plate.

Day 5-6: Analysis
-----------------

Analyze the cells via microscopy or :doc:`flow cytometry <./tc-basics/flow_cytometry>`.