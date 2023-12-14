==========================
Homemade EU click
==========================

.. _EUclick:
 
1 rxn = 1 single 24-well (250 µL EU or 175 µL click mix).

Note that ascorbic acid should be made fresh and **EU will likely be the limiting reagent.**

.. important::
    The NaN3 is important to include in any single color controls! We observe that presence of EU doesn't change CFSE only control signal but any azide addition (with or without EU) significantly changes FSC/SSC and CFSE signal.
    The following image shows the effects of azide addition on 1 dpi CFSE-labeled MEFs flowed at 4 dpi.

    .. figure:: img/Az_effect_on_CFSE.png
        :align: center


Stock solutions
-----------------------------------

    - Main solutions

    ===================================   ==========================   =========================================================================  ==========================
    **Stock solutions**                   **Stock concentration**      **How to make**                                                            **Final concentration**  
    ===================================   ==========================   =========================================================================  ==========================
    EU (100X)                              100 mM                       5 mg EU + 186 µL **DMSO** (74 rxns)                                        1 mM
    CuSO4.5H2O (100X)                      200 mM                       250 mg CuSO4.5H2O + 5 mL H2O (2,800 rxns)                                  2 mM
    Ascorbic acid (10X) **MAKE FRESH**     200 mg/ml                    120 mg Ascorbic acid + 600 µL H2O (34 rxns)                                20 mg/mL
    ===================================   ==========================   =========================================================================  ==========================

    - Main azide solutions

    ===================================   ==========================   =========================================================================  ==========================
    **Stock solutions**                   **Stock concentration**      **How to make**                                                            **Final concentration**  
    ===================================   ==========================   =========================================================================  ==========================
    NaN3 (use to make 500X soln)             4 M                        250 mg NaN3 + 961 µL H2O                                                   --
    NaN3 (500X)                              4 mM                       1 µL of 4 M NaN3 + 1,000 µL H2O (2,800 rxns)                               8 µM
    Sulfo-Cy5 azide (500X)                   4 mM                       5 mg Sulfo-Cy5 azide + 1,638 µL H2O (4,600 rxns)                           8 µM
    BDP TR azide (500X)                      4 mM                       5 mg BDP TR azide + 2,469 µL **DMSO** (7,000 rxns)                         8 µM
    ===================================   ==========================   =========================================================================  ==========================


    - Misc/wash solutions

    ===================================   =================================================================================  
    **Stock solutions**                    **How to make**                                                         
    ===================================   =================================================================================  
    0.5% Tween-20 in PBS                   50 mL PBS + 250 µL Tween-20. **Add Tween-20 to 1 mL PBS first to mix easier!**  
    3.7% PFA in PBS                        44 mL PBS + 5.7 mL 32% PFA
    (*Optional*) 0.1 µg/mL DAPI in PBS     Dilute 0.1 mg/mL DAPI (1,000X stock in -20/Olaf) into PBS
    ===================================   ================================================================================= 


.. note::
    The 200 mg/mL ascorbic acid (10X) should be made fresh day of. It takes a while to dissolve so start it early and vortex often.

.. warning:: Azides are toxic! Always use azides in the fume hood and do not breathe it in!
    Azide waste should be collected in the satellite accumulation area in the fume hood.


Add EU to cells
----------------

1.  In BSC hood, add 2.5 µL of 100 mM EU (100X) to 250 µL of complete growth medium (DMEM/FBS or N3 with no neurotrophics) per 24-well. For a full 24-well plate, 60 µL into 6 mL (90 µL into 9 mL if need more for single color controls). 
2.  Incubate cells for 1 hour at 37°C.


Dissociate
----------------

3.  Remove media, wash with PBS, trypsinize, and spin down in eppendorfs. 

.. note::
    We did not notice a difference but you can precoat with 7.5% BSA/PBS and/or use low-retention eppendorfs. For 7.5% BSA/PBS precoating, just pipette up and down (no need to incubate).


Fix cells
----------------

4.  Add 100 µL of 3.7% PFA/PBS to each Eppendorf and mix well. Let sit 15 at RT in the dark (covered).
5.  Add 1 mL PBS and spin cold at 4°C to pellet cells. 
6.  Remove supernatant.


Permeabilize
----------------

7. Add 100 µL 0.5% Tween/PBS. Let sit 15 minutes at RT in the dark (covered). 
8. Wash by adding 900 µL PBS and spin down at 4°C. 
   
(*Alt to step 8*) Just add 175 µL of label mix to cells. 


.. note::
    Other protocols use 0.5% Triton X-100, but comparing Tween-20 and Triton X-100 we observed that the pellets permeabilized with Triton disappeared after the click step. 


.. important:: 
    Any immunostaining should be done at this point, before the click reaction. Staining after the click reaction results in high levels of non-specific
    staining and no detectable specific signals.

Prepare click/label mix
--------------------------------------------------

9.  Make label mix just before use by combining (in this order: precipitate is formed after addition of CuSO4 to PBS, this is dissolved after addition of ascorbate):
    
    - The following mix is enough for a full 24-well plate: 4,500 µL ~ 25 rxns (OR  1,000 µL for NaN3 ctrls)

    ============================   =================================================
    **Solution**                   **Volume (for NaN3 ctrls)**
    ============================   =================================================
    PBS                             4,000 µL (or 888 µL)
    CuSO4 (100X, 200 mM)               45 µL (or 10 µL)
    Azide (500X, 4 mM)                  9 µL (or 2 µL)
    Ascorbate (10X, 200 mg/mL)        450 µL (or 100 µL)
    ============================   =================================================


Label and wash
--------------------------------------------------------

10. Add 175 µL click/label mix per tube and incubate cells 30 min at RT with label mix on rotator, protected from light, at room temp. 
11. Wash by adding 900 µL PBS and spin down at 4°C.
12. (*Optional*) Incubate cells 5 minutes with 175 µL of 0.1 µg/mL DAPI/PBS if you want to detect nuclei in flow
13. Wash by adding 900 µL PBS and spin down at 4°C.
14. Analyze by flow. 


.. note::
    All spins are performed at ~500 rcf for 5 min. Our centrifuge follows RCF = 1e-4*[rpm]^2 + 4e-2*[rpm] - 6e1, where **2200 rpm = 512 rcf**.
    It is recommended to perform all spins at 4°C once the cells have been fixed to prevent pellet loss.