========================================================
MEF-to-iPSC Reprogramming
========================================================
**Last updated: 3/31/2025 by MC**

This protocol outlines the timeline of MEF-to-iPSC reprogramming and links to protocols as they are appropriate in the timeline.
MC is currently optimizing this protocol to produce iPSCs using Oct4-GFP trasgenic MEFs.

.. _MEF_to_iPSC:

Days 1 - 6: Production and transduction of viruses encoding reprogramming factors
---------------------------------------------------------------------------------
See :ref:`here for the complete Plat-E virus production protocol <platEProd>`. 

At minimum, iPSC reprogramming requires the transduction of stem cell-specific transcription factors. Oncogenes such as p53DD are being evaluated for their ability to improve reprogramming efficiency. The following plasmids are frequently used as sources of stem cell TFs or oncogenes and are encoded on retroviral backbones compatible with production in Plat-E cells.

Single TF and polycistronic cassettes are being tested, with additional polycistronic cassettes in development.

=================   ================================
**pKG number**      **Plasmid Name**
=================   ================================
pKG03903             pMXs-Oct4
pKG03904             pMXs-Klf4
pKG00011             pMXs-Sox2
pKG01962             pMXs-MKOS
pKG03523             pMXs-CIDD-WPRE
pKG03525             pMXs-CISDD-WPRE
pKG03526             pMXs-SDDIC-WPRE
pKG03336             pMXs-SDDIR
pKG00060             pMXs-p53DD
pKG01292             pMXs-Snap-p53DD-IRES-hRasG12V
=================   ================================


Day 1:
######

1. Seed **650,000** Plat-E cells per well of a :ref:`gelatin-coated <gelatin>` 6-well for each virus to be made.

   - Each well of a 6-well plate makes approximately 1.1 mL of virus. This is exactly enough to transduce 100 wells of 96-well scale (11 μL of virus per well of a 96-well plate). If more virus is needed, additional Plat-E wells should be seeded.

.. tip::
	If starting from frozen, **start growing Plat-E cells 1 week prior** - they will be slow growing at first (don't change culture medium during the first 3 days). Split Plat-Es 4X-6X every 2-3 days when culture reaches 70-90% confluency.

2. Thaw MEFs on to gelatin-coated 10 cm dish or gelatin-coated T-75 flask. Expect 2-3 million MEFs to be recovered per frozen vial. 

Day 2:
######

3. Transfect Plat-E cells using 1.8 μg of DNA per well of the 6-well plate. Typically, this is done late in the afternoon (~4:00 PM).
4. Check on MEFs to see if they need a media change.
   
Day 3:
######

5. Media change Plat-E cells. Remove media and add back 1.25 mL DMEM + 10% FBS + **25 mM HEPES** per well. Typically done in the morning around 10:00 AM to minimize PEI-related toxicity. 
6. Seed MEFs

   i.  Coat wells in 0.1% gelatin for approx. ~10 min.
   ii. Seed at **5k** cells/96-well in DMEM + 10% FBS.

.. note::
    MC has been doing triplet plate assays to allow for 4 dpi flow, miscroscopy, and 21 dpi flow.
    Testing O+S+K and MKOS with oncogenes.

Day 4 (-1 day post infection):
##############################


7.  Harvest and filter each Plat-E virus using a 0.45 μm syringe filter ~24 hours after previous media change. Replace media on Plat-E cells so that you may collect virus again the next day.
8.    Mix Plat-E retroviruses in DMEM/FBS as outlined in your experimental design and according to the Plat-E production protocol, 11 μL of each Plat-E retrovirus  per well of a 96-well plate.
9.    Remove media on MEFs and replace with your completed virus mixtures. 
10.   Incubate cells overnight with virus. 

Day 5 (0 days post infection):
##############################

11.   Harvest and filter each Plat-E virus for the last time ~24 hours after previous virus collection. 
12.   Mix Plat-E retroviruses as outlined in your experimental design and according to their respective production protocol. Typically 11 μL of each Plat-E retrovirus and 2 μL of concentrated 293T-produced virus per well of a 96-well plate.
13.   Remove media on MEFs and replace with your completed virus mixtures. 
14.   Incubate cells overnight with virus.

Day 6 (1 day post infection):
#############################

19. ~24 hours after previous transduction, remove virus-containing media and replace with fresh media.

.. note::
   For R1-R3, MC has replaced media with DMEM+10% FBS, but will be trying :ref:`iPSC reprogramming media <iPSCmedia>` on R4.
    
20.  Perform :ref:`CellTrace Staining <cellTraceStaining>` to assess early proliferation.

Days 7 - 23: Media changes
--------------------------

Day 7 (2 days post infection):
##############################

No action required.

Day 8 (3 days post infection):
##############################

21. Media change plates to :ref:`iPSC media<iPSCmedia>`:

    i. Spike in 1,000X RepSox to media for desired experimental conditions.

.. note:: 
    MC has been using RepSox in all experimental conditions except Puro controls.
    In R3 Puro controls did not recieve LIF.

Day 9 (4 days post-infection):
##############################

**Assays for early indicators of reprogramming potential are performed on this day.**

22. Perform :ref:`Snap-tag labeling<snaptag>`.
23. Peform flow cytometry to quantify CellTrace dilution and Snap signal.

Days 10 (5 dpi), 12, ..,. 23 (19 dpi):
######################################

23.	Change iPSC media every 2 days until done.

.. note::
    MC has gone to 21 dpi in R1 and R2, 14 dpi in R3, and will do 21 dpi for R4.

Day 19 (21 dpi): Assay reprogramming rate
------------------------------------------

1.  Fix one plate for :ref:`immunofluorescent staining <antibodystaining>` and microscopy.
2.  Perform flow cytometry to measure Oct4-GFP expression.

.. note:: 
    After 8 dpi, it is recommended to dissociate with (:ref:`DNAse/Papain <MNdissociate>`) instead of trypsin.
    MC has been using DNASe/Papain.
