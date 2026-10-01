Design and preparation of DNA IVT template
=============================================
We currently have three harbors (pHAs) for IVT: 

  * pKG01864: contains human beta globin 5' and 3' UTRs 
  * pKG01834: contains the 5' and 3' UTRs from the Pfizer-BioNTech COVID-19 vaccine
  * pKG03198: contains human beta globin 5' and 3' UTRs AND polyA is encoded on the plasmid

.. important::
  When making new DNA IVT templates, use pKG03198! This plasmid already encodes the polyA and the template is generated with a simple MluI digest.


Creating a new IVT template plasmid
-------------------------------------
pKG03198 is compatible with existing pPV2s for BsaI golden gate cloning, as is pKG01864.

If a desired CDS is not available, you can either 1) make a pPV2 or 2) clone directly into pKG01864 via Gibson. If proceeding with option 2, the plasmid backbone can be PCR amplified with the following primers: 

    VECTOR-FWD: 5'-ctcgagctcaagcttcgaattcac-3'

    VECTOR-REV: 5'-gaccggtagcgtgcttt-3'


Generating IVT linear DNA template from an IVT template plasmid
-----------------------------------------------------------------

Our IVT platform relies either on MluI digestion (pKG03198 backbone) or on PCR amplification (pKG01864 or pKG01834 backbone) using a universal primer pair and a plasmid harboring the CDS of interest as template to generate the IVT template. 
The forward and reverse primers bind to the 5' and 3' beta globin UTR, respectively.  The forward and reverse primers also encode the T7 polymerase promoter and the polyA tail, respectively. 

PCR-amplified template
-------------------------

1. If a PCR-generated linear template already exists, skip to step 4. Else, perform a small-scale PCR on a new IVT template to verify desired amplification and product specificity:

================================= =================================================
  Component                          Amount
================================= =================================================
 5x Q5 buffer                     5
 dNTP mix                         0.4 µL
 CleanCap AG F-primer (10 µM)     0.2 µL 
 R-primer (10 µM)                 0.2 µL
 Plasmid Template DNA (1 ng/µL)   1.0 µL
 Q5 polymerase                    0.1 µL
 Water                            to 20 µL
================================= =================================================   

.. important:: 
  Make sure you're using the correct primer pairs for a given plasmid IVT template backbone!   

2. Perform PCR using 57 C annealing temperature, adjust extension time based on length of linear template.
   
3. Cleanup the PCR product and run an aliquot on a gel to validate the desired product size was amplified. 

.. note:: This template can now serve as a "master" PCR template for future PCR amplifications. This is advantageous for tricky PCR amplicons and essential for those that contain internal primer binding sites (such as pKG02007, which harbors Cas9), as the annealing temperature can be increased due to the lengthened primer/template homology.


4. Perform the PCR outlined in step 1, substituting the Plasmid Template DNA with the PCR-generated linear template DNA. Scale-up accordingly to generate the amount of linear IVT template needed for your IVT reaction. Store unused linear PCR template in the IVT box and use as needed.  

MluI digested template
------------------------

.. note:: 
  You should get about 1 µg (100 ng/µL, 10 µL) of IVT template using this method which is good for 3 IVT reactions (each IVT gives ~50-60 µg so at 100ng/96-well, this should give modRNA for ~15-18 plates)


1. Combine the following in a PCR strip tube:

  =================== =========== =========
  Reagent             Amount      Notes
  =================== =========== =========
  DNA IVT plasmid     ~1 µg 
  rCutSmart buffer     5 µL 
  MluI                 1 µL  
  rSAP                 1 µL        Dephosphorylates 5\' DNA ends to prevent re-ligation of digested product
  Elga water           X µL        Add Elga water to reach total volume
  **Total**           **50 µL**
  =================== =========== =========

2. Incubate the mixture at 37ºC in the water bath for 1 hour.
   
3. PCR clean-up the linearized template DNA and use for downstream IVT reactions. Elute in ~10 µL.




.. important:: 
  As of 2023.06.04: use pKG01864. The Pfizer-BioNTech template (pKG01834) contains two point mutations in the 3' UTR, presumably from using 293T genomic DNA for cloning. We've witnessed poor expression in primary cells (both MEFs and human adult fibroblasts) relative to the beta-globin UTRs. If anyone would like to fix these and characterize (undergrad project?), that could prove useful!
