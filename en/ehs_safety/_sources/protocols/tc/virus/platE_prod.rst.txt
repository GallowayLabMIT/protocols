======================================
Plat-E Retroviral Production
======================================

Plat-Es are a retrovirus packaging line that produce retroviruses that can only infect mouse cells. Plat-E cells contain gag, pol and env genes, allowing retroviral packaging with a single plasmid transfection.
Supposedly, Plat-E viruses can't be frozen but we have seen frozen Plat-E virus work fine.

.. note::
	Do a **10 µg/mL blast and 1 µg/mL puro selection every ~3 passages**. This is to ensure cells are expresssing the retroviral structure proteins.


Plat-E Transfection
-------------------

Day One (seed Plat-Es):

1. :ref:`Gelatin coat <gelatin>` a 6-well plate (1x6-well makes enough virus for 1x96-well plate)
2. Seed 2 mL of 425k cells/mL onto 6-well plates (850k Plat-E's/6-well total) onto the gelatin coated plates.
3. Rock the plate back and forth, side to side to mix, then place back in incubator. *Rocking side to side prevents cells from clustering at the well edge.*

.. tip::
	If starting from frozen, **start growing Plat-E cells 1 week prior** - they will be slow growing at first (don't change culture medium during the first 3 days). Split Plat-Es 4X-6X every 2-3 days when culture reaches 70-90% confluency.


Day Two (transfect Plat-Es):

1.  Make a mastermix (MM) of PEI and Knockout DMEM as follows (MM for 1 well/each virus):

    a.	For *just 1 well of a 6-well plate*:

        i.  In a 1.5 mL tube, FIRST add 180 µL KO DMEM.
        ii. SECOND, add 7.2 µL PEI (1 mg/mL) for a 4:1 ratio (of µg PEI:µg DNA ratio).
        iii. Gently flick to mix. Let sit for 5 minutes.

    b.	For *3.5 rxns or wells of a 6-well plate*, same as above but use 630 µL KO DMEM + 25.2 µL PEI (1 mg/ml) for a 4:1 ratio

.. important::
	Ensure that you **add PEI to KO DMEM, NOT the other way around!!** Also make sure to use KO DMEM as KO DMEM facilitates lipid-mediated transfections (e.g. PEI) which might be disrupted by regular DMEM.

.. note::
    PEI optimal concentration varies by batch and must be tested before transfection. Current batch is 4:1 as of 2022.03.17 (typical range 4:1 to 6:1).

2.	Add DNA to this MM as follows, then mix and wait 15 minutes:

    a. 1.8 µg DNA/well, (or 6.3 µg DNA total for 3.5 rxns)
    b. For example:

    =============================   ==============   =================   ====================
    Component                        Volume/ 1 rxn    Volume / 3.5 rxn    **Total Vol/well**
    =============================   ==============   =================   ====================
    pMXs-mGL (500 µg/µL)                 3.6 µL          12.6 µL          **190.8 µL/well**
    =============================   ==============   =================   ====================

3.	Add each KO DMEM + PEI + DNA mix to a single 6-well (1 WELL PER VIRUS) **DROPWISE** and evenly around the plate, rocking the plate back and forth, side to side to mix. Place back in incubator.


Day Three (Plat-E media change + seed mouse cells):

1.	Change with 1.25 mLs fresh media (:ref:`DMEM/HEPES + 10% FBS <HEPES>`) after 24 hours. Note: NBW transfects ~4pm and media changess ~10am next day to minimize PEI cytotoxicity.
2.	Seed mouse cells

    i.  Coat wells in 0.1% gelatin for approx. ~10 min.
    ii. Seed at 10k cells/96-well. For larger sizes, scale accordingly according to surface area

        =================   ==========================   ===============================================================
        **Culture plate**    **Scale factor**              **# of 6-wells of Plat-E you'll need for a full plate**
        =================   ==========================   ===============================================================
        6-wells              30                            2
        12-wells             11                            1.5
        24-wells             6                             1.5
        48-wells             3                             1.5
        96-wells             1                             1
        =================   ==========================   ===============================================================

Day Four (Plat-E media change + infect 1):

1.	Harvest media after another 24 hours and add 1.25 mL fresh media (:ref:`DMEM/HEPES + 10% FBS <HEPES>`) to Plat-E plates for a second time.
2.	Transduce mouse cells with retroviruses made from the Plat-E cells

    .. note::
        Each virus will make ~1 mL/well from each 6-well of Plat-E (enough for 1x96-well plate). 11 µL of each virus will be added to each well of a 96-well plate ALONG WITH POLYBRENE (1,000X at 5 mg/mL)

    a.  Filter each virus through a 0.45 µm filter
    b.  Master mixes will be made for simpler "aliquoting" into wells. The following table is a guide for the final total volume for each well depending on the plate.

        =================   =================================================
        **Culture plate**    **Total DMEM (i.e. MEF media) + virus per well**
        =================   =================================================
        6-wells              2 mL
        12-wells             1 mL
        24-wells             500 µL
        48-wells             250 µL
        96-wells             100 µL
        =================   =================================================

.. note::
    You can either 1. filter each virus then mix together (minimizes filtering) or 2. mix altogether then filter (standardizes mixing). Because filtering is the most annoying step, it is advised to minimized filtering.

3.	Add virus mixes to each well dropwise, rocking back and forth to mix.


Day Five (infect 2):

1.	Collect media from Plat-Es again and reinfect/retransduce the cells for a second day.

.. note::
    Centrifugation of target cells with virus (spinfection) can improve infection efficiency. Spinfection is typically performed on the second day of transduction. Spinfection protocol is :ref:`here <spinfection>`.


Day Six (1 dpi):

1.	Change media on transduced mouse cells



.. note::
    NBW has found you can freeze PlatE virus. I will concentrate a single 6-well collected over 2 days (~2.1 mL + 700 µL Lenti-X concentrator) and resuspend into 100 µL where I use 2 µL/96-well.
    **You will lose ~50% of your virus so I go with frozen virus from 2x6-wells will infect 1x96-well plate**.