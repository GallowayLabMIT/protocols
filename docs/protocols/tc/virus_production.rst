=======================
Virus production
=======================

.. time::
    4-5 days. Note that on the **transfection day**, you must change
    the media 6-8 hours after the transfection.

Scale and virus type selection
------------------------------

- Decide on a scale to perform the virus production. This method gives virus titers roughly
  high enough to infect an equal-area plate initially; each subsequent freeze-thaw cycle
  will reduce virus titer by roughly 50%. A 10cm dish is sufficient to infect about one and a half
  96-well plates. Look up relevant values from the scale table.
- Decide on a virus type; this determines your packaging and envelope plasmids. Look up the
  packaging and envelope plasmids in the virus type table.

**Scale:**

========    ===========    ======================    ===================    ============================
Scale       Area (cm^2)    Seeding amount (cells)    Total DNA mass (ug)    Collection media volume (mL)
========    ===========    ======================    ===================    ============================
10cm        56.7            7.5 x 10^6               24                     6.5 
6-well      9.6             1.0 x 10^6               4.1                    1
========    ===========    ======================    ===================    ============================

If using a different virus production scale, the total DNA mass should be scaled by surface area.
The collection media volume should be roughly half of the standard amount of media used for that scale.

**Virus type:**

===========     ===================     ================
Type            Packaging plasmid       Envelope plasmid
===========     ===================     ================
Lentivirus      psPAX2 (pKG362)         pMD2.G (pKG096)
Retrovirus      pIK-MLVgp (pKG015)      pHDMG (pKG022)
===========     ===================     ================

Production
----------
The following is given for a 10cm-dish production scale. For other scales, substitute
the correct seeding amounts/total DNA mass/other values from the scale table.

Day 0
*****
1. Seed confluent 293T cells onto a gelatin-coated virus production plate/dish. For a 10cm dish, this
   should be 7.5-8.0 million cells (use the calculated **seeding amount** for other scales).

Day 1
*****
1. Transfect your cells when they are 70-80% confluent. This should be roughly 18-24 hours
   after you seeded the cells.
2. Prepare a mastermix of PEI and knockout DMEM. It is helpful to prepare a 110% master mix
   (include 10% extra mix) to account for pipetting losses. Ensure that you
   **add the PEI to the KO-DMEM** and not in the other order.
   
   a. Use the total number of micrograms of DNA (24 for a 10cm dish) times the
      experimentally-determined PEI ratio to get the number of microliters of
      1mg/mL PEI you need to add. In other words, the PEI ratio is a PEI:DNA mass ratio.
   b. We use 1.33 mL of KO-DMEM per 10cm dish, but the transfection seems relatively insensitive
      to this ratio.

3. After waiting for 10-15 minutes, mix the following amounts of DNA with the PEI-KO DMEM master mix.
   You can add the master mix to the DNA or add the DNA to aliquoted master mix.

   =======      ==================  ===================  ==================
   Scale        Mass Transfer (ug)  Mass Packaging (ug)  Mass Envelope (ug)
   =======      ==================  ===================  ==================
   Ratio        1                   1                    2
   10cm         6                   6                    12
   6-well       1.02                1.02                 2.05
   =======      ==================  ===================  ==================


4. After waiting an additional 10-15 minutes, add the mixture *dropwise* and *evenly* around the
   plate. After adding, be sure to gently rock the plate side-by-side to mix.

   .. important::
        The six-to-eight hour timing is important for this protocol. We use a relatively
        large amount of transfected DNA, which means we are also adding a high concentration
        of PEI. Media changing after six-to-eight hours can greatly reduce transfection-related
        cell death.

5. Six-to-eight hours after transfection, replace the media on the plates with HEPES-buffered
   DMEM. Use the collection volume of media, which is 6.5mL for a 10cm dish.


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

Day 2, 3, ... (n - 1)
**********************

1. 24 hours after the last media change, collect the media, 
   replacing it with the same volume of fresh HEPES-buffered DMEM. 
   The collected media from separate days can be stored in the same
   50mL conical tube. Keep the collected media at 4°C

.. note::
    Two collections give high enough virus titer to infect the vast majority (70%+) of
    cells. However, a third collection can also be taken to further increase titer.

Day (n)
*******

1. On the last day of collection, either:
   
   a. Proceed to the :doc:`virus_concentration` protocol if you want to store your virus long-term.
   b. Filter the collected virus using a 0.45um filter, and keep the unconcentrated virus at 4°C for
      up to a few days. The virus media can be used instead of normal DMEM in order to directly infect
      cells.

      For example, 100 uL of unconcentrated virus media can be added to each well of a 96-well to perform
      an infection.

.. note::
   Virus infection is more efficient if it is done at the same time as seeding. If possible, after
   counting, you can resuspend pelleted cells in virus-containing media when plating.