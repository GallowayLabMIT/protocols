=============
Gap-RUN
=============

This protocol is based on.


anti-GFP-MNase protein production
=================================


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

3. 50 mL of **5M NaCl stock solution**:

   =======================    ================ ========  ====================
   Component                   Concentration    g / L     Amount / 10 mL
   =======================    ================ ========  ====================
   NaCl                           5 M            292.21    14.611 g
   Elga water                  to 50 mL
   =======================    ================ ========  ====================

4. 50 mL of **2.5M CaCl2**:

   =======================    ================ ========  ====================
   Component                   Concentration    g / L     Amount / 10 mL
   =======================    ================ ========  ====================
   CaCl2 dihydrate              2.5 M           147.02    18.38 g
   Elga water                  to 50 mL
   =======================    ================ ========  ====================

5. 10 mL of **500 mM EDTA (pH 8.0) stock solution**

   =======================    ==================== ========  ==========================
   Component                   Concentration          g / L     Amount / 10 mL
   =======================    ==================== ========  ==========================
   EDTA                           500 mM           186.1        1.861 g
   Elga water                  to ~7 mL                       
   NaOH                        to pH 8                         ~0.75 mL of 12N NaOH
   Elga water                  to 10 mL                       
   =======================    ==================== ========  ==========================

   The EDTA makes the solution acidic. Adding the NaOH will help it dissolve.

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
1. Prepare the following buffers fresh:

   - 5 mL of **Wash Buffer** (enough for 12 samples, e.g. ~400 uL per sample, excess already included):

     =======================    ==================== ==========================
     Component                   Concentration        Amount / 5 mL
     =======================    ==================== ==========================
     1M HEPES-KOH                     20 mM                100 uL 
     5M NaCl                          150 mM               150 uL
     500 mM spermidine                0.5 mM                 5 uL
     Elga water                       to 5 mL               4.74 mL                       
     =======================    ==================== ==========================

2. Ensure there is at least 50 uL of 100x PIC dissolved in Wash Buffer. If there is not enough, dissolve 1 Pierce EDTA-free Protease Inhibitor Cocktail tablet in 500 uL of Wash Buffer and store at 4C.
3. Take 20 uL of digitonin (CST #16359) and transfer it to a PCR tube. Heat the tube to 95C for 5 minutes, then place on ice.
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

   1. Resuspend ConA beads via trituration, and aliquot 10 uL per sample.
   2. Place the beads on the magnet and, once clear, remove the supernatant.
   3. Add 100 uL of activation / binding buffer per 10 uL sample. Let sit at room temperature for 10-15 minutes.
   4. Place the beads on the magnet, remove the supernatant.
   5. If using the Cell Signaling Technology beads, repeat this 100 uL wash step, because CST provides
      enough reagents for two washes.
   6. Resuspend beads in 10 uL of activation/binding buffer per sample.

7. Wash aliquots of 200-500k cells twice with 100 uL of Wash Buffer + PIC. Resuspend the washed cell pellets in 100 uL of Wash Buffer + PIC.
8. Combine the 100 uL of cells with 10 uL of activated ConA beads. After mixing well via trituration, place the tubes on a Nutator at room temperature for 10 minutes.

.. note:: 

    You can optionally take some of the supernatant and confirm that the concentration of cells has been reduced by ConA bead binding.


9. Magnetically separate the cells bound to ConA beads, and resuspend each in 50 uL of Complete Wash Buffer (Wash + PIC + **digitonin**). 
10. Spike in one microliter of the LaG16 MNase per 100k cells, mix well, and nutate overnight at 4C.

Day 2
-----
1. Prepare fresh Complete Wash Buffer (500 uL per sample, excess included), using the recipe from the previous day.

   

3. Magnetically separate and wash the beads with 200 uL of Complete Wash Buffer (Wash + PIC + digitonin), transferring the washed beads to a new PCR tube.

.. note:: 

    Moving the beads reduces the amount of background.

2. Repeat the wash step.
3. Resuspend beads in 50 uL of Complete Wash Buffer, mixing via gentle pipetting, and place on ice for at least two minutes.
4. Spike in 1 uL of 150 mM CaCl2. Place samples on the Nutator at 4C for 2 hours.
5. Prepare Stop Buffer, adding the RNase A and glycogen shortly *(and outside the genomics hood!)* before the 2 hours are up. You need 50 uL per sample (excess **not** included)

   =======================    ==================== ==========================
   Component                   Concentration        Amount / 500 uL
   =======================    ==================== ==========================
   5M NaCl                          340 mM               17 uL
   500 mM EDTA                      20 mM                20 uL
   500 mM EGTA                      10 mM                10 uL
   CST digitonin                                        12.5 uL
   Elga water                       to 500 uL           434 uL
   20 mg/mL glycogen                50 ug/mL             1.25 uL
   20 mg/mL RNase A                 100 ug/mL            2.5 uL
   =======================    ==================== ==========================

6. Remove the samples from the Nutator, keeping them on ice. Add in 50 uL of Stop Buffer to each sample **outside of the genomics hood**, and mix with gentle pipetting.
7. Incubate samples at 37C for 10 minutes in a thermocycler, with the lid set to 65C.
8. Place samples on the magnetic rack **outside the genomics hood**, and transfer the cleared supernatant to fresh low-binding 1.7 mL tubes.
9. Use the Monarch DNA cleanup kit (using the small, non-miniprep columns), following the instructions that **retains small fragments**. Elute in 50 uL of 1x TE.
10. Libraries can be stored at -20C until ready to perform library preparation. Library preparation will take around ~3 hours.

Day 3
-----
1. Follow the instructions for NEBNext Ultra II DNA Library Prep Kit, without performing size selection (e.g. follow steps 3B instead of 3A).
2. Perform test PCRs at 17/20/23 cycles to determine the target number of cycles. A normal number of final cycles is 12 (e.g. 17 test-PCR cycles).
3. Perform indexed "full" PCRs, following the volumes and SPRI cleanup instructions given in the Ultra II DNA Library Prep Kit. Elute in 33 uL of 0.1x TE. Eluted libraries can be stored at -20C.
4. Quantify the libraries and pool for sequencing.
