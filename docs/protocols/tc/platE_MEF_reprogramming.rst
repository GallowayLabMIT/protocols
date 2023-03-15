======================================
Plat-E Retroviral Transduction of MEFs
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

.. tip::
	**Start growing MEFs today (2 days before seeding)**. If they don't do well by the next day, this gives you 1 more day to defrost more.


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

    a.	1.8 µg DNA/well, (or 6.3 µg DNA total for 3.5 rxns)

    =============================   ==============   =================   ====================
    Component                        Volume/ 1 rxn    Volume / 3.5 rxn    **Total Vol/well***
    =============================   ==============   =================   ====================
    Brn2 (4.49 µg/µL)                0.40 µL          1.40 µL             **189.40 µL/well**
    Ascl1 (2.78 µg/µL)               0.65 µL          2.27 µL             **189.65 µL/well**
    Myt1l (2.1 µg/µL)                0.86 µL          3.00 µL             **189.86 µL/well**
    Ngn2 (4.4 µg/µL)                 0.41 µL          1.43 µL             **189.41 µL/well**
    Isl1 (6.2 µg/µL)                 0.29 µL          1.02 µL             **189.29 µL/well**
    Lhx3 (5.4 µg/µL)                 0.33 µL          1.17 µL             **189.33 µL/well**
    p53DD (3.93 µg/µL)               0.46 µL          1.60 µL             **189.46 µL/well**
    HRasG12V (0.9 µg/µL)             2.00 µL          7.00 µL             **191.00 µL/well**
    NIL (7.35 µg/µL)                 0.24 µL          0.86 µL             **189.24 µL/well**
    =============================   ==============   =================   ====================

3.	Add each KO DMEM + PEI + DNA mix to a single 6-well (1 WELL PER VIRUS) **DROPWISE** and evenly around the plate, rocking the plate back and forth, side to side to mix. Place back in incubator. *Rocking side to side prevents cells from clustering at the well edge.*


Day Three (Plat-E media change + seed MEFs):

1.	Change with 1.25 mLs fresh media (`DMEM/HEPES + 10% FBS <HEPES>`) after 24 hours. Note: NBW transfects ~4pm and media changess ~10am next day to minimize PEI cytotoxicity.
2.	Seed MEFs

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

1. Harvest media after another 24 hours and add 1.25 mL fresh media (`DMEM/HEPES + 10% FBS <HEPES>`) to Plat-E plates for a second time.
2. PROCEED TO TRANSDUCTION!


Transduction of Mouse Embryonic Fibroblasts (MEFs)
--------------------------------------------------

Day Four (Plat-E media change + infect 1):

1.	Transduce MEFs with retroviruses made from the Plat-E cells

    .. note::
        Each virus will make ~1 mL/well from each 6-well of Plat-E (enough for 1x96-well plate). 11 µL of each virus will be added to each well of a 96-well plate ALONG WITH POLYBRENE (1,000X at 5 mg/mL)

    a.  Filter each virus through a 0.45 µm filter

        i.  For 6F, all 6 TFs (BAMNIL) will be filtered through the same syringe together to simplify adding them each individually to MM combos.

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

2.	Examples of mixing AFTER filtering

    i.  Example - 6F alone (96-well = 100 µl total/96-well):

        *For 1 rxn, 96-well*: 66 µL 6F (= 11 µL PER FACTOR*6) + 34 µL DMEM + 0.1 µL polybrene (1,000X) = 100 µL total/96-well

        *For 3.5 rxn, 96-well*: 231 µL 6F + 119 µL DMEM + 0.35 µL polybrene (1,000X) = 350 µL total for 3.5 96-wells

    ii.  Example - 6F + DD + RR (96-well = 100 µL total/96-well):

        *For 1 rxn, 96-well*: 66 µL 6F + 11 µL p53DD + 11 µL hRasG12V + 12 µL DMEM + 0.1 µL polybrene (1,000X) = 100 µL total/96-well

        *For 3.5 rxn, 96-well*: 231 µL 6F + 38.5 µL p53DD + 38.5 µL hRasG12V + 42 µL DMEM + 0.35 µL polybrene (1,000X) = 350 µL total for 3.5 96-wells

3.	Add virus mixes to each well dropwise, rocking back and forth to mix.


Day Five (infect 2):

1.	Collect media from Plat-Es again and reinfect/retransduce the MEFs for a second day.


Day Six (1 dpi):

1.	Change media on transduced MEFs according to transduction MM table (e.g. 100 µL for 96-well)
2.  If doing CFSE, do it now: :doc:`/protocols/biochem_and_analytics/cfse_labeling`


Day Eight (3 dpi):

1.	Media change plates to N3 media

    a. N3 media = N3 base + BDNF/CNTF/GDNF (1,000X, 10 µg/mL) + FGF (10,000X, 100 µg/mL) + *2% FBS (optional)*

2.  **Spike in 1,000X RepSox to N3 media for RR conditions**


Day 10, 12, 14, etc:

1.	Change N3 media every 2 days (can do 3 days if after ~8 days and weekend but 2 is ideal) until done (usually 14 dpi).

.. note:: 
    After 8 dpi, it is recommended to dissociate with  (`DNAse/Papain <MNdissociate>`) instead of trypsin