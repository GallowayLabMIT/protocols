============================
Droplet Digital PCR (ddPCR)
============================

This protocol describes how to run ddPCR copy number variability assays on the `BioRad QX200 <https://www.bio-rad.com/en-us/life-science/digital-pcr/qx200-droplet-digital-pcr-system>`_ system, 
following instructions from the STRAIGHT-IN *Nature Protocols* paper. [#blanch-asensio2024]_
See also `this presentation <https://mitprod.sharepoint.com/:p:/s/GallowayLab/EaPOh1lNzpZHpF5xqf2SNscBnhMz82q7pHYbfiS__mnsvw?e=1zoBkN>`_ from A.B.A. on the SharePoint.

Design 
------

The presentation above and `resources from BioRad <https://www.bio-rad.com/webroot/web/pdf/lsr/literature/Bulletin_6407.pdf>`_ contain useful information for designing new assays.

Each assay consists of a primer set and a corresponding probe. The probes are in one of two fluorescence channels, HEX or FAM, so each 
reaction can measure up to two targets. To detect copy number, one of the targets is typically a reference gene on the 
genome. For human cells, we use *RPP30*, which has a copy number of two in normal diploid cells. However, HEK293T cells have unstable genomes
and are often aneuploid---we've measured the copy number for *RPP30* as 2.7, but this and other genes may be unstable.

In lab, we currently have primers and probes (assays) for the following targets:

    +----------+---------------------------------+
    | Probe    | Target                          |
    +==========+=================================+
    | HEX      | *RPP30* -- human reference gene |
    +----------+---------------------------------+
    | FAM      | *mRuby2*, *mScarletI*           |
    |          +---------------------------------+
    |          | *PuroR*, *BleoR*                |
    |          +---------------------------------+
    |          | *AmpR*, pUC19 backbone          |
    +----------+---------------------------------+

Note that the instrument runs a set of 8 reactions (1 strip of PCR tubes) at a time, so aim to run multiples of 8 reactions to optimize consumable use.
Include a negative control (e.g., unedited cells) and a positive control (e.g., cells with a known/high copy number of your target) in each set of reactions, especially for new assays.

Protocol
--------

1. Extract high-quality genomic DNA from your cells, e.g., using the `Qiagen DNeasy Blood and Tissue Kit <https://www.qiagen.com/us/products/discovery-and-translational-research/dna-rna-purification/dna-purification/genomic-dna/dneasy-blood-and-tissue-kit>`_.
   Nanodrop to measure concentration and confirm purity.

2. Obtain 20X assay mixes that include a probe and matching primer set.
   
   We make these in ~100 µL aliquots, which is enough for ~90 reactions.
   They are stored in A.B.A.'s rack in Olaf (-20ºC) and should be thawed on ice.

    **20X Assay Mix**:

    ===================== =============
    Component               Amount (µL)
    ===================== =============
    Probe (100 µM)           5 
    Fwd primer (100 µM)     18
    Rev primer (100 µM)     18
    IDTE buffer             59
    **Total**             **100**
    ===================== =============

3. Prepare the PCR reaction mixes for each condition on ice.
   
   We prepare 22 µL per condition so that 20 µL can be easily loaded into the machine without bubbles.
   The following table shows amounts for one reaction and for 8.8 reactions (a full set plus extra), which is useful for making a master mix for 8 samples.
   The 2X ddPCR Supermix is the `ddPCR Supermix for Probes (no dUTP) <https://www.bio-rad.com/en-us/life-science/digital-pcr/digital-pcr-supermixes/ddpcr-supermix-for-probes-no-dutp>`_ 
   from BioRad.

    **Reaction Mix**:

    ===================   ============  ===============
    Component              1X              8.8X
    ===================   ============  ===============
    2X ddPCR Supermix        11            96.8
    20X HEX Assay            1.1           9.68
    20X FAM Assay            1.1           9.68
    HindIII                  0.55          4.84
    gDNA                     3             
    Elga water               5.25          46.2
    **Total**                **22 µL**          
    ===================   ============  ===============

  If making a master mix for several samples, combine 19 µL MM with 3 µL of sample gDNA.
  The amount of gDNA to add to each reaction depends on the expected copy number of the gene. For low copy targets, aim to add ~100-200 ng of gDNA to each reaction.
  Scale down this amount for high-copy targets (e.g., PiggyBac-integrated cargoes).

4. Bring your reactions and supplies over to the Weiss lab, where the ddPCR machine is located.
   We buy our own consumables for the instrument and store them in the Weiss lab, so you should also bring over pipettes (P200 and P20 for accuracy) and tips.

.. note:: TODO: Finish steps for running on instrument and analyzing data

References
----------

.. [#blanch-asensio2024]
    Blanch-Asensio, A., Grandela, C., Mummery, C.L. et al. 
    STRAIGHT-IN: a platform for rapidly generating panels of genetically modified human pluripotent stem cell lines. 
    Nature Protocols (2024). 
    https://doi.org/10.1038/s41596-024-01039-2