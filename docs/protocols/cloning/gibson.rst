========================
Gibson assembly
========================

Gibson assembly allows us to create a construct out of overlapping fragments. During a Gibson reaction, an exonuclease chews back the 5' ends of both the backbone and the inserts. The complimentary ends can then anneal, with nucleotides added by a DNA polymerase to fill in gaps in the annealed fragments. Finally, a ligase enzyme removes nicks to generate one contiguous plasmid. Since this method makes use of an exonuclease, it is important for fragments to have at least 30 bp of overlap.

Protocol
=========
1. Design the assembly. Online tools such as `NEB Builder <http://nebuilder.neb.com/>`_ and built-in tools such as those in SnapGene are helpful for designing this.

.. note::
	If desigining Gibson primers manually, having an overlap region of at at least 30bp is recommended. Each fragment should also be over 200bp.

2. Generate fragments by either PCR followed by DpnI digest, or restriction-digest of a target template. Measure concentration of fragments via Nanodrop.

.. note::
	Skipping the DpnI digest step will often still work, but will tend to increase the number of background colonies because the source plasmid is still around. If the cloning strategy selects using a different antibiotic resistance cassette, it may be possible to skip this digest step.

3. Calculate volumes of each fragment required for Gibson reaction. `NEBioCalculator <https://nebiocalculator.neb.com/#!/ligation>`_ is a helpful tool. Generally, 150 ng of the vector backbone fragments should be used. For inserts, a 2:1 molar ratio is usually successful, although a 3:1 ratio may be used for smaller fragments.
4. Setup a reaction with the calculated volumes of each fragment and 2X Gibson master mix/HIFI assembly mix solution. The master mix is 2X by volume, so add amount equal to the sum of all vector/insert volumes added.

.. hint:: 
	If your backbone vector is 5 kb at a concentration of 50 ng/uL, you need to add 3 uL to the reaction. If your insert is 1 kb at a concentration of 30 ng/uL, you need to add 2 uL (2:1 molar ratio) to the reaction. Finally, the sum of vector and insert volumes is 5 uL, so 5 uL of the 2X master mix should be added.

5. Incubate at 50°C for 15 minutes (2-3 fragments) or for 60 minutes (4-6 fragments).
6. :doc:`Transform competent cells <transformation>` with 2 uL of the Gibson mixture.

.. note::
	If you're skipping outgrowth step, adding water up to 300 µL total volume helps spread the transformed bacteria.

6. Store unused Gibson products at -20°C
