========================
Measuring viral titer
========================

Here, a known number of cells are infected with a dilution series made from concentrated virus. By measuring the fraction of infected cells 
at each dilution, the **viral titer (transducing units per volume)** can be calculated for that batch of virus. This number can then be used to 
standardize the **multiplicity of infection (MOI, transducing units per plated cell)** in subsequent infections. This controls for differences in 
viral production efficiency across constructs or batches of virus.

Infection in suspension
------------------------

1. Starting with :doc:`concentrated virus <virus_production>`, dilute the virus in the appropriate culture medium at half-volume (50 µL/condition for a 96-well plate). 
   
    - A dilution series of factors of 2-10 (starting with 1-2 dilutions greater than an estimated MOI of 1) may work well, and 5 dilutions is likely 
      sufficient.
    - It is convenient to perform the dilution series in a clean 96-well plate so that a multi-channel pipette can be used, especially when 
      calculating titer of multiple viruses. 
    - Alternatively, you can use one of these spreadsheets (`1 <https://mitprod.sharepoint.com/:x:/s/GallowayLab/EQEnStlTAd1NqKOPG0S18LIBFpaybN1_KckEwNsxueirOw?e=V5Gy4G>`_, `2 <../../_static/files/MOItemplate.xlsx>`_)
      to compute dilution volumes / virus amounts to avoid making 2x volume of the final dilution. Note that this pipetting will be more annoying.  

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

1. One day ahead, seed the standard number of cells per well in an appropriately coated plate (e.g., 2e4 HEK293T cells/well in a gelatin-coated 96-well plate). Include several extra wells.
2. The next day, make the virus dilution series using a half-volume of media (e.g., 50 µL/well for a 96-well plate) as described above.
3. Prepare a second half-volume of media per well containing polybrene at a 1:500 dilution. This mimics the cell solution above; mix enough for all your wells in one tube.

.. note:: 
  Alternatively, you prepare the virus dilution series using a full volume of media and add polybrene at a 1:1000 dilution.
  However, this requires spiking in the polybrene to each condition after the dilutions have been performed, so that the polybrene amount remains constant.
  This is more pipetting, so it is recommended to follow the protocol as written above.

4. Aspirate the media from the plated cells and replace with a half-volume of the media + polybrene solution using a multi-channel.
5. Add a half-volume of the virus dilution series to each well, such that the total is now a full volume in each well.
6. Dissociate several spare wells of cells and count the number of cells per well at the time of infection.

.. note:: 
  Alternatively, you can estimate the number of cells per well as twice the amount you seeded the day before, assuming a 24 hour doubling time.

7. After 24 hours (1 dpi), change to fresh media (normal volume).
8. After another 24-48 hours, (2-3 dpi), measure infection via :doc:`flow cytometry </protocols/tc/tc-basics/flow_cytometry>`.


Computing titer from infection data
-----------------------------------

.. warning:: TO DO