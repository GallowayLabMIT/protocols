=======================
Region-Capture Micro-C
=======================

RCMC is a complicated protocol! Don't let this discourage you; there are plenty of intermediate QC steps
you can do along the way to ensure that you are proceeding correctly through the process.

The big-picture protocol is:

- Cross-link and fix cells, which preserves the chromatin contacts.
- Run a test MNase digestion to select an optimal MNase concentration. This must be done fresh every time!
- Run the real MNase digestion. Then, cross-ligate fragments together and do DNA manipulations to biotinylate fragments.
- Extract and purify religated fragments. Perform library prep and PCR on the fragments.
- Region-capture the resulting library. PCR the region-captured library again for sequencing.

Protocol numbers will be sequentially numbered throughout the entire procedure, for easy referencing.

The overall days are split up:

.. contents::
    :depth: 1
    :local:

Day -n: Buffer preparation
--------------------------


Shared genomics buffers
^^^^^^^^^^^^^^^^^^^^^^^
- Make sure there is sufficient amounts of the following :doc:`shared genomics buffers </protocols/biochem_and_analytics/genomics_sequencing/shared_genomics_buffers>`:
  
  - 5M NaCl
  - 1M Tris-HCl, pH 7.5
  - 0.5M EDTA, pH 8.0
  - 10% SDS
  - 1M MgCl2
  - 2.5M CaCl2

.. _rcmc_specific_buffers:

RCMC-specific buffers
^^^^^^^^^^^^^^^^^^^^^^

**10 mM Tris, 10 mM NaCl (1 mL)**

======================  =======
Component               Volume
======================  =======
1 M Tris-HCl pH 7.5     10 µL
5 M NaCl                 2 µL
DEPC-treated water      988 µL
======================  =======

**2xBW (50 mL)**

======================  ========
Component               Volume
======================  ========
Water (Elga or DEPC)    29.4 mL
5 M NaCl                20 mL
1 M Tris-HCl pH 7.5     500 µL
0.5M EDTA pH 8.0        100 µL
0.2 µm sterile filter
======================  ========


**1xTBW (50 mL)**

=====================   ======
Component               Volume
=====================   ======
Water (Elga or DEPC)    25 mL
2xBW                    25 mL
100% Tween-20           50 µL
0.2 µm sterile filter
=====================   ======

**MB1 (50 mL)**

=================== ==============  ========
Component           Concentration   Volume
=================== ==============  ========
5 M NaCl            50 mM           0.5 mL
1 M Tris-HCl pH 7.5 10 mM           0.5 mL
1 M MgCl2            5 mM           0.25 mL
2.5 M CaCl2          1 mM           20 µL
DEPC-treated water                  48.7 mL
=================== ==============  ========

**MB2 (50 mL)**

=================== ==============  ========
Component           Concentration   Volume
=================== ==============  ========
5 M NaCl            50 mM           0.5 mL
1 M Tris-HCl pH 7.5 10 mM           0.5 mL
1 M MgCl2           10 mM           0.5 mL
DEPC-treated water                  48.5 mL
=================== ==============  ========

**MB3 (50 mL)**

=================== ==============  ========
Component           Concentration   Volume
=================== ==============  ========
1 M Tris-HCl pH 7.5 50 mM           2.5 mL
1 M MgCl2           10 mM           0.5 mL
DEPC-treated water                  47 mL
=================== ==============  ========

**20 mg/mL BSA (prepare fresh each day)**

=================== ======
Component           Amount
=================== ======
BSA                 20 mg
DEPC-treated water  1 mL
=================== ======

MNase resuspension and storage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
We want to avoid temperature cycles of the MNase! To prevent temperature cycles, we make
aliquots of 20U / µL MNase.

1. Based on the documented units of lyophilized MNase (on the packing slip), prepare and resuspend the MNase to 40U / µL in the following buffer:

   **2xMNase storage buffer (10 mL)**

   ======================  ==============  =======
   Component               Concentration   Volume
   ======================  ==============  =======
   1M Tris-HCl, pH 7.5     20 mM           200 µL
   5 M NaCl                100 mM          200 µL
   500 mM EDTA, pH 8.0      2 mM            40 µL
   DEPC-treated water                      9.56 mL
   ======================  ==============  =======

2. Add an equal volume of 100% glycerol to reach 20U / µL. Mix well and aliquot, store in a **reliable** -80°C freezer.

Protease inhibitor cocktail
^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Dissolve one Protease Inhibitor Cocktail tablet in 500 µL of MB1. The protease inhibitor cocktail will
  not fully dissolve, but aliquot the resulting slurry. This is your 100x PIC solution.


Day 1: MNase titration
----------------------

Buffer preparation
^^^^^^^^^^^^^^^^^^

Cell harvest and fixation
^^^^^^^^^^^^^^^^^^^^^^^^^
.. note::

    It is convenient to have someone helping you on Day 1.

    In particular, one person can harvest and wash the cells. Then,
    while one person is counting, the other person can prepare the crosslinking buffers.


1. Remove enough DSG from the refrigerator and allow it to come to room temperature before starting.
   Each 50 mg of DSG is enough for 50 mL of solution (50M cells).
2. Prepare sufficent 100x BSA (200 µg / mL) to aid to help cells pellet and limit cell losses.
3. Collect cells following normal passaging conditions. Collect into and wash in the same 50 mL tube. After collecting and spinning down the cells,
   perform a PBS wash before resuspending and counting cells. Spike in 100x BSA prior to spinning down the cells in the PBS wash.
4. Count the cells. We want as high cell counts as possible; it is good to crosslink and fix as many
   cells as possible instead of throwing away cells at this step.
5. Resuspend each vial of DSG in 500 µL of DMSO to make 100x DSG Stock Solution.
6. Dilute enough DSG Stock Solution in PBS for fixation of all cells: per 10M cells, 100 µL Stock Solution diluted to 10 mL.
7. In a fumehood, resuspend each cell pellet to 1 million cells per mL. Use a P-1000 to do the initial resuspension,
   then use a serological pipette to add the rest of the fixation solution.
8. Incubate at room temperature on a plate shaker for 35 minutes.
9. While waiting, cool a centrifuge to 4°C and place sufficient PBS on ice.

   .. note::
        
        The following steps need to be done in a timely manner. It is helpful to have someone
        helping you if you have more than a 2-3 conditions. Precompute volumes using a spreadsheet;
        all volumes can be calculated from the cell-count per condition.

   .. warning::

        Collect all of the following wash steps as formaldehyde waste until step the cells are resuspended prior to aliquoting.

10. In a fumehood, add 1 mL of fresh 16% formaldehyde per 15 mL of cells (15M cells), in a dropwise but relatively rapid manner.
    Use the 10mL and 1mL ampules either opened fresh or opened and stored in the last ~48 hours.
11. Incubate for 10 minutes at room temperature on the plate shaker.
12. Add pH 7.5 Tris dropwise to a final concentration of 0.375M. This is 3.45 mL of 2M Tris per 15M cells.
13. Incubate for 5 minutes at room temperature. Spike in 100x BSA prior to spinning at 400 xg at 4°C for 5 minutes.
14. Remove the supernatant, wash with cold PBS at a concentration of 1M cells / mL. Spike in 100x BSA prior to spinning at 400 xg at 4°C for 5 minutes.
15. Resuspend the cell pellet to 20M cells / mL, in cold PBS with spiked-in 100x BSA. Make the desired aliquots of these cells.
    For the MNase titration, you will need at least one aliquot of 5M cells. If processing the rest of the cells, in the same reaction,
    you can freeze down a "large" aliquot.

    .. note::

        For smaller aliquots, make sure you use **low-binding** 1.7 mL tubes instead of normal 1.7 mL tubes.
16. Spin down aliquots, aspirate the supernatant and snap-freeze the cell pellets in liquid nitrogen. Store at -80°C.
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
It is very important that this titration is performed every single time when running RCMC!
This controls for batch-to-batch differences in fixation, snap freezing, and MNase activity.

For each cell type (iPS11, Leiden iPSCs, 293Ts, reprogrammed neurons), you should perform the titration. It is not necessary
to have a titration per genetic edit.

You will need a single 5M cell aliquot to perform the titration on.

.. note::

    At this point, the cell pellets are fixed. All waste from the titration can be collected and sink-disposed.

    Use low-binding 1.7 mL tubes for all steps requiring this tube size.

17.  Prepare fresh Complete MB1 and place on ice. For the standard 5M cell titration, you need 1.5 mL of this buffer,
     but this can be scaled up or down.
    
     **Complete MB1 (2 mL)**:
    
     ======================  ========
     Component               Volume
     ======================  ========
     MB1                     1940 µL
     10% NP-40 alternative   40 µL
     100x PIC (in MB1)       20 µL
     ======================  ========

18. Thaw a 5M cell pellet on ice and resuspend in 500 µL of Complete MB1 (1M cells per 100 µL).
19. Incubate for 20 minutes on ice. While waiting, unfreeze a fresh MNase aliquot on ice.

    .. note::
        You can technically reuse MNase aliquots 2-3 times, but MNase is cheap compared to redoing an experiment 
        because the aliquot you used went bad.


        If performing the MNase titration and the "real" digestion on the same day, you can pool multiple
        unfrozen aliquot(s) on ice and use them for the real digestion.
        You will need roughly 0.5 µL of MNase per million cells, so unfreeze accordingly.

20. Centrifuge at 1750 xg for 5 minutes at 4°C. 
21. Remove the supernatant, leaving ~10-20 µL in the tube.
22. Wash the nuclei pellet with 500 µL of Complete MB1. Centrifuge at 1750 xg for 5 minutes at 4°C.
23. Removing as much supernatant as possible, resuspend the cell pellet in 500 µL of Complete MB1 (1M cells per 100 µL).
24. Split the cells into 5 low-binding 1.7 mL tubes, with 100 µL of cells each, keeping them on ice.
25. Decide on your titration series. A common series is 2U, 4U, 7U, 12U, and 20U. For the small volumes,
    prepare a 1:10 dilution of the 20U / µL stock solution in 10 mM Tris-HCl, pH 7.5.

.. important::

    Use the **exact same** digestion procedure here and in the "real" digestion! This means 
    as close to 20 minutes as possible, working carefully but rapidly.

26. Add MNase to each 1M cell aliquot. Briefly vortex the tubes to ensure uniform MNase distribution,
    then incubate at 20 min at 37°C with shaking at 1000 rpm.
27. Transfer the digested nuclei to ice and add 0.8 µL of 500 mM EGTA. to reach a final concentration of 4 mM EGTA.
28. Briefly vortex the tube, then incubate for 10 minutes at 65°C with no shaking (but using the Thermomixer).
29. While waiting on the inactivation, prepare 0.9 mL of Reverse Crosslinking Solution **at room temperature and outside of the genomics hood**
    because of the RNase A. The SDS will precipitate out if you put it on ice.

    Reverse Crosslinking Solution (0.9 mL):

    ======================= ======
    Component               Volume
    ======================= ======
    1x TE                   720 µL
    10% SDS                 90 µL
    5M NaCl                 36 µL
    20 mg/mL Proteinase K   45 µL
    10 mg/mL RNaseA         9 µL
    ======================= ======

30. Centrifuge at 1750 xg for 5 minutes at 4°C.
31. Discard the supernatant and resuspend each pellet in 150 µL of Reverse Crosslinking Solution.
32. Reverse cross-links for a minimum of 2 hours to overnight at 65°C with 1000 rpm shaking. This step does not 
    noticeably improve after 2 hours, you just have the option to stop.
33. Clean up the resulting DNA fragments using the genomics-only Monarch DNA cleanup kit. Use a 5:1 ratio of binding buffer : sample. Elute in 25 µL.
34. Quantify the DNA via Nanodrop. Load 1-5 µg of sample per thin-comb well using Orange Loading Dye onto a 1.5% agorase gel. Run at 100V for 30 minutes, then image.
35. Select the MNase to cell ratio that is optimally digested: 80-90% monomer, 10-20% dimer, faint trimer band, no tetramer.


Day 1 continued: post-titration digestion and end repair
--------------------------------------------------------

Buffer preparation
^^^^^^^^^^^^^^^^^^
36. Prepare sufficient 20 mg/mL BSA if needed. You don't need super large amounts: 1 mL should be sufficient.
37. Prepare enough Complete MB1, MB2, and MB3 on ice for all of your samples.
    You will need 3 mL of Complete MB1 per 10M cells:

    **Complete MB1 (10/50 mL)**:

    ======================  ================    ================
    Component               Volume per 10 mL    Volume per 50 mL
    ======================  ================    ================
    MB1                     9.7 mL              48.5 mL
    10% NP-40 alternative   200 µL              1000 µL
    100x PIC (in MB1)       100 µL               500 µL
    ======================  ================    ================

    You will also need 2 mL of Complete MB2 per sample (not per cell count):

    **Complete MB2 (10 mL)**:
    
    =============== ======
    Component       Volume
    =============== ======
    MB2             10 mL
    20 mg/mL BSA    50 µL
    =============== ======

    and 1 mL of Complete MB3 per sample (not per cell count):

    **Complete MB3 (5 mL)**:

    =============== ======
    Component       Volume
    =============== ======
    MB3             5 mL
    20 mg/mL BSA    25 µL
    =============== ======
    
    Then, prepare fresh 100 mM DTT. Prepare 1 mL of this buffer; do not go smaller because our balances have limited precision.

    **100 mM DTT (1 mL)**:

    ======================= =========
    Component               Amount
    ======================= =========
    DTT                     0.01543 g
    1 M  HEPES pH 7.5       25 µL
    DEPC-treated water      975 µL
    ======================= =========

38. On ice, start defrosting NEBuffer 2.1 and ATP for the end labeling and Biotin-dATP, Biotin-dCTP, dTTP, dGTP, and T4 DNA ligase buffer for the end labeling step.

MNase digestion
^^^^^^^^^^^^^^^
39. Thaw the cell pellets on ice and resuspend in Complete MB1 at a concentration of 1M cells per 100 µL.
40. Incubate for 20 minutes on ice. If you did not already unfreeze fresh MNase aliquots, unfreeze enough fresh
    aliquots for all of your cells given the titration ratio.
41. Centrifuge at 1750 xg for 5 minutes at 4°C. 
42. Remove the supernatant, leaving ~10-20 µL in the tube.
43. Wash the nuclei pellet with complete MB1, at a concentration of 1M cells per 100 µL. Centrifuge at 1750 xg for 5 minutes at 4°C.
44. Removing as much supernatant as possible, resuspend the cell pellet in Complete MB1 (1M cells per 100 µL).
45. Using the optimal ratio of MNase to cells, add MNase to each tube. Briefly vortex the tubes to ensure uniform MNase distribution,
    then incubate at 20 min at 37°C with shaking at 1000 rpm.
46. Transfer the digested nuclei to ice and add 500 mM EGTA to a final concentration of 4 mM (0.8 µL per 100 µL / 1M cells).
47. Briefly vortex the tube, then incubate for 10 minutes at 65°C with no shaking (but using the Thermomixer).
48. Centrifuge at 1750 xg for 5 minutes at 4°C. Wash the nuclei pellet twice in 1 mL of cold Complete MB2.

Fragment end repair
^^^^^^^^^^^^^^^^^^^

49. Prepare a master mix for the end-chewing step on ice. You can scale this linearly up with cell count; if you have fewer than
    2.5M cells, do not go below 45 µL of master mix per condition. Strictly add the components in the order listed.

    **End Chewing Master Mix (90 µL / 5M cells)**

    =================== ======
    Component           Volume
    =================== ======
    DEPC-treated water  50 µL
    10X NEBuffer 2.1    10 µL
    10 mM ATP           20 µL
    100 mM DTT           5 µL
    10U / µL T4 PNK      5 µL
    =================== ======

    .. note::

        It is easiest to perform the math for the master mix by
        multiplying these numbers by (N+1), for N the number of samples,
        instead of adding 5 or 10%.

50. After removing the Complete MB2 supernatant from each sample, resuspend the cells in 90 µL of End Chewing Master Mix per 5M cells.
51. Incubate for 15 minutes at 37°C, with 1000 rpm shaking.
52. Add 10 µL of 5U/µL Klenow Fragment to each sample. Incubate again for 15 minutes at 37°C, with 1000 rpm shaking.

End labeling
^^^^^^^^^^^^
53. While waiting on the incubation, prepare a master mix for end labeling on ice. As with the end chewing, do not scale below 45 µL per condition; if you have
    fewer cells, it is fine if they are more dilute.

    **End Labeling Master Mix (50 µL / 5M cells)**
    
    =========================== ========
    Component                   Volume
    =========================== ========
    DEPC-treated water          22.75 µL
    1 mM Biotin-dATP               10 µL
    1 mM Biotin-dCTP               10 µL
    10 mM dTTP                      1 µL
    10 mM dGTP                      1 µL
    10X T4 DNA ligase buffer        5 µL
    20 mg/mL BSA                 0.25 µL
    =========================== ========

54. Add 50 µL of End Labeling Master Mix to each sample, pipetting to mix.
55. Incubate for 45 minutes at 25°C with interval mixing (1000 rpm for 1 minutes, 3 minutes still, repeat).
56. Add 500 mM EDTA to a final concentration of 30 mM (9 µL per 150 µL / 5M cells).
57. Briefly vortex, then incubate at 65°C for 20 minutes, without shaking.

.. warning:: 
    
    Be careful when removing the supernatant in the following two steps; the pellet will be very loose!

58. Centrifuge at 1750 xg for 5 minutes at 4°C and carefully remove the supernatant.
59. Wash once with 1 mL of cold Complete MB3. Centrifuge at 1750 xg for 5 minutes at 4°C.

Proximity ligation
^^^^^^^^^^^^^^^^^^
60. Prepare enough Proximity Ligation Master Mix on ice:
    
    **Proximity Ligation Master Mix (500 µL / 5M cells)**

    =========================== ========
    Component                   Volume
    =========================== ========
    DEPC-treated water          422.5 µL
    10X T4 DNA ligase buffer       50 µL
    20 mg/mL BSA                  2.5 µL
    400U/µL T4 DNA ligase          25 µL
    =========================== ========

61. Carefully remove the supernatant and resuspend each sample in 500 µL of Proximity Ligation Master Mix per 5M cells.
62. Incubate for at least 2.5 hours (but normally overnight) at room temperature on a nutator.


Day 2: Reverse crosslinking
---------------------------
.. time:: 1 hour in-lab

Now that we have properly biotin-labeled proximity-ligated fragments, the reverse crosslinking step reverses
the fixation process. The solution should go from cloudy to clear as this process happens, and samples
should be fully clear by the following day.

63. Defrost NEBuffer 1 on ice.
64. Centrifuge the samples at 3000 xg for 5 minutes at 4°C.
65. Prepare enough Biotin Removal Master Mix on ice.
    As before, do not scale down volumes by more than half if you have less than 2.5M cells.

    **Biotin Removal Master Mix (200 µL / 5M cells)**

    ========================== ======
    Component                  Volume
    ========================== ======
    DEPC-treated water         170 µL
    10X NEBuffer 1              20 µL
    100 U / µL Exonuclease III  10 µL
    ========================== ======

66. Resupend the nuclei pellet in 200 µL of Biotin Removal Master Mix per 5M cells.
67. Incubate at 37°C for 15 minutes with interval mixing (1000 rpm for 1 minute, 3 minute still, repeat).
68. Prepare Reverse Crosslinking Master Mix at room temperature **outside of the genomics hood**.
    Do not scale volumes down by more than half.

    **Reverse Crosslinking Master Mix (39 µL / 5M cells)**

    ======================  ========
    Component               Volume
    ======================  ========
    5M NaCl                 10.4 µL
    20 mg/mL Proteinase K   26 µL
    10 mg/mL RNase A        2.6 µL
    ======================  ========

69.  **Outside of the genomics hood**, add 39 µL of Reverse Crosslinking Master Mix per 5M cells to the 200 µL / 5M samples. Mix via pipetting.
70. **Outside of the genomics hood**, add 26 µL of 10% SDS per 5M cells. This must be spiked in! Otherwise you would inactivate the Proteinase K.
    The final total volume is 265 µL / 5M cells.
71. Incubate at 65°C overnight in the thermomixer, without shaking.

Day 3: Fragment cleanup and library prep
----------------------------------------

Buffer preparation
^^^^^^^^^^^^^^^^^^
72. Ensure there is enough 2xBW and 1xTBW. These have very long shelf lives and were previously prepared.
    You need 3 mL of 1xTBW per sample and 150 µL 2xBW per sample.
73. Take out the T1 streptavidin beads and let them equilibrate to room temperature.
74. Defrost End Prep Reaction Buffer, Ligation Master Mix, and Ligation Enhancer from the NEBNext Ultra II DNA Library Prep Kit on ice.

Bead cleanup
^^^^^^^^^^^^

75.  Clean up each sample following the NEB Monarch Clean & Concentrator kit. Use miniprep (25 µg capacity) columns
     instead of 5 µg columns. Use 6x binding buffer and elute twice with 40 µL of warm elution buffer (total of 80 µL).

     .. note::

         Use the Thermomixer to heat up the elution buffer.

76.  Estimate the concentration of the library using the Nanodrop.
77.  Perform a double-sided SPRISelect cleanup to select for dinucleosomes. Use a 0.7x right side and 0.85x left side selection and elute in 32 µL 0.1xTE.

    a. Vortex the room-temperature SPRI beads until well mixed, at least 30 seconds.
    b. To each 80 µL sample, add 0.7x of the initial volume (56 µL) of SPRI beads. Mix will by pipetting and incubate at room temperature for 1 minute.
    c. Place the tubes on the magnet and separate the beads. Move the **supernatant** to a new tube.
    d. Add 0.15x of the initial volume (12 µL) of SPRI beads to the supernatant. Mix well by pipetting and  incubate at room temperature for 1 minute.
    e. Place the tubes on the magnet and separate the beads. **Remove** the supernatant.
    f. With the tubes still on the magnet, add 200 µL of **freshly prepared** 80% ethanol, incubate for 30 seconds, then remove the ethanol. Repeat this wash step
    g. Use a P10 pipette to remove residual ethanol, while the tubes are still on the magnet.
    h. Wait for the beads to dry, not longer than 5 minutes. The beads should go from "shiny" to "matte".
    i. Elute by adding 32 µL 0.1xTE. Take the tubes off the magnet and mix well. After a 1 minute incubation, place back on the magnet until the beads are pelleted.
    j. Move the 32 µL samples to new PCR tubes.

78. Quantify the concentration of your samples with Qubit. We are expecting at least 10 ng total.  

    a. Dilute the Qubit light-sensitive reagent 1:200 in Qubit dilution buffer to make working buffer. For 8 samples + 2 standards, this is 10 µL reagent + 1.990 dilution buffer.
    b. In Qubit tubes, dilute 10 µL of Standard 1 and Standard 2 with 190 µL of working buffer.
    c. In Qubit tubes, dilute 2 µL of each sample with 198 µL of working buffer.
    d. Vortex all tubes to mix well.
    e. Measure at the BMC.

.. note::

    If needed, you can store the eluted 30 µL samples at -20°C or -80°C and pause the protocol.

79. Vortex the T1 streptavidin beads well. For N samples, transfer 30 * N µL of beads to a low-binding 1.7 mL tube.
80. Pipetting up and down to mix well before taking each sub-sample, transfer 30 µL beads to separate low-binding 1.7 mL tubes.
    
    .. note:: 
        You will be using the same 1.7 mL tubes until you elution step after adapter ligation. Don't transfer samples
        to PCR tubes.

81. Add 1 mL of 1xTBW to each tube to wash the beads. Incubate for 1 minute, then place on magnet until beads separate.
82. Remove the supernatant while the tubes are still on the magnet.
83. Remove the 1.7 mL tubes from the magnet and resuspend in 150 uL of 2xBW.
84. Dilute the remaining 30 µL DNA samples to 150 µL by adding 120 µL of DEPC-treated water.
85. Add the samples to the tubes with beads. Mix well at room temperature with 300 rpm shaking for 30 minutes.

.. note::
    
    If needed, you can leave the bead + sample solution mix overnight and start the steps the following day.
    With the enhanced speed of the SPRI-based cleanup, we merged Day 3 and Day 4 of the original protocol.

86. Add 950 µL of 1xTBW to each sample. Mix by pipetting and then shake at room temperature and 1200 RPM for 5 minutes.
87. Place on the magnet to settle the beads, remove the supernatant, and repeat the previous step.
88. After the second wash, remove the supernatant and quickly add 950 µL of 10 mM Tris-HCl pH 7.5 while
    the tubes are still on the magnet. Leave the Tris-HCl on the beads until right before the following steps.

End repair and A-tailing
^^^^^^^^^^^^^^^^^^^^^^^^

89. Prepare enough End Repair Master Mix. This (and following steps) are no longer scaled per cell count; use the same volume
    for all samples.

    **End Repair Master Mix (60 µL / sample)**

    ==========================  ======
    Component                   Volume
    ==========================  ======
    DEPC-treated water          50 µL
    End Prep Reaction Buffer    7 µL
    End Prep Enzyme Mix         3 µL
    ==========================  ======

90. Remove the 10 mM Tris and carefully resuspend each sample in 60 µL of End Repair Master Mix, avoiding bubble formation.
91. Incubate for 30 minutes at 20°C with interval mixing (1000 rpm for 1 minute, 3 minutes still, repeat).
92. Incubate for 30 minutes at 65°C without mixing.
93. Transfer samples to ice.

Adapter ligation
^^^^^^^^^^^^^^^^

94. Prepare enough diluted Illumina adapter and Reaction Master Mix.
    
    You need 1 µL of diluted adapter per condition. Use the following dilutions based on the
    estimated DNA concentration as measured by the Qubit. Dilute in 10 mM Tris-HCl pH 7.5 + 10 mM NaCl.

    **Adapter dilution**

    ==============  ============
    DNA amount      Dilution
    ==============  ============
    1 µg - 100 ng   None
    100 ng - 5 ng   Dilute 1:10
    < 5 ng          Dilute 1:25
    ==============  ============

    **Reaction Master Mix, (31 µL / sample)**:

    ======================= ======
    Component               Volume
    ======================= ======
    Ligation Master Mix     30 µL
    Ligation enhancer        1 µL
    ======================= ======

95. Add 1 µL of diluted adapter into each tube, separately. Add in 31 µL of Reaction Master Mix, mixing with pipetting
    while avoiding bubble formation.
96. Incubate for 30 minutes at 20°C with interval mixing (1000 rpm for 1 minute, 3 minutes still, repeat).
97. Add in 3 µL of USER enzyme to each tube. Incubate for 15 minutes at 37°C with interval mixing (1000 rpm for 1 minute, 3 minute still, repeat).
98. Add 950 µL of 1x TBW to each tube, mix well, and incubate for 3 minutes at room temperature at 1200 rpm.
99. Briefly spin the tube, transfer to the magnet, and remove the supernatant while still on the magnet.
100. Repeat the wash step by adding 950 µL of 1x TBW, mixing well, incubating, spinning, and placing on the magnet.
101. While still on the magnet, rinse the beads wtih 950 µL of 10 mM Tris-HCl, pH 7.5. Incubate on the magnet for 1 minute, then remove supernatant while still on the magnet.
102. Resuspend the beads in 23 µL of 0.1x TE; the resulting bead slurry is used in downstream steps because the pulled-down fragments are relatively irreversibly bound to the beads.
     This does not interfere with the PCR.

     .. warning::
        Do not freeze the bead slurry! Store at 4°C or on ice.


Test PCR
^^^^^^^^

103. Following the :doc:`Test PCR protocol </protocols/biochem_and_analytics/genomics_sequencing/test_pcrs>`, using the following variables:
     
     - Use 3 µL of the 23 µL bead slurry for test PCR purposes. 19 µL will be used in the real PCR, so :math:`\log_2(19/ 0.7) = 4.76` delta cycles.
     - Use the ``ligation_fwd`` and ``ligation_rev`` primers.
     - Target at least 500 ng, erroring on the higher side. Perform 12/14/16 test cycles.
     - The final cycle count should be between 6-9 cycles.


Real PCR
^^^^^^^^

104. Prepare enough Master Master mix for each condition, 76 µL per condition.
     
     **Master Master Mix (76 µL / condition)**

     =================================  ======
     Component                          Volume
     =================================  ======
     DEPC-treated water                 26 µL
     2x NEBNext Ultra II Q5 Master Mix  50 µL
     =================================  ======

105. Assign dual-indexes to each condition. We buy the pre-indexed plates from NEB, so this means assigning a 
     well of a 96-well to each condition (e.g. A4 is condition 1, B4 is condition 2, ...).
106. Prepare reaction mixes per condition by combining the following:
     
     =============================  ======
     Component                      Volume
     =============================  ======
     Master Master mix              76 µL
     Premixed dual-index primers    5 µL
     Bead slurry (add last)         19 µL
     =============================  ======

107. Split reaction mixes across two PCR tubes, e.g. so each tube has 50 µL total volume. Run the following PCR program:

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

     .. note::

        If some of the conditions have a different optimal cycle count, you can use
        the same 42°C hold technique as the test PCR; e.g. do 7 cycles, have a 42°C hold where you remove
        the tubes that only need 7 cycles, resume for another cycle or two, and so on.

108. Pool the split reactions back together.
109. To each 100 µL sample, add 90 µL of Ampure beads. Mix well via pipetting.
110. Incubate at room temperature for 15 minutes.
111. Place tubes on the magnetic rack. Remove the supernatant, and wash twice with 200 µL of **freshly prepared** 80% EtOH
     without disturbing the beads (e.g. keep the tubes on the magnet).
112. Remove residual EtOH wash using a P10.
113. Air-dry the beads until the shiny-to-matte transition happens, not longer than 5 minutes.
114. Add 25 µL of 0.1x TE to elute. Mix well via pipetting and incubate off-magnet for 2 minutes at room temperature.
115. Place the tubes back on the magnet and transfer the supernatant to nicely labled, new low-binding 1.7 mL tubes. Store at -20°C. This is a good pause step.

Pre-amplification library quantification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
116. Following the instructions for the NEB Next Library Quant Kit, quantify the concentration of each library.
117. Perform a 1:200 dilution Qubit quantification of each library.

        a. Dilute the Qubit light-sensitive reagent 1:200 in Qubit dilution buffer to make working buffer. For 8 samples + 2 standards, this is 10 µL reagent + 1.990 dilution buffer.
        b. In Qubit tubes, dilute 10 µL of Standard 1 and Standard 2 with 190 µL of working buffer.
        c. In Qubit tubes, dilute 1 of each sample with 199 µL of working buffer.
        d. Vortex all tubes to mix well.
        e. Measure at the BMC.
118. Based on these measurements, calculate volumes required to pool 500 ng of each condition together, up to a maximum of 4 µg per capture reaction.
     Trust the library quant kit result over the Qubit quantification, though both should be close. The Qubit measures
     total DNA, whereas the library quant kit measures only DNA containing amplifiable Illumina primers.

Day 4: Region capture
---------------------

.. time::
    
    The first capture day has very short hands-on time. It ends with a 16 hour incubation step
    that should be precisely followed! Start the incubation step at the end of the day so that you
    will have sufficient time to prepare buffers and such the following day.

.. warning::

    If you google the Twist Target Hybridization Protocol, there are multiple versions of the
    protocol! Make sure your protocol version matches the reagents you have.

    We currently use the `v2 protocol </_static/files/twist_target_enrichment_v2.pdf>`__.

119. Combine 500 ng of each condition together into a single pool in a fresh PCR tube. Load another PCR tube
     with an equivilant amount of water.
120. Thaw required ragents on ice (Hybridization Mix, Hybridization Enhancer, Universal Blockers, Blocker Solution).
121. Use a lyophilizer to dry the indexed pool, in no-heat mode.
     
     a. Fill the condenser with liquid nitrogen.
     b. Place the PCR tubes **(with caps open!)** within 1.7 mL tubes, then place these inside the lyo centrifuge.
     c. Make sure the lid seals, then turn on the centrifuge, keeping the heater **off**.
     d. Turn on the vacuum pump and open the valve to the centrifuge. Wait at the centrifuge until the
        vacuum monitor reaches mill-Torr.
     e. Lyophilize the pooled library for at least 90 minutes.
     f. There should be a thin film of DNA visible after drying is complete, with no visible liquid.

121. Near the end of the lyophilization, set a water bath to 65°C and set a thermocycler to 95°C (lid temp 105°C).
122. Heat the Hybridization Mix in the water bath for 10 minutes. Cool at room temperature for 5 minutes.
123. In a clean PCR tube, prepare Probe Solution. Mix well.

     **Probe Solution**

     ================== ======
     Component          Volume
     ================== ======
     Hybridization mix  20 µL
     Twist Custom Panel 4 µL
     Water              4 µL
     ================== ======

124. Resuspend the library pool with the following reagents. Flick and pipette to mix.

     ====================== ======
     Component              Volume
     ====================== ======
     Dried library pool     n/a
     Blocker solution       5 µL
     Universal blockers     7 µL
     ====================== ======

125. Heat the Probe Solution to 95°C for two minutes in the thermocycler (with the lid closed to prevent condensation), then remove tube and place on ice for 5 minutes.
126. While the Probe Solution is cooling, heat the library pool to 95°C on the thermocycler (with the lid closed to prevent condensation) for 5 minutes, followed by 5 minutes at room temperature.
127. Vortex and spin down the probe solution, then transfer the whole volume into the resuspended library pool. Mix well.
128. Pulse-spin the tube.
129. Add 30 µL of Hybridization Enhancer to the top of the reaction. This enhancer floats on the top like oil.
130. Pulse-spin the tube.
131. Incubate the hybridization reaction at 70°C for 16 hours in a thermocycler, with the lid at 85°C.

.. note::
    Shoot for 16 hours. You can stop the hyrbidization between 15 and 17 hours, so you have some, but limited room.

Day 5: Region capture part 2
----------------------------

132. Follow the `Twist instructions </_static/files/twist_target_enrichment_v2.pdf>`__ with the following changes:
    
     a. Instead of guessing on a number of amplification cycles, perform a test PCR. Twist has you elute in 45 µL,
        so if you perform 30 µL test reactions with 3 µL template, subtract off :math:`\log_2(45/3) = 3.9` cycles from
        the gel quantification. Use the NEBNext Ultra II mix for the test PCR.
     b. You can use either the provided Equinox library amplification mix, or the NEBNext Ultra II mix for the final PCR.
     c. Quantify the resulting 30 µL libraries (eluted in 10 mM Tris-HCl, pH 8) both with the `NEB Library Quant kit </_static/files/neb_library_quant_kit_manual.pdf>`__ and by submitting
        a sample to the FragmentAnalyzer in the BMC.

