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

Day -n: Buffer preparation
--------------------------

Shared genomics buffers
^^^^^^^^^^^^^^^^^^^^^^^

RCMC requires many, many buffers

MNase resuspension and storage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Avoid temperature cycles! This means keeping it in a reliable -80°C freezer.

Protease inhibitor cocktail
^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Need it in MB1

Day 1: MNase titration and digestion
-------------------------------------

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

17.  Prepare fresh complete MB1 and place on ice. For the standard 5M cell titration, you need 1.5 mL of this buffer,
    but this can be scaled up or down.
    
    **Complete MB1 (2 mL)**:
    
    ======================  ========
    Component               Volume
    ======================  ========
    MB1                     1940 µL
    10% NP-40 alternative   40 µL
    100x PIC (in MB1)       20 µL
    ======================  ========

18. Thaw a 5M cell pellet on ice and resuspend in 500 µL of complete MB1 (1M cells per 100 µL).
19. Incubate for 20 minutes on ice. While waiting, unfreeze a fresh MNase aliquot on ice.

    .. note::
        You can technically reuse MNase aliquots 2-3 times, but MNase is cheap compared to redoing an experiment 
        because the aliquot you used went bad.

        If performing the MNase titration and the "real" digestion on the same day, you can keep the unfrozen
        aliquot(s) on ice and use them.

20. Centrifuge at 1750 xg for 5 minutes at 4°C. 
21. Remove the supernatant, leaving ~10-20 µL in the tube.
22. Wash the nuclei pellet with 500 µL of complete MB1. Centrifuge at 1750 xg for 5 minutes at 4°C.
23. Removing as much supernatant as possible, resuspend the cell pellet in 500 µL of complete MB1 (1M cells per 100 µL).
24. Split the cells into 5 low-binding 1.7 mL tubes, with 100 µL of cells each, keeping them on ice.
25. Decide on your titration series. A common series is 2U, 4U, 7U, 12U, and 20U. For the small volumes,
    prepare a 1:10 dilution of the 20U / µL stock solution in 10 mM Tris-HCl, pH 7.5.

.. important::

    Use the **exact same** digestion procedure here and in the "real" digestion! This means 
    as close to 20 minutes as possible, working carefully but rapidly.

26. Add MNase to each 1M cell aliquot. Briefly vortex the tubes to ensure uniform MNase distribution,
    then incubate at 20 min at 37°C with shaking at 1000 rpm.
27. Transfer the digested nuclei to ice and add 0.8 µL of 500 mM EGTA. to reach a final concentration of 4 mM EGTA.
28. Briefly vortex the tube, then incubate for 10 minutes at 65°C with no shaking (but in the Thermomixer).
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

