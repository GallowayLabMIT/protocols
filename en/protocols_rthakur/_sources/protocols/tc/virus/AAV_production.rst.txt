======================================
AAV production in HEK293T
======================================

This protocol describes how to produce AAV in HEK293T cells.

.. time::
    6 days. Note that on the **transfection day**, you must change
    the media 6-8 hours after the transfection.

Scale and Plasmids
------------------

========    ===========    ======================    ===================    ============================
Scale       Area (cm^2)    Seeding amount (cells)    Total DNA mass (ug)    Collection media volume (mL)
========    ===========    ======================    ===================    ============================
10cm        56.7            6.0 x 10^6                 24                     6.5
6-well      9.6             1.0 x 10^6                 4                      1.25
========    ===========    ======================    ===================    ============================

If using a different virus production scale, the total DNA mass should be scaled by surface area.
The collection media volume should be roughly half of the standard amount of media used for that scale.

===========     ===================     =====================
Type            Packaging plasmid       Helper plasmid
===========     ===================     =====================
AAV             pAAV2/2 (pKG1378)        pAdDeltaF6 (pKG1548)
===========     ===================     =====================

.. note:: It is highly recommended to full plasmid sequence the packaging and helper plasmids before use.

.. note::
    Two other serotypes have been tested (AAV8 and AAV9n), but AAV2 was the consistently the best at infecting 293Ts, MEFs, and HDFs.

    Self-complementary AAV (scAAV) also outperforms single-stranded AAV (ssAAV). With the current protocol ssAAV is only able to consistently infect 293Ts.

    ssAAV has a total cloning capacity of 4.4kb between the ITRs (4.7kb including ITRs).

    scAAV has a total cloning capacity of ~2.2kb between the ITRs.

Virus Production
----------------
The following is given for a 10cm-dish production scale. For other scales, substitute
the correct seeding amounts/total DNA mass/other values from the scale table.

Day 0
*****
1. Seed confluent 293T cells onto a gelatin-coated virus production plate/dish. For a 10cm dish, this
   should be 6-6.5 million cells (use the calculated **seeding amount** for other scales).

Day 1
*****
1. Transfect your cells when they are 70-80% confluent. This should be roughly 18-24 hours
   after you seeded the cells.
2. Prepare a mastermix of PEI and knockout DMEM. It is helpful to prepare a 110% master mix
   (include 10% extra mix) to account for pipetting losses. Ensure that you
   **add the PEI to the KO-DMEM** and not in the other order.

   a. Use the total number of micrograms of DNA (24 for a 10cm dish, 4 for a 6-well) times the
      experimentally-determined PEI ratio to get the number of microliters of
      1mg/mL PEI you need to add. In other words, the PEI ratio is a PEI:DNA mass ratio.
   b. We use 1.33 mL of KO-DMEM per 10cm dish (222uL for a 6-well).

3. After waiting for 10-15 minutes, mix the following ratios of DNA with the PEI-KO DMEM master mix.
   You can add the master mix to the DNA or add the DNA to aliquoted master mix.

   ===========  ==================================  ===========    =================== ====================== ========================
   Plasmid      Size                                Molar Ratio    Approx. Mass Ratio  Approx. Mass 10cm (ug) Approx. Mass 6-well (ug)
   ===========  ==================================  ===========    =================== ====================== ========================
   Helper       15420 bp                             1               3                  13.1                  2.18
   Packaging    7468 bp                              1               1.5                6.54                  1.09
   Transfer     variable (usually 4-5kb for scAAV)   1               1                  4.36                  0.73
   ===========  ==================================  ===========    =================== ====================== ========================

.. note::
    BAD has also used a molar ratio of 2:1.5:1 (as recommended by Braatz Lab) and didn't notice any difference in 293T or MEF infection efficiency.
    It might be fine to use a set mass ratio like with Retro and Lenti virus, but this has not tested in lab yet.

4. After waiting an additional 10-15 minutes, add the mixture *dropwise* and *evenly* around the
   plate. After adding, be sure to gently rock the plate side-by-side to mix.

   .. important::
        The six-to-eight hour timing is important for this protocol. We use a relatively
        large amount of transfected DNA, which means we are also adding a high concentration
        of PEI. Media changing after six-to-eight hours can greatly reduce transfection-related
        cell death.

5. Six-to-eight hours after transfection, replace the media on the plates with HEPES-buffered
   DMEM. Use the collection volume of media, which is 6.5mL for a 10cm dish or 1.25mL for a 6-well.


    Use the following recipes to prepare both the 1M stock solution of HEPES and the HEPES-buffered
    DMEM.

    **1M HEPES stock solution** (filter sterilize after pH-ing)

    ==============================  =============================== ==============
    Component                       Concentration                   Amount/50 mL
    ==============================  =============================== ==============
    HEPES-potassium salt            1M                              13.82 g
    DI H2O                          main solvent                    50 mL
    Hydrochloric acid               to pH 7.0
    ==============================  =============================== ==============

    **HEPES-buffered DMEM**

    ==============================  =============================== ==============
    Component                       Concentration                   Amount/50 mL
    ==============================  =============================== ==============
    DMEM + 10% FBS                  main Component                  48.75 mL
    Sterile 1M HEPES                25 mM                           1.25 mL
    ==============================  =============================== ==============

.. warning::
   Viral particles may be present after the first media change.
   Be sure to use proper PPE (i.e., lab coats, disposable sleeves) and wipe down the hood with Pre-Empt after use, from here on!

   AAV is human-infecible, so be sure to use BSL2+ precautions if delivering oncogenes.

Day 4 or 5
**********************

1. 48-72 hours after the last media change, collect the media.
2. Filter the collected virus using a 0.45um filter. You can keep the unconcentrated virus at 4°C for
   up to a few days. The virus media can be used instead of normal DMEM in order to directly infect
   cells.

.. tip:: 
    BAD finds the addition of polybrene does not affect AAV infection efficiency, unlike with Retro and Lenti virus.

    Infecting multiple times or for a longer duration can increase infection efficiency.

    BAD has not tested making AAV in a 10cm dish yet. Only 6-well plates have been used so far.

