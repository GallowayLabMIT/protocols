=========================================
Cloning tips, tricks, and troubleshooting 
=========================================

Help! I got no colonies
=======================

Troubleshooting assemblies
--------------------------

- Are you sure you added all components to the assembly reaction? When in doubt, set up a new reaction.
- Check out tips on the protocols for each type of assembly to increase reaction efficiency.
- You can PCR amplify the assembly to determine whether any correct product formed. Choose primers that span fragment junctions.

Troubleshooting transformations
-------------------------------

- Double check that the antibiotic in the agar plate you used matches the antibiotic resistance of your plasmid product.
- Be sure to outgrow plasmids containing kanamycin or chloramphenicol resistance before plating. Outgrow in SOC for 1 hour, but not much longer (1.7-mL tubes are not aerated, so the bacteria will eventually die).
- For plasmids containing ccdB (usually alongside chloramphenicol resistance), be sure to transform ccdB resistant bacteria (not NEB Stable cells).
  This usually applies to destination vectors, Harbor plasmids, and Janus / Multi Janus vectors (but not Gateway or Golden Gate assemblies that use these as inputs).
- Try some of the other tips in the :doc:`transformation protocol </protocols/cloning/transformation>` to increase efficiency.


Designing cloning
=================

Adding short sequences
----------------------

- To make point mutations, order primers with the mutations in the middle of the sequence (flanked by ~8 bp on either side). Typically,
  it works well to order the forward and reverse primers with complementary sequences and use them with another pair of primers to generate 
  two PCR fragments (forward with mutation + other reverse, reverse with mutation + other forward). These fragments can then be assembled via a Gibson reaction.
- To insert very short sequences (<20 bp), add the sequence to the primer when amplifying a fragment with PCR, then use Gibson assembly. 
  You can also PCR these fragments with new primers to add longer sequences.
- To insert short sequences (<100 bp), try ligation with annealed oligos. Note that you can PCR the backbone to add restriction sites (also add
  ~6 bp between the RE binding site and the end of the fragment for efficient digestion). For sequences up to ~60-100 bp, you can use two sets of annealed oligos.
  (More than two likely will be too inefficient to work.)
- To insert sequences 100-200 bp, your best bet is probably Golden Gate cloning from PCR fragments with custom connector sequences. This 
  size of fragment is too long for annealed oligos but too short for Gibson assembly. 

Designing Gibson assemblies
---------------------------

- Choose fragments such that no one fragment contains both the origin of replication and the antibiotic resistance cassette. 
  This reduces background colonies.
- When generating fragments that do not contain an antibiotic resistance cassette (i.e., most fragments that are not the vector backbone), try to choose 
  templates that have a different antibiotic resistance from your final plasmid product. This reduces background colonies.
- Gibson assemblies with >4 fragments will likely be inefficient. To reduce the number of fragments, perform an :ref:`overlap extension PCR <overlap_ext_pcr>`.
  This will generate a single fragment from two shorter ones.
- Avoid assembling a single fragment into a plasmid. Instead, generate two fragments to improve efficiency (and probably reduce PCR times!).
  