========================
Ligation assembly
========================

.. time:: At least 1 hour, or overnight for best efficiency


`Ligation <https://en.wikipedia.org/wiki/Ligation_(molecular_biology)>`_ creates phosphodiester bonds between different DNA fragments to generate a larger linear fragment or plasmid.
Ligation reactions can be performed with :doc:`restriction digest </protocols/cloning/digest>` products and/or :doc:`oligos </protocols/cloning/oligo_annealing>` that contain compatible sticky ends.

Protocol
=========
1. **Design the assembly** such that each fragment has compatible sticky ends (~4 bp sequences of single-stranded DNA at the 5' and 3' ends).
   Sticky ends allow for DNA fragments to bind each other for efficient ligation. Built-in tools in SnapGene are helpful for designing these.

2. **Generate the fragments** for ligation. Perform a :doc:`restriction digest </protocols/cloning/digest>` of the recipient vector 
   as well as of any desired inserts to create fragments with sticky ends. If ligating using oligos, :doc:`anneal and phosphorylate <oligo_annealing>` oligos prior to assembly, as 5' phosphorylation is required for proper ligation. 

.. tip::
	Performing the vector digest with rSAP to dephosphorylate the backbone can reduce background colonies and increase efficiency when assembling using oligos.
	
	Similarly, gel extraction of digests can also be useful to decrease background ligation products.

3. Mix the reaction.

	**Ligation with general digest products:** Mix 150 ng of digested vector backbone and desired inserts in a 1:3 molar ratio (backbone : insert).
	`NEBioCalculator <https://nebiocalculator.neb.com/#!/ligation>`_ is very useful for calculating required masses for ligation reactions based on vector and insert lengths (a spreadsheet can also be helpful for quickly calculating the required masses and volumes for multiple fragments).
	
	======================================= ===========================
	Reagent                   		 		Amount (µL)
	======================================= ===========================
	Vector digest (150 ng)           		X
	Insert(s) (1:3 molar ratio) 			Y
	T4 ligase buffer          		 		1
	T4 ligase enzyme          		 		0.5
	Water                     		 		to 10
	======================================= ===========================


	**Ligation with oligos only:** Use 1 µL of oligos that were separately phosphorylated and annealed, or 1 µL of a 1:10
	dilution of oligos where these steps were performed simultaneously.
	Additionally, multiple annealed oligo fragments with compatible sticky ends can be assembled to create longer fragments for insertion.
	Add 1 µL of each set of oligos.

	======================================= ===========================
	Reagent                   		 		Amount (µL)
	======================================= ===========================
	Vector digest (150 ng)           		X
	Oligos (annealed and phosphorlyated) 	1 each set
	T4 ligase buffer          		 		1
	T4 ligase enzyme          		 		0.5
	Water                     		 		to 10
	======================================= ===========================

4. Incubate at 16ºC for one hour or at room temperature overnight for best efficiency.
5. :doc:`Transform competent cells <transformation>` with at least 5 µL of the ligation product.
6. Store unused ligation products at -20°C.

Example
-------

You want to replace microRNA target sites that are between two restriction enzyme sites, AvrII and HindIII, that are on the 5' and 3' ends respectively of the region of interest on your plasmid. To swap out the sites, you choose to do a ligation reaction with oligos.

To be compatible with the vector, you design your new target site oligos with a 5' AvrII sticky end on the top strand and a 5' HindIII sticky end on the bottom strand. You anneal and phosphorylate these oligos and then perform a digest of the template with AvrII and HindIII, ending up with a concentration of 75 ng/µL.

A quick calculation shows that 2 µL of digest contains the 150 ng of DNA template required for the reaction. You then perform a ligation reaction by mixing the digest product with the oligos as detailed above and incubating at room temperature overnight. 