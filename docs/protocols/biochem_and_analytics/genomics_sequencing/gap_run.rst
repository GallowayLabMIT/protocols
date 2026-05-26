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

Prepare and check for sufficient amounts of the following buffers; many of them are common genomics buffers.

1. 10 mL **1M Tris (pH 7.5)**

   =======================    ================ ========  ====================
   Component                   Concentration    g / L     Amount / 10 mL
   =======================    ================ ========  ====================
   Tris-HCl                     1 M             157.64       1.57g
   Elga water                  to 9 mL
   NaOH                        to pH 7.5                 ~140 uL of 12 N NaOH
   Elga water                  to 10 mL
   =======================    ================ ========  ====================


2. 10 mL of **500 mM EDTA (pH 8.0) stock solution**

   =======================    ==================== ========  ==========================
   Component                   Concentration          g / L     Amount / 10 mL
   =======================    ==================== ========  ==========================
   EDTA                           500 mM           186.1        1.861 g
   Elga water                  to ~7 mL                       
   NaOH                        to pH 8                         ~0.75 mL of 12N NaOH
   Elga water                  to 10 mL                       
   =======================    ==================== ========  ==========================

   The EDTA makes the solution acidic. Adding the NaOH will help it dissolve.

3. 50 mL of **5M NaCl stock solution**:

   =======================    ================ ========  ====================
   Component                   Concentration    g / L     Amount / 10 mL
   =======================    ================ ========  ====================
   NaCl                           5 M            292.21    14.611 g
   Elga water                  to 50 mL
   =======================    ================ ========  ====================

4. 1 mL of **1M IPTG**:

   ==============================    ================ ========  ====================
   Component                          Concentration    g / L     Amount / 1 mL
   ==============================    ================ ========  ====================
   IPTG                                  1 M           238.3     0.238 g
   Elga water                           to 1 mL
   Sterile filter, 0.22μm filter
   ==============================    ================ ========  ====================

5. 200 mL of **Protein purification buffer**:

   ==============================    ================ ========  ====================
   Component                          Concentration    g / L     Amount / 200 mL
   ==============================    ================ ========  ====================
   Tris-HCl                                125 mM      19.70     3.94 g
   NaCl                                    150 mM      43.83     8.77 g
   NaOH                                to pH 8.0
   Elga water                           to 200 mL
   ==============================    ================ ========  ====================

6. 50 mL of **0.1M K2PO4 (pH 7.0)**:

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

Day n
------
Following the RCMC MNase titration protocol, the activity of the anti-GFP-MNase can be benchmarked against commercial MNase.

GapRUN
=======

Stock buffer preparation
------------------------
Prepare and check for sufficient amounts of the following buffers. Suggested amounts
of buffer are given; these stock solutions are enough for many experiments (and useful
for other genomics techniques)


1. 10 mL of **1M HEPES-NaOH (pH 7.5)**

   =======================    ================ ========  ====================
   Component                   Concentration    g / L     Amount / 10 mL
   =======================    ================ ========  ====================
   HEPES                         1 M            238.3       2.383 g
   Elga water                  to 6 mL
   NaOH                        to pH 7.5                 ~250 uL of 12 N NaOH
   Elga water                  to 10 mL
   =======================    ================ ========  ====================

2. 500 uL of **500 mM spermidine**, aliquoted and stored at -20C

   ===========================    ================ ========  ====================
   Component                        Concentration    g / L     Amount / 500 uL
   ===========================    ================ ========  ====================
   Spermidine trihydrochloride        500 mM        254.6       63.7 mg
   Elga water                       to 500 uL
   ===========================    ================ ========  ====================

3. **5M NaCl stock solution**: see above.

4. 50 mL of **2.5M CaCl2**:

   =======================    ================ ========  ====================
   Component                   Concentration    g / L     Amount / 10 mL
   =======================    ================ ========  ====================
   CaCl2 dihydrate              2.5 M           147.02    18.38 g
   Elga water                  to 50 mL
   =======================    ================ ========  ====================

5. **0.5M EDTA (pH 8.0)**: see above.

6. 500 uL of **500 mM EGTA stock solution**

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