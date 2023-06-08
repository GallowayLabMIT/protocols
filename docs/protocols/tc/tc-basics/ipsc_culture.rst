Culturing Human iPSCs
======================

Reagents
--------

**Media**

Human iPSCs can be cultured in a range of media; in this lab, we mainly use `mTeSR-Plus <https://www.stemcell.com/products/mtesr-plus.html#section-protocols-and-documentation>`_.
The medium has two components: the basal medium and the 5X supplement. The supplement is stored at -20°C in 10mL aliquots in 50mL concials; the basal medium is stored at 4°C.
To make the  complete medium, add 40mL basal medium to the 10mL supplement aliquot; alternatively, add the entire 100mL supplement to the entire 400mL basal medium.
The complete medium is stored at 4°C; long-term stability at this temperature has not been tested, so aliquotting is preferred.

Some protocols recommend warming media to room temperature before use, but this does not seem to be necessary.

**Dissociation Reagents**

There are two main dissociation reagents we use:

1. `ReLeSR <https://www.stemcell.com/products/relesr.html>`_: non-enzymatic dissociation of cells in clumps; better for regular passaging so as not to disturb the cells too much
2. `Accutase <https://www.sigmaaldrich.com/US/en/product/sigma/a6964>`_: enzymatic dissociation to single cells; necessary for counting and seeding

**Other Reagents**

- `GelTrex <https://www.thermofisher.com/order/catalog/product/A1413301>`_: basement membrane for coating plates; 50X stored at -20°C in 120 µL aliquots, enough each for one 6-well plate
- `ROCK inhibitor <https://www.caymanchem.com/product/10005583>`_: Y-27632, a chemical inhibitor of ROCK activity used to prevent differentiation upon thawing and passaging; 1000X stored at -20°C
- DMEM/F12 for coating plates and spinning down cells
- PBS

GelTrex coating plates
----------------------

.. important:: Plates require at least 1 hour to coat, so start early or make extras up to a week ahead of time!

1. Thaw GelTrex on ice (use the designated TC styrofoam for ice).


   - Thaw one tube (50X, 120 µL aliquot) per 6-well plate to coat. It is recommended to only do ~2 at a time to avoid unintentional gelling.
   - Flick the tube to mix as it thaws and to speed up the process.
   - While the GelTrex is thawing, prepare other materials in the BSC: 6-well plate(s), 15mL conical, DMEM/F12

2. Prepare at 15 mL conical with 6 mL DMEM/F12. Immediately once the GelTrex has thawed, pipet it into the prepared 15 mL conical. Pipet 1 mL of the DMEM/F12 mix back into the GelTrex tube to wash out any residual solution and return the liquid to the conical.
3. With a serological pipette, pipet up and down once, then dispense 1 mL per well into the 6-well plate. Rock the plate to coat the entire surface.
4. Let the plate sit to coat:

   - *If using same-day*: leave the plate at 37°C for at least 1 hour
   - *If preparing ahead*: parafilm the plate, then leave it at room temperature overnight. Plates can be stored at room temperature for at least a week.

5. Immediately before seeding cells, aspirate the liquid from the coated well(s). Leave the liquid on any unused wells; these can be aspirated and used at a later date.

Thawing
---------

.. time:: ~30 min

1. Remove cryovial(s) of cells from liquid nitrogen and thaw quickly in the 37°C bead bath.

.. important:: Thaw cells quickly and spin down as soon as all ice is gone to limit the cells' exposure to DMSO.

2. Pipet the contents of the cryovial into a 15 mL conical with 10 mL of DMEM/F12. Optionally, pipet 1 mL of liquid from the conical around in the cryovial to remove any residual cells, then return the liquid to the conical.
3. Spin down cells at Xg (*speed TBD, 400g seems fine but ~210g has also been recommended*) for 4 min.
4. Aspirate the media and *gently* resuspend in 10 mL fresh DMEM/F12 to wash the cells again (iPSCs are sensitive to trace DMSO and may differentiate otherwise).
5. Spin down the cells and then aspirate the media. Aspirate the coating liquid from the wells to plate onto.
6. *Gently* resuspend the cells in the culture medium (i.e., mTeSR) with ROCK inhibitor (1000X stock) and plate. Typically, iPSCs are frozen such that 1 vial goes to 1 well of a 6-well plate.
7. Within 24 hours (e.g., the next day), media change to fresh mTeSR to remove the ROCK inhibitor. Then, culture as normal.

.. note::
    Addition of ROCK inhibitor leads to cytoskeletal remodeling, so cells will have a spiky morphology the day after thawing.
    Let the cells recover for at least a day without ROCK inhibitor (i.e., 2+ days post-thaw) before passaging.

General Culturing Tips
----------------------

- Always culture human iPSCs on GelTrex-coated plates (or other similar matric coating).
- Typically, all culturing is done in 6-well plates. Use at least 2 mL of media per well.
- Change to fresh media *every day* to keep the cells healthy. iPSCs are very metabolically active and can easily spontaneously differentiate, so if the media looks very yellow try refreshing with a larger volume (e.g., 3 mL).
- Some amount of cell death is expected, but media changes every 24 hrs with enough fresh media should mitigate this.
- To maintain optimal cell health, be sure to passage cells before they are 100% confluent. Typically, healthy cells that are passaged 1:6 will need to be passaged again 2 days later.
- Splits of 1:6 to 1:12 are recommended. Larger dilutions may impede growth if the cells are too sparse, and lower dilutions will require very frequent passaging.
- iPSCs grow in colonies with a cobblestone-like cell morphology. The edges of the colonies should be smooth, not spiky. However, ROCK inhibitor remodels the cytoskeleton, so changes to spiky morphology are expected the day after thawing and passaging.
- Be extra attentive with sterile technique (i.e., don fresh gloves before beginning, use separate glass pipet aspirators for different cell lines) to avoid contamination.

Passaging with ReLeSR
---------------------

.. time:: ~15 min — don't forget to coat plates at least 1 hr ahead of time!

To passage for general cell culture maintenance, use ReLeSR to dissociate cells in clumps. This is less disruptive and may improve the long-term integrity of the iPSCs.
For seeding or other applications that require counting, dissociate with Accutase to achieve a single-cell suspension (see :ref:`accutase-dissociation` below).

1. Aspirate the old media. Gently wash with 1 mL PBS and aspirate.
2. Add 1 mL ReLeSR and incubate at 37°C for 1 min.
3. Immediately after the 1 min is up, aspirate to remove the ReLeSR. At this point, *no cells should be lifting off from the plate*.
4. Incubate the empty plate (it essentially has a thin film of liquid) at 37°C for 5 min.
5. Optional: while the plate is incubating, prepare fresh media with ROCK inhibitor (i.e., mTeSR complete medium + 1000X ROCK inhibitor). It is up to you to decide how/when to mix in the ROCK inhibitor, but it is convenient to prepare the media in a new conical.
6. When the plate is done incubating, add 1-3 mL media to each well and tap the plate to dislodge the cells.

   - It is convenient to add 0.5 mL of media for each new well you're passaging into, e.g., 3 mL media for passaging one well 1:6.

7. Gently pipet up the liquid with a serological and dispense into the prepared wells.

   - Use a serological pipette rather than a P1000 to maintain cell clumps.
   - Pipet up and down 1-2 times in the well to resuspend as many cells as possible, since the cells tend to stick to the well. However, don't pipet too much—this will break up the clumps!

8. Add additional media to each well to bring the total volume to the desired amount (e.g., 2 mL). Pipetting up and down here is not necessary; rocking back and forth achieves sufficient mixing.

   - Alternatively, dissociated cells from the previous step can be pipetted into a conical to be mixed with fresh media, then transferred from the conical to the new wells.
   - After dissociation, avoid excessive pipetting to maintain cell clumps.

9. Within 24 hours (e.g., the next day), media change to fresh mTeSR to remove the ROCK inhibitor. Then, culture as normal.

.. note::
    Addition of ROCK inhibitor leads to cytoskeletal remodeling, so cells will have a spiky morphology the day after passaging.
    The morphology should return to normal a day or so after the ROCK inhibitor is removed.

.. _accutase-dissociation:

Dissociating with Accutase
--------------------------

.. todo::

Freezing
---------

1. Passage cells with ReLeSR through step 4 - incubate empty plate at 37 °C for 5 min.
2. Add 0.9 mL of media to each well, tap to dislodge cells.
3. Gently pipet up the liquid with a serological and dispense into a labeled cryovial. 1 well of a 6-well plate per cryovial.  
   - Alternatively, dissociated cells from multiple wells can be pooled into a conical tube before aliquoting for freezing. 
   - After dissociation, avoid excessive pipetting to maintain cell clumps.
4. Add 100 uL of DMSO to cryovial to achieve a final concentration of 10% DMSO. 
   - If multiple wells were pooled in the previous step, add 100 uL of DMSO per well pooled, and then aliquot 1 mL of final mixture into labeled cryovials. 
5. Transfer tubes to styrofoam boxes in -80 °C freezer for overnight freezing. 
6. The following day, transfer frozen tubes to liquid nitrogen for longe term storage. 