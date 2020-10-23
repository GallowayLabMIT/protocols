=================
ATAC-see
=================

Transposase buffer preparation
---------------------------------

.. time:: 1.5 hours.

1. Order the following primers:

    ============ ====== ============= ================ ====================================
    Primer name  Scale  Purification   5' modification  Sequence
    ============ ====== ============= ================ ====================================
    Tn5ME_rev    25nmol DSL             Phosphate       `CTGTCTCTTATACACATCT`
    Tn5ME_A      50nmol HPLC            Cy5             `TCGTCGGCAGCGTCAGATGTGTATAAGAGACAG`
    Tn5ME_B      50nmol HPLC            Cy5            `GTCTCGTGGGCTCGGAGATGTGTATAAGAGACAG`
    ============ ====== ============= ================ ====================================

2. Resuspend each primer separately to 100 uM (the standard stock dilution, nmol * 10 uL).
3. Prepare 1:1 solutions of Tn5ME_rev / Tn5ME_A (A+rev) and Tn5ME_rev / Tn5ME_B (B+rev). Each primer is now
   at 50 uM.
4. Assemble these double stranded oligos by heating to 95C for 5 minutes, followed by slow cooling to room temperature.
   To do this on a thermocycler, use a program that does ends after the denaturation step, instead of ending in a hold step.
5. Prepare 5 uM stock solution of Tn5/Cy5. Prepare this either from freshly purified Tn5 in dialysis buffer:

    ================= ===============
    Component         Volume fraction
    ================= ===============
    A+rev primers       0.125
    B+rev primers       0.125
    Glycerol            0.4
    Dialysis buffer     0.12
    50 mM Tn5           0.1
    DI H2O              0.13
    ================= ===============

   If Tn5 is already stored in a 50% glycerol/50% 2x dialysis stock solution at 20 mM, use the following recipe:

    ================== ===============
    Component          Volume fraction
    ================== ===============
    A+rev primers       0.125
    B+rev primers       0.125
    Glycerol            0.25
    20 mM Tn5+Glycerol  0.25
    DI H2O              0.25
    ================== ===============

ATAC-see
--------

We need the following prepared buffers:

* **Nuclear permeabilization buffer**:

    ==================  ============== ====================
    Component            Concentration Amount/100 mL final
    ==================  ============== ====================
    Tris-Cl                 10 mM           0.1576 g
    NaCl                    10 mM           0.058 g
    MgCl2(anhydrous)        3 mM            0.0287 g
    Igepal CA-630           0.01%           10 uL
    HCl                 to pH 7.4
    ==================  ============== ====================

* **Wash buffer**:

    ================== ============== ====================
    Component          Concentration   Amount/100 mL final
    ================== ============== ====================
    PBS                 Base
    SDS                 0.01%           .01 g
    EDTA                50 mM           1.461 g
    ================== ============== ====================

* **2x TD buffer** (from `this nature paper <https://www.nature.com/articles/nprot.2013.118>`_):

    ==============================  =============================== ==============
    Component                       Concentration                   Amount/L final
    ==============================  =============================== ==============
    Tris                            20 mM                            3.264 g
    MgCl2                           10 m                             0.95 g
    DI H2O                          main solvent
    Acetic acid                     to pH 7.6, before DMF addition
    Dimethylformamide(DMF)          20% (v/v)
    ==============================  =============================== ==============

1. After cell fixation, permeabilize cells with lysis buffer for 10 minutes at room temperature.
2. Wash with PBS twice.
3. Prepare transpose mixture:

    ================== ===============
    Component          Volume fraction
    ================== ===============
    2x TD buffer        0.5
    5 mM assembled Tn5  0.02
    DI H2O              0.48
    ================== ===============

4. Add 50 uL of transpose mixture to cells to be transposed. Place the cells in a humid 37C box for 30 minutes.
5. For plated cells, wash with wash buffer three times, for 15 minutes each at 55C. For suspended cells, wash twice.
6. Add PBS media to cells and image/flow the resulting cells.