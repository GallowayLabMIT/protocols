======================================
Virus production in HEK293T cells
======================================

.. _virusProd:

This protocol describes how to produce lentivirus and retrovirus in HEK293T cells, including an optional final concentration step.

.. time::
    4-6 days. Note that on the transfection day, you must change
    the media 6-8 hours after the transfection.

.. important::
   We use precautions beyond those for normal BL2 tissue culture when producing human-infectible virus. Read over the 
   :doc:`/protocols/tc/virus/virus_safety` protocol before beginning.

Setup
-------

The plasmids and exact amounts to use at each step vary based on the virus type (lentivirus or retrovirus) and scale.
We mostly make lentivirus in HEK293T cells, though we can also produce retrovirus for transduction of human cells (e.g., for 
human cell reprogramming). The protocol below is written for a default 10cm-dish scale (i.e., one virus per dish), which
is recommended. It seems that virus production is less efficient in a 6-well plate, so smaller production scales are 
not usually effective, especially if you'll be titering the virus.

Check out `this spreadsheet </docs/_static/files/2025.12.11_virus-production-transfection.xlsx>`__ as a template for the transfection calculations.
Note that the "transfer plasmid" refers to the plasmid containing the lentiviral backbone with your cargo between viral LTRs.
You'll also need to co-transfect separate packaging and envelope plasmids specific to the virus type.

**Scale:**

========    ===========    ========================    ===================    ============================    ========================
Scale       Area (cm^2)    Seeding amount (# cells)    Total DNA mass (µg)    Collection media volume (mL)    Concentrated volume (μL)
========    ===========    ========================    ===================    ============================    ========================
10cm        56.7            6.0 x 10^6 *               24                     6.5                             200
6-well      9.6             1.0 x 10^6                 4.1                    1.25                            40
========    ===========    ========================    ===================    ============================    ========================

If using a different virus production scale, the total DNA mass should be scaled by surface area.
The collection media volume should be roughly half of the standard amount of media used for that scale.

.. note::
   \* Lab members have successfully used seeding densities between 6 and 7.5 million cells per 10cm dish. We have not directly assessed how
   this variable impacts viral titer, though it is important to have an appropriate cell confluency for transfection the next day.
   For consistent titers across batches, use the same seeding density. Always ensure your cells are 
   growing healthily before seeding, as they will be under a lot of stress during the production process.

**Virus type:**

===========     ================================  ===================================
Type            Packaging plasmid                  Envelope plasmid
===========     ================================  ===================================
Lentivirus      psPAX2 (pKG0362, Addgene #12260)   pMD2.G (pKG0096, Addgene #12259)
Retrovirus      pIK-MLVgp (pKG0015)                pHDMG (pKG0022, Addgene #164440)
===========     ================================  ===================================

Typically, we prep common stocks of the packaging and envelope plasmids (TC aliquots box in Bruni 4ºC, additional aliquots in common box in Olaf -20ºC).
These are maxipreps normalized to 500 ng/µL, but double-check the concentrations on the tubes to be sure. We sequence-confirm each prep of these 
plasmids to make sure they are high quality.


Virus Production
----------------
The following is given for a 10cm-dish production scale. For other scales, substitute
the correct values from the scale table.

Day 0
*****
1. Seed HEK293T cells onto gelatin-coated 10cm dishes. (For other scales, use the correct seeding amount above.)

.. note::
   In theory, any HEK293T cells can be used to produce virus. In lab, we have the Lenti-X 293T line (`Takara <https://www.takarabio.com/products/gene-function/viral-transduction/lentivirus/packaging-systems-and-cells/lenti-x-293t-cells>`_)
   which is a particular HEK293T clone shown to produce high-titer lentivirus. However, in our hands, there is not much difference between
   these Lenti-X and regular HEK293T cells---so either cell line can be used effectively.

.. tip::
   If making many plates of virus, you'll need a lot of cells. A good rule of thumb is to culture one T182 flask of cells for every 
   ~6-8 10cm dishes you need. A very confluent T182 can yield 60 million cells, which is enough for 8 x 10cm dishes (7.5 million cells per dish).

Day 1
*****
Co-transfect your cells with transfer, packing, and envelope plasmids.

1. Prepare a mastermix of PEI and knockout DMEM. It is helpful to prepare a 110% master mix
   (include 10% extra mix) to account for pipetting losses. Ensure that you
   **add the PEI to the KO DMEM** and not in the other order.

   - As included in the transfection calculation spreadsheet, we use 1.33 mL of KO DMEM per 10cm dish (though the transfection seems relatively insensitive
     to this ratio).
   - The amount of PEI is set by the mass ratio of PEI:DNA experimentally determined for each batch, as for any PEI transfection.
     We use 24 µg total of DNA per dish.

2. Incubate the PEI-KO DMEM mastermix for 10-15 minutes at room temperature. While waiting, prepare the DNA mixes (next step).
3. Combine the transfer, packaging, and envelope plasmid DNA for each condition in the following ratios.

   =======      ==================  ===================  ==================
   Scale        Transfer            Packaging            Envelope
   =======      ==================  ===================  ==================
   Ratio        1                   1                    2
   10cm         6 µg                6  µg                12  µg
   6-well       1.02  µg            1.02  µg             2.05  µg
   =======      ==================  ===================  ==================

   - Use the calculation spreadsheet to determine appropriate volumes.
   - If you are transfecting multiple dishes per virus, consider mixing 10% extra of the final condition mix to account for pipetting loss when adding to the dishes.
   - When transfecting multiple virues, it can be helpful to create a mastermix of the packaging and envelope plasmids to reduce pipetting. Add these 
     to the empty condition mix tubes first, then add the transfer plasmid DNA.
   - It it important to **mix all the DNA together** before adding the PEI-KO DMEM mastermix in the next step. That way, the transfection complexes
     contain equal ratios of all the plasmids. (You don't have to pipet a ton, just don't add the packaging and envelope plasmids to the PEI-KO DMEM
     mastermix separately.)

4. Pipet the PEI-KO DMEM mastermix into the DNA mixes to form the final condition mixes. Incubate at room temperature for 10-15 minutes.
5. Add the mixture *dropwise* and *evenly* around the dish, then gently rock to mix. Place the cells back in the incubator for 6-8 hours.

.. important::
      The six-to-eight hour timing is important for this protocol. We use a relatively large amount of transfected DNA, which means we are 
      also adding a high concentration of PEI. Media changing after 6-8 hours can greatly reduce transfection-related cell death.
      Changing the media sooner can also work, but it may reduce transfection efficiency and thus viral titer. Being consistent with the
      timing of this media change can help reduce variability in titer across batches of virus.

6. Six-to-eight hours after transfection, replace the media on the plates with HEPES-buffered
   DMEM + 10% FBS. Use the collection volume of media, which is 6.5 mL for a 10cm dish.

   The recipes to prepare both the 1M stock solution of HEPES and the HEPES-buffered DMEM can be :ref:`found here<HEPES>`.
   Typically, there is a common bottle of HEPES-buffered DMEM in Bruni (TC 4ºC).

.. warning::
   Viral particles may be present after the first media change.
   Be sure to use proper PPE (i.e., lab coats, disposable sleeves) and wipe down the hood with Pre-Empt after use, from here on!
   **If the virus contains oncogenes or inhibitors of tumor suppressors (e.g., HRASG12V, p53DD), BL2+ precautions are required.**
   See the :doc:`/protocols/tc/virus/virus_safety` protocol for details.

Day 2
******

1. 18-24 hours after the last media change, collect the media,
   replacing it with the same collection volume of fresh HEPES-buffered DMEM.

2. Store the collected media at 4°C. The collected media from separate days can be stored in the same conical tubes. 

.. note::
   Two collections (on Days 2 and 3) elicit sufficiently high titer virus.
   However, a third collection (on an extra day between Days 2 and 3 written here) may further increase titer.

Day 3
*******

1. On the last day of collection (typically the second collection), combine all collected media for the same virus. If making multiple 
   dishes of the same virus, the collected media can be combined into a single tube (two days of collection for 3 dishes can fit into 
   a single 50 mL conical). Filter the media through a 0.45 µm filter using a syringe to remove cells/cell debris.

.. note::
   It is okay to store unfiltered or filtered virus at 4ºC for several days before concentrating or transducing cells.

2. Then, either:

   a. Proceed to the :ref:`virus_concentration` protocol (below). This is useful for long-term storage.
   b. Within a few days of collection, transduce cells (:doc:`protocol here </protocols/tc/virus/virus_infection>`) directly with unconcentrated virus.

.. note::
   Unconcentrated virus appears to lead to more cell death than does concentrated virus, possibly because a much larger volume of viral media is required.
   Therefore, concentrating the virus is advised.


.. _virus_concentration:

Virus Concentration
-------------------

.. time::
	1 hour in-TC time, 1 day overnight time

1. To the collected and filtered virus, add 1/3 volume of Lenti-X concentrator (e.g., for 30 mL of virus, add 10 mL of Lenti-X). Mix by inverting several times.
2. Store at 4°C overnight.
3. The next day, centrifuge at 1500 x g at 4°C for 45 minutes (use the lower centrifuge). Be sure to use the caps/lids on the centrifuge buckets.
4. Aspirate the supernatant. There will be a little liquid left; this is okay.
5. Resuspend the pellet gently in the remaining liquid. Add media to reach the desired final volume suggested in the "Concentrated volume" column of the scale table above.

.. note::
   Measuring to the exact desired final volume can be tedious. If you are planning to titer the virus before use, it is okay to resuspend in a 
   set volume without confirming the final volume, as titer is a concentration value (transducing units per µL).
   Of course, measured titers will be more consistent if you resuspend precisely.

6. Use or store the concentrated virus.
   
   a. To use: Transduce cells according to the :doc:`Transduction of concentrated virus <virus_infection>` protocol.
   b. To store: Store the virus (or any remaining after transduction) in a cryovial at -80°C.

.. note::
   Store virus only in cryovials with threaded lids. Normal Eppendof tubes can pop open when cooling, which is an exposure risk.

.. note::
   Freeze-thaw cycles may affect transduction of concentrated virus. It is best practice to store an aliquot of concentrated virus 
   for titering, separate from the main aliquot for later transduction. However, we have not rigorously quantified loss in 
   effective titer over freeze-thaw cycles, so a limited number of freeze-thaw cycles may not have much of an impact.