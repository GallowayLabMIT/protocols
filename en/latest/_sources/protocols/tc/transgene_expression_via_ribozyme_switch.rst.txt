============================================================================
Transgene expression control through ribozyme switch (96-well plate version)
============================================================================

Materials
---------

- Cells
- Plates
- DMEM supplemented with 10% FBS
- KO DMEM
- PEI
- DNA containing the transgene-ribozyme switch cassette

    - Our lab most commonly uses two ribozyme switches: (1) the p2G6 ribozyme which is an ON-switch inducible with Guanine and (2) the Theo.CAUAA which is an ON-switch inducible with Theophylline.

- DNA with ribozyme controls (*Optional: These controls are useful comparisons for the dynamic range of inducible ribozyme switches*)
  
    - sTRSV ribozyme is the "maximum cleaving" control. This would be the lowest expression level you could expect with a Rz.
    - sTRSVctl ribozyme is the "minimum cleaving" control. This would be the highest expression level you could expect with a Rz.

- Small-molecule inducer such as theophylline or guanine (check the concentration that you will need)
- Vehicle for small molecule as a control (e.g. DMSO, NaOH)

.. note:: 
  :doc:`Aliquots are 25mM in NaOH <../../recipes/tc/small_mol_stocks>`, and a final concentration of 100uM has been used by BAD/JCA.

  Theophylline is used for the Theo.CAUAA ribozyme switch. Aliquots are 25mM in water, and a final concentration of 300uM is used by BAD/JCA.

  To make Theophylline Stock:

    1. Dissolve 4.50 mg Theophylline / 1 mL Elga Water. You may need to vortex and/or slightly warm the solution.
    2. Filter sterilize with 0.22 uM filter before use.
    3. Make sure the Theophylline is fully dissolved before use. It tends to crystallize out of solution when kept in the fridge.



Procedure
=========

Day 1: Seed cells
-----------------------------------

1. Seed the cells at a density of 25-40k cells/well in a 96-well plate.
2. Incubate the cells at 37°C overnight.

Day 2: Transfection
-------------------

1. Transfect 100μg of a plasmid expressing transgene-ribozyme switch cassette per well with PEI by following the :doc:`general transfection protocol <./tc-basics/transient_transfection>`. If your small molecule or the solvent has cytotoxicity, using a lower PEI:DNA ratio of 3:1 is recommended.
2. Incubate the cells at 37°C for 4-6 hours.
3. Remove the media from the wells carefully to not lose the cells, and add 100μl of fresh media that contains the small-molecule inducer.
4. Incubate the cells overnight.

.. note::
  If you are using ON-switch, where the ribozyme activity is inactivated by the small molecule (stabilizing the transcript), you don't need to treat the cells with the small molecules at 4-6 hours post transfection, you can do this next day.

  If you are using OFF-switch, where the ribozyme activity is activated by small the molecule (destabilizing the transcript), you MUST do the small-molecule treatment at 4-6 hours post transfection so that transcribed mRNA binds with the molecule before being translated to protein.

.. note::
  Be careful when changing the media for 293T cells—they easily detach, especially in a 96-well plate.

Day 3 or 4
---------------

- After 24 hours post small-molecule treatment, you should be ready for analysis via microscopy or flow cytometry.
- A 24-hour incubation with the small molecule should be generally enough to measure the output transgene expression, but longer incubations of 48 or 72 hours may improve detection.
