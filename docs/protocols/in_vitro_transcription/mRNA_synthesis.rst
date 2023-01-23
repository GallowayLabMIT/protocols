mRNA synthesis
==============
This procedure outlines mRNA synthesis with Cap O structure, where IVT and capping is conducted sequentially, with lithium chloride purification steps after IVT and capping (i.e., IVT => purification => capping => purification).

This workflow is amenable to simultaneous IVT and capping with Cap 1 structure using `CleanCap AG reagent <https://www.neb.com/protocols/2019/09/23/co-transcriptional-capping-using-cleancap-reagent-ag-from-trilink-and-hiscribe>`_. Just be certain that your IVT template contains an AG directly downstream of the T7 promoter element: 5’ TAATACGACTCACTATA **AG** 3’


You could also use Anti-Reverse Cap Analog `(ARCA) <https://www.neb.com/products/s1411-3-o-me-m7g5ppp5g-rna-cap-structure-analog#Product%20Information>`_, but this 
workflow has fallen out of favor since the development of CleanCap, as ARCA 1) reduces yield of capped mRNA and 2) contaminates the product with uncapped mRNA, which elicits an immunogenic response.   

.. important:: 
  Please be careful to avoid `degradation from RNase <https://www.neb.com/tools-and-resources/usage-guidelines/avoiding-ribonuclease-contamination>`_. Although I haven't encountered noticeable RNA degradation,
  it's probably a good idea to adhere to some of these general guidelines. I recommend using a new pair of gloves each time you enter/exit lab. Also, use barrier pipette tips when handling any of the reagents (nucleosides, buffers, enzymes) to prevent RNase contamination for other users. 


IVT reaction
==========================
The protocol for IVT is adapted from the `standard NEB HiScribe protocol <https://www.neb.com/protocols/0001/01/01/standard-rna-synthesis-e2040>`_.

1. Recipe for Golden Gate reaction (total volume = 10 µL):

================================= =================================================
  Component                          Amount
================================= =================================================
 75 ng/plasmid
 10X T4 DNA ligase buffer          1 µL
 T4 DNA ligase (400 U/µL)          1.25 µL (500 U)
 Type II RE                        0.5 µL (increase to 1 µL if >10 inserts)
 H2O                               to 10 µL
================================= =================================================


Purification of IVT reaction with lithium chloride
=======================================================
The protocol for lithium chloride purification is adapted from `Thermo <https://www.thermofisher.com/us/en/home/references/ambion-tech-support/rna-isolation/general-articles/the-use-of-licl-precipitation-for-rna-purification.html>`_.

Capping of purified IVT mRNA (if performing sequential capping workflow)
================================================================================================
The protocol for capping is adapted from the `NEB Vaccinia capping system protocol <https://www.neb.com/protocols/0001/01/01/capping-protocol-m2080>`_.
