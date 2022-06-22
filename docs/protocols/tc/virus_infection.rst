
Transduction with concentrated virus
====================================

This protocol describes how to transduce cells with concentrated virus (see :ref:`Virus Concentration protocol <virus_concentration>`).
Virus produced in HEK293T cells can be used to transduce either human or mouse cells.
The following calculations are for transduction in a 96-well plate; volumes can be scaled up accordingly for other plate sizes.

This protocol describes transduction of both :ref:`plated cells <plated>` and :ref:`cells in suspension <suspension>`.

.. tip::
   Virus infection is more efficient if it is done at the same time as seeding.

.. warning::
    Since virus produced in HEK293T cells is able to infect human cells, be sure to use proper PPE (i.e., lab coats, disposable sleeves) and wipe down hoods with Pre-Empt after use.

.. _plated:

Transduction of plated cells
----------------------------

1. The day before (18-24 hours prior) infection, seed cells on 0.1% gelatin-coated plates. Seeding densities may vary, but typically this will be 10k cells/well for a 96-well plate.
2. Calculate the volume of concentrated virus to use per well.

    As an initial rule-of-thumb, ~1-2% of the total virus produced in one 10cm dish (e.g., 2-4 µL if concentrated and resuspended in 200 µL total) is appropriate for infection of one well in a 96-well plate.

.. note::
   If it is important to know the titer of the concentrated virus, an initial infection (transduction) can be performed to calculate this value before conducting experiments.
   See the :doc:`MOI Calculation </protocols/tc/moi>` protocol for more details.

.. note::
    Viral titer is reported to decrease during freezing and thawing. Therefore, it is recommended to double the amount of virus used for every freeze-thaw cycle.

3. Dilute virus in fresh media and polybrene (total volume = total well volume):

=============================== =============
Component                        Volume
=============================== =============
Concentrated virus               calculated
1000X polybrene                  0.1 µL
Media                            to 100 µL
=============================== =============

.. tip::
    Since the amount of polybrene for a single well is so small, it is recommended to infect many wells or make a media-polybrene master mix.

4. Aspirate the media from the cells.
5. Add the virus-media mix to each well.
6. The next day (1 dpi), aspirate and replace with fresh media.

.. note::
    Viral particles are no longer present after 3 days or 1 media change.

7. Continue culturing cells (e.g., select for integration) or proceed with end-point assay (e.g., flow cytometry).


.. _suspension:

Transduction of cells in suspension
-----------------------------------

.. warning:: TODO!