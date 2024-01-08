
Transduction with concentrated virus
====================================

This protocol describes how to transduce cells with concentrated virus (see :ref:`Virus Concentration <virus_concentration>` protocol).
Virus produced in HEK293T cells with the VSV-G envelope protein can be used to transduce either human or mouse cells.
The following calculations are for transduction in a 96-well plate; volumes can be scaled up accordingly for other plate sizes.

**Calculate amount of virus to use**

Before beginning, calculate the volume of concentrated virus to use per well.

As an initial rule-of-thumb, ~1-2% of the total virus produced in one 10cm dish (e.g., 2-4 µL if concentrated and resuspended in 200 µL total) may be appropriate for infection of one well in a 96-well plate.
(FURTHER VALIDATION REQUIRED.)

.. note::
   If it is important to know the titer of the concentrated virus, an initial infection (transduction) can be performed to calculate this value before conducting experiments.
   See the :doc:`MOI Calculation </protocols/tc/virus/moi>` protocol for more details.

.. note::
    Viral titer is reported to decrease during freezing and thawing. Therefore, you may double the amount of virus used for every freeze-thaw cycle. NOTE: FURTHER TESTING NEEDED.

.. note::
    Generally, higher total virus per well increases infection efficiency.

**Protocol**

This protocol describes transduction of both :ref:`plated cells <plated>` and :ref:`cells in suspension <suspension>`.

.. tip::
   Virus infection is more efficient if it is done at the same time as seeding (i.e., in suspension).

.. warning::
    Since virus produced in HEK293T cells is able to infect human cells, be sure to use proper PPE (i.e., lab coats, disposable sleeves) and wipe down hoods with Pre-Empt after use.

.. _plated:

Transduction of plated cells
----------------------------

1. The day before (18-24 hours prior) infection, seed cells on 0.1% gelatin-coated plates. Seeding densities vary by target cell type. For mouse embryonic fibroblasts, this is typically 10k cells/well for a 96-well plate.
2. Dilute virus according to calculations in fresh media and polybrene (total volume = total well volume):

=============================== =============
Component                        Volume
=============================== =============
Concentrated virus               calculated
1000X polybrene                  0.1 µL
Media                            to 100 µL
=============================== =============

.. tip::
    Since the amount of polybrene for a single well is so small, it is recommended to infect many wells or make a media-polybrene master mix.

3. Aspirate the media from the cells.
4. Add the virus-media mix to each well.
5. The next day (1 dpi), aspirate and replace with fresh media.

.. note::
    Viral particles are no longer present after 3 days or 1 media change.

6. Continue culturing cells (e.g., select for integration) or proceed with end-point assay (e.g., flow cytometry).


.. _suspension:

Transduction of cells in suspension
-----------------------------------

1. Coat plates with 0.1% gelatin. Do this first to provide at least 10 min for coating (plates will be used at step 5).
2. Dissociate and count cells to infect.
3. Resuspend cells in fresh media at double the final concentration.
   For instance, if using 10k cells/well in a 96-well plate, resuspend at a concentration of 10k cells per 50 µL.
4. Dilute virus according to calculations in fresh media and polybrene (total volume = **half** total well volume):

=============================== =============
Component                        Volume
=============================== =============
Concentrated virus               calculated
1000X polybrene                  0.1 µL
Media                            to **50 µL**
=============================== =============

.. tip::
    Since the amount of polybrene for a single well is so small, it is recommended to infect many wells or make a media-polybrene or cells-polybrene master mix.

5. Add virus-media mix (50 µL or half well volume) to gelatin-coated plate. Then add cells (50 µL or half well volume) and pipette to mix.

.. tip::
    It is convenient to use a multichannel pipette to transfer the cells from a reservoir to the plate.

6. The next day (1 dpi), aspirate and replace with fresh media.

.. note::
    Viral particles are no longer present after 3 days or 1 media change.

7. Continue culturing cells (e.g., select for integration) or proceed with end-point assay (e.g., flow cytometry).

.. _spinfection:

Spinfection
----------------------------

After following the transduction protocols above for either plated cell or cells in suspension, additional spinning could increase infection efficiency. The combined protocol is dubbed "spinfection."

For the spinning steps follow the below protocol.

1. Move plate into TC centrifuge.

.. important:: Ensure to cover the centrifuge buckets with the plate spinner tray caps.

2. Centrifuge the plate at 1500 xg for 90 min at 32C.
3. Subsequently transferred to 37oC incubator.
