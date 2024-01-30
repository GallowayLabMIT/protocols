========================
Viral Titer Calculation
========================

Here, a known number of cells are infected with a dilution series made from concentrated virus. By measuring the fraction of infected cells 
at each dilution, the **viral titer (transducing units per volume)** can be calculated for that batch of virus. This number can then be used to 
standardize the **multiplicity of infection (MOI, transducing units per plated cell)** in subsequent infections. This controls for differences in 
viral production efficiency across constructs or batches of virus.

Infection in suspension
------------------------

1. Dilute :doc:`concentrated virus <virus_production>` in the appropriate culture medium at half-volume (50 µL/condition for a 96-well plate). 
   
    - See `this spreadsheet <https://mitprod.sharepoint.com/:x:/s/GallowayLab/EQEnStlTAd1NqKOPG0S18LIBFpaybN1_KckEwNsxueirOw?e=V5Gy4G>`_ for 
      formulas to calculate volumes of virus and media for the dilution series.
    - A dilution series of factors of 2-10 (starting with 2 times the typical amount of virus) may work well, and 5 dilutions may be 
      sufficient.
    - It is convenient to perform the dilution series in a clean 96-well plate so that a multi-channel pipette can be used, especially when 
      calculating titer of multiple viruses. 
    - Example factor of 2 dilution series for one virus in duplicate, with 10% extra and initial dilution 4 µL/well virus:

        ======  =========  ===========  ============== =================
        Well    Dilution   Media (µL)     Virus (µL)    Virus source
        ======  =========  ===========  ============== =================
        1        2           204             8.8         Virus stock
        2        1           103             103         Well 1 solution
        3        0.5         96              96          Well 2 solution
        4        0.25        83              83          Well 3 solution
        5        0.125       55              55          Well 4 solution
        ======  =========  ===========  ============== =================

    - Alternatively, dilution volumes can be fixed and virus amounts per condition can be computed. See `this spreadsheet <../../_static/files/MOItemplate.xlsx>`__ 
      for the corresponding calculations.

2. Dissociate and dilute cells to the appropriate count in half-volume (e.g., 2e4 HEK293T cells per 50 µL).
3. Add polybrene to the cells just before plating. Use a 1:500 dilution (e.g., 0.1 µL polybrene per 50 µL cells).
4. Plate 50 µL cells/well in a gelatin-coated 96-well plate.
5. Using a multi-channel pipette, add 50 µL diluted virus to the corresponding wells containing cells. (The final volume of each well 
   should be 100 µL.) Pipet to mix.
6. After 24 hours (1 dpi), change to fresh media (full volume).
7. After another 24-48 hours, (2-3 dpi), measure infection via :doc:`flow cytometry </protocols/tc/tc-basics/flow_cytometry>`.


Infection of plated cells
-------------------------

.. note::

    Infection in suspension is preferred because the amount of cells can be precisely controlled. For cell types that infect better when 
    plated, use the following modified protocol.

1. One day ahead, seed the standard number of cells per well in a gelatin-coated 96-well plate (e.g., 2e4 HEK293T cells/well). Include several extra wells.
2. The next day, make the virus dilution series using a full volume rather than half-volume of media (i.e., 100 µL instead of 50 µL).
3. Add polybrene at a 1:1000 dilution to the virus solutions (e.g., 0.1 µL polybrene per 100 µL solution).
4. Aspirate the media from the plated cells and replace with the virus dilution (100 µL/well).
5. Dissociate several spare wells of cells and count the number of cells per well at the time of infection.
6. After 24 hours (1 dpi), change to fresh media (normal volume).
7. After another 24-48 hours, (2-3 dpi), measure infection via :doc:`flow cytometry </protocols/tc/tc-basics/flow_cytometry>`.


Computing titer from infection data
-----------------------------------

.. warning:: TO DO