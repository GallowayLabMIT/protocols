modRNA synthesis
=================


This procedure outlines modRNA synthesis with Cap 1 structure, where IVT and capping is conducted simultaneously using `CleanCap AG reagent <https://www.neb.com/protocols/2019/09/23/co-transcriptional-capping-using-cleancap-reagent-ag-from-trilink-and-hiscribe>`_. Just be certain that your IVT template contains an AG directly downstream of the T7 promoter element: 5’ TAATACGACTCACTATA **AG** 3’


You could also use Anti-Reverse Cap Analog `(ARCA) <https://www.neb.com/products/s1411-3-o-me-m7g5ppp5g-rna-cap-structure-analog#Product%20Information>`_, but this 
workflow has fallen out of favor since the development of CleanCap, as ARCA 1) reduces yield of capped mRNA and 2) contaminates the product with uncapped mRNA, which elicits an immunogenic response.   

.. important:: 
  Please be careful to avoid `degradation from RNase <https://www.neb.com/tools-and-resources/usage-guidelines/avoiding-ribonuclease-contamination>`_.
  
  Perform these steps in the genomics hood, wipe down all surfaces with the RNase surface decontaminant, and
  use a new pair of gloves sprayed with the decontaminant each time you enter/exit the lab.

  Also, use fresh barrier tips from inside the genomics hood when handling any of the reagents (nucleosides, buffers, enzymes).


IVT reaction
==========================
The protocol for IVT is adapted from the `NEB HiScribe protocol <https://www.neb.com/protocols/2021/10/12/mrna-synthesis-protocol-with-modified-nucleotides-using-the-hiscribe-t7-mrna-kit-with-cleancap-reagent-agneb-e2080>`_.

1. Thaw the necessary kit components on ice and microfuge to collect solutions to tube bottoms.
2. Assemble the IVT reaction at room temperature in the following order (total volume = 20 µL):



================================= =================================================
  Component                          Amount
================================= =================================================
 nuclease-free water               10.8 - X µL (for 20 µL final volume)
 10X T7 IVT reaction buffer        2.0 µL
 ATP (100 mM)                      1.2 µL (6 mM final)
 CTP (100 mM)                      1.0 µL (5 mM final)
 GTP (100 mM)                      1.0 µL (5 mM final)
 m1Ψ-UTP (100 mM)                  1.0 µL (4 mM final)
 CleanCap AG (100 mM)              0.8 µL (4 mM final)
 Template DNA                      100 ng, X µL
 Pyrophosphatase (U)               0.2 µL
 T7 RNA Polymerase Mix             2.0 µL
================================= =================================================

.. note:: If performing multiple IVTs, one can prepare a mastermix. Dilute each template DNA to 5 µL total volume, prepare mastermix using 5.8 µL Nuclease-free water (based on one 20 µL reaction), and distribute 15 µL of master mix to each 5 µL DNA template tube.    

3. Gently mix reactions, microfuge, and incubate at 37 C in a thermoblock for 2-4 hours (longer incubation times recommended for transcripts >3 kb).

4. Optional: post IVT, you can treat you sample with DNase I if your application cannot tolerate residual amounts of DNA template. Add nuclease-free water to 50 µL, add 1 µL DNase I, and incubate at 37 C for 15 min. 
   
5. Purify modRNA with `NEB Monarch RNA Cleanup Kit <https://www.neb.com/products/t2050-monarch-rna-cleanup-kit-500-ug#Protocols,%20Manuals%20&%20Usage>`_ following manual provided in kit.

6. Keep the purified modRNA on ice to perform quality control analysis. Nanodrop to determine concentration (for a 20 µL reaction, one should expect ~50 micrograms of RNA). 
  
7. Perform gel electrophoresis to confirm the full-length product was synthesized. Add nanodropped samples to a new PCR tube containing 8 µL of NEB 2X RNA Loading Dye (blue reagent), incubate at 90 C for 3 minutes, and immediately place on ice for 2 minutes. This is to denature RNA secondary structure so it can be resolved on a native agarose gel.

8. In parallel, prep a `ssRNA ladder <https://www.neb.com/products/n0362-ssrna-ladder#Product%20Information>`_ to serve as a standard. 
  
9. Run your denatured RNA samples on a gel to confirm product size. 

.. important:: 
  Ethidium bromide does not stain ssRNA very well, prepare your gel using SYBR safe!

10. Aliquot modRNA into single-use tubes (scale appropriately for your experiment) and store in -80 C. We have a box for
    synthesized modRNA in Nokk.

.. note:: I have observed no reduction in product quality multiple months after storing. Although I have witnessed some sublimination which leads to more concentrated RNA samples.    


IVT using MluI-digested pKG3198 (polyA encoded on plasmid)
===========================================================

The protocol for IVT is adapted from the `NEB HiScribe protocol <https://www.neb.com/protocols/2021/10/12/mrna-synthesis-protocol-with-modified-nucleotides-using-the-hiscribe-t7-mrna-kit-with-cleancap-reagent-agneb-e2080>`_.

.. note:: 
  Wear a blue lab coat and wipe down area and pipets before starting.
  Use barrier tips when handling any of the reagents (nucleosides, buffers, enzymes).

1. Thaw the necessary kit components, gently invert to mix, and microfuge to collect solutions to tube bottoms.

.. note:: 
  Thaw DTT, dNTPs, and CleanCap at room temp, then make a master mix of 7.8 µL per tube. Then add template, water, and enzymes separately.

2. Assemble the IVT reaction at room temperature in the following order (total volume = 20 µL):

================================= =================================================
  Component                          Amount
================================= =================================================
 10X T7 IVT rxn buffer              2 µL
 DTT                                1 µL
 GTP                                1 µL
 CTP                                1 µL
 ATP                                1 µL
 m1Ψ (100 mM)                       1 µL 
 CleanCap Reagent AG                0.8 µL 
 Template (~300-400 ng)             X µL
 Nuclease-free water                9.2 - X µL  
 ECIPP                              1 µL
 T7 RNAP mix                        2 µL
 Total                              20 µL
================================= =================================================  

3. Gently mix reactions, microfuge, and incubate at 37°C in a thermoblock for 2-4 hours (longer incubation times recommended for transcripts >3 kb).

.. note:: The reaction should be cloudy if successful. The ECIPP is a pyrophosphatase to counter pyrophosphates which will precipitate with magnesium and decrease IVT efficiency but even with the ECIPP, it will precipitate and look cloudy if successful.

4. Optional: post IVT, you can treat you sample with DNase I if your application cannot tolerate residual amounts of DNA template. Add 30 µL nuclease-free water (to ~50 µL), add 2 µL DNase I, and incubate at 37°C for 30 min. 
   
5. Purify modRNA with `NEB Monarch RNA Cleanup Kit <https://www.neb.com/products/t2050-monarch-rna-cleanup-kit-500-ug#Protocols,%20Manuals%20&%20Usage>`_ following manual provided in kit. 60 µL elution with nuclease-free water should give ~800 ng/µL.

6. Keep the purified modRNA on ice to perform quality control analysis. Nanodrop to determine concentration (for a 20 µL reaction, one should expect ~50-60 micrograms of RNA). 
  
7. Perform gel electrophoresis to confirm the full-length product was synthesized. Add nanodropped samples to a new PCR tube containing 8 µL of NEB 2X RNA Loading Dye (blue reagent), incubate at 90 C for 3 minutes, and immediately place on ice for 2 minutes. This is to denature RNA secondary structure so it can be resolved on a native agarose gel.

.. note:: 
  You want >500 ng RNA to resolve on SYBR safe gel. You can put 8 µL NEB RNA loading dye / PCR-tube prior to nanodrop and then add the nanodrop sample directly to the loading dye.

8. In parallel, prep a `ssRNA ladder <https://www.neb.com/products/n0362-ssrna-ladder#Product%20Information>`_ to serve as a standard. Use 2 µL ssRNA + 8 µL RNA loading dye. 
  
9. Run your denatured RNA samples on a gel to confirm product size. 

.. important:: 
  Ethidium bromide does not stain ssRNA very well, prepare your gel using SYBR safe!

10. Aliquot modRNA into single-use tubes (scale appropriately for your experiment) and store in -80 C. We have a box for
    synthesized modRNA in Nokk. If ~2,400 ng aliquots, you'll have ~20 aliquots.

.. note:: I have observed no reduction in product quality multiple months after storing. Although I have witnessed some sublimination which leads to more concentrated RNA samples.  
