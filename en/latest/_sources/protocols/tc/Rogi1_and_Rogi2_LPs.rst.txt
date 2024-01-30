===================
Rogi1 and Rogi2 LPs
===================

We currently have monoclones for v2 and v3. The table below highlights the key attributes of each LP architecture:

Line summary
------------

V2 Rogi1/Rogi2 dual LP RMCE line:

=========       ===============      =============      ===============================              ===============================
locus            pHA for cargo        recombinase       positive selection (gene, drug)              counterselection (gene, drug)

=========       ===============      =============      ===============================              ===============================
Rogi1 LP            pKG01862                Cre                       N/A                                     iCasp9, AP1903
Rogi2 LP            pKG02278                Bxb1                      N/A                                HSV-TK SR39h, GCV or PCV
=========       ===============      =============      ===============================              ===============================

V3 Rogi1/Rogi2 dual LP single site integrase line:

=========       ===============      =============      ===============================              ===============================
locus            pHA for cargo        recombinase       positive selection (gene, drug)              counterselection (gene, drug)

=========       ===============      =============      ===============================              ===============================
Rogi1 LP            pKG02180              Bxb1                  BsdR, Blasticidin                       HSV-TK SR39h, GCV or PCV
Rogi2 LP            pKG02181             PhiC31                 BleoR, Zeocin                                iCasp9, AP1903
=========       ===============      =============      ===============================              ===============================


Integration into landing pad lines
----------------------------------

.. note::

    These protocols are still being optimized! Important variables that need optimization include:
    1) the ratio of recombinase to donor plasmid
    2) dosing schedule of drug selection/counterselection 
    3) scale needed to obtain a sufficient number of recombined cells 


Day -1
~~~~~~~
Seed cells at 120k per 24 well.

Day 0
~~~~~~
Transfect the donor DNA, using Mirus transfection reagent.

.. note:: 
    The full Mirus manual is `here <../../_static/files/Mirus.TransIT.LT1.DNA.transfection.reagent.protocol.pdf>`__ if you have questions.

1. Make a condition mix by combining 500 ng of plasmid donor DNA (per 24 well) with 50 µL (per 24 well) of OptiMEM reduced serum media, mixing gently via pipetting.

.. important::

    Use OptiMEM, not knockout DMEM! It really does give better results.

2. Add 3 µL of Mirus TransIT-LT1 reagent per µg of donor DNA. That is, add 1.5 µL of transfection reagent per 24 well to the condition mix. Pipette gently to mix.
3. Let the condition mixes incubate at room temperature for 15 to 30 minutes. 
4. Add 50 µL of each condition mix to each 24 well, dropwise. Gently rock the media back and forth.

Day 1
~~~~~
Transfect the modRNA. You do not need to media change after the DNA transfection.

.. note:: 
    The full MessengerMAX manual is `here <../../_static/files/Lipofectamine_MessengerMAX_man.pdf>`__ if you have questions.


1. Determine how much recombinase mass you need to add:
   
   ============= ====================  ================================
   Recombinase      Mass per 24 well    Recombiase:donor plasmid ratio
   ============= ====================  ================================
   Bxb1                 100 ng                1:4
   PhiC31               100 ng                1:4
   Cre                  6.25 ng               1:64
   ============= ====================  ================================

2. Create **Solution 1** condition mixes by combining recombinase modRNA with 20 µL of OptiMEM per 24 well.
3. Create **Solution 2** condition mixes by combining 2 µL of MessengerMAX per µg of modRNA added in the previous step with 20 µL of OptiMEM. Incubate at room temperature for ten minutes.
4. Add solution 1 to solution 2 for each condition mix, and incubate for 5 minutes.
5. Add 40 uL of the resulting condition mix dropwise to the wells.

Day 2
~~~~~~
Media change the cells to fresh DMEM.

Day 5
~~~~~~
Begin selection. The recommended concentrations for selection are:

===========     =========
Selection       Quantity
===========     =========
Puro            10,000x
Zeocin          100x
===========     =========

The recommended concentrations for counterselection are

=================   =============   ========
Counter-selection   Concentration   Dilution
=================   =============   ========
GCV                 10 µM           1000x
AP1903              10 nM           1000x
=================   =============   ========

Day n
~~~~~
Continue selecting / passaging until you get a sortable population.