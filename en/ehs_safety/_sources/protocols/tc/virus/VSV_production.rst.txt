============================================================
VSV production
============================================================

Materials
---------

- Cells
- Plates
- DMEM supplemented with 10% FBS
- PEI
- Plasmids:

  - pCAG-VSVN (pKG00756)
  - pCAG-VSVP (pKG00755)
  - pCAG-VSVL (pKG00757)
  - pCAG-VSVG (pKG00758)
  - pCAG-T7 (pKG00759)
  - pVSV eGFP dG (pKG00760)

Procedure
---------

Day 1. Seed cells
-----------------------------------
1. Seed HEK293T cells in a 6-well plate (2ml of 5.0 x 10^5 cells/mL) (**Plate_A**).
2. Incubate at 37°C.

Day 2. Transfection
-------------------
1. Transfect the following plasmid mixture to the cells on **Plate_A** through the :doc:`general transfection protocol </protocols/tc/tc-basics/transient_transfection>`:

============= ==============
Plasmid        Amount of DNA
============= ==============
pVSV eGFP dG        5μg
pCAG-VSVN         1.5μg
pCAG-VSVP         2.5μg
pCAG-VSVL         0.5μg
pCAG-T7pol          5μg
pCAG-VSVM           4ug
pCAG-VSVG           4μg
============= ==============

2. Incubate the cells at 37°C for 5-6 hours.
3. Remove the media and add fresh complete media (2 mL/well of a 6-well).
4. Incubate at 37°C for about 48 hours.
5. After transfection, seed HEK293T cells in an another 6-well plate or 10cm dish for the following amplification process (**Plate_B**).

Day 3. VSVG transfection for viral amplification
------------------------------------------------

1. Transfect pCAG-VSVG to the HEK293T cells on **Plate_B**, for viral particle amplification:

   - If using a 6-well plate, transfect 2μg of pCAG-VSVG
   - If using a 10cm dish, transfect 10μg of pCAG-VSVG

2. Incubate at 37°C.

.. note::
  There is nothing that you have to do for the cells on **Plate_A** at Day 3.

Day 4. Collect the viral particles and amplify with HEK293T
--------------------------------------------------------------
1. Remove the media from the cells on **Plate_B** (HEK293T cells transfected with pCAG-VSVG at Day 3), and tansfer the supernatant of HEK293T cells on **Plate_A**.
2. Incubate at 37°C for about 48-72 hours to amplify the viral vector in the cells on **Plate_B**.

Day 6-14.
---------------
1. Monitor the cells for the development of virus-induced CPE or GFP expression if you are making GFP-expressing VSV. When 40-100% of the cells show signs, the supernatant can be harvested.
2. Harvest the supernatant and remove cells and cell debris by centrifugation for 10 min at 450xg or by filtering the supernatant with 0.45μm filter.

.. note::
  Amplification period depends on the RNA structure of the genome. Usually, reporter gene expression should be able to be seen by day 7-8.
