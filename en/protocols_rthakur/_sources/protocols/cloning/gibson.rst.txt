========================
Gibson assembly
========================

Gibson assembly a larger DNA fragment or plasmid from overlapping fragments. During a Gibson reaction, an exonuclease chews back the 5' ends of each fragment.
The complimentary ends can then anneal, with nucleotides added by a DNA polymerase to fill in gaps in the annealed fragments.
Finally, a ligase repairs nicks to generate one contiguous fragment or plasmid.

Since this method makes use of an exonuclease, it is important that **each fragment is longer than 200 bp**.
Additionally, because the reaction takes place at 50ºC, the overlapping sequences should have a 
melting temperature greater than 50ºC. (The SnapGene tool will warn you if this is not the case.)
Practically, this means the fragments should **overlap by at least 20 bp**.

Protocol
=========
1. Design the assembly. Online tools such as `NEB Builder <http://nebuilder.neb.com/>`_ and built-in tools in SnapGene are helpful for doing this.
2. Generate fragments by either :doc:`PCR </protocols/cloning/pcr>` followed by DpnI digest, or by :doc:`restriction digest </protocols/cloning/digest>` of a target template. Measure the concentrations of fragments via Nanodrop.

	.. note::
		The DpnI digest step for PCR fragments is not strictly necessary, but it reduces the number of background colonies from leftover template plasmid.
		This is relevant if the template plasmid and your final plasmid have the same antibiotic resistance.

3. Calculate volumes of each fragment required for the Gibson reaction. `NEBioCalculator <https://nebiocalculator.neb.com/#!/ligation>`_ is a helpful tool.
   Generally, 150 ng of the vector backbone fragment should be used. For inserts, a 2:1 molar ratio (insert : backbone) is usually successful, although a 3:1 ratio may be used for smaller fragments.
4. Set up a reaction with the calculated volumes of each fragment and 2X NEB HiFi assembly mix. The master mix is 2X by volume, so add an amount equal to the sum of all backbone and insert volumes used.

	.. hint:: 
		If your backbone vector is 5 kb at a concentration of 50 ng/µL, you need to add 3 µL to the reaction.
		If your insert is 1 kb at a concentration of 30 ng/µL, you need to add 2 µL (2:1 molar ratio) to the reaction.
		Finally, the sum of vector and insert volumes is 5 µL, so add 5 µL of the 2X master mix.

5. Incubate at 50°C for 15 minutes (2-3 fragments) or for 60 minutes (4-6 fragments).
6. :doc:`Transform competent cells <transformation>` with 2-5 µL of the reaction.
7. Store unused Gibson products at -20°C.
