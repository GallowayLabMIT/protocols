========================================================
MEF-to-iMN Reprogramming
========================================================

Our lab uses the reprogramming of mouse embryonic fibroblasts (MEFs) to induced motor neurons (iMNs) as a testbed system to study the process of cell fate transitions. To initiate and study reprogramming, a number of common lab protocols are combined, including virus production, CellTrace Labeling, and dissociation using DNAse and Papain. 

This protocol outlines the timeline of MEF-to-iMN reprogramming and links to protocols as they are appropriate in the timeline. 

.. _platEreprogram:

Days 1 - 6: Production and transdcution of viruses encoding reprogramming factors
---------------------------------------------------------------------------------
See :ref:`here for the complete Plat-E virus production protocol <platEProd>`. 

See :ref:`here for the complete 293T virus production protocol <virusProd>`. 

At minimum, iMN reprogramming requires the transduction of motor neuron-specific transcription factors. Typically, the oncogenes p53DD and hRasG12V are also introduced to enhance reprogramming efficiency. The following plasmids are frequently used as sources of motor neuron TFs or oncogenes and are encoded on retroviral backbones compatible with production in Plat-E cells.

=================   ================================
**pKG number**      **Plasmid Name**
=================   ================================
pKG00121              pMXs-Ascl1
pKG00010              pMXs-Brn2
pKG00003              pMXs-Myt1L
pKG00006              pMXs-Ngn2
pKG00009              pMXs-Isl1
pKG00008              pMXs-Lhx2
pKG01169              pMXs-NIL
pKG01574              pMXs-LNI3xHA
pKG00060              pMXs-p53DD
pKG00121              pMXs-hRasG12V
pKG00121              pMXs-hRasG12V-IRES-p53DD
pKG00121              pMXs-Snap-p53DD-IRES-hRasG12V
=================   ================================


Day 1:
######

1. Seed 700,000 - 850,000 Plat-E cells per well of a :ref:`gelatin-coated <gelatin>` 6-well for each virus to be made.

   - Each well of a 6-well plate makes approximately 1.1 mL of virus. This is exactly enough to transduce 100 wells of 96-well scale (11 μL of virus per well of a 96-well plate). If more virus is needed, additional Plat-E wells should be seeded.

.. note::
	AMB uses 700,000 Plat-E cells, NBW uses 850,000 Plat-E cells to similar results.

.. tip::
	If starting from frozen, **start growing Plat-E cells 1 week prior** - they will be slow growing at first (don't change culture medium during the first 3 days). Split Plat-Es 4X-6X every 2-3 days when culture reaches 70-90% confluency.

2. If using lentiviruses or other 293T-produced viruses that will be concentrated before infection, seed 293Ts on gelatin-coated or 10 cm dishes or in 6-well plates, depending on needed scale. See virus :ref:`production protocol <virusProd>` for more details.
3. Thaw MEFs on to gelatin-coated 10 cm dish or gelatin-coated T-75 flask. Expect 2-3 million MEFs to be recovered per frozen vial. 

Day 2:
######

3. If using 293T-produced viruses, transfect transfer plasmids (containing your gene of interest), packaging, and envelope plasmids. Do this early in the day, as the media is changed 6-8 hours after transfection. 
4. Transfect Plat-E cells using 1.8 μg of DNA per well of the 6-well plate. Typically, this is done late in the afternoon (~4:00 PM).
5. Media change 293Ts 6-8 hours after transfection. Remove media and add back 1.25 mL (for 6-well scale) or 6.5 mL (for 10 cm scale) of DMEM + 10% FBS + **25 mM HEPES**. 

Day 3:
######

6. Media change Plat-E cells. Remove media and add back 1.25 mL DMEM + 10% FBS + **25 mM HEPES** per well. Typically done in the morning around 10:00 AM to minimize PEI-related toxicity. 
7. If using 293T-produced viruses, harvest virus-containing media 18-24 hours after the previous media change. Replace with fresh media so that you can collect more virus the next day. Store collected virus in the 4℃ refrigerator overnight.
8. Seed MEFs

   i.  Coat wells in 0.1% gelatin for approx. ~10 min.
   ii. Seed at 10k cells/96-well. For larger sizes, scale accordingly according to surface area
    
=================   ==========================   ===============================================================
**Culture plate**    **Scale factor**              **# of 6-wells of Plat-E you'll need for a full plate**
=================   ==========================   ===============================================================
6-wells              30                            2
12-wells             11                            1.5
24-wells             6                             1.5
48-wells             2.6                           1.5
96-wells             1                             1
=================   ==========================   ===============================================================

Day 4 (-1 day post infection):
##############################

9. If using 293T-produced viruses, harvest (for the last time), filter, and begin concentrating each virus.
  
   i. Harvest virus-containing media 18-24 hours after the previous collection
   ii. Pool virus-containing media from with collection day 1
   iii. Filter media using a 0.45 μm syringe filter
   iv. Add Lenti-X concentrator.
   v. Store virus in the 4℃ refrigerator overnight to precipitate the virus.

10. Harvest and filter each Plat-E virus using a 0.45 μm syringe filter ~24 hours after previous media change. Replace media on Plat-E cells so that you may collect virus again the next day.

    i. For conditions using the 6F transcription factor cocktail, the viruses encoding the 6 TFs (Brn2, Ascl1, Myt1L, Ngn2, Isl1, Lhx3) can be filtered through the same syringe together to simplify virus mixing.


.. note::
   You can either 1. filter each virus then mix together (minimizes filtering) or 2. mix altogether then filter (standardizes mixing). Because filtering is the most annoying step, it is advised to minimized filtering.

   Examples of mixing AFTER filtering

   i. Example - 6F alone (96-well = 100 µl total/96-well):

      *For 1 rxn, 96-well*: 66 µL 6F (= 11 µL PER FACTOR*6) + 34 µL DMEM + 0.1 µL polybrene (1,000X) = 100 µL total/96-well

      *For 3.5 rxn, 96-well*: 231 µL 6F + 119 µL DMEM + 0.35 µL polybrene (1,000X) = 350 µL total for 3.5 96-wells

   ii. Example - 6F + DD + RR (96-well = 100 µL total/96-well):

       *For 1 rxn, 96-well*: 66 µL 6F + 11 µL p53DD + 11 µL hRasG12V + 12 µL DMEM + 0.1 µL polybrene (1,000X) = 100 µL total/96-well

       *For 3.5 rxn, 96-well*: 231 µL 6F + 38.5 µL p53DD + 38.5 µL hRasG12V + 42 µL DMEM + 0.35 µL polybrene (1,000X) = 350 µL total for 3.5 96-wells

11.   Mix Plat-E retroviruses as outlined in your experimental design and according to the Plat-E production protocol. Typically 11 μL of each Plat-E retrovirus  per well of a 96-well plate. Only retroviruses are included on -1 dpi.
12.   Remove media on MEFs and replace with your completed virus mixtures. 
13.   Incubate cells overnight with virus. 

Day 5 (0 days post infection):
##############################

14.  If using 293T-produced viruses, centrifuge precipitated virus at 4℃ as described to concentrate. Remove supernatent and resuspend in desired volume with DMEM + 10% FBS. Typically 200 μL for each 10 cm dish of virus produced and 40 μL for each well of a 6-well used to produce the virus.
15.  Harvest and filter each Plat-E virus for the last time ~24 hours after previous virus collection. 
16.  Mix Plat-E retroviruses and 293T-produced viruses as outlined in your experimental design and according to their respective production protocol. Typically 11 μL of each Plat-E retrovirus and 2 μL of concentrated 293T-produced virus per well of a 96-well plate.
17.  Remove media on MEFs and replace with your completed virus mixtures. 
18.  Incubate cells overnight with virus.

.. tip::
    Before returning cells to the incubator, cells can be centrifuged to improve transduction efficiency. The protocol for :ref:`spinfection is here <spinfection>`.


Day 6 (1 day post infection):
#############################

19. ~24 hours after previous transduction, remove virus-containing media and replace with fresh media. 
20. If you are interested in early proliferation during reprogramming, perform :ref:`CellTrace Staining <cellTraceStaining>` on ths day.

Days 7 - 18: Media changes
--------------------------

Day 7 (2 days post infection):
##############################

No action required.

Day 8 (3 days post infection):
##############################

21. Media change plates to N3 media:

    i. N3 media = N3 base + BDNF/CNTF/GDNF (1,000X, 10 µg/mL) + FGF (10,000X, 100 µg/mL)
    ii. Spike in 1,000X RepSox to N3 media for desired experimental conditions.

Day 9 (4 days post-infection):
##############################

**Assays for early indicators of reprogramming potnetial are performed on this day.**

22. If assaying early indicators of reprogramming potential, the following assays are typically performed on this date.

    1. Flow cytometry quantification of CellTrace dilution.
    2. Nascent transcription rate via :ref:`EU incorporation<EUclick>`.
    3. Protein expression via antibody staining :ref:`antibody staining<antibodyStaining>`
    4. And many others...

If assaying actual reprogramming rates, no action required on this day.

Days 10 (5 dpi), 12, ..,. 18 (13 dpi):
######################################

23.	Change N3 media every 2 days (can do 3 days if after ~8 days and weekend but 2 is ideal) until done (usually 14 dpi).

.. note:: 
    After 8 dpi, it is recommended to dissociate with (:ref:`DNAse/Papain <MNdissociate>`) instead of trypsin

Day 19 (14 dpi): Assay reprogramming rate
------------------------------------------

24. Assay reprogramming rate via microscopy or flow cytometry. 