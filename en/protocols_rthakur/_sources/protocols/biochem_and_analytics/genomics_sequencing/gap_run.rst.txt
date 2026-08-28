=============
GapRUN
=============

This protocol is based on the work of [Longo2024]_ and [Koidl2021]_.

Measure MNase activity
======================

A key variable in any genomics assay with MNase is the ratio of MNase to cells required to properly digest the DNA. 
Before using the nanobody-MNase protein (fusion of an anti-GFP nanobody to MNase, produced in-house according to :doc:`this protocol </protocols/protein_production/gaprun_protein_production>`) 
in the GapRUN assay, benchmark its activity against commercial MNase.
This only needs to be performed once per batch of protein, but should be performed for each cell type (iPS11, Leiden iPSCs, induced neurons, etc.).
It is not necessary to perform a titration per genetic edit.

You will need two 5-million (5M) cell aliquots to perform the titration, one aliquot each for the nanobody-MNase and the commercial MNase.
The cells can be fixed and snap-frozen any time prior to the titration. 

Preparing fixed, snap-frozen cell aliquots
------------------------------------------

1. Grow up at least 10M cells using normal culturing conditions. On the day of harvest, proceed accordingly.
2. Prepare sufficent 100x BSA (200 µg / mL) to aid to help cells pellet and limit cell losses. Cool a centrifuge to 4°C and place sufficient PBS on ice.
3. Collect cells following normal passaging conditions. Collect into and wash in the same 50 mL tube. After collecting and spinning down the cells,
   perform a PBS wash before resuspending and counting cells. Spike in 100x BSA prior to spinning down the cells in the PBS wash.
4. Count the cells. We want as high cell counts as possible; it is good to crosslink and fix as many
   cells as possible instead of throwing away cells at this step.

   .. warning::

        Collect all of the following wash steps as formaldehyde waste until step the cells are resuspended prior to aliquoting.

5. In a fumehood, add 1 mL of fresh 16% formaldehyde per 15 mL of cells (15M cells), in a dropwise but relatively rapid manner.
   Use the 10mL and 1mL ampules either opened fresh or opened and stored in the last ~48 hours.
6. Incubate for 10 minutes at room temperature on the plate shaker.
7. Add pH 7.5 Tris dropwise to a final concentration of 0.375M. This is 3.45 mL of 2M Tris per 15M cells.
8. Incubate for 5 minutes at room temperature. Spike in 100x BSA prior to spinning at 400 xg at 4°C for 5 minutes.
9. Remove the supernatant, wash with cold PBS at a concentration of 1M cells / mL. Spike in 100x BSA prior to spinning at 400 xg at 4°C for 5 minutes.
10. Resuspend the cell pellet to 20M cells / mL, in cold PBS with spiked-in 100x BSA. Make the desired aliquots of these cells.
    For the MNase titration, you will need at least one aliquot of 5M cells. If processing the rest of the cells, in the same reaction,
    you can freeze down a "large" aliquot.

   .. note:: For smaller aliquots, make sure you use **low-binding** 1.7 mL tubes instead of normal 1.7 mL tubes.

11. Spin down aliquots, aspirate the supernatant and snap-freeze the cell pellets in liquid nitrogen. Store at -80°C.
    For consistency, snap-freeze and store the main samples even if you are proceeding on the same day.
    There is no benefit to having "fresh" un-snap-frozen cells.

    .. note::
        
        To snap-freeze, using the LN2 PPE, fill the small dewar with LN2. Then, pour some LN2 into a styrofoam
        container. Place the tubes to be snap-frozen in the foam holders we use for water baths, then float
        them in the LN2.

        Use tongs / some similar tool and the LN2 gloves to remove the samples. 

MNase titration
---------------

.. time:: 2 hours to pause point (reverse crosslinking)

.. note::

    At this point, the cell pellets are fixed. All waste from the titration can be collected and sink-disposed.

    Use low-binding 1.7 mL tubes for all steps requiring this tube size.

1. Prepare MB1 following the instructions in the :ref:`RCMC protocol <rcmc_specific_buffers>`.
2.  Prepare fresh Complete MB1 and place on ice. For the standard 5M cell titration, you need 1.5 mL of this buffer per 5M cells,
    but this can be scaled up or down.
    
    **Complete MB1 (2 mL)**:
    
    ======================  ========
    Component               Volume
    ======================  ========
    MB1                     1940 µL
    10% NP-40 alternative   40 µL
    100x PIC (in MB1)       20 µL
    ======================  ========

3. Thaw two 5M cell pellet on ice and resuspend in 500 µL of Complete MB1 (1M cells per 100 µL).
4. Incubate for 20 minutes on ice. While waiting, unfreeze a fresh MNase aliquot on ice to compare to.

   .. note::
       You can technically reuse MNase aliquots 2-3 times, but MNase is cheap compared to redoing an experiment 
       because the aliquot you used went bad.

       You will need roughly 0.5 µL of MNase per million cells, so unfreeze accordingly.

5. Centrifuge at 1750 xg for 5 minutes at 4°C. 
6. Remove the supernatant, leaving ~10-20 µL in the tube.
7. Wash the nuclei pellet with 500 µL of Complete MB1. Centrifuge at 1750 xg for 5 minutes at 4°C.
8. Removing as much supernatant as possible, resuspend the cell pellet in 500 µL of Complete MB1 (1M cells per 100 µL).
9. Split the cells into 5 low-binding 1.7 mL tubes, with 100 µL of cells each, keeping them on ice.
10. Decide on your titration series. A common series is 2U, 4U, 7U, 12U, and 20U for the commercial enzyme and 5U, 10U, 15U, 20U, 40U (assuming 20U/µL)
    for our in-house enzyme.
11. Add MNase to each 1M cell aliquot. Briefly vortex the tubes to ensure uniform MNase distribution,
    then incubate at 20 min at 37°C with shaking at 1000 rpm.
12. Transfer the digested nuclei to ice and add 0.8 µL of 500 mM EGTA. to reach a final concentration of 4 mM EGTA.
13. Briefly vortex the tube, then incubate for 10 minutes at 65°C with no shaking (but using the Thermomixer).
14. While waiting on the inactivation, prepare 0.9 mL of Reverse Crosslinking Solution **at room temperature and outside of the genomics hood**
    because of the RNase A. The SDS will precipitate out if you put it on ice.

    **Reverse Crosslinking Solution (1.8 mL)**

    ======================= =======
    Component               Volume
    ======================= =======
    1x TE                   1440 µL
    10% SDS                 180 µL
    5M NaCl                 72 µL
    20 mg/mL Proteinase K   90 µL
    10 mg/mL RNaseA         18 µL
    ======================= =======

15. Centrifuge at 1750 xg for 5 minutes at 4°C.
16. Discard the supernatant and resuspend each pellet in 150 µL of Reverse Crosslinking Solution.
17. Reverse cross-links for a minimum of 2 hours to overnight at 65°C with 1000 rpm shaking. This step does not 
    noticeably improve after 2 hours, you just have the option to stop.
18. Clean up the resulting DNA fragments using the genomics-only Monarch DNA cleanup kit. Use a 5:1 ratio of binding buffer : sample. Elute in 25 µL.
19. Quantify the DNA via Nanodrop. Load 1-5 µg of sample per thin-comb well using Orange Loading Dye onto a 1.5% agorase gel. Run at 100V for 30 minutes, then image.
20. Compare the digestion bands to estimate the activity on the nanobody-MNase, in the same units as the commercial MNase.
    Expect that the in-house nanobody-MNase has at least 5x worse activity.

|

GapRUN
=======

Stock buffer preparation
------------------------
1. Prepare and check that there is sufficient amounts of the following :doc:`shared genomics buffers </recipes/biochem_and_analytics/shared_genomics_buffers>`:
  
  - 1M HEPES, pH 7.5
  - 5M NaCl
  - 2.5M CaCl2
  - 0.5M EDTA, pH 8.0

2. Prepare 500 uL of **500 mM spermidine**, aliquoted and stored at -20C

   ===========================    ================ ========  ====================
   Component                        Concentration    g / L     Amount / 500 uL
   ===========================    ================ ========  ====================
   Spermidine trihydrochloride        500 mM        254.6       63.7 mg
   Elga water                       to 500 uL
   ===========================    ================ ========  ====================

3. Prepare 500 uL of **500 mM EGTA stock solution**

   =======================    ==================== ========  ==========================
   Component                   Concentration          g / L     Amount / 10 mL
   =======================    ==================== ========  ==========================
   EGTA                           500 mM           389.36        0.0973 g
   Elga water                  to 0.5 mL                       
   =======================    ==================== ========  ==========================


Two days before Day 1 (Day -1)
------------------------------
Infect cells (or otherwise turn on expression) of the GapR-EGFP fusion protein two days before collection.

Day 0 (N days before)
---------------------
Check the Concanavalin A (ConA) beads for aggregation. To do so, after pipetting
to resuspend the beads, dilute 1 uL of beads with 9 uL of 0.1x TE (or water).
You should not see large clumps of beads with the hemocytometer. This is your last
chance to order more ConA beads!

Day 1
-----
.. time:: 3 hours

1. Prepare the following buffers fresh:

   - 5 mL of **Wash Buffer** (enough for 12 samples, e.g. ~400 uL per sample, excess already included):

     =======================    ==================== ==========================
     Component                   Concentration        Amount / 5 mL
     =======================    ==================== ==========================
     1M HEPES-NaOH                    20 mM                100 uL 
     5M NaCl                          150 mM               150 uL
     500 mM spermidine                0.5 mM                 5 uL
     Elga water                       to 5 mL               4.74 mL                       
     =======================    ==================== ==========================

2. Ensure there is at least 50 uL of 100x PIC dissolved in HEPES-NaCl (Wash Buffer without spermidine). If there is not enough, dissolve 1 Pierce EDTA-free Protease Inhibitor Cocktail tablet in 500 uL of Wash Buffer and store at 4C.
3. Defrost digitonin (CST #16359) and pipette to mix. Freshly transfer 20 uL to a PCR tube. Heat the tube to 95°C for 5 minutes, then place on ice.
   
   .. note::
      This thermocycler protocol is ``GapRUN/digprep``

4. Make the following two buffers immediately before the protocol calls for it. The following recipes are given per 100 uL.

   - **Wash Buffer + PIC**

     =======================    ==========================
     Component                   Amount / 100 uL
     =======================    ==========================
     Wash Buffer                      100 uL 
     100x PIC                           1 uL
     =======================    ==========================

   - **Complete Wash Buffer (Wash + PIC + digitonin)**

     =======================    ==========================
     Component                   Amount / 100 uL
     =======================    ==========================
     Wash Buffer                      100 uL 
     100x PIC                           1 uL
     CST digitonin                     2.5 uL
     =======================    ==========================

     .. note::

        Cell Signaling Technologies digitonin is batch normalized to an activity level, not a concentration.
        This is why we specify CST's digitonin and give the amount as a volume ratio.


5. Non-enzymatically detach cells and count them in FBS-containing media suing Trypan Blue. For iPSCs, this means using Gentle Cell Disassociation Reagent and counting in DMEM/F12 + 1% FBS.
6. While spinning down the cells as described, activate the Concanavalin A beads. You can activate the ConA beads
   in larger batches (e.g. activate 8 reactions worth in 1.7 mL tubes).

   a. Resuspend ConA beads via trituration, and aliquot 10 uL per sample.
   b. Place the beads on the magnet and, once clear, remove the supernatant.
   c. Add 100 uL of activation / binding buffer per 10 uL sample. Let sit at room temperature for 10-15 minutes.
   d. Place the beads on the magnet, remove the supernatant.
   e. If using the Cell Signaling Technology beads, repeat this 100 uL wash step, because CST provides
      enough reagents for two washes.
   f. Resuspend beads in 10 uL of activation/binding buffer per sample.

7. Wash aliquots of 200-500k cells twice with 100 uL of Wash Buffer + PIC. Resuspend the washed cell pellets in 100 uL of Wash Buffer + PIC.

   .. warning::
      Collect these two washes as biowaste, since the cells are not fixed. Bleach the waste and sink-dispose.

8. Combine the 100 uL of cells with 10 uL of activated ConA beads. After mixing well via trituration, place the tubes on a Nutator at room temperature for 10 minutes.

   .. note:: 

      You can optionally take some of the supernatant and look with a hemocytometer to confirm that the concentration of cells has been reduced by ConA bead binding.


9. Magnetically separate the cells bound to ConA beads, and resuspend each in 50 uL of Complete Wash Buffer (Wash + PIC + **digitonin**). Place the cells on ice.
10. On ice, spike in one microliter of the LaG16 MNase per 100k cells, mix well (optionally, with a multichannel), and nutate overnight at 4C.

Day 2
-----

.. time:: 4.5 hours

1. Prepare fresh Complete Wash Buffer (500 uL per sample, excess included), using the recipe from the previous day.
2. Magnetically separate and wash the beads with 200 uL of Complete Wash Buffer (Wash + PIC + digitonin), transferring the washed beads to a new PCR tube.
   When not pipetting, keep cells on ice

.. note:: 

    Moving the beads reduces the amount of background.

3. Repeat the wash step.
4. Resuspend beads in 50 uL of Complete Wash Buffer, mixing via gentle pipetting, and place on ice for at least two minutes.
5. Dilute 2.5M CaCl2 to 150 mM in DEPC-treated water. Dilute 1 µL of 2.5M CaCl2 with 15.6 µL water.
6. Spike in 1 uL of 150 mM CaCl2. Place samples on the Nutator at 4C for 2 hours.
7. Prepare Stop Buffer, adding the RNase A and glycogen shortly *(and outside the genomics hood!)* before the 2 hours are up. You need 50 uL per sample (excess **not** included)

   **Stop Buffer**

   =======================    ==================== ==========================
   Component                   Concentration        Amount / sample (50 uL)
   =======================    ==================== ==========================
   5M NaCl                          340 mM               1.7 uL
   500 mM EDTA                      20 mM                2.0 uL
   500 mM EGTA                      10 mM                1.0 uL
   CST digitonin                                        1.25 uL
   Elga water                       to 500 uL           43.4 uL
   20 mg/mL glycogen                50 ug/mL             0.125 uL
   20 mg/mL RNase A                 100 ug/mL            0.25 uL
   =======================    ==================== ==========================

7. Remove the samples from the Nutator, keeping them on ice. Add in 50 uL of Stop Buffer to each sample **outside of the genomics hood**, and mix with gentle pipetting.
8. Incubate samples at 37C for 10 minutes in a thermocycler, with the lid set to 65C.

   .. note::
      This thermocycler protocol is ``GapRUN/stop``

9. Place samples on the magnetic rack **outside the genomics hood**, and transfer the cleared supernatant to fresh low-binding 1.7 mL tubes.
10.  Use the Monarch DNA cleanup kit (using the small, non-miniprep columns), following the instructions that **retains small fragments**.
     
     a. Add 200 µL of binding buffer to each 100 µL sample.
     b. Add 600 µL of IPA and mix well. Do not try to combine this with the previous step, SDS will crash out!
     c. Perform two washes plus a dry spin.
     d. Elute in 50 µL of 1x TE, for compatibility with the library prep kit.

11.  Libraries can be stored at -20C until ready to perform library preparation (Day 3).

Day 3
-----

.. time:: 2.5 hours

1. Follow the instructions for `NEBNext Ultra II DNA Library Prep Kit </_static/files/nebnext_ultraII_library_prep_kit.pdf>`__, without performing size selection (e.g. follow steps 3B instead of 3A). Elute in 18 µL instead of 17 µL and stop before Step 4 (PCR enrichment).
2. Follow the :doc:`Test PCR protocol </protocols/biochem_and_analytics/genomics_sequencing/test_pcrs>` with the following parameters:

     - Use 3 µL of the 18 µL elution for test PCR purposes. 15 µL will be used in the real PCR, so :math:`\log_2(15/ 0.7) = 4.42` delta cycles.
     - Use the ``ligation_fwd`` and ``ligation_rev`` primers.
     - Target at least 500 ng. Perform 16/19/22 test cycles.
     - The final cycle count should be around 12 cycles.

5. Perform indexed "full" PCRs, following the volumes and SPRI cleanup instructions given in the Ultra II DNA Library Prep Kit instructions from above. Elute in 33 uL of 0.1x TE. Eluted libraries can be stored at -20C.
6. Quantify the libraries and pool for sequencing.


References
----------

.. [Longo2024] Longo, GMC, et al. "Type II topoisomerases shape multi-scale 3D chromatin folding in regions of positive supercoils." *Molecular Cell* (2024). https://dx.doi.org/10.1016/j.molcel.2024.10.007
.. [Koidl2021] Koidl, S, and Timmers, HTM. "greenCUT&RUN: Efficient Genomic Profiling of GFP-Tagged Transcription Factors and Chromatin Regulators." *Current Protocols* (2021). https://dx.doi.org/10.1002/cpz1.266