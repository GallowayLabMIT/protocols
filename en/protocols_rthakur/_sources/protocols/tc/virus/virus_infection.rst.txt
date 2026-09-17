
Viral transduction
==================

This protocol describes how to transduce cells with unconcentrated or concentrated virus (see :ref:`Virus Concentration <virus_concentration>` protocol).
The method for each is the same, though the volume of viral solution to add to the cells will differ (much more for unconcentrated virus).
Virus produced in HEK293T cells with the VSV-G envelope protein can be used to transduce either human or mouse cells.

Before beginning, calculate the amount of virus to use. The following calculations are for transduction in a 96-well plate;
volumes can be scaled up accordingly for other plate sizes. Below are three common scenarios for virus amounts:

    - As an initial rule-of-thumb, ~1% of the total virus produced in one 10cm dish (e.g., 1-2 µL if concentrated and resuspended in 200 µL total) 
      is a good starting place for transducing one well in a 96-well plate.
    - When transducing to calculate viral titer, follow the :doc:`Measuring viral titer</protocols/tc/virus/viral_titer>` protocol, transducing several wells with a serial dilution of the virus.
    - If the viral titer (transducing units, TU, per µL) is known, calculate the volume to use based on the number of cells and the desired multiplicity of infection (MOI): 
    
        virus volume (µL) = # cells * MOI (TU/cell) / titer (TU/µL)

    Typically, an MOI of 0.3 or lower is used to ensure single-copy transduction. An MOI of 3 or higher is useful to ensure most of the cells are transduced with at least one copy.

.. note::
    Viral titer is reported to decrease during freezing and thawing. Therefore, you may wish to increase the amount of virus used for every freeze-thaw cycle.
    However, we have not rigorously quantified the degree to which this matters, so it may be fine to ignore this for few freeze-thaw cycles.
    It is best practice to store an aliquot of concentrated virus for titering, separate from the main aliquot for later transduction.

Cells may be transduced in suspension (i.e., at the same time as seeding) or after plating. Transduction is more efficient in suspension,
and efficiency can be increased for plated cells through spinfection. However, there may be a tradeoff between efficiency and cell viability.
All three methods are described below.

.. important::
   We use precautions beyond those for normal BL2 tissue culture when transducing any human-infectible virus. Read over the 
   :doc:`/protocols/tc/virus/virus_safety` protocol before beginning.


.. _plated:

Transduction of plated cells
----------------------------

1. The day before (18-24 hours prior), seed cells on plates with the appropriate coating. Seeding densities vary by target cell type.
   Typical densities are 10k cells/well for mouse embryonic fibroblasts and 10-15k cells/well for hiPSCs.
2. Combine the calculated amount of virus with the appropriate amount of media and 1000X polybrene. For a 96-well plate, this is:

    =============================== =================
    Component                        Volume
    =============================== =================
    Virus                            calculated above
    1000X polybrene                  0.1 µL
    Media                            to 100 µL
    =============================== =================

    .. tip::
        Since the amount of polybrene for a single well is so small, if you are not infecting several wells with the same virus, you may wish to make a media-polybrene master mix.
        For instance, make a virus-media mix (without polybrene) to 50 µL/well, then add 50 µL/well of a 2X polybrene + media solution.

    .. note::
        When transducing unconcentrated virus, the virus volumes may be large. Calculate amounts to add at least a half-well volume (e.g., 50 µL for a 96-well plate) of fresh
        media per well, even if this leads to a larger total well volume. This will make sure the cells have enough fresh media to stay healthy. Don't forget to
        adjust the volume of polybrene if the total well volume changes!

3. Aspirate the media from the cells.
4. Add the virus mix to each well.
5. The next day (1 day post-infection, dpi), aspirate and replace with fresh media. This is a good time to add any small molecule inducers, if applicable.
6. Continue culturing cells, observing proper virus precautions. Typically, a good end point for flow cytometry is 3 dpi.

.. important::
    Viral particles are no longer present after 3 days AND 2 media changes. Use proper :doc:`virus safety </protocols/tc/virus/virus_safety>` until then.


.. _suspension:

Transduction of cells in suspension
-----------------------------------

1. Coat plates. Do this first to provide sufficient time for coating (e.g., at least 10 min for 0.1% gelatin), as plates will be used at step 5.
2. Dissociate and count the cells that you will transduce.
3. Resuspend cells in fresh media at **double** the final concentration.
   For instance, if using 20k cells/well in a 96-well plate (a typical amount for HEK293T cells), resuspend at a concentration of 20k cells per 50 µL.
   To this mix, add 2X polybrene (i.e., 1:500 dilution of the 1000X stock).

.. note:: Polybrene can be added either to the cell solution or to the virus-media mix (next step). Typically, adding to the cells is easier because it reduces pipetting.

4. Combine the calculated amount of virus with the appropriate amount of media to a **half-well volume**. For a 96-well plate, this is 50 µL/well.
5. Aspirate the coating from the prepared plate and add a half-well volume of the cell solution to each well (e.g., 50 µL/well for a 96-well plate). Use the multichannel for easier pipetting.
6. Add a half-well volume of the virus-media mix to the appropriate wells and pipet to mix. Each well should now contain a full well volume of cells, polybrene, virus, and media.
7. The next day (1 day post-infection, dpi), aspirate and replace with fresh media. This is a good time to add any small molecule inducers, if applicable.
8. Continue culturing cells, observing proper virus precautions. Typically, a good end point for :doc:`flow cytometry </protocols/tc/tc-basics/flow_cytometry>` is 3 dpi.

.. important::
    Viral particles are no longer present after 3 days AND 2 media changes. Use proper :doc:`virus safety </protocols/tc/virus/virus_safety>` until then.

    
.. _spinfection:

Spinfection
------------

After following the transduction protocols above for either plated cell or cells in suspension, spinning the plate can increase transduction efficiency.
This may help the viral particles settle on, and ultimately be taken up by, the cells.
The combined protocol of transduction plus spinning is dubbed "spinfection."

1. Immediately after combining the virus with cells, polybrene, and fresh media as described above (with either :ref:`plated cells <plated>` or cells :ref:`in suspension <suspension>`), 
   move the plate into the bottom TC centrifuge rather than into the incubator.

.. important:: Cover the centrifuge buckets with the plate spinner tray caps.

2. Centrifuge the plate at 1500 x g for 30 min at 32ºC.

.. note:: The centrifuge won't heat to 32ºC before the spin, but it will warm up during.


1. After the spin is complete, transfer the plate to the 37ºC incubator. Continue as normal with the 1 dpi media change and subsequent treatments, readouts, etc.
