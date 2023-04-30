==================
Cell Line Creation
==================


.. time:: 1 month

    While the initial transfection does not take very long, the selection
    process takes a long time!

.. note::
    Except for day 0, all steps are the same for the creation of PiggyBac, Crispr,
    or TALEN cell lines

    This protocol is still in development! In particular, for PiggyBacs, the ratio of
    transposase to integration plasmid is a key variable that must be tuned!

    An efficient selection method has also not been fully tested.

Day -1
~~~~~~
Seed your cells such that they will be around 30-40% confluent on the next day. There is an
extended selection outgrowth period required, which means we should start with lower confluence.
Recommended rough seeding counts are:

=========       ============================
Cell type       Seeding amount (per 96 well)
=========       ============================
293T            12.5k cells
U2-OS           7.5k cells
=========       ============================

Day 0
~~~~~~
Follow the step for the cell line type to generate
    - PiggyBac
        - Co-transfect the PiggyBac plasmid alongside your plasmid containing PB recognition sites at a 3:1, template:transposase mass ratio.
    - Crispr
        - Co-transfect the Crispr/guide plasmid alongside your plasmid containing locus-specific recognition sites at a 1:1 mass ratio.
    - TALEN
        - Co-transfect the TALEN-R and TALEN-L plasmids alongside your plasmid containing locus-specific recognition sites at a 1:1:1 mass ratio.

.. note::
    When transfecting, leave some untransfected wells where you just add the KO-DMEM/PEI master mix, without plasmids.
    This allows you to tell if your selection is working as expected, and also gives you a proxy for how much PEI-mediated
    cell death you are seeing.

Day 1
~~~~~~
Media change into selection media. Tested concentrations for PiggyBac are:

=========   ====================
Cell type   Puro
=========   ====================
293T        1.0 ng/mL (10,000x)
U2-OS       0.25 ng/mL (40,000x)
=========   ====================

Day 2-4
~~~~~~~
Continue selecting the cells until decent cell death occurs, or the cells are too dense.

.. note::
    Puromycin at the given concentration should decidedly kill your untransfected wells.
    If you do not see sufficient cell death, try using a different aliquot.


Day 5 - Week 2
~~~~~~~~~~~~~~
Dilute cells into both 96-well plates (one per condition) and onto 24 well plates for outgrowth.

Onto the 96-well plates, hard dilute to ~2 cells per well and use 200 uL of media per well (for 40 cells per mL).
The extra media ensures that the plate will not fully evaporate over the next week.
If you need
a very large fold dilution, it is more accurate to do this as a stepwise dilution in conical tubes
(e.g. first a 1000x dilution, then another 1000x dilution).


For the 24-well plates, dilute to the following amount:

=========       ============================
Cell type       Seeding amount (per 24 well)
=========       ============================
293T            5k cells
U2-OS           2k cells
=========       ============================

This reseeding should proceed for about a week, until cells finish outgrowing.


Week 2 + 1 day
~~~~~~~~~~~~~~
After cells have adhered to the 24-well plates, switch back into selection media if
some non-integrated cells are visible via microscopy, and maintain it until these cells
have  died off.


Week 3
~~~~~~
At this point, you should see round colonies coming from either outgrowth condition.

.. figure:: /img/post_pb_dilution.png
    :width: 50%
    :align: center

    Example of what outgrowth looks like when grown out from a single-cell dilution.
    This is one well in a 96-well dilution plate.

If the overall integration percentage is high enough, you can do FACS or the BioMicroCenter
single-cell sorting to isolate clonal lines. If not, you can use the microscope to re-pick.

Clonal selection or enrichment via flow sorting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. time:: 2 hours pre-flow-sort, 20 minutes per sample for flow sorting (min 90 minutes of sort time).

.. note::

   This assumes that you are sorting on the Sony in the flow core.
   You can review the `Sony SOP <https://docs.google.com/document/d/1toqMY_qnDy0_YDkcEr2ktDJWcteKe0Pj42_scukqT5s/edit?usp=sharing>`__

1. Two to three days before the sort, make sure you have enough cells going for conditioned media collection.
   A T75 flask of 293Ts or whatever cell type you are using are a good source for this.
2. The day before the sort, make sure you have enough cells to sort. You should have more than a million cells,
   ideally several million.
3. Prepare your destination tubes and plates. For tubes, if your media does not contain FBS, it is recommended
   to coat the inside of the tubes with 7.5% BSA solution (put ~1mL in, swirl it around, aspirate). For plates,
   remember to gelatin coat.
4. Prepare conditioned media. Collect 1-2 day old media from cells, and filter through a 0.22 micron filter. Combine
   this 1:1 with fresh media.
5. Spin down cells, as if you were passaging. Resuspend the cells and count them.
6. Resuspend cells to a final volume of 2-5 million cells per mL.
7. Add the prepared conditioned media to your tubes and plates to be sorting into.
8. Prep a box to bring with you to flow sorting. You should bring:
   
   - A P1000 and tips.
   - Gloves
   - Prepared tubes and plates to sort onto.
   - An extra plate for aligning, if sorting onto plates.
   - Falcon tubes with cell strainer caps.
   - Enough ice for how many plates you are sorting onto. Ideally, cells stay directly touching the ice once they are sorted.

9. Bring your stuff to the flow core and sort!

.. note::

    If sorting onto plates, you should update the settings to place 100 cells in well A1, with 1 cell in other wells.
    This ensures that you will be able to locate the cells during outgrowth.

10. Return your cells to the **quarantine** incubator as quickly as possible.
11. At the end of the week, you likely will need to "top off" media to address evaporation.
12. One week later, you should be able to locate colonies under the microscope.
13. One week after that, passage cells onto 6-well plates.

Repicking
~~~~~~~~~
Repicking requires some trial and error using a pipette tip, but can get good enrichment of a target colony relatively quickly.

1. View the well of interest under the Keyence. Mark where the colony is on the top of the plate.

2. Prepare gelatin-coated destination plates. These should typically be 96 well plates. Fill the plates with media.

3. In the BSC, take a P200 tip, set to 50uL and depress the plunger. Scrape the pipette tip in small circles in the target area
   of the source plate, while slowly withdrawing media to suck up the cells as you scrape them off the bottom.

4. Deposit the 50 uL of cells into the destination plate.

5. Check the scraped regions under the Keyence, repeating if you missed the desired colony. If the media level in the source plate
   gets too low, just add more media to that well.
