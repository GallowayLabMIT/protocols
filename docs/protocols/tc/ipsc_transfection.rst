=================================
Transient Transfection of iPSCs
=================================

Conceptually, transfection of iPSCs is the same as of other cell types. However, transfections tend to be less efficient, and iPSCs 
are more sensitive to the transfection reagents. Thus, we do not use PEI; instead, we've found that the 
`FuGENE® HD <https://fugene.com/wp-content/uploads/2022/12/FuGENE_HD-Users-Guide_2023.pdf>`_ reagent works well
(at least for the iPS11 cell line) and 
`Lipofectamine 3000 <https://assets.thermofisher.com/TFS-Assets/LSG/manuals/lipofectamine3000_protocol.pdf>`_
is a reasonable substitute for plasmid DNA. For mRNA, the 
`Lipofectamine Stem <https://assets.thermofisher.com/TFS-Assets%2FBID%2Fmanuals%2Ftransfection-psc-lipofectamine-stem-mtesr1-protocol.pdf>`_ 
reagent is optimal. 

Calculations
------------

For all calculations, you can refer to the 
`iPSC transfection template <https://mitprod.sharepoint.com/:x:/s/GallowayLab/ES4uWltgGuFPp4ySG7b3ZbgBSlJ-3WxlB4nHcQb2l2-hSA?e=jClhpT>`_ 
in the shared projects folder.

Empirically determined reagent amounts to use:

=============================================================================================================================================== ==========================================
 Reagent                                                                                                                                         Ratio [reagent (µL) : nucleic acid (µg)]
=============================================================================================================================================== ==========================================
 `FuGENE® HD <https://fugene.com/wp-content/uploads/2022/12/FuGENE_HD-Users-Guide_2023.pdf>`_                                                      3:1
 `Lipofectamine 3000 <https://assets.thermofisher.com/TFS-Assets/LSG/manuals/lipofectamine3000_protocol.pdf>`_                                     2:1 
 `Lipofectamine Stem <https://assets.thermofisher.com/TFS-Assets%2FBID%2Fmanuals%2Ftransfection-psc-lipofectamine-stem-mtesr1-protocol.pdf>`_      2:1
=============================================================================================================================================== ==========================================

.. note:: Not all reagent amounts have been rigorously optimized. 


Protocol
--------

1. One day prior to transfection, seed healthy iPSCs on Geltrex-coated plates with ROCK inhibitor (Ri), at a density equivalent to 100,000 
   (1e5) cells/well in a 24-well plate.

    - Dissociate iPSCs to single cells for seeding using :ref:`Gentle Cell Dissociation Reagent <gcdr-dissociation>`.
    - Addition of Ri is important to promote survival of single cells.
    - The equivalent density for a 96-well plate is 20,000 (2e4) cells/well; for a 6-well plate it is 500,000 (5e5) cells/well.

2. On the day of transfection, first prepare condition mixes of nucleic acid (pDNA or mRNA) diluted in Opti-MEM for a final volume of 
   5µL (96-well plate), 25µL (24-well plate), or 125µL (6-well plate) per well. These volumes are specified in the 
   `transfection template <https://mitprod.sharepoint.com/:x:/s/GallowayLab/ES4uWltgGuFPp4ySG7b3ZbgBSlJ-3WxlB4nHcQb2l2-hSA?e=jClhpT>`_.

    - If using Lipofectamine 3000, add P3000 to each condition mix at 2µL/µg DNA.

3. If using Lipofectamine 3000 or Lipofectamine Stem, prepare the reagent master mix. Dilute the appropriate volume of reagent in Opti-MEM
   for a final volume of 5µL (96-well plate), 25µL (24-well plate), or 125µL (6-well plate) per well.
4. Add the FuGENE® HD reagent or Lipofectamine master mix to each condition mix to form the final complexes. Incubate for 10 minutes at room temperature.
5. Add the final complexes dropwise to the cells, 5µL (96-well plate), 25µL (24-well plate), or 125µL (6-well plate) per well for FuGENE® HD
   transfections, and twice that amount for Lipofectamine transfections.
6. Gently rock the plate back-and-forth, side-to-side to distribute the complexes. Return the cells to the incubator.
7. After 4-6 hours, media change to fresh mTeSR-Plus to remove the transfection reagent and Ri. Waiting longer than this may compromise cell health.
8. Analyze expression via microscopy or :doc:`flow cytometry <./tc-basics/flow_cytometry>`, or continue with downstream experimental steps.

   - mRNA expression peaks at ~12 hours post-transfection.
   - pDNA expression is visible at 24 hours post-transfection (1 dpt) and increases through at least 3 dpt.
   - To analyze via flow cytometry, follow the framework for analysis of other cell types, except dissociate in GCDR instead of trypsin.