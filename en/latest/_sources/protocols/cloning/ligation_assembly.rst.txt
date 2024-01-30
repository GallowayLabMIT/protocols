========================
Ligation assembly
========================

.. time:: At least 1 hour, or overnight for best efficiency


`Ligation <https://en.wikipedia.org/wiki/Ligation_(molecular_biology)>`_ assembly is used to assemble DNA fragments by creating phosphodiester bonds between different fragments to generate a larger linear fragment or plasmid. Ligation reactions can be performed with restriction digest products and/or oligos that contain compatible sticky ends.

Protocol
=========
1. Design the assembly such that each fragment has compatible sticky ends.  Sticky ends allow for DNA fragments to bind each other for efficient ligation. Built-in tools such as those in SnapGene are helpful for designing this.

2. Generate the fragments for ligation. Perform a restriction digest of the recipient vector plus any desired inserts to generate sticky ends. If ligating using oligos, :doc:`anneal and phosphorylate <oligo_annealing>` oligos prior to assembly, as 5' phosphorylation is required for proper ligation. 

.. tip::
	Performing the vector digest with rSAP to dephosphorylate the backbone has sometimes led to reduced background colonies and greater efficiency when assembling using oligos.

.. tip:: 
	Gel extraction of digests can also be useful to decrease background ligation products.

3. Setting up the reaction mix is dependent on whether you choose to ligate digestion products or ligate using oligos. 

**Ligation with general digest products:** Mix 150 ng of digested vector and 3x molar ratios of desired inserts. `NEBioCalculator <https://nebiocalculator.neb.com/#!/ligation>`_ is very useful for calculating required masses for ligation reactions based on vector and insert lengths (A spreadsheet can also be helpful for quickly calculating the required masses and volumes for multiple fragments). Add 2 uL of T4 ligase buffer, 1 uL of T4 ligase enzyme, and water to bring the total volume of reaction mix to 20 uL.

**Ligation with oligos only:** Mix the reagents as follows if performing ligation assembly using one set of annealed oligos:

================================ ===========================
Reagent                   		 Amount (uL)
================================ ===========================
Vector digest (150 ng)           X
Oligos (annealed/phosphorlyated) 1
T4 ligase buffer          		 0.5
T4 ligase enzyme          		 1
Water                     		 10 - X
================================ ===========================

Multiple oligos with compatible sticky ends can be assembled to create longer fragments for insertion. In this case, add 1 uL of each set of oligos while maintaining the total volume of 10 uL.

4. Incubate at 16 C for one hour or at room temperature overnight for best efficiency.
5. :doc:`Transform competent cells <transformation>` with 5 uL of the ligation product.

.. note::
	If you're skipping recovery, adding water up to 300 µL total volume helps spread the transformed bacteria.

6. Store unused ligation products at -20°C.

Example
-------

You want to replace microRNA target sites that are between two restriction enzyme sites, AvrII and HindIII, that are on the 5' and 3' ends respectively of the region of interest on your plasmid. To swap out the sites, you choose to do a ligation reaction with oligos.

To be compatible with the vector, you design your new target site oligos with a 5' AvrII sticky end on the top strand and a 5' HindIII sticky end on the bottom strand. You anneal and phosphorylate these oligos and then perform a digest of the template with AvrII and HindIII, ending up with a concentration of 75 ng/uL.

A quick calculation shows that 2 uL of digest contains the 150 ng of DNA template required for the reaction. You then perform a ligation reaction by mixing the digest product with the oligos as detailed above and incubating at room temperature overnight. 