======================================
Virus production in HEK293T
======================================

This protocol describes how to produce lentivirus and retrovirus in HEK293T cells, including a final concentration step.

.. time::
    4-6 days. Note that on the **transfection day**, you must change
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
6-well      9.6             1.0 x 10^6               4.1                    1.25
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

Virus Production
----------------
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

.. warning::
   Viral particles may be present after the first media change.
   Be sure to use proper PPE (i.e., lab coats, disposable sleeves) and wipe down the hood with Pre-Empt after use, from here on!

Day 2, 3, ... (n - 1)
**********************

1. 24 hours after the last media change, collect the media,
   replacing it with the same volume of fresh HEPES-buffered DMEM.
   The collected media from separate days can be stored in the same
   50mL conical tube. Keep the collected media at 4°C.

.. note::
    Two collections give high enough virus titer to infect the vast majority (70%+) of
    cells. However, a third collection can also be taken to further increase titer.

Day (n)
*******

1. On the last day of collection, either:

   a. Proceed to the :ref:`virus_concentration` protocol if you want to store your virus long-term.
   b. Filter the collected virus using a 0.45um filter, and keep the unconcentrated virus at 4°C for
      up to a few days. The virus media can be used instead of normal DMEM in order to directly infect
      cells.

         For example, 100 µL of unconcentrated virus media (plus 0.1µL polybrene) can be added to each well of a 96-well plate to perform an infection.

.. note::
   Unconcentrated virus appears to lead to more cell death than concentrated virus does. Therefore, concentrating the virus is advised.


.. _virus_concentration:

Virus Concentration
-------------------

.. time::
	1 hour in-TC time, 1 day overnight time

1. Filter collected virus through a 0.45µm syringe filter into a 50ml conical.  This eliminates any 293T cells that may have been carried over or collected in the media.
2. Add 1/3 volume of Lenti-X concentrator (e.g., for 30ml virus, add 10ml Lenti-X). Mix by inverting several times.
3. Store at 4°C for 24 hours (or overnight).

.. note::
   If you plan to infect plated cells the next day after concentrating the virus, seed cells on gelatin-coated plates the same day as virus filtration and concentrator addition.
   Typically, this is 10k cells/well of a 96-well plate.

4. The next day, centrifuge at 1500 x g at 4°C for 45 minutes (use the lower centrifuge). Be sure to use the caps/lids on the centrifuge buckets.
5. Aspirate the supernatant. There will be a little liquid left; this is okay.
6. Resuspend the pellet gently in the remaining liquid and transfer the entire volume to an Eppendorf tube.
7. Add media to the Eppendorf tube to reach the desired final volume (e.g., 100 or 200 µL).
8. Use or store the concentrated virus.
   a. To use: Infect according to the :doc:`Transduction of concentrated virus <virus_infection>` protocol.
   b. To store: Store all or any extra virus remaining after infection in a cryovial at -80°C.

