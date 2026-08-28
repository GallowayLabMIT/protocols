=========
CUT&Tag
=========

.. important::

   This protocol is modified from the :download:`Active Motif protocol </_static/files/cut_and_tagIT_express_manual.pdf>`.
   Our modifications typically make the process more efficient or are gentler on the cells. Additionally, the final
   PCR step diverges, as we perform a :doc:`test PCR </protocols/biochem_and_analytics/genomics_sequencing/test_pcrs>`
   first.
   
   We follow the same numbering as the linked protocol for easy comparison, i.e., step 1 in this protocol maps to
   step 1 of the actual protocol. You may want to print out both. Steps labeled with letters (e.g., step a) are 
   steps we've added to streamline the protocol in our hands.

We buy the following kits from Active Motif:

- `CUT&Tag-IT Express <https://www.activemotif.com/catalog/1395/cut-tag-it-express>`__ (Active Motif 53175/53177): the main kit. 
  The kit contains components stored at room temperature (cupboard under the genomics bench), at 4ºC (drawer in Sven), and at 
  –20ºC (Active Motif boxes in Sven). Be sure to unpack and store components properly when they arrive.
- `CUT&Tag Spike-in Control <https://www.activemotif.com/catalog/1377/cut-tag-spike-in>`__ (Active Motif 53168/53173): spike-in nuclei 
  and corresponding primary antibody. Pick the spike-in control kit that **matches the secondary antibody** you will be using for the 
  marks of interest. Active Motif sells anti-rabbit and anti-mouse controls. The control primary antibody is stored at –20ºC (with other 
  Active Motif antibodies in Sven), and the nuclei are stored at –80ºC (currently in a bag in the red bin in Queen Iduna).

Background
==========
CUT&Tag uses Tn5 conjugated to protein-A/protein-G to tagment DNA
at sites determined by primary/secondary antibody binding. The advantage
of this is a higher signal-to-noise ratio relative to CUT&RUN, which
uses MNase conjugated to protein-A. CUT&Tag libraries are directly tagmented
with PCR-compatible adapters, which allows you to skip the library ligation
step.

However, Tn5 has a related accessibility bias (like the bias measured
in ATAC-seq!). CUT&Tag buffers do the tagmentation in a higher-salt buffer
than ATAC-seq, which increases electrostatic screening and thus disrupts
nucleosome and chromatin interactions, lessening the accessibility signal.

This protocol can be reasonably split over three days.

- **Day 1**: cell counting, bead binding, primary antibody binding overnight. For 32 samples, this takes ~3 hours after cell dissociation and counting.
- **Day 2**: secondary antibody binding, tagmentation, DNA cleanup. For 32 samples, this takes ~9 hours.
- **Day 3+**: test PCR, PCR amplification, library quantification. These steps can easily be split across several days if needed.


Experimental setup
==================

Active Motif does *not* recommend using an IgG control antibody condition. Instead,
use a common histone mark (H3K27me3, H3K27ac) as your control. If your experiment
already calls for one of these histone marks, then you do not need an explicit
separate control.

Select primary antibodies that have the same species, either rabbit or mouse. Then,
order a spike-in nuclei kit from Active Motif with the matching species. 
   
Design your experiment such that you have in excess of **500k cells per antibody** for 
each cell condition of interest at the day of collection. For example, if you have
four antibodies, culture cells such that you collect more than 2M cells. The protocol below 
refers to your different cell treatments as **conditions** and each combination of condition 
and antibody as a **sample** or **reaction**. For example, with eight cell conditions and four 
antibodies each, you'd have 32 reactions (aka samples).


Preparation (N days before)
============================
- Order the CUT&Tag-IT Express and CUT&Tag Spike-in Control kits linked above. These typically ship within a few days of ordering.
  Store the reagents at the proper temperature:

   - **Room temperature** (open bottles inside genomics hood, extras in cabinet): Tn5 Release Solution, DNA Purification Binding Buffer, DNA Purification Wash Buffer, DNA Purification Elution Buffer
   - **4ºC** (Sven drawer): 1X Binding Buffer, Dig-Wash Buffer, Dig-300 Buffer, Antibody Buffer, Tagmentation Buffer, ConA beads (tube), silica beads (tube), SPRI beads
   - **–20ºC** (Sven Active Motif box): Protease Inhibitor Cocktail (PIC), 5% Digitonin, secondary antibodies (alpaca anti-rabbit, rabbit anti-mouse), pA-Tn5 Transposomes, Glycogen, Proteinase K, i5 and i7 index primers
   - **–20ºC** (Sven CUT&Tag antibodies sleeve): primary antibodies, Spike-in control antibody
   - **–80ºC** (Queen Iduna red bin): Spike-in nuclei

- Check the Concanavalin A (ConA) beads for aggregation. To do so, pipet thoroughly to 
  resuspend the beads, then dilute 1 µL of beads in 9 µL of 0.1x TE (or water). Transfer
  the 10 µL to the hemocytometer (there's one by the microscope in 66-219) and look under the microscope.
  You should not see large clumps of beads; if you do, then the beads are NOT good to use.
  If you got the beads from Active Motif (e.g., in the kit linked above), contact customer support:
  they will ship you new beads overnight for free. Otherwise, order more from a vendor of your choice
  (e.g., `Cell Signaling Technology 93569S <https://www.cellsignal.com/products/cut-run-kits-reagents/concanavalin-a-magnetic-beads-and-activation-buffer/93569>`__).

.. warning:: 

    Do **NOT** store Concanavalin A (ConA) beads below 4ºC. These beads are 
    extremely sensitive to freezing.

    Some protocols tell you not to vortex ConA beads, to avoid shearing
    the ConA from the beads, so we avoid vortexing the beads in the initial
    steps.

Day 1
======

.. time::
   ~3 hours plus time to collect and count cells; usually **~4 hours total**

Prepare buffers
---------------
.. note::

   These steps are not numbered in the original protocol. We use letters for steps
   that do not appear in the original protocol.

.. note:: 
   For all the solutions listed, make extra to account for pipetting loss across multiple samples.
   A good rule of thumb is to make **10% extra** for all the recipes listed. For the Transposomes Master Mix, 
   make a bit less than this, since the kit does not provide much extra of these reagents.
   

a. Defrost Protease Inhibitor Cocktail (PIC) on ice and 5% Digitonin at room temperature.
b. Prepare Complete Antibody Buffer and Dig-Wash + PIC. Make extra of each of these!
   
   **Complete Antibody Buffer (51 µL / reaction)**

   ============================= ======
   Component                     Volume
   ============================= ====== 
   Antibody Buffer                50 µL
   Protease Inhibitor Cocktail   0.5 µL
   5% Digitonin                  0.5 µL
   ============================= ======

   **Dig-Wash + PIC (101 µL / reaction)**

   ============================  =======
   Component                     Volume 
   ============================  =======
   Dig-Wash Buffer               100 µL 
   Protease Inhibitor Cocktail   1 µL  
   ============================  =======

Activate ConA beads
-----------------------------
.. note::
   
   The original protocol suggests you do this before preparing the cells, but does not order the
   protocol in this way.

6. Resuspend the ConA beads via trituration and aliquot 10 µL per sample in low-binding 1.7-mL tubes. Batch up to 80 µL (for 8 samples) per tube.
7. Place tubes on the magnet. Once clear, remove the supernatant.
8. Remove tubes from the magnet and resuspend in 100 µL of activation / binding buffer (Active Motif 1X Binding Buffer) per sample. This should be 10x the original bead volume. Incubate at room temperature for 10-15 minutes.
9. Place tubes on the magnet and discard the supernatant once clear.

c. If using the Cell Signaling Technology ConA beads, repeat the 100 µL wash step, as CST provides enough reagents
   for two washes.

10. Remove tubes from the magnet and resuspend in 10 µL of activation / binding buffer per sample. Aliquot each 10-µL
    sample of beads into fresh PCR tubes (one tube per sample).

Prepare cells
-------------

1. Collect your target cells **without using trypsin** or other enzymatic methods.
   For iPSCs, this means using Gentle Cell Disassociation Reagent. Sort cells if required. Then, resuspend 
   cells in media that allows for good pelleting (for iPSCs: DMEM/F12 + 1% FBS) and count live cells using Trypan Blue.

d. After counting, take spike-in nuclei out of the –80ºC freezer and defrost on ice. Combine enough nuclei
   for all samples together into a single tube for better reproducibility.

   .. note::
      
      We want the spike-in reads to be 5-10% of the overall sequencing reads. Use a spike-in nuclei : cell ratio
      of 1:25 for common marks, increasing to 1:10 for rare marks. For H3K27me3, H3K27ac, H3K4me3, we used 20,000
      spike-in nuclei for 500,000 cells.

      Active Motif provides vials of 160 µL at 500 nuclei/μL, so 20,000 nuclei is 40 µL (4 reactions per vial).

e. Calculate the volume of cells needed to obtain 500k cells per CUT&Tag reaction.
   If you are running multiple reactions (antibodies) per cell condition, you can make a cell "master mix"
   (e.g., calculate volume for 2M cells if you have 4 antibodies). It is helpful to use a spreadsheet 
   for these calculations.

   .. note:: 

      If you do not have 500k cells per reaction, you can use fewer cells.
      However, you need to adjust the amount of spike-in nuclei for each reaction!
      It is very important that the cell : spike-in-nuclei ratio is constant.

      For example, if most of your conditions have 500k cells, but one only has 400k cells,
      then you should use the entire 400k while only adding in 4/5th of the amount of spike-in
      nuclei.

2. Aliquot 500k cells per reaction into low-binding 1.7-mL tubes.

f. Add spike-in nuclei to the cell aliquots.

4. Centrifuge cells for 3 minutes at 600xg at 4°C and discard the supernatant.

   .. warning:: 
      Since these are still live cells, collect the supernatant as BL2 waste and decontaminate with bleach.
      It is simplest to do this in the quarantine BSC. 

      All other waste from this protocol (unless otherwise noted) can be collected in a 50-mL conical in 
      the genomics hood for sink disposal.

5. Resuspend cells in 100 µL Dig-Wash + PIC per sample.

11. Add 100 µL of cells per sample to the Con A beads in PCR tubes prepared earlier. Resuspend via trituration
    and incubate on a Nutator (e.g., `this <https://www.vwr.com/us/en/product/4787436/vwr-nutating-mixer>`__) 
    for 10 minutes at room temperature.

Bind primary antibody 
------------------------
g. Prepare Complete Antibody Buffer plus the chosen antibodies on ice. Prepare slight excess (e.g., 17x for 16 samples), 
   and make one master mix per antibody:
   
   **Complete Antibody Buffer plus Antibodies (52 µL / condition)**

   ============================  ======================================
   Component                     Volume
   ============================  ======================================
   Complete Antibody Buffer      50 µL
   Target antibody                1 µL (or manufacturer recommendation)
   Spike-in control antibody      1 µL
   ============================  ======================================

12. Remove tubes from the Nutator and briefly spin down. Place the tubes on the magnet and discard the supernatant.
13. Resuspend the beads/cells in 52 µL of cold Complete Antibody Buffer plus Antibodies.

15. Place samples on a Nutator overnight at 4°C.

Day 2
=====

.. time::
   - For 32 samples and one person: ~5 hours through tagmentation, ~4 hours for DNA extraction; **total ~9 hours**
   - For 5 and 2 samples: 7 hours and 5.5 hours total, respectively

Prepare buffers
------------------

.. note::

   The proposed volumes in the Active Motif documentation are greatly in excess! As described above, a good rule of thumb 
   is to make **10% extra** for all the recipes listed. For the Transposomes Master Mix, make a bit less, since 
   the kit doesn't provide much extra of this reagent.

h. Defrost Protease Inhibitor Cocktail (PIC) on ice and 5% Digitonin at room temperature.
i. Prepare Complete Tagmentation Buffer, Complete Dig-300 Buffer, and Complete Dig-Wash buffer per condition. Make some excess.
   
   .. note::

      Some volumes are small; if you are only doing 1 sample, scale up just for the purpose of pipetting no less than 0.5 µL.
   
   **Complete Tagmentation Buffer (40 µL / reaction)**

   ============================= ======== 
   Component                     Volume   
   ============================= ======== 
   Tagmentation Buffer            40 µL 
   Protease Inhibitor Cocktail   0.4 µL 
   5% Digitonin                  0.08 µL 
   ============================= ======== 

   **Complete Dig-300 Buffer (500 µL / reaction)**

   ============================  ====== 
   Component                     Volume
   ============================  ====== 
   Dig-300 Buffer                500 µL
   Protease Inhibitor Cocktail     5 µL 
   5% Digitonin                    1 µL
   ============================  ======

   **Complete Dig-Wash Buffer (700 µL / reaction)**

   ============================= ====== 
   Component                     Volume 
   ============================= ====== 
   Dig-wash Buffer               700 µL
   Protease Inhibitor Cocktail     7 µL
   5% Digitonin                    7 µL 
   ============================= ====== 

Bind secondary antibody
-----------------------

16. Remove tubes from the Nutator and briefly spin to collect solution at the bottom. Place on the magnet and remove the supernatant.
17. Wash the beads by resuspending in 200 µL of Complete Dig-Wash Buffer. Transfer the solution to fresh PCR tubes and place the tubes back on the magnet.
18. Prepare a secondary antibody master mix:

    **Secondary Master Mix (100 µL / reaction)**

    ============================ ====== 
    Component                    Volume
    ============================ ====== 
    Complete Dig-Wash Buffer     100 µL 
    Secondary antibody             1 µL
    ============================ ====== 

    Remove the supernatant from the beads. Resuspend each sample in 100 µL of Secondary Master Mix.

19. Place the tubes on a Nutator at room temperature for 15 minutes.
20. Pipet gently to resuspend beads, then place back on the Nutator for another 15 minutes.
21. Remove tubes from the Nutator and briefly spin to collect solution at the bottom.
22. Place the tubes on the magnet, then discard the supernatant.
23. Resuspend in 200 µL of Complete Dig-Wash Buffer, then place back on the magnet.
24. Repeat the wash step by removing the supernatant, adding Complete Dig-Wash buffer, mixing, and placing back on the magnet.

Bind CUT&Tag-IT Assembled pA-Tn5 Transposomes
---------------------------------------------
25. Dilute CUT&Tag-IT Assembled pA-Tn5 Transposomes in Complete Dig-300 Buffer. Make very slight excess.
    
    **Transposomes Master Mix (101 µL / reaction)**

    ==============================  ====== 
    Component                       Volume
    ==============================  ======
    Complete Dig-300 Buffer         100 µL
    Assembled pA-Tn5 Transposomes   1 µL  
    ==============================  ======

26. Discard the supernatant.
27. Add 100 µL of Transposomes Master Mix and pipet to resuspend the beads.
28. Place tubes on a Nutator at room temperature for 15 minutes.
29. Pipet gently to resuspend beads, then place back on the Nutator for another 15 minutes.
30. Remove tubes from the Nutator and spin briefly to collect solution at the bottom.
31. Place the tubes on the magnet, then discard the supernatant.
32. Add 200 µL of Complete Dig-300 Buffer and gently pipet to resuspend the beads.
33. Repeat the wash step by placing on the magnet, discarding the supernatant, and resuspending in Complete Dig-300 Buffer.

Tagment
------------
34. Place the tubes on the magnet and discard the supernatant.
35. Add 40 µL of Complete Tagmentation Buffer. Gently pipet to resuspend the beads.
36. Incubate at 37°C in a thermocycler for one hour.
    
   .. note::
      This is the ``C&T/tagment`` protocol.

j. Thaw Glycogen at room temperature and Proteinase K on ice.
k. Prepare Complete Tn5 Release solution on ice. Vortex the Tn5 Release Solution for at least 30 seconds.
   
   **Complete Tn5 Release Solution (40 µL / reaction)**

   ======================  =======
   Component               Volume 
   ======================  ======= 
   Tn5 Release Solution    40 µL  
   Glycogen                0.8 µL 
   Proteinase K            0.8 µL 
   ======================  =======

Extact DNA 
--------------

37. Place the tubes on the magnet and discard the supernatant.
38. Vortex the Complete Tn5 Release Solution, then add 40 µL of Complete Tn5 Release Solution per sample.
39. Mix well via pipetting.
    
    .. note::

      It is typical for the beads to form a large clump during the incubation. Do your best to mix
      here and in the next few steps; it will be difficult to fully homogenize the solution. This requires
      **at least 1 minute** of pipetting per sample at this step.

40. Incubate the reaction for 1 hour at 55°C in a thermocycler, with the heated lid set to 65°C.

   .. note::

      This is the ``C&T/tag_stop`` thermocycler protocol.

l. If the extraction buffers are new, follow the instructions on the bottles: add 9 mL IPA to the DNA Purification Binding Buffer
   and 40 mL ethanol to the DNA Purification Wash Buffer.

41. Add 40 µL of DEPC-treated water to each sample and mix well via pipetting. Place back at 55°C for 5 minutes.

   .. note::
      This is the ``C&T/release`` thermocycler protocol.

44. While the samples are incubating, prepare the silica beads. Begin by vortexing the silica beads for at least 30 seconds.
45. Pipet 25 µL of silica beads per sample into fresh PCR tubes. Place tubes on a magnet.

m. Discard the supernatant from the silica beads, then take the beads off the magnet. Add 35 µL of DNA Purification Binding Buffer (yellow solution).

n. When the samples are done incubating, pipet well until the bead/cell clump is broken up. Add 100 µL of DNA Purification Binding Buffer (60% IPA)
   to each sample to help with homogenization. Pipet with the volume set below 180 µL to avoid air bubbles.
   Place the samples on the magnet and ensure the beads pellet well.

48. Remove ~180 µL total supernatant from the samples while still on the magnet, adding it to the silica bead tubes.
    Pipet well to mix and incubate at room temperature for 5 minutes.

    .. warning::
      It is important that as few magnetic beads as possible are transferred! You don't need to transfer all 180 µL
      of supernatant if it comes with some beads.

49. Place the tubes on the magnet and discard the supernatant.
50. Resuspend in 200 µL of DNA Purification Wash Buffer.
51. Place tubes back on the magnet and discard the supernatant.
52. Repeat the wash step by adding wash buffer, pipetting to resuspend, placing back on the magnet, and discarding the supernatant.
53. Leave the tubes on the magnet with the caps open, and use a 10-µL pipet to remove any remaining wash buffer. Air dry until the beads transition from shiny to matte, not more than 5 minutes.
54. Remove the tubes from the magnet and resuspend in 24 µL of DNA Purification Elution Buffer. Incubate for 1 minute.
55. Place tubes on the magnet and transfer 23 µL of supernatant to fresh PCR tubes.
   
    .. note::
      At this point, pre-amplification libraries can be stored at –20ºC. Alternatively, further steps can be performed on the same day if desired.

Day 3+
======

.. time::
   Total: ~8 hours
      - Test PCR ~2.5 hours
      - "Real" PCR and cleanup ~2 hours 
      - Library QC ~2.5 hours
      - Library pooling <1 hour

PCR amplify
-----------

o. Follow the :doc:`Test PCR protocol </protocols/biochem_and_analytics/genomics_sequencing/test_pcrs>` with the following parameters:

  - Use 3 µL of the 23 µL elution for the test PCR; 20 µL will be used in the "real" PCR
  - Use the ``tagmentation_fwd`` and ``tagmentation_rev`` primers
  - Perform the test PCR with cycle counts 16, 19, 22
  - For the "real" PCR, target 100 ng of the final amplified libraries; this should require ~12 cycles

56. Set up the "real" PCR with indexed primers.
    Choose a unique set of indexed primers for each library. For instance, use a different i7 primer for each cell condition and 
    a different i5 primer for each antibody. Use the primers that come with the CUT&Tag kit (Sven –20ºC kit box). For the master mix,
    use the NEBNext reagent (`NEB E7645 <https://www.neb.com/en-us/products/e7645-nebnext-ultra-ii-dna-library-prep-kit-for-illumina>`__, Sven –20ºC "Library prep reagents" box) instead of the one that comes with the kit.
    
    =======================================  ======
    Component                                Volume
    =======================================  ======
    2x NEBNext Ultra II Q5 Master Mix        25 µL
    i5 indexed primer (Nextera compatible)   1 µL
    i7 indexed primer (Nextera compatible)   1 µL
    Water                                    3 µL
    Pre-amplification library                20 µL
    =======================================  ======

57. Using the optimal cycle counts from the test PCR, run the "real" PCR with the following program (``lib_prep/pcr``):

     ==========  =============  ==============================================
     Temp (°C)   Time (MM:SS)   Description
     ==========  =============  ==============================================
     72          5:00           Polymerase activation
     98          0:30           Initial denaturation
     --          --             *Optimal number of cycles of:*
     98          0:10           Denaturation
     65          1:15           Extension
     --          --             *[end cycle]*
     4           Hold           Final hold
     ==========  =============  ==============================================

     It is possible that the cycle counts will differ across samples. If that is the case, use the ``lib_prep/test_pcr`` thermocycler protocol, removing samples
     at the hold steps as needed.

p. Vortex SPRI beads well, at least 30 seconds. Prepare fresh 80% ethanol for the bead wash steps, 400 µL per sample.

58. Perform a double-sided SPRI bead clean-up. Add 25 µL SPRI (0.5x) to each sample, pipet to mix, and incubate at room temperature for 5 minutes.
59. Place tubes on the magnet and move the supernatant to new PCR tubes. Discard the beads.
60. Add 35 µL of SPRI beads to the sample (0.7x sample volume, for a 1.2x final ratio), mix well via pipetting, and incubate at room temperature for 5 minutes.
61. Place tubes on the magnet and discard the supernatant. Wash the beads twice with 200 µL of 80% ethanol, without disturbing the beads
    or removing the beads from the magnet (i.e., do not resuspend).
62. Allow the beads to dry until they transition from shiny to matte in appearance, not longer than 5 minutes. Add 22 µL of DNA Purification Elution buffer, pipet to mix,
    and incubate at room temperature for 1 minute.
63. Place the tubes back on the magnet, and transfer the 22 µL to a fresh low-binding 1.7-mL tube, one tube per library. Since these are the final libraries, 
    label the tubes well: include the date, genomics technique (e.g., "C&T lib"), and sample identification on a sticker on the cap. Store at –20°C. 
    

Perform in-house QC
-------------------

q. Quantify the resulting libraries with the `NEB Library Quant kit </_static/files/neb_library_quant_kit_manual.pdf>`__ (protocol TODO).
r. Run a sample of each library on the Fragment Analyzer in the BMC (protocol TODO).

Pool libraries for sequencing
-----------------------------

s. TODO
