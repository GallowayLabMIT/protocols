Culturing Human iPSCs
======================

Reagents
--------

**Media**

Human iPSCs can be cultured in a range of media. All media come as two components: the basal medium and a 5X or 10X supplement. 
The supplement is stored at -20°C; the basal medium is stored at 4°C.
To make the  complete medium, add an entire bottle of supplement to the bottle of basal medium.
The complete medium is stored at 4°C (entire bottle) or at -20ºC (40 mL aliquots). Media should be warmed before adding to cells; be sure to warm only an aliquot.

.. important:: 
   Do not warm the entire media bottle! Instead, aliquot what you will need and only warm that tube. As a bonus, this smaller volume will warm faster.

Media we use:

- `mTeSR-Plus <https://www.stemcell.com/products/mtesr-plus.html>`_: optimized for clump passaging, we mainly use with iPS11 cells
- `eTeSR <https://www.stemcell.com/products/etesr.html>`_: a variant of mTeSR optimized for single-cell passaging
- `StemFlex <https://www.thermofisher.com/order/catalog/product/A3349401>`_: good for single-cell passaging, used with STRAIGHT-IN cell lines

**Coating**

iPSCs are cultured on plates with specific coatings, either extracellular matrix typically derived from a cancer cell line or a defined, single polymer.
Often, a defined matrix is preferred to eliminate lot variability, but these reagents tend to be more expensive.
While it is relatively easy to adapt a cell line to a new medium, it takes longer (2 passages) to adapt to a new coating.

- `Geltrex <https://www.thermofisher.com/order/catalog/product/A1413301>`_: basement membrane derived from murine tumor cells; 50X stored at -20°C in 120 µL aliquots, enough each for one 6-well plate (see :ref:`Geltrex Aliquoting <_geltrex-aliquot>` for more information)
- `Laminin-521 <https://www.stemcell.com/products/celladhere-laminin-521.html>`_: a defined culture matrix consisting of a single protein that is expressed in human blastocysts; 20X aliquots are stored long-term at -20ºC, and a working aliquot is good at 4ºC for up to 3 months

See coating protocols below for :ref:`Geltrex <geltrex-coating>` and :ref:`laminin-521 <laminin-521-coating>`.

**Dissociation Reagents**

There are several dissociation reagents with different use cases.

- `ReLeSR <https://www.stemcell.com/products/relesr.html>`_: non-enzymatic dissociation of cells in clumps (clump passaging is preferred for regular maintenance to reduce genomic instability); stored at room temperature
- `Gentle Cell Dissociation Reagent <https://www.stemcell.com/products/gentle-cell-dissociation-reagent.html>`_ (GCDR): non-enzymatic dissociation to single cells; preferred over harsher, enzymatic treatments like Accutase; stored at room temperature
- `Accutase <https://www.sigmaaldrich.com/US/en/product/sigma/a6964>`_: enzymatic dissociation to single cells; stored long-term at -20ºC, and working aliquots are stored at 4ºC

See dissociation protocols below for :ref:`ReLeSR <relesr-dissociation>`, :ref:`GCDR <gcdr-dissociation>`, and :ref:`Accutase <accutase-dissociation>`.

**Survival-promoting small molecules**

When thawing iPSCs or passaging them as single cells, it is necessary to add inhibitor(s) to prevent apoptosis and promote cell survival. 
These compounds should be removed after 24 hours by performing a media change. 
It is common to observe significant changes in cell morphology with these inhibitors; the cells should return to their typical form a few days after removal.
There are several small-molecule formulations that work well:

- `ROCK inhibitor <https://www.stemcell.com/products/y-27632.html>`_ (ROCKi, RI): Y-27632, a single chemical inhibitor of ROCK (Rho-associated, coiled-coil containing protein kinase) activity; 1000X aliquots are stored at -20°C, and a working aliquot is kept at 4ºC
- `RevitaCell Supplement <https://www.thermofisher.com/order/catalog/product/A2644501>`_ (RC): a proprietary blend of a ROCK inhibitor and other antioxidant small molecules; 100X aliquots (*can also be used as a 200X solution*) are stored at -20°C, and a working aliquot is kept at 4ºC
- `CloneR2 <https://www.stemcell.com/products/cloner2.html>`_: a defined supplement to promote survival, genomic integrity, and differentiation potential in high-stress culturing conditions like clonal expansion; 10X solution is stored long-term at -20ºC, and working aliquots are stored at 4ºC

**Freezing solutions**

Like MEFs, iPSCs should be frozen in a solution of 10% DMSO and 90% serum or serum equivalent. 

- 10% DMSO + 90% FBS: use a 15 mL aliquot of FBS labeled "iPSC only"
- 10% DMSO + 90% `KnockOut Serum Replacement <https://www.thermofisher.com/order/catalog/product/10828028>`_: a more defined, FBS-free serum equivalent with less lot variability

See :ref:`freezing protocol <freeze-ipscs>` below.

**Other Reagents**

- DMEM/F12: for coating plates and spinning down cells, use bottle labeled "iPSC only"
- DMEM/F12 + 1% FBS: for spinning down cells; the added protein helps the cells pellet well
- PBS: normal phosphate buffered saline without calcium and magnesium (–/–) for washes; use autoclaved bottle labeled "iPSC only"
- `PBS +/+  <https://www.thermofisher.com/order/catalog/product/14040117>`_: phosphate buffered saline that includes calcium and magnesium ions; used for Laminin-521 coating; stored at 4ºC
- `Penicillin-streptomycin <https://www.fishersci.com/shop/products/gibco-penicillin-streptomycin-10-000-u-ml-3/15140122>`_ (Pen/Strep, P/S): optional antibiotic to reduce contamination; 100X stored at 4ºC


General Culturing Tips
----------------------

- Change to fresh media *every other day* to keep the cells healthy. iPSCs are very metabolically active and can easily spontaneously differentiate, so if the media looks very yellow try refreshing with a larger volume.
- If media cannot be changed in two days (e.g., over the weekend), use twice the normal media volume. This should keep the cells healthy for 3 days until the next media change (as long as they are not confluent).
- Some amount of cell death is expected, but regular media changes should keep this to a minimum.
- To maintain optimal cell health, be sure to passage cells before they are 100% confluent. Regular 1:10 passaging can usually be done every 3-4 days.
- iPSCs grow in colonies with a cobblestone-like cell morphology. The edges of the colonies should be smooth, not spiky. However, morphology will change with ROCKi/RevitaCell, but should return to normal 1-2 days after removal. Each cell line has its own normal morphology; be aware of any changes.
- Also look out for large spaces between cells or flat, more transparent cells growing away from a colony. These are signs of differentiation.
- Be extra attentive with sterile technique (e.g., don fresh gloves before beginning, use separate glass pipette aspirators for different cell lines) to avoid contamination.

====================================== ================ ======================
**Reagent / Step**                     iPS11             STRAIGHT-IN
====================================== ================ ======================
 Media                                 mTeSR-Plus        StemFlex + P/S
 Coating                               Geltrex           Laminin-521
 Dissociation for passaging/freezing   ReLeSR (clumps)   GCDR (single cells)
 Survival-promoting addition           ROCKi             RevitaCell
====================================== ================ ======================


.. _geltrex-coating:

Coating plates with Geltrex
---------------------------

.. important:: Plates require at least 1 hour to coat, so start early or make extras up to a week ahead of time!

Geltrex is stored in aliquots sufficient to coat an entire plate, and once thawed, it must be used immediately. If you do not need an entire plate coated, you can either
coat extra wells of a new plate and store that plate at 4ºC or coat your entire plate and use the extra wells later (e.g., for the next passage). 
Wells with Geltrex + additional DMEM/F12 should still be good as long as the liquid has not evaporated too much and exposed the surface.

1. Thaw Geltrex at 4ºC, on ice (use the designated TC styrofoam for ice), or quickly at room temperature.

   - Thaw one tube (50X, 120 µL aliquot) per 6-well plate to coat. It is recommended to do no more than 2 at a time to avoid unintentional gelling.
   - Flick the tube to mix as it thaws and to speed up the process.
   - While the Geltrex is thawing, prepare other materials in the BSC: 6-well plate(s), 15mL conical, DMEM/F12.

2. Prepare a 15 mL conical with 6 mL DMEM/F12. Immediately once the Geltrex has thawed, pipet it into the prepared 15 mL conical. Pipet 1 mL of the DMEM/F12 mix back into the Geltrex tube to wash out any residual solution and return the liquid to the conical.
3. With a serological pipette, pipet up and down once, then dispense 1 mL per well into the 6-well plate. Rock the plate to coat the entire surface.
4. Incubate the plate at 37ºC for 1 hour to coat.

   - *If using same-day*: Leave the plate in the incubator until use.
   - *If preparing ahead*: Add an additional 1-2x volume of DMEM/F12 to each well. Parafilm the plate, then store at 4ºC (Oaken). Plates can be stored at 4ºC for several weeks.

.. note::
   The official recommendation is to store coated plates at 4ºC for up to 2 weeks. As long as the liquid has not evaporated/condensed, the plates should be okay for several weeks longer.

5. To use the plates, ensure they have been pre-warmed in the incubator. Immediately before seeding cells, aspirate the liquid from the coated well(s).


.. _laminin-521-coating:

Coating plates with Laminin-521
-------------------------------

Materials

- `CellAdhere Laminin-521  <https://www.stemcell.com/celladhere-laminin-521.html>`_ (20X; aliquots stored at -20ºC, working aliquot at 4ºC is good for 3 months)
- `PBS +/+  <https://www.thermofisher.com/order/catalog/product/14040117>`_ (stored at 4ºC)

.. important::
	PBS +/+ is critical as divalent cations (Mg2+, Ca2+) are important for structure and function of laminin-521. Do not use normal, autoclaved PBS!

Protocol

1. If using a new aliquot from -20ºC, thaw laminin-521 at 4°C or on ice.
2. Dilute laminin-521 in sterile PBS +/+ to a final concentration of 5 µg/mL (dilute 1:20). See the table below for helpful volumes. If coating only 1-2 wells, the dilution can be done directly in the well; for larger volumes, using a tube is helpful.
3. Incubate plates for ~2 hours at 37°C.
4. If not using immediately, parafilm the plate and store at 4ºC for up to 4 weeks.
5. Immediately before seeding cells, aspirate the liquid from the coated well(s) *using a P1000 pipette* (not the aspirator) to avoid dislodging the laminin-521.


===================   =========================================   ===========================   ===========================   ======================
 **Culture plate**     **Surface area per well (cm\ :sup:`2`)**   **Total volume (µL/well)**     **Laminin-521 (µL/well)**     **PBS +/+ (µL/well)**
===================   =========================================   ===========================   ===========================   ======================
6-well                 9.4                                          1,000                          50                           950  
12-well                3.8                                          500                            25                           475  
24-well                1.9                                          300                            15                           285     
48-well                0.76                                         150                            7.5                          142.5     
96-well                0.32                                         70                             3.5                          66.5     
===================   =========================================   ===========================   ===========================   ======================


Thawing
---------

.. time:: ~30 minutes — don't forget to coat plates ahead of time!

Typically, cells dissociated in clumps are frozen such that 1 vial contains 1 well of a 6-well plate. Recovery is variable and depends on clump size, so 1 vial can be thawed into 1-6 wells of a 6-well plate. 
Decide how many wells to use based on the size of the pellet. ROCKi can be added to improve recovery, but it is not strictly necessary.

For cells dissociated as single cells, 1 vial usually contains 1 well of a 12-well or 24-well plate (this should be labeled on the vial). Recovery is quite high with ROCKi or RevitaCell, so it is recommended to thaw the vial into multiple wells.
For instance, a vial containing 1 well from a 24-well plate could be thawed into two new wells of a 24-well plate, split 1/3 and 2/3 into each well. This helps ensure one of the wells will be ready to passage in 2-4 days (optimal).

1. Coat a plate with the appropriate coating. If using a pre-coated plate from the fridge, allow to warm in the incubator.
2. Warm the appropriate volume of media (e.g., 2 mL/well for a 6-well plate) and, if using, DMEM + 1% FBS (5 mL per vial thawed).
3. Remove cryovial(s) of cells from liquid nitrogen and thaw quickly (1-2 minutes) in the 37°C bead bath.

   .. important:: Thaw cells quickly and spin down as soon as all the ice is gone to limit the cells' exposure to DMSO.

4. As soon as cryovial is thawed, transfer the contents to a 15 mL conical using 5 mL serological pipette.
5. Using a P1000 pipette, **SLOWLY** add 1 mL of DMEM/F12 (or warm DMEM/F12 + 1% FBS) to the conical dropwise, shaking the tube every 2-3 drops to evenly mix thawed cells with DMEM/F12. *Optionally*, pipet 1 mL of DMEM/F12 into the cryovial to remove any residual cells, then add dropwise to conical.

   .. important:: Slow addition of DMEM/F12 is important to prevent osmotic shock to the iPSCs.

6. Using a serological pipette, **GENTLY** add 4 more mL of DMEM/F12 (or warm DMEM/F12 + 1% FBS) dropwise, mixing every 3-5 drops (total tube volume ~6 mL).
7. Spin down cells at 40g (for clumps) or 400g (for single cells) for 4 minutes.
   
   .. note:: If clumps of cells do not pellet well at 40g, you can try 400g, but cells frozen in these smaller clumps may not recover as well without ROCKi.

8. Aspirate the plate coating and the supernatant from the cell pellet. *Gently* resuspend the cells in the warm culture medium with ROCKi/RevitaCell (if using) and plate. 
9. Within 24 hours (i.e., the next day), change to fresh media to remove dead cells and ROCKi/RevitaCell. Then, continue culturing as normal.


.. _relesr-dissociation:

Passaging with ReLeSR
---------------------

.. time:: ~15 minutes — don't forget to coat plates ahead of time!

To passage iPS11 cells for general culture maintenance, use ReLeSR to dissociate cells in clumps. This is less disruptive and may improve the long-term genomic integrity of the iPSCs.
For seeding or other applications that require counting, dissociate with Gentle Cell Dissociation Reagent (preferred) or Accutase to achieve a single-cell suspension 
(see :ref:`gcdr-dissociation` and :ref:`accutase-dissociation` below).

1. Warm media in the 37ºC bead bath.
2. Aspirate the old media. Gently wash with 1 mL PBS and aspirate.
3. Add 1 mL ReLeSR and incubate at room temperature for 1 minute.
4. Immediately after the 1 minute is up, aspirate to remove the ReLeSR. At this point, *no cells should be lifting off from the plate*.
5. Incubate the empty plate (it essentially has a thin film of liquid) at 37°C for 5-7 minutes.
6. When the plate is done incubating, add 1-3 mL media to each well and tap the plate *for 30-60 seconds* to dislodge the cells.

   - Suggestion: Add 0.5-1 mL of media for each new well you're passaging into, e.g., 3 mL media for passaging one well 1:6.

7. Gently pipet up the liquid with a serological and dispense into the prepared wells (with coating aspirated).

   - Use a serological pipette rather than a P1000 to maintain cell clumps.
   - Pipet up and down 1-2 times in the well to resuspend as many cells as possible, since the cells tend to stick to the well. However, don't pipet too much—this will break up the clumps!

8. Add additional media to each well to bring the total volume to the desired amount (e.g., 2 mL). Rock back and forth to mix.

   - Alternatively, dissociated cells from the previous step can be pipetted into a conical to be mixed with fresh media, then transferred from the conical to the new wells.
   - It can also be helpful wash the old well with this additional media before adding to the new well.
   - After dissociation, avoid excessive pipetting to maintain cell clumps.

   .. tip:: 
      Look at the cell clumps under the microscope before putting the plate in the incubator. 
      This can help give you a sense of the clump size to aim for in the future based on how the cells look the next day.

9. Within 24 hours (i.e., the next day), change to fresh media. Then, culture as normal.


.. _gcdr-dissociation:

Dissociating with Gentle Cell Dissociation Reagent (GCDR)
---------------------------------------------------------

.. time:: ~15 minutes — don't forget to coat plates ahead of time!

To seed cells for an experiment, use Gentle Cell Dissociation Reagent (GCDR) to dissociate single cells for counting. 
GCDR is also used for regular passaging of STRAIGHT-IN lines. 
GCDR is preferred over Accutase because it is non-enzymatic and gentler on the cells.
During seeding, be sure to add a survival-promoting small molecule (ROCKi or RevitaCell).

.. note::
    Addition of ROCKi/RevitaCell leads to cytoskeletal remodeling, so cells will have a spiky morphology the day after passaging.
    The morphology should return to normal a day or so after ROCKi/RevitaCell is removed.

1. Warm media and DMEM/F12 + 1% FBS (if using) in the 37ºC bead bath.
2. Aspirate old media. Gently wash with 1 mL PBS and aspirate.
3. Add a 0.5-1x well-volume (e.g., 1 mL in a 6-well plate, 100 uL for a 96-well plate) of GCDR and incubate at 37°C for 8-10 minutes until cells ball up on the plate. 

   .. note:: Cells are ready to detach when they have balled up/become round, retreating from their neighbors. You will likely NOT observe cells lifting off.

4. Gently pipet up and down to dislodge cells. Add the dissociated cells to a 15 mL conical, optionally with warm DMEM/F12 + 1% FBS,
   and spin at 400g.
   
   - Technically, no quenching/diluting step is needed; cells can be spun down in GCDR alone. However, the proteins in DMEM/F12 + 1% FBS can help the cells pellet. 
  
5. Aspirate the media and gently resuspend the cells in a small volume of media with ROCKi/RevitaCell (e.g., 0.5 mL).
6. If seeding cells for an experiment, count cells :ref:`as normal <counting>`.

   .. note:: 
      Counting iPSCs can be difficult! GCDR doesn't always produce perfect single cells; often, clusters of a few cells will remain. 
      Do your best to count accurately.

7. Dilute the cells to the appropriate volume in media with ROCKi/RevitaCell. Aspirate the coating solution and plate cells.
8. Within 24 hours (i.e., the next day), change to fresh media without ROCKi/RevitaCell. Then, proceed with culturing or an experiment as normal.


.. _accutase-dissociation:

Dissociating with Accutase
--------------------------

.. time:: ~15 minutes — don't forget to coat plates ahead of time!

Accutase can be used to dissociate iPSCs to single cells for seeding. However, Gentle Cell Dissociation Reagent (GCDR) is preferred, since
Accutase (enzymatic) is harsher on the cells than GCDR (non-enzymatic).

.. note::
    Addition of ROCKi/RevitaCell leads to cytoskeletal remodeling, so cells will have a spiky morphology the day after passaging.
    The morphology should return to normal a day or so after ROCKi/RevitaCell is removed.

1. Warm media and DMEM/F12 + 1% FBS (if using) in the 37ºC bead bath.
2. Aspirate old media. Gently wash with 1 mL PBS and aspirate.
3. Add a 0.5-1x well-volume (e.g., 1 mL in a 6-well plate, 100 uL for a 96-well plate) of Accutase and incubate at 37°C for 5-7 minutes until cells begin to lift off the plate. 
4. Gently pipet up and down to dislodge cells. Add the dissociated cells to a 15 mL conical with DMEM/F12 or warm DMEM/F12 + 1% FBS,
   and spin at 400g.
   
   - Accutase must be quenched/diluted before spinning, as it contains enzymes. The proteins in DMEM/F12 + 1% FBS can help the cells pellet. 
  
5. Aspirate the media and gently resuspend the cells in a small volume of media with ROCKi/RevitaCell (e.g., 0.5 mL).
6. If seeding cells for an experiment, count cells :ref:`as normal <counting>`.

   .. note:: 
      Counting iPSCs after dissociation with Accutase may be easier than for GCDR, as it can better break apart clumps/clusters.

7. Dilute the cells to the appropriate volume in media with ROCKi/RevitaCell. Aspirate the coating solution and plate cells.
8. Within 24 hours (i.e., the next day), change to fresh media without ROCKi/RevitaCell. Then, proceed with culturing or an experiment as normal.


.. _freeze-ipscs:

Freezing
---------

Appropriate volumes of freezing soluation (10% DMSO + 90% FBS or KOSR):

- 24-well plate: 300-500 µL per well
- 12-well plate: 500 µL per well
- 6-well plate: 0.5-1 mL per well

.. important::
   Be sure to label the cryovials well! It is best practice to include the media and coating, since we have the same lines adapted to different conditions.
   It is also a good idea to indicate whether the cells are frozen in clumps (ReLeSR) or as single cells (GCDR), in addition to the well size.

1. Dissociate cells :ref:`in clumps (ReLeSR) <relesr-dissociation>` or :ref:`as single cells (GCDR) <gcdr-dissociation>` as described above, stopping before resuspending in media.
2. Instead, resuspend in an appropriate volume of FBS or KOSR (e.g., 270 µL/well for 24-well or 900 µL/well for 6-well plate) and transfer to a cryovial.

   - For cells dissociated with ReLeSR, add FBS or KOSR after incubating the cells with a thin film of ReLeSR for 8-10 minutes. 
     Tap the plate vigorously *for 30-60 seconds* to dislodge the cells. Gently transfer the cells to a cryovial using a serological pipette to avoid disturbing the clumps.
   - For cells dissociated with GCDR, after spinning down the cells, resuspend the pellet in FBS or KOSR.

3. Add the appropriate volume of DMSO to the cryovial to achieve a final concentration of 10% DMSO (e.g., 30 µL/well for 24-well or 100 µL/well for 6-well plate).
4. Place the cryovials in the styrofoam boxes in the -80°C freezer to cool slowly overnight.
5. The following day, transfer frozen cryovials to liquid nitrogen for long-term storage.
