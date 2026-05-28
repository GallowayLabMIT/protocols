=============
Gap-RUN
=============

This protocol is based on the work of [Longo2024]_ and [Koidl2021]_


anti-GFP-MNase protein production
=================================

Required materials
------------------
In addition to the buffer components listed below, we use the following kits and other components:

- B-Per: bacterial lysis kit (Thermo Fisher 78248)
- EDTA-free protease inhibitors (Thermo Fisher A32965)
- Glutathione spin columns (Thermo Fisher 16106)
- Biotin-tagged thrombin protease (Sigma-Aldrich SAE0147-5KU)
- T1 streptavidin beads (Thermo Fisher 65601)
- 10 kDa MWCO protein concentrator spin columns (Thermo Fisher 88513)

Stock buffer preparation
-------------------------

1. Prepare and check that there is sufficient amounts of the following :doc:`shared genomics buffers </protocols/biochem_and_analytics/genomics_sequencing/shared_genomics_buffers>`:
  
  - 1M Tris-HCl, pH 7.5
  - 0.5M EDTA, pH 8.0
  - 5M NaCl

2. 1 mL of **1M IPTG**:

   ==============================    ================ ========  ====================
   Component                          Concentration    g / L     Amount / 1 mL
   ==============================    ================ ========  ====================
   IPTG                                  1 M           238.3     0.238 g
   Elga water                           to 1 mL
   Sterile filter, 0.22μm filter
   ==============================    ================ ========  ====================

3. 200 mL of **Protein purification buffer**:

   ==============================    ================ ========  ====================
   Component                          Concentration    g / L     Amount / 200 mL
   ==============================    ================ ========  ====================
   Tris-HCl                                125 mM      19.70     3.94 g
   NaCl                                    150 mM      43.83     8.77 g
   NaOH                                to pH 8.0
   Elga water                           to 200 mL
   ==============================    ================ ========  ====================

4. 50 mL of **0.1M K2PO4 (pH 7.0)**:

   ==============================    ================ ========  ====================
   Component                          Concentration    g / L     Amount / 50 mL
   ==============================    ================ ========  ====================
   K2PO4                               100 mM          17.42     0.871 g
   HCl                                 to pH 7.0
   Elga water                           to 50 mL
   ==============================    ================ ========  ====================


Day -n
------

1. Transform the plasmid encoding GST-LaG16-MNase (`Addgene 170978 <https://addgene.org/170978>`_) into BL21 (DE3) cells.
   Streak the resulting bacteria to singles on LB-Amp plates.

Day 0
-----

1. From one colony, start two 5 mL overnight cultures in LB-Amp media.
2. Autoclave four baffled 1L flasks, each filled with 200 mL of freshly prepared LB media.
3. After the flasks have cooled to room temperature (or the following day before starting), spike-in Amp.
4. Prepare fresh **sample buffer**. Sample buffer made within the last month or two can also have fresh
   β-mercaptoethanol spiked in lieu of making fresh buffer.

   =======================    ==================== ==========================
   Component                   Concentration        Amount / 10 mL
   =======================    ==================== ==========================
   50% glycerol                  10%                  2 mL
   1M Tris (pH 7.5)              50 mM                500 μL
   0.5M EDTA (pH 8.0)            20 mM                400 μL
   10% SDS                       2%                   2 mL
   β-mercaptoethanol             1%                   100 μL
   Bromophenol blue             to desired color
   Elga water                   to 10 mL              5 mL
   =======================    ==================== ==========================


Day 1
-----
1. Take a sample of the LB-Amp flasks for blanking the NanoDrop.
2. Inoculate each flask (containing 200 mL of media) with 2 mL of the overnight culture.
3. Incubate the flasks at 37C, shaking at 200 rpm, until it reaches an OD600 of 0.5, about two hours.
4. Take a 1.5 mL "pre-induction" sample, spin it down, and resuspend in 300 μL of sample buffer, storing it at -20C
   for future analysis.
5. Induce protein production by adding 200 μL of 1M IPTG to each flask. Lower the incubator
   temperature to 18C (or, whatever room temperature is) and let flasks grow overnight.

Day 2
-----
1. Measure the OD of the flasks by diluting a sample five-fold. The OD600 should have reached at least 6.0.
2. Take a 500 μL "post-induction" sample, spin it down, and resuspend in 300 μL of sample buffer, storing it at -20C
   for future analysis.
3. Split the bacterial culture into 50 mL tubes, not exceeding 40 mL per tube (to prevent spillage upon centrifugation in the fixed rotor).
4. Pellet the cells at maximum speed (14000 g) using the fixed-angle rotor. Combine the pellets together and mass them.
5. Prepare 100x protease inhibitor cocktail (1 EDTA-free protease inhibitor tablet dissolved in 500 uL) if there is not enough.
   The tablet will not fully dissolve: pipette up and down to resuspend settled particles.
6. Prepare 4 mL of complete B-Per (4 mL B-Per buffer, 2 μL lysosome, 2 μL DNAse I, both included in the B-Per kit, plus 40 μL of 100x protease inhibitor cocktail) per 1g of cell mass.
7. Resuspend the pellet in the B-Per. Use a 5 mL serological pipette to fully resuspend the pellet. 
8. After incubation at room temperature for 15 minutes, subject the slurry to two freeze thaw cycles to -80C and back to room temperature.
9. Clarify the lysate by spinning at 14000 g in a fixed-angle rotor for 30 minutes at 4C.
10. Take a 50 μL sample of the clarified lysate, dilute it to 300 μL in sample buffer, and store it at -20C for later analysis.
11. Dilute the clarified lysate 2:1 in protein purification buffer.
12. Prepare two 0.2 mL glutathione spin columns, by washing it twice with two column volumes of wash buffer.
13. Load the clarified lysate onto the columns. This takes many, many spins because our vacuum manifold isn't strong enough.

.. note::

   When you spin the columns, don't screw on the caps! Leave the red caps off the columns.

14. Once the lysate has been loaded, wash the columns with successive washes (2 column volumes: 400 μL) until
    the A280 absorbance drops to background levels. This takes about 10 total washes (20 CVs).
15. Cover the bottom of the columns with parafilm.
16. To each column, combine 100 units of biotin-tagged thrombin protease diluted to 200 μL in wash buffer to each column.
    Incubate overnight at 4C.

.. note::

   You can likely reduce the amount of protease; I used excess to ensure cleavage worked well. 

Day 3
------
1. Prepare 400μL fresh 1M dithiothreitol (DTT). This is much in excess, but we are limited by balance accuracy.

   ==============================    ================ ========  ====================
   Component                          Concentration    g / L     Amount / 400 μL
   ==============================    ================ ========  ====================
   DTT                                 1M             154.25     0.077 g
   Elga water                           to 400 μL
   ==============================    ================ ========  ====================

2. Prepare 5 mL of sterile filtered, PIC-spiked fresh Buffer A:

   =======================    ==================== ==========================
   Component                   Concentration        Amount / 5 mL
   =======================    ==================== ==========================
   0.1M K2PO4 (pH 7.0)               20 mM               1 mL
   50% glycerol                  10%                   1 mL
   0.5M EDTA (pH 8.0)            0.5 mM                5 μL
   1M DTT                          1 mM                  5 μL
   Elga water                     to 5 mL                3 mL
   0.22 micron filter
   100x PIC                                           50 μL
   =======================    ==================== ==========================

2. Spin the columns, collecting "elution 1". Wash with 1 CV (200 μL) for two successive elutions.
3. Combine elutions that have significant A280 absorption: typically, the first two elutions are combined. 
4. Wash 60 μL of T1 streptavidin beads three times with PBS. Wash with 200 μL each time.
5. Combine the elutions with the washed streptavidin beads. Rotate the elutions at 4C for 30 minutes.
6. Remove the streptavidin beads with a magnet, and transfer the elution fraction to fresh low-binding tubes.
7. Take a 10 μL sample of the combined elution, dilute to 20 μL in sample buffer, and store at -20C for future analysis.
8. Load the elution fraction to 10 kDa MWCO protein concentrator spin columns, and concentrate to a volume of around 100 μL.
9. Buffer exchange by adding prepared Buffer A. Buffer exchange by adding 100 μL of Buffer A on top, re-concentrating to 100 μL. Repeat this four times.
10. Concentrate the protein to a volume of around 37.5 uL per column. Combine the two volumes to around 75 μL, diluting with
    Buffer A as needed.
11. Add 75 μL of 100\% glycerol on top, to reach 150 μL of purified protein, to be stored at -20C.
12. Load the accumulated samples in sample buffer onto a :doc:`prepared denaturing protein gel </protocols/protein_production/denaturing_protein_gel>`, to confirm a single elution band
    corresponding to the anti-GFP-MNase.

Day 4
-----

Cell harvest and fixation
^^^^^^^^^^^^^^^^^^^^^^^^^
1. Prepare sufficent 100x BSA (200 µg / mL) to aid to help cells pellet and limit cell losses. Cool a centrifuge to 4°C and place sufficient PBS on ice.
2. Collect cells following normal passaging conditions. Collect into and wash in the same 50 mL tube. After collecting and spinning down the cells,
   perform a PBS wash before resuspending and counting cells. Spike in 100x BSA prior to spinning down the cells in the PBS wash.
3. Count the cells. We want as high cell counts as possible; it is good to crosslink and fix as many
   cells as possible instead of throwing away cells at this step.

   .. warning::

        Collect all of the following wash steps as formaldehyde waste until step the cells are resuspended prior to aliquoting.

4. In a fumehood, add 1 mL of fresh 16% formaldehyde per 15 mL of cells (15M cells), in a dropwise but relatively rapid manner.
   Use the 10mL and 1mL ampules either opened fresh or opened and stored in the last ~48 hours.
5. Incubate for 10 minutes at room temperature on the plate shaker.
6. Add pH 7.5 Tris dropwise to a final concentration of 0.375M. This is 3.45 mL of 2M Tris per 15M cells.
7. Incubate for 5 minutes at room temperature. Spike in 100x BSA prior to spinning at 400 xg at 4°C for 5 minutes.
8. Remove the supernatant, wash with cold PBS at a concentration of 1M cells / mL. Spike in 100x BSA prior to spinning at 400 xg at 4°C for 5 minutes.
9. Resuspend the cell pellet to 20M cells / mL, in cold PBS with spiked-in 100x BSA. Make the desired aliquots of these cells.
   For the MNase titration, you will need at least one aliquot of 5M cells. If processing the rest of the cells, in the same reaction,
   you can freeze down a "large" aliquot.

   .. note::

      For smaller aliquots, make sure you use **low-binding** 1.7 mL tubes instead of normal 1.7 mL tubes.
10. Spin down aliquots, aspirate the supernatant and snap-freeze the cell pellets in liquid nitrogen. Store at -80°C.
    For consistency, snap-freeze and store the main samples even if you are proceeding on the same day.
    There is no benefit to having "fresh" un-snap-frozen cells.

    .. note::
        
        To snap-freeze, using the LN2 PPE, fill the small dewar with LN2. Then, pour some LN2 into a styrofoam
        container. Place the tubes to be snap-frozen in the foam holders we use for water baths, then float
        them in the LN2.

        Use tongs / some similar tool and the LN2 gloves to remove the samples. 

MNase Titration
^^^^^^^^^^^^^^^
.. time:: 2 hours to pause point (reverse crosslinking)

A key variable is the ratio of MNase to cells required to properly digest the DNA.

For each cell type (iPS11, Leiden iPSCs, 293Ts, reprogrammed neurons), you should perform the titration. It is not necessary
to have a titration per genetic edit.

You will need two 5M cell aliquots to perform the titration on and compare to the commercial MNase.

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
20. Compare the digestion bands to estimate the activity on the anti-GFP-MNase, in the same units as the commercial MNase.
    Expect that the in-house anti-GFP-MNase has at least 5x worse activity.

GapRUN
=======

Stock buffer preparation
------------------------
1. Prepare and check that there is sufficient amounts of the following :doc:`shared genomics buffers </protocols/biochem_and_analytics/genomics_sequencing/shared_genomics_buffers>`:
  
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
- Check the Concanavalin A (ConA) beads for aggregation. To do so, after pipetting
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

11.  Libraries can be stored at -20C until ready to perform library preparation. Library preparation will take around ~3 hours.

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


.. [Longo2024] https://dx.doi.org/10.1016/j.molcel.2024.10.007
.. [Koidl2021] https://dx.doi.org/10.1002/cpz1.266