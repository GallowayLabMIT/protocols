=================================
STRAIGHT-IN Landing Pad Creation
=================================

STRAIGHT-IN is one method of engineering cell lines by precisely integrating DNA payloads into an hiPSC acceptor line.

Landing Pad Targeting in hiPSCs
=================================
The first step is to install a landing pad cassette in the hiPSC genome at a safe harbor 
locus (e.g. CLYBL, AAVS1) via CRISPR-Cas9 or TALENS-mediated homologous recombination.

Step 1: Landing Pad Targeting
-----------------------------

1. Follow standard hiPSC seeding protocol on a laminin coated plate such that the cells will 
   reach ~30% confluency the following day for transfection.
2. With Lipofectamine Stem co-transfect the hiPSCs with a selection of following:

   - Cas9 expression plasmid + sgRNA plasmid targeting the safe harbor locus + HDR donor plasmid + (optional: p53DD modRNA)
   
   - AIO Cas9 & sgRNA plasmid  + HDR donor plasmid
   
   - Control HDR donor plasmid only (this will give background fluorescence from the landing pad and an indicator for dilution out of the HDR plasmid)

.. note:: 
    We have observed p53DD modRNA boosts knock-in efficiency in co-transfection

3. After 4 hours add fresh StemFlex media (iPSC aren't happy in Opti-MEM for long periods)
4. Passage the cells 48 hours post transfection using GCDR (after a passage the cells should lose most plasmid fluorescence due to dilution)

Step 2: Selection and Clonal Isolation
--------------------------------------
TODO
