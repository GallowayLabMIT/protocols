=========
CUT&Tag
=========

.. important::

   This protocol is modified from the `Active Motif protocol </_static/files/cut_and_tagIT_express_manual.pdf>`__.
   Our modifications typically make the process more efficient or are gentler on the cells. Additionally, the final
   PCR step diverges, as we perform a :doc:`test PCR </protocols/biochem_and_analytics/genomics_sequencing/test_pcrs>`
   first.
   
   It follows the same numbering as the linked protocol for easy comparison, e.g. step 1 in this protocol maps to
   step 1 of the actual protocol. You may want to print out both.

We buy the following kits from ActiveMotif:

- `CUT&Tag-IT Express <https://www.activemotif.com/catalog/1395/cut-tag-it-express>`__.
- `CUT&Tag Spike-in nuclei <https://www.activemotif.com/catalog/1377/cut-tag-spike-in>`__. Pick the spike-in control kit
  that **matches the secondary antibody** you will be using for the marks of interest. Active Motif sells
  anti-rabbit and anti-mouse.

Background
==========
CUT&Tag relies on a protein-A/protein-G conjugated Tn5 to tagment DNA
based on primary/secondary antibody binding. The advantage
of this is a higher signal-to-noise ratio, relative to CUT&RUN, which
relies on protein-A conjugated MNase, CUT&Tag libraries are directly tagmented
wtih PCR-compatible adapters, which allows you to skip the library ligation
step.

However, Tn5 has a related accessibility bias (like the bias you are measuring
in ATAC-seq!). CUT&Tag buffers do the tagmentation in a higher-salt buffer
than ATAC-seq, which increases electrostatic screening and thus disrupts
nucleosome and chromatin interactions, which lessens the accessibility signal.

This protocol is most sanely split over three days.

- Day 1: cell counting, bead binding, primary antibody binding overnight. This step is fairly short: 32 samples took ~4 hours. 
- Day 2: secondary antibody binding, tagmentation, DNA cleanup, test PCR. This is a very long day! Nearly ~11 hours for 32 samples.
- Day 3: PCR amplification, library quantification.

The overall days are split up:


Experimental setup
==================

Active Motif does *not* recommend using an IgG control antibody condition. Instead,
use a common histone mark (H3K27me3, H3K27ac) as your control. If your experiment
already calls for one of these histone marks, then you do not need an explicit
separate control.

Select primary antibodies that have the same species, either rabbit or mouse. Then,
order a spike-in nuclei kit from Active Motif with the matching species. 


.. warning:: 

    Do **NOT** store Concanavalin A beads below 4C. These beads are 
    extremely sensitive to freezing and should never be stored below 4C.

    Some protocols tell you not to vortex ConA beads, to avoid shearing
    the ConA from the beads, so we avoid vortexing the beads in the initial
    steps.
   

Preparation (N days before)
============================
- Seed cells and split your conditions so that you have a bit in excess
  of **500k cells per antibody** you wish to use. For example, if you have
  four antibodies, seed cells such that you have more than 2M cells.
- Check the Concanavalin A (ConA) beads for aggregation. To do so, after pipetting
  to resuspend the beads, dilute 1 uL of beads with 9 uL of 0.1x TE (or water).
  You should not see large clumps of beads with the hemocytometer. If so, you
  should order more. If you got the beads from Active Motif, contact customer support:
  they will ship you new beads overnight for free.

Day 0
=====
- Check for ConA bead aggregation if you did not previously. This is your last chance to order beads!
  Cell Signaling Technologies sells ConA beads and will overnight ship to you.

Day 1
======

Prepare buffers
---------------
.. note::

   These steps are not numbered in the original protocol. We use letters for steps
   that do not appear in the original protocol.

a. Defrost Protease Inhibitor Cocktail on ice and 5% Digitonin at room temperature.
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

Prepare / activate ConA beads
-----------------------------
.. note::
   
   The original protocol suggests you do this before preparing the cells, but does not order the
   protocol in this way.

6. Resuspend the ConA beads via trituration, and aliquot 10 µL per sample, up to batches of 80 µL per low-binding 1.7 mL tube.
7. Place the tubes on the magnet. Once clear, remove the supernatant.
8. Remove from the magnet and resuspend in 100 µL of activation / binding buffer per sample. Incubate at room temperature for 10-15 minutes.
9. Place on the magnet and remove the supernatant once clear.

c. If using the Cell Signaling Technology ConA beads, repeat the 100 µL wash step, as CST provides enough reagents
   for two washes.

10. Remove from the magnet and resuspend in 10 µL of activation / binding buffer per sample. Aliquot each 10 µL
    sample of beads into fresh PCR tubes.

Prepare cells
-------------

1. Disassociate your target cells **without using trypsin** or other enzymatic methods.
   For iPSCs, this means using Gentle Cell Disassociation Reagent. Resuspend your cells in some FBS-containing media\
   (for iPSCs: DMEM/F12 + 1% FBS) and count your cells, using Trypan Blue.

d. After counting, take spike-in nuclei out of the -80C freezer and defrost on ice. Combine enough nuclei
   for your required reactions together into a single tube for better reproducibility.

   .. note::
      
      We want the spike-in reads to be 5-10% of the overall sequencing reads. Use a spike-in nuclei : cell ratio
      of 1:25 for common marks, increasing to 1:10 for rare marks. For H3K27me3, H3K27ac, H3K4me3, we used 20,000
      spike-in nuclei to 500,000 cells.

e. Calculate the volume of cells needed to reach 500k cells per CUT&Tag reaction.
   If you are running multiple antibodies per sample, you can "master mix"
   and combine conditions together (e.g. calculate for 2M cells if you have 4 antibodies).

   .. note:: 

      If you do not have 500k cells per reaction, you can resuspend fewer cells.
      However, you need to adjust the amount of spike-in nuclei for each reaction!
      It is very important that the cell-to-spike-in-nuclei ratio is constant.

      For example, if most of your conditions have 500k cells, but one only has 400k cells,
      then you should spin down the entire 400k while only adding in 4/5th of the amount of spike-in
      nuclei. Normally, we use 40 uL of spike-in nuclei per 500k cells, so this would
      mean reducing this to 32 uL of spike-in nuclei.

2. Aliquot 500k cells per reaction into a low-binding 1.7 mL tube.

f. Add spike-in nuclei to the cell aliquots.

4. Centrifuge cells for 3 minutes at 600xg at 4°C and remoe the supernatant.
5. Resuspend cells in 100 µL Dig-Wash + PIC.

11. Add washed, resuspended cells to the Con A beads prepared in PCR tubes. Resuspend via trituration
    and incubate on a Nutator for 10 minutes at room temperature.

Primary Antibody Binding
------------------------
g. Prepare Complete Antibody Buffer plus the chosen antibodies on ice. Prepare slight excess, and do one master mix
   per antibody type (e.g. one for H3K27me3, one for Pol II, ...):
   
   **Complete Antibody Buffer plus Antibodies (52 µL / condition)**

   ============================  ======================================
   Component                     Volume
   ============================  ======================================
   Complete Antibody Buffer      50 µL
   Target antibody                1 µL (or manufacturer recommendation)
   Spike-in control antibody      1 µL
   ============================  ======================================

12.  Remove tubes from the Nutator and briefly spin down. Place the tubes on the magnet and discard the supernatant.
13.  Resuspend the beads/cells using 50 µL of cold Complete Antibody Buffer plus Antibodies. Pipette to mix

15. Place samples on a Nutator overnight at 4°C.

Day 2
=====

Buffer preparation
------------------

.. note::

   The proposed volume in the Active Motif documentation is greatly in excess! The volumes
   listed here are exactly the volumes you need, so you should make some excess, but not to the
   extent that the official protocol does.

h. Defrost Protease Inhibitor Cocktail on ice and 5% Digitonin at room temperature.
i. Prepare Complete Tagmentation Buffer, Complete Dig-300 Buffer, and Complete Dig-Wash buffer per condition. Make some excess.
   
   .. note::

      Some volumes are small; if you are only doing 1 sample, scale up just for the purpose of pipetting no less than 0.5 µL.
   
   **Complete Tagmentation Buffer (40 µL/sample)**

   ============================= ========    ==================
   Component                     Volume      Volume / 8 samples
   ============================= ========    ==================
   Tagmentation Buffer            40 µL      320 µL
   Protease Inhibitor Cocktail   0.4 µL      3.2 µL
   5% Digitonin                  0.08 µL     0.64 µL
   ============================= ========    ==================

   **Complete Dig-300 Buffer (500 µL / sample)**

   ============================  ======
   Component                     Volume
   ============================  ======
   Dig-300 Buffer                500 µL
   Protease Inhibitor Cocktail     5 µL
   5% Digitonin                    1 µL
   ============================  ======

   **Complete Dig-Wash Buffer (700 µL / sample)**

   ============================= ======
   Component                     Volume
   ============================= ======
   Dig-wash Buffer               700 µL
   Protease Inhibitor Cocktail     7 µL
   5% Digitonin                    7 µL
   ============================= ======

Bind Secondary Antibody
-----------------------

16. Remove tubes from the Nutator, spin to collect tubes at the bottom. Place on the magnet and remove and discard the supernatant.
17. Wash the beads by adding 200 µL of Complete Dig-Wash Buffer, resuspending the beads, transferring them to a fresh PCR tube, and placing back on the magnet.
18. Prepare a secondary antibody master mix:

    **Secondary Master Mix (100 µL/sample)**

    ============================ ======
    Component                    Volume
    ============================ ======
    Complete Dig-Wash Buffer     100 µL
    Secondary antibody             1 µL
    ============================ ======

    Remove the supernatant from the beads. Add 100 µL of Secondary Master Mix and pipette to resuspend the beads.
19. Place the tubes on a Nutator at room temperature for 15 minutes.
20. Pipette gently to resuspend beads, then place back on the Nutator for another 15 minutes.
21. Remove the tubes from the Nutator and spin the tubes briefly.
22. Place the tubes on the magnet, then remove and discard the supernatant.
23. Add 200 µL of Complete Dig-Wash Buffer, pipetting to mix, then place back on the magnet.
24. Repeat the wash step by removing the supernatant, adding Complete Dig-Wash buffer, mixing, and placing back on the magnet.

Bind CUT&Tag-IT Assembled pA-Tn5 Transposomes
---------------------------------------------
25. Dilute CUT&Tag-IT Assembled pA-Tn5 Transposomes in Complete Dig-300 Buffer. Make very slight excess.
    
    **Transposomes Master Mix (101 µL / sample)**

    ==============================  ======
    Component                       Volume
    ==============================  ======
    Complete Dig-300 Buffer         100 µL
    Assembled pA-Tn5 Transposomes   1 µL
    ==============================  ======
26. Remove and discard the supernatant.
27. Add 100 µL of Transposomes Master Mix and pipette to resuspend the beads.
28. Place on a Nutator at room temperature for 15 minutes.
29. Pipette gently to resuspend beads, then place back on the Nutator for another 15 minutes.
30. Remove tubes from the Nutator and spin briefly.
31. Place the tubes on the magnet, then remove and discard the supernatant.
32. Add 200 µL of Complete Dig-300 Buffer and gently pipette to resuspend the beads.
33. Repeat the wash step by placing on the magnet, discarding the supernatant, adding Complete Dig-300 Buffer, and resuspending.

Tagmentation
------------
34. Place the tubes on the magnet and discard the supernatant.
35. Add 40 µL of Complete Tagmentation Buffer. Gently pipette to resuspend the beads.
36. Incubate at 37°C in a thermocycler for one hour.

j. Thaw Glycogen at room temperature and Proteinase K on ice.
k. Prepare Complete Tn5 Release solution on ice. Vortex the Tn5 Release Solution for at least 30 seconds.
   
   **Complete Tn5 Release Solution (40 µL / sample)**

   ======================  =======
   Component               Volume
   ======================  =======
   Tn5 Release Solution    40 µL
   Glycogen                0.8 µL
   Proteinase K            0.8 µL
   ======================  =======

DNA Extraction
--------------

37. Place the tubes on the magnet and discard the supernatant. Vortex the Complete Tn5 Release Solution
38. Add 40 µL of Complete Tn5 Release Solution per sample.
39. Mix well via pipetting.
    
    .. note::

      It is typical for the beads to form a large clump during the incubation.

40. Incubate the reaction for 1 hour at 55°C in a thermocycler, with the heated lid set to 65°C

   .. note::

      This is the ``C&T/tag_stop`` thermocycler protocol.

41. Add 40 µL of DEPC-treated water to each sample and mix well via pipetting. Place back at 55°C for 5 minutes.

l. Pipette well until the bead/cell clump is broken up. Pipette under the max volume to avoid air bubbles. Add 100 µL of DNA Purification Binding Buffer (60% IPA).
   to each sample to help with homogenization of the bead clump. Place the samples on the magnet and ensure the beads pellet well.

44. Vortex the silica beads well, at least 30 seconds.
45. Pipette 25 µL of silica beads per sample to fresh PCR tubes. Place on a magnet.

m. Remove the supernatant from the beads, add 35 µL of DNA Purification Binding Buffer, remove from the magnet and mix well.

48. Remove ~180 µL total supernatant from the samples while still on the magnet, adding it to the silica bead tubes. Pipette well to mix and ijncubate at room temperature for 5 miutes.

    .. warning::
      It is important that as few magnetic beads as possible are transferred! You don't need to transfer all 180 µL
      of supernatant if it comes with some beads.

49. Place the tubes on the magnet and remove and discard the supernatant.
50. Add 200 µL of DNA Purification Wash Buffer, remove from the magnet, and pipette to resuspend.
51. Place tubes back on the magnet and remove and discard the supernatant.
52. Repeat the wash step by adding Wash buffer, pipetting to resuspend, placing back on the magnet, and removing the supernatant.
53. Leave the PCR tube caps open, and use a 10 µL pipette to remove any remaining wash buffer. Air dry until the shiny-to-matte transition happens, not more than 5 minutes.
54. Add 24 µL of DNA Purification Elution Buffer and resuspend the beads off the magnet. Incubate for 1 minute.
55. Place tubes on the magnet and transfer 23 µL to fresh PCR tubes.
   
    .. note::
      This is a good stopping point if needed.

n. Follow the :doc:`Test PCR protocol </protocols/biochem_and_analytics/genomics_sequencing/test_pcrs>` with the following parameters:

     - Use 3 µL of the 23 µL elution for test PCR purposes. 20 µL will be used in the real PCR, so :math:`\log_2(15/ 0.7) = 4.84` delta cycles.
     - Use the ``tagmentation_fwd`` and ``tagmentation_rev`` primers.
     - Target 100 ng. Perform 16/19/22 test cycles.
     - The final cycle count should be around 12 cycles.

56. Using the optimal cycle counts from the test PCR, setup indexed PCR reactions:
    
    
    =======================================  ======
    Component                                Volume
    =======================================  ======
    2x NEBNext Ultra II Q5 Master Mix        25 µL
    i5 indexed primer (Nextera compatible)   1 µL
    i7 indexed primer (Nextera compatible)   1 µL
    Water                                    3 µL
    Tagmented DNA sample                     20 µL
    =======================================  ======

57.  Perform PCRs with the following program:

     ==========  =============  ==============================================
     Temp (°C)   Time (MM:SS)   Description
     ==========  =============  ==============================================
     72          5:00           Polymerase activation
     98          0:30           Initial denaturation
     --          --             Optimal number of cycles
     98          0:10           Denaturation
     65          1:15           Extension
     --          --             cycle end
     4           Hold           Final hold
     ==========  =============  ==============================================

o. Vortex SPRI beads well, at least 30 seconds. Prepare fresh 80% ethanol for the bead wash steps, 400 µL per sample.

58. Perform a double-sided SPRI bead clean-up. Add 25 µL SPRI (0.5x) to each sample, pipette to mix, and incubate at room temperature for 5 minutes.
59. Place tubes on the magnet and move the supernatant to new PCR tubes. Discard the beads.
60. Add 35 µL of SPRI beads to the sample (0.7x sample volume, for a 1.2X final ratio), mix well via pipetting, and incubate at room temperature for 5 minutes.
61. Place tubes on the magnet, remove and discard the supernatant. Wash the beads twice with 200 µL of 80% ethanol, without disturbing the beads
    or removing the beads from the magnet.
62. Allow the beads to dry until the shiny-to-matte transition happens, not longer than 5 minutes. Add 22 µL of DNA Purification Elution buffer, pipette to mix,
    let sit at room temperature for 1 minute.
63. Place the tubes back on the magnet, and transfer the 22 µL to a fresh low-binding 1.7 mL tube. The libraries can be stored at -20°C.

p. Quantify the resulting libraries both with the `NEB Library Quant kit </_static/files/neb_library_quant_kit_manual.pdf>`__ and by submitting a sample to the Fragment Analyzer in the BMC.
