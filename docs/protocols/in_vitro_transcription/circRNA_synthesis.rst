circRNA synthesis
=================


This procedure outlines circRNA synthesis based on `Engineering circular RNA for enhanced protein production <https://www.nature.com/articles/s41587-022-01393-0>`_.


Generating IVT linear DNA template from plasmid
==================================================================

Our IVT platform relies on PCR amplification using a universal primer pair and a plasmid harboring the CDS of interest as template to generate the IVT template. The forward and reverse primers bind to the 5' and 3' beta globin UTR, respectively.  The forward and reverse primers also encode the T7 polymerase promoter and the polyA tail, respectively. 

.. note:: Alternatively, one could encode these elements on the plasmid and generate IVT template via restriction digestion. Although obviating the need for PCR and using an expensive oligo, the downside of this method is variable polyA tail length due to truncation of long repeat A sequences in E. coli. `There is a report of reducing these recombination events, <10.1261/rna.069286.118>`_ if someone is feeling ambitious and would like to build/test this :) 

1. If a PCR-generated linear template already exists, skip to step 4. Else, perform a small-scale PCR on a new IVT template to verify desired amplification and product specificity:

================================= =================================================
  Component                          Amount
================================= =================================================
 PrimeSTARv2 (2X)                    12.5 µL
 Water                                9.5 µL
 circRNA_fwd (10 µM)                  1 µL 
 circRNA_rev (10 µM)                  1 µL
 Plasmid Template DNA (5 ng/µL)       1 µL
================================= =================================================   

.. note:: 
    circRNA_fwd: 5' AAAAAAAAAAAAAAAAAAAAAAAAAAAGGCCAGTGAATTGTAATACGACTCACTATAGGG 3'
    circRNA_rev: 5' TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTCAAAAAACCCCTCAAGACCCGTTTAGAGGC 3'

1. Perform 2-step PCR, adjust extension time based on length of linear template. 98°C for 10s, 68°C for X s, x35 cycles.
   
2. Gel extract PCR product

.. note:: This template can now serve as a "master" PCR template for future PCR amplifications. This is advantageous for tricky PCR amplicons and essential for those that contain internal primer binding sites (such as pKG02007, which harbors Cas9), as the annealing temperature can be increased due to the lengthened primer/template homology.

3. Perform the PCR outlined in step 1, substituting the Plasmid Template DNA with the PCR-generated linear template DNA. Scale-up accordingly to generate the amount of linear IVT template needed for your IVT reaction. Store unused linear PCR template in the IVT box and use as needed.  


IVT reaction for circRNA
==========================
The protocol for IVT is adapted from the `NEB HiScribe protocol <https://www.neb.com/en-us/protocols/0001/01/01/standard-rna-synthesis-e2040>`_ and `Engineering circular RNA for enhanced protein production <https://www.nature.com/articles/s41587-022-01393-0>`_.

1. Thaw the necessary kit components on ice and microfuge to collect solutions to tube bottoms.
2. Assemble the IVT reaction at room temperature in the following order (total volume = 20 µL):

.. warning:: 
  This needs to be updated (8/22/2025 - NBW)

.. note:: 
  Wear a blue lab coat and wipe down area and pipets before starting.
  Use barrier tips when handling any of the reagents (nucleosides, buffers, enzymes).

1. Thaw the necessary kit components, gently invert to mix, and microfuge to collect solutions to tube bottoms.

.. note:: 
  Thaw reaction buffer, DTT, and dNTPs, and CleanCap at room temp, then make a master mix of 11 µL per tube. Then add template, water, and enzymes separately.

2. Assemble the IVT reaction at room temperature in the following order (total volume = 20 µL):

================================= =================================================
  Component                          Amount
================================= =================================================
 10X T7 IVT rxn buffer              2 µL
 ATP (100 mM)                       1 µL
 GTP (100 mM)                       1 µL
 UTP (100 mM)                       1 µL
 CTP (100 mM)                       1 µL
 DTT (0.1 M)                        1 µL
 Template (~1 µg)                   X µL
 Nuclease-free water                10 - X µL  
 ECIPP                              1 µL
 T7 RNAP mix                        2 µL
 Total                              20 µL
================================= =================================================  

1. Gently mix reactions, microfuge, and incubate at 37°C in a mixing thermoblock overnight at 1,000 rpm (12-16h)

.. note:: The reaction should be cloudy if successful. The ECIPP is a pyrophosphatase to counter pyrophosphates which will precipitate with magnesium and decrease IVT efficiency but even with the ECIPP, it will precipitate and look cloudy if successful.

2. Add 30 µL nuclease-free water (to ~50 µL), add 2 µL DNase I, and incubate at 37°C for 30 min. 
   
3. Purify circRNA with `NEB Monarch Spin RNA Cleanup Kit <https://www.neb.com/en-us/protocols/2025/01/10/monarch-spin-rna-cleanup-kit-protocol>`_ following manual
   provided in kit. 60 µL elution with nuclease-free water should give ~1,500 ng/µL.

4. Keep the purified circRNA on ice and Nanodrop to determine concentration (for a 20 µL reaction, one should expect ~90-100 micrograms of RNA). 
  
5. Digest purified circRNA with 1 U RNaseR (20 U/µL) per of µg RNA add 2 µL DNase I, and incubate at 37°C for 30 min. 
   If circRNA is ~1,500 ng/µL, 13 µL should be about 20 µg circRNA.


================================= =================================================
  Component                          Amount
================================= =================================================
 10X RNase R rxn buffer             2 µL
 circRNA (20 µg)                    X µL (~13-15ish)
 RNaseR (20 U/µL)                   1 µL
 Nuclease-free water                17 - X µL  
 Total                              20 µL
================================= =================================================  


6. Repeat step 3 to clean up RNA and elute in 60 µL nuclease-free water 
  
7. QC by sumitting samples to `BMC AATI Fragment Analyzer <https://bmcwiki.mit.edu/index.php/BioMicroCenter:Advanced_analytical_Fragment_analyzer>`_. 
   It's $15/sample for 5 µL and the Nano kit can handle 5 to 500 ng/µl (25 to 2500 ng) or Pico RNA 0.05 to 5 ng/µl (0.25 to 25 ng).
   I submit 0.5 µL circRNA + 4.5 µL nuclease-free water.



.. todo:: 
  Add image of QC