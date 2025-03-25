========================================================
Human Fibroblast to iMN Reprogramming
========================================================


This protocols outlines the reprogramming of human dermal fibroblasts (HDFs) to induced motor neurons (iMNs). 

This protocol outlines the timeline of Human Fibroblast to iMN reprogramming and links to protocols as they are appropriate in the timeline. 


Days 1 - 6: Production and transduction of viruses encoding reprogramming factors
---------------------------------------------------------------------------------

See :doc:`here for the complete 293T virus production protocol <../virus/virus_production>`. 

At minimum, iMN reprogramming requires the transduction of motor neuron-specific transcription factors. Typically, the oncogenes (p53DD, hRasG12V, c-MYC, myrAKT, BCL2) are also introduced to enhance reprogramming efficiency. The following plasmids are frequently used as sources of motor neuron TFs or oncogenes and are encoded on retroviral backbones compatible with production 273Ts.

=================   ================================
**pKG number**      **Plasmid Name**
=================   ================================
pKG00121              pMXs-Ascl1
pKG00010              pMXs-Brn2
pKG00003              pMXs-Myt1L
pKG00006              pMXs-Ngn2
pKG00009              pMXs-Isl1
pKG00008              pMXs-Lhx2
pKG00002              pMXs-NeuroD1
pKG01169              pMXs-NIL
pKG01574              pMXs-LNI3xHA
pKG00060              pMXs-p53DD
pKG00121              pMXs-hRasG12V
pKG00747              pMXs-myrAkt-P2A-BCL2
pKG00751              pMXs-cMyc
=================   ================================


Day 1:
######

1. Seed 6 million 293Ts in each :ref:`gelatin-coated <gelatin>` 10 cm plate for each virus to be made.

   - Each 10 cm plate makes 200 uL of concentrated virus. This is exactly enough to transduce 20 wells of 96-well scale (5 μL of virus per well of a 96-well plate, 2 days of infection). If more virus is needed, additional 10 cm plates should be seeded.

.. tip::
	If starting from frozen, **start growing 293Ts 1 week prior** - they will be slow growing at first (don't change culture medium during the first 3 days). Split 293Ts 4X-6X every 2-3 days when culture reaches 70-90% confluency.

    You will likely need 2 to 3 T-182 flasks of 293Ts per human reprogramming experiment.


Day 2:
######

1. Transfect transfer plasmids (containing your gene of interest), packaging, and envelope plasmids. Do this early in the day, as the media is changed 6-8 hours after transfection.
   :doc:`See here for the complete 293T virus protocol <../virus/virus_production>`.
2. Media change 293Ts 6-8 hours after transfection. Remove media and add back 6.5 mL of DMEM + 10% FBS + **25 mM HEPES**. 

Day 3 and 4:
############

.. warning:: 
    Be sure to use :doc:`BSL2+ precautions <../virus/virus_safety>` when working with the human-infectible retrovirus containing oncogenes.

1. Collect virus-containing media 18-24 hours after the previous media change in 50 mL conicals. Two plates can be combined into 1 tube. Replace with fresh media so that you can collect more virus the next day. Store collected virus in the 4℃ refrigerator overnight.
2. Repeat the following day ~24 hours later, collecting virus in the same tubes.

    
Day 5:
######

1. Collect virus for the 3rd and last time.
2. Filter with at 0.45 um filter into a new 50 mL conical.
3. Add 1/3 volume of Lenti-X concentrator (e.g., for 36 mL virus, add 12 mL Lenti-X). Mix by inverting several times.
   
    .. tip:: 
        There is enough room in one 50 mL conical to collect 2 plates of virus for 3 days and add the appropriate volume of Lenti-X.

        BAD prefers to add Lenti-X to the new 50 mL conicals and then filter the virus directly into the Lenti-X.

4. Store virus at 4°C overnight or over the weekend to precipitate the virus.
5. Thaw HDFs into a gelatin coated T-182 so they can recover over the weekend. When culturing HDFs, it is recommended to use DMEM + 15% FBS + non-essential amino acids.


Day 8:
######

1.   Centrifuge precipitated virus at 1500 x g at 4°C for 45 minutes (use the lower centrifuge) to pellet the virus.
2.   Remove supernatent and resuspend in 200uL per 10 cm plate with DMEM + 15% FBS + non-essential amino acids (HDF media).
3.   Seed HDFs at 5k/96-well (for 35dpi reprogramming) or 13k/48-well (for a 7dpi CTV experiment) onto gelatin coated plates.

Days 9-10:
##########

1.   Dilute virus according to calculations in fresh HDF media and polybrene. Use 5 uL of each concentrated virus per 96-well or 13 uL per 48-well.
2.   To improve infection efficiency, spin the plate at 1500 x g for 90 minutes at 32°C :ref:`as described <spinfection>`. Be sure to cover the centrifuge buckets with the plate spinner tray caps.
3.   Repeat the next day, ~24 hours later.


Day 11 (1 day post infection):
##############################

1.  ~24 hours after previous transduction, remove virus-containing media and replace with fresh HDF media. 
2.  If you are interested in early proliferation during reprogramming, perform :ref:`CellTrace Staining <cellTraceStaining>` on ths day.

Days 12-16 (2-6 days post infection):
#####################################

1. Change the media once around 4 or 5dpi with fresh HDF media. The cells are no longer BL2+ after this media change.

Day 17 (7 days post infection):
###############################

1. If assaying proliferation, complete flow cytometry quantification of CellTrace dilution on this day.
2. If assaying reprogramming rates, re-seed cells on this day.
   
   1. Gelatin coat a new 96-well plate as usual.
   2. Dilute aliquot of 100x laminin in PBS.
   3. Aspirate gelatin and replace with 67 uL of laminin.
   4. Incubate plate at 37°C for 1 hour to laminin coat.
   5. Dissociate 7dpi cells with 3x diluted trypsin.
   6. Quench with 200 uL HDF media.
   7. Aspirate laminin and transfer dissociated cells to laminin coated plate.

Day 18 (8 days post infection):
###############################

1. 24 hours after replating the cells, media change to N3 media:

    i. N3 media = N3 base + BDNF/CNTF/GDNF (1,000X, 10 µg/mL) + FGF (10,000X, 100 µg/mL)
    ii. Spike in 1,000X RepSox to N3 media for all experimental conditions. This differs from MEF reprogramming.

.. note:: 
    It is recommended to use a multi-channel pipette to aspirate the media to avoid losing cells.

    BAD aspirates 80 uL of media and replaces it with 85-90 uL fresh media.

Days 19-44 (9-34 days post-infection):
######################################

1. Continue to do N3 media changes every 3-4 days (2 times a week).


Day 45 (35 days post-infection): Assay Reprogramming
####################################################

1. For flow staining quantification, dissociate cells with :ref:`DNAse/Papain <MNdissociate>`, and combine 2 96-wells into 1 eppendorf tube.
2. *Optional*: Do a Live/Dead stain (e.g. Zombie).

    1. Dilute `ZombieNIR™ <https://www.biolegend.com/en-gb/products/zombie-nir-fixable-viability-kit-8657>`_ 1:1000x in PBS.
    2. Wash dissociated and pelleted cells with PBS.
    3. Resuspend cells in 100 uL diluted Zombie stain.
    4. Incubate at room temperature for 15-30 minutes in the dark.
    5. Wash with DMEM + 10% FBS.
    6. Proceed to fixation step.

.. note:: Zombie NIR™ dye is excited by the red laser and has fluorescence emission maximum at 746 nm.

3. Proceed with plate or flow staining as :doc:`described here <../../biochem_and_analytics/antibody_staining>`.

.. note:: 
    BAD uses the following antibodies:

      - 1:500 diluted mouse anti-Tuj1 (BioLegend Cat #801201) with 1:500 diluted anti-mouse AF-488.
      - 1:500 diluted rabbit anti-MAP2 with 1:500 diluted anti-rabbit AF-546 or AF-647.