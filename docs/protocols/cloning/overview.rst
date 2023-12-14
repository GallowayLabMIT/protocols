Cloning Workflow Overview
=========================

Molecular cloning is the process by which we construct synthetic DNA sequences, aka how we build plasmids in lab. 
(Since, alas, we do not have cheap, multi-kilobase-scale DNA printer. Perhaps someday soon!) The broad outline of 
the workflow is described below and links to specific, relevant protocols at each step.

Step 1: Generate DNA fragments
------------------------------

To begin, we first must generate sufficient copies of the DNA fragments we want to stitch together, possibly with
defined 5\' and 3\' ends. Typically, these fragments are generated from existing sequences in lab, though they can
also be ordered from DNA synthesis companies.

Methods of DNA fragment generation include:

- PCR, with or without new ends added by primer overhangs
- Restriction digest
- :doc:`Annealing oligos <oligo_annealing>` synthesized by an external company (e.g., Genewiz)
- Ordering a long dsDNA sequence from an external company (e.g., gBlock from Genewiz)
- Obtaining an existing plasmid to use directly as a fragment (e.g., pPV plasmid for our :ref:`Golden Gate cloning scheme <_pPV-scheme>`)


Step 2: Assemble plasmids
-------------------------

Next, fragments are assembled into plasmids, circular pieces of DNA on the order of 1-15 kilobases. Plasmids are
the primary means by which we delivery DNA to mammalian cells. Assembly occurs in a biochemical reaction in a tube,
and efficiencies of these reactions vary widely.

Methods of plasmid assembly include:

- :doc:`Ligation <ligation_assembly>`
- :doc:`Gibson (aka Hifi) <gibson>` 
- :doc:`Gateway <lr_cloning>`
- :doc:`Golden Gate <golden_gate>`


Step 3: Transform bacteria
--------------------------

The product of the assembly reaction is then :doc:`transformed <transformation>` into bacteria. This serves two functions:

1. To select for correctly formed products via antibiotic or other selection methods.

    Bacteria are plated on agar containing antibiotic(s) for which the desired plasmid confers resistance.
    Non-transformed bacteria and bacteria transformed with assembly products (or original reactant plasmids)
    containing the wrong resistance marker die.

    Another selection method is the ccdB protein: when expressed from a plasmid, this protein kills the host cell.
    When the ccdB expression sequence is removed in your desired plasmid, this is useful for selecting against
    cells harboring the original plasmid or other incorrect assembly products. This strategy is used in Gateway cloning.

2. To generate single clones of bacteria harboring plasmid products for screening.

    Transformed bacteria are plated at a density sparse enough to allow single clones to be isolated. This
    may mean scaling down the reaction for highly efficient assemblies, or scaling up the reaction (e.g.,
    using more cells, increasing the reaction volume) for very inefficient reactions.


.. _screening:

Step 4: Screen colonies
-----------------------

Next, single colonies are screened to determine whether they contain the desired plasmid. While the selection
step eliminates many incorrect plasmid products, it may not be possible by selection alone to identify correct 
clones (e.g., when a plasmid used as a template for generating fragments has the same resistance marker as the 
desired plasmid, or when there are multiple fragments to assemble).

The standard approach for screening colonies is :doc:`colony PCR <colony_pcr>`, since the tiny amount of plasmid DNA present in a
small bacterial colony is sufficient to generate results. Other screening approaches, such as plasmid digestion,
typically require larger volumes of DNA and are therefore more common as a secondary confirmation metric. Of course,
screening at this stage can be skipped, but this is only advisable for extremely efficient reactions (or if 
reagent/sequencing/time costs are not an issue).

As colonies are screened, a portion of the colony is often reserved to enable multiple bacterial cultures to be
grown easily. For colony PCR, this involves streaking the implement used to pick the colony (e.g., a toothpick or
pipette tip) on a fresh agar plate. Alternatively, for large colonies, a portion of the colony may be picked for screening,
leaving a portion remaining on the plate for later use.


Step 5: Purify plasmid DNA
--------------------------

To obtain sufficient quantities of the putatively correct plasmid for use or further confirmation, we next 
inoculate a liquid culture from the colony of interest (e.g., from the original plate or from a streaked plate
generated during screening). After growth for 12-16 hours, the plasmid DNA can be harvested from the bacterial
culture using a `miniprep kit <https://www.neb.com/en-us/protocols/2015/11/20/monarch-plasmid-dna-miniprep-kit-protocol-t1010>`_. 
Purified plasmid DNA should be assessed on the Nanodrop (or similar machine) to determine concentration and confirm purity.


Step 6: Sequence
----------------

The recent widespread availability of low-cost whole-plasmid sequencing has unmasked lurking issues in plasmid
preps, such as mutations, plasmid dimerization, and the presence of additional "piggy backing" plasmids---which 
may not be readily identifiable by Sanger sequencing and often lead to headaches down the line. Thus, it's usually 
a good idea to whole-plasmid sequence DNA vital to experimental workflows. 

However, at close to one-fourth the cost of whole-plasmid sequencing, traditional Sanger sequencing remains useful
in some circumstances. These cases include:

- Plasmids with small inserts/edits to existing plasmids that are fully covered by three or fewer ~800-1000 bp reads
- Intermediate plasmids where mutations outside of the sequenced region will not be passed on in the next cloning step
- Use as a screening step before whole-plasmid sequencing candidates from inefficient or error-prone assemblies


Step 7: Glycerol stock
----------------------

Once plasmids are sequence-confirmed, we want to save the bacterial clone harboring the plasmid so that we can 
purify more of it later. Bacteria streaked on agar plates only last on the order of ~1 month at 4ºC; for longer-term 
storage, we make a :doc:`glycerol stock <glycerol_stocking>` (in triplicate) that is added to our lab's shared set of stocks. 
To allow others in lab---and eventually the wider scientific community, upon publication---to access our plasmids, the 
sequence should be added to our existing plasmid database and assigned a ``pKG`` number for reference.

.. tip::

  Don't wait too long to stock plasmids! Stocking a giant batch all at once often feels tedious, while stocking a few 
  at a time may be more manageable. Also, you don't want your agar plate to dry out! If this does happen, or you are 
  otherwise unable to recover the bacterial clone harboring the plasmid, you can re-transform the plasmid according to the steps below.


Starting with an assembled plasmid
----------------------------------

To make a stock of a plasmid for which you only have a DNA prep (e.g., obtained from a collaborator, or the original agar plate dried out), 
simply transform (or re-transform) the plasmid directly without needing to reassemble it. This means you can skip Steps 1 and 2 above, beginning
directly with Step 3.

**Step 3:** :doc:`Transform <transformation>` chemically competent cells with 0.5 µsxL plasmid DNA.
   
   .. tip::
    The transformation should be highly efficient since all the DNA is (presumably) the correct plasmid product. You may want to
    scale down the volume of cells or plate only a fraction of the reaction to avoid overcrowding of the colonies the next day.
    Be careful not to overgrow such that the colonies merge!

**Step 4:** It is usually okay to skip the initial screening step if your plasmid DNA is pure. Instead, pick 1-2 colonies directly 
into liquid cultures and shake overnight at 30ºC. The next day, save ~2 uL to inoculate a new culture or streak onto a fresh plate.

**Steps 5-7:** Perform as described above.


Cloning Workflow Timeline
=========================

The timeline from cloning design to sequence-confirmed product is typically ~4 days, since several steps require 
time for bacterial growth. The sequence can accelerated in a pinch, with greater probability of error, reduced
efficiency, and additional reagent consumption.

Typical Timeline
----------------

**Day 1:** Generate fragments, assemble plasmids, transform bacteria (*incubate overnight*)

  Note that some assembly reactions may need to run overnight before transformation (e.g., Gateway or an inefficient Golden Gate).

**Day 2:** Screen colonies, start liquid cultures of candidates (*shake overnight*)

  If plates are streaked with colonies in the morning, cultures can usually be started from them in the evening.
  Otherwise, the streaked plates may need to incubate overnight.

**Day 3:** Purify plasmid DNA, send for sequencing (*typically next-day turn-around*)

  Same-day sequencing results are sometimes possible for Azenta/Genewiz orders submitted for 9am pickup; results
  usually are ready around 6pm.

**Day 4:** Asses sequencing results, start liquid cultures for glycerol stock (*shake overnight*)

**Day 5:** Make glycerol stock


Accelerated Timeline
--------------------

.. warning::

  This timeline is not recommended, since it is more error-prone and uses more reagents.

**Day 1:** Generate fragments, assemble plasmids, transform bacteria (*incubate overnight*)

  Even incubating at 37ºC, it is difficult to see colonies faster than 12-16 hours.

**Day 2 (am):** Screen colonies, start liquid cultures (*shake at 37ºC for ~8 hours*)

  Start a liquid culture directly for each picked colony; after screening, discard cultures for incorrect clones.

**Day 2 (pm):** Miniprep, send for Sanger sequencing (*by 7pm pickup*)

  Note that plasmid preps will likely have low concentrations after growing for an abbreviated period. You may 
  want to start new cultures to grow overnight and prep after the sequencing results come in on Day 3.

**Day 3:** Assess sequencing results

  Sequencing results may be ready before 6am, or not until 2pm---plan experiments accordingly.