========================================================
Human Fibroblast to iMN Reprogramming
========================================================


This protocols outlines the reprogramming of human dermal fibroblasts (HDFs) to induced motor neurons (iMNs). 

This protocol outlines the timeline of Human Fibroblast to iMN reprogramming and links to protocols as they are appropriate in the timeline. 


Days 1 - 6: Production and transduction of viruses encoding reprogramming factors
---------------------------------------------------------------------------------

See :doc:`here for the complete 293T virus production protocol <../virus/virus_production>`. 

At minimum, iMN reprogramming requires the transduction of motor neuron-specific transcription factors. Typically, the oncogenes (p53DD, hRasG12V, c-MYC, myrAKT, BCL2) are also introduced to enhance reprogramming efficiency. The following plasmids are frequently used as sources of motor neuron TFs or oncogenes and are encoded on retroviral backbones compatible with production 293Ts.

=================   ================================
**pKG number**      **Plasmid Name**
=================   ================================
pKG00121              pMXs-Ascl1
pKG00010              pMXs-Brn2
pKG00003              pMXs-Myt1L
pKG01439              pMXs-Ngn2-x3HA
pKG00009              pMXs-Isl1
pKG00008              pMXs-Lhx2
pKG00002              pMXs-NeuroD1
pKG01169              pMXs-NIL
pKG01574              **pMXs-LNIx3HA**
pKG00060              pMXs-p53DD
pKG00121              pMXs-hRasG12V
pKG00747              **pMXs-myrAkt-P2A-BCL2**
pKG00751              pMXs-cMyc
pKG03523              **pMXs-cMyc-IRES-p53DD**
pKG03525              pMXs-cMyc-IRES-SNAP-p53DD
=================   ================================

The recommended combination of plasmids for human fibroblast to iMN reprogramming is currently LNIx3HA, myrAKT-P2A-BCL2, and cMYC-IRES-p53DD (LNI + ABCD).

To generate more general neurons (typically glutamatergic/cortical-like) rather than motor neurons, swap LNIx3HA for Ngn2-x3HA. BD has observed that Ngn2 alone can actually result in better overall neuronal reprogramming efficiency than LNI.

Day 1:
######

1. Seed 6 million 293Ts in each :ref:`gelatin-coated <gelatin>` 10 cm plate for each virus to be made.

   - Each 10 cm plate makes 200 uL of concentrated virus. If more virus is needed, additional 10 cm plates should be seeded.

.. tip::
	If starting from frozen, **start growing 293Ts 1 week prior** - they will be slow growing at first (don't change culture medium during the first 3 days). Split 293Ts 4X-6X every 2-3 days when culture reaches 70-90% confluency.

2. Thaw HDFs into a gelatin coated flask so they can recover over several days. When culturing HDFs, be sure to use DMEM + **15% FBS + non-essential amino acids** (HDF media).

Day 2:
######

3. Transfect transfer plasmids (containing your gene of interest), packaging (pLK-MLVgp, pKG0015), and envelope (pHDMG, pKG0022) plasmids at a ratio of (0.5 transfer : 0.45 packaging : 0.05 envelope). Do this early in the day, as the media is changed 6-8 hours after transfection.
   :doc:`See here for the complete 293T virus protocol <../virus/virus_production>`.
4. Media change 293Ts 6-8 hours after transfection. Remove media and add back 6.5 mL of DMEM + 10% FBS + **25 mM HEPES** (HEPES media). 

Day 3:
######

.. warning:: 
    Be sure to use :doc:`BSL2+ precautions <../virus/virus_safety>` when working with the human-infectible retrovirus containing oncogenes.

5. Collect virus-containing media 22-24 hours after the previous media change in 50 mL conicals. Up to 3 plates of the same virus can be combined into 1 tube. Replace with 6.5 mL of fresh HEPES media so that you can collect more virus the next day. Store collected virus in the 4℃ refrigerator overnight.

Day 4:
######

6. Repeat the virus collection ~24 hours later, collecting virus in the same tubes.
7. Filter with a 0.45 um filter into a new 50 mL conical.
8. Add 1/3 volume of Lenti-X concentrator (e.g., for 36 mL virus, add 12 mL Lenti-X). Mix by inverting several times.
   
    .. tip:: 
        There is enough room in one 50 mL conical to collect 3 plates of virus for 2 days and add the appropriate volume of Lenti-X.

        BD prefers to add Lenti-X to the new 50 mL conicals and then filter the virus directly into the Lenti-X.

9. Store virus at 4°C overnight to precipitate the virus.
10. Seed HDFs at 3k/96-well (for 35dpi reprogramming) or 8k/48-well (for a 7dpi CTV experiment) onto gelatin coated plates.
    
Day 5:
######

11.   Centrifuge precipitated virus at 1500 x g at 4°C for 45 minutes (use the lower centrifuge) to pellet the virus.
12.   Remove supernatant and resuspend in 200 uL per 10 cm plate with DMEM + 15% FBS + non-essential amino acids (HDF media).
13.   Dilute virus according to calculations in fresh HDF media and polybrene. Use 1 uL of each concentrated virus per 96-well or 2.6 uL per 48-well.
14.   To improve infection efficiency, spin the plate at 1500 x g for 30 minutes at 32°C :ref:`as described <spinfection>`. Be sure to cover the centrifuge buckets with the plate spinner tray caps.

.. note:: 
    The amount of virus per well may require further optimization.
    Ideally the volume should be calculated based on the titer of each virus, and an optimal MOI should be established to reduce batch-to-batch and experiment-to-experiment variability.


Day 6 (1 day post infection):
##############################

15.  ~24 hours after transduction, remove virus-containing media and replace with fresh HDF media. 
16.  If you are interested in early proliferation during reprogramming, perform :ref:`CellTrace Staining <cellTraceStaining>` on this day.

Days 7-11 (2-6 days post infection):
#####################################

17. Change the media once around 4 or 5 dpi with fresh HDF media. The cells are no longer BL2+ after this media change.

Day 12 (7 days post infection):
###############################

18. If assaying proliferation, complete flow cytometry quantification of CellTrace dilution on this day.
19. If assaying reprogramming rates, re-seed cells on this day.
   
   1. Gelatin coat a new 96-well plate as usual.
   2. Aspirate the gelatin and coat the plate with mouse laminin (described :doc:`here <laminin_coating_reprogram>`).
   3. Dissociate 7 dpi cells with 40 uL/96-well of 3x diluted trypsin. (scale as needed for larger well sizes)
   4. Quench with 200 uL/96-well of HDF media. (scale as needed for larger well sizes)
   5. Aspirate laminin and transfer dissociated cells to laminin coated plate.

Day 13 (8 days post infection):
###############################

20. 24 hours after replating the cells, media change to N3 media:

    i. N3 media = N3 base (DMEM/F12 with N2 and B27) + BDNF/CNTF/GDNF (1,000X, 10 µg/mL) + FGF (10,000X, 100 µg/mL)
    ii. Spike in 1,000X RepSox to N3 media for all experimental conditions. This differs from MEF reprogramming.

Days 14-25 (9-20 days post-infection):
######################################

21.  Do half N3 media changes every 3-4 days (2 times a week). Aspirate ~45 µL media, and add back ~50 µL fresh N3 media. However, if the media is very yellow, do a full media change and/or increase frequency of media changes.

Days 26-32 (21-27 days post-infection):
#######################################

22.   If doing an EdU purification to selectively kill proliferating cells, add N3 media containing 40 uM EdU (250x dilution from a 10 mM stock) for a total of 4 days (96 hours) beginning on 21 dpi. Refresh the media with EdU after the first 2 days. After the full 4 days, remove EdU and replace with fresh N3 media.

    .. note::
        - EdU is a thymidine analog that is incorporated into DNA during active DNA synthesis.
          High concentrations and long exposure to EdU is toxic to proliferating cells, which enables the enrichment of post-mitotic neurons.
        - BD has seen that cell death can be seen starting ~7 days after initial EdU exposure. If doing EdU purification, it is recommended to assay reprogramming on 35 dpi to ensure sufficient time for neuronal purification.
        - Neurons are more likely to lift off the plate after the proliferating cells die, so be sure to handle the cells gently during media changes and staining.

23.   Continue to do half N3 media changes every 3-4 days (2 times a week) until it is time to assay reprogramming.

Day 33-40 (28-35 days post-infection): Assay Reprogramming
##########################################################

24. For flow staining quantification, dissociate cells with :ref:`DNAse/Papain <MNdissociate>` or Accutase.
25. *Optional*: Do a Live/Dead stain (e.g. Zombie).

    1. Dilute `ZombieNIR™ <https://www.biolegend.com/en-gb/products/zombie-nir-fixable-viability-kit-8657>`_ 1:1000x in PBS.
    2. Wash dissociated and pelleted cells with PBS.
    3. Resuspend cells in 100 uL diluted Zombie stain.
    4. Incubate at room temperature for 15-30 minutes in the dark.
    5. Wash with DMEM + 10% FBS.
    6. Proceed to fixation step.

.. note:: Zombie NIR™ dye is excited by the red laser and has fluorescence emission maximum at 746 nm.

26. Proceed with plate or flow staining as :doc:`described here </protocols/biochem_and_analytics/staining_labeling/antibody_staining>`.

.. note:: 
    BD has used the following antibodies for neuronal staining:

      - 1:500 diluted mouse anti-Tuj1 (TUBB3) (BioLegend Cat #801201)
          - Stored at 4°C.
          - BD typically uses 1:500 diluted anti-mouse AF-488, but other secondary antibodies can be used.
          - TUJ1 is an immature pan-neuronal marker. However, fibroblasts (especially with neuronal transcription factors) can stain for low levels of Tuj1.
          - Works well for looking at cell morphology in plate staining.
          - Does not give good separation between neurons and non-neurons for flow staining.
      - 1:500 diluted rabbit anti-MAP2 (Cell Signaling Technology Cat #4542S)
          - Stored at -20°C.
          - BD typically uses 1:500 diluted anti-rabbit AF-546 or AF-647, but other secondary antibodies can be used.
          - If it is too dim, you can also use 1:250 dilution for both primary and secondary antibodies.
          - MAP2 is a mature pan-neuronal marker.
          - Might work for flow staining, but requires further validation. It worked well for flow staining fixed iPSC-derived neurons and MEF reprogramming with a 1:250 dilution.
      - 1:10 diluted mouse anti-Hb9 (DSHB Cat #81.5C10)
          - Stored at -20°C in ABA's antibody box in Olaf (cloning -20°C).
          - BD has used 1:250 diluted anti-mouse AF-488, but other secondary antibodies can probably be used.
          - Hb9 is a motor neuron-specific marker. Nuclear localized.
          - Did not work for flow staining.
      - 1:200 diluted mouse anti-PSA-NCAM, PE (Miltenyi Biotec Cat #130-117-394).
          - Stored at 4°C.
          - Conjugated to PE (red, excitation 565 nm, emission 575 nm), so no secondary antibody is needed.
          - Works well for looking at morphology in plate staining.
          - PSA-NCAM has worked for flow staining iPSC-derived neurons and MEF reprogramming (live or fixed), but signal can be affected by dissociation method.
          - Accutase results in higher PSA-NCAM staining than papain, but papain may offer clearer separation between neurons and non-neurons (somewhat reduced background staining).
          - Still needs to be validated for flow staining of human fibroblast to iMN reprogramming.