========================
Gibson assembly
========================

Gibson assembly allows us to create a construct out of overlapping fragments.

Protocol
=========
1. Design the assembly. Online tools such as `NEB Builder <http://nebuilder.neb.com/>`_ and built-in tools such as those in SnapGene are helpful for designing this.

.. note::
	If desigining Gibson primers manually, having an overlap region of at at least 30bp is recommended. Each fragment should also be over 200bp.

2. Generate fragments by either PCR followed by DpnI digest, or restriction-digest of a target template.

.. note::
	Skipping the DpnI digest step will often still work, but will tend to increase the number of background colonies because the source plasmid is still around. If the cloning strategy selects using a different antibiotic resistance cassette, it may be possible to skip this digest step.

3. Setup a reaction with 150 ng of the vector fragment, followed by a 2x molar ratio of each of the inserts. Add 2x by-volume Gibson master mix/HIFI assembly mix solution.
4. Incubate at 50°C for 15 minutes (2-3 fragments) or for 60 minutes (4-6 fragments).
5. :doc:`Transform competent cells <transformation>` with 2 uL of the Gibson mixture.

. note::
	If you're skipping recovery, adding water up to 300 µL total volume helps spread the transformed bacteria.

6. Store unused Gibson products at -20°C

Example
-------
If you are cloning with pENTR and your vector concentration is 50 ng/ul, your insert is 1 kb and 50 ng/ul, then you want 3 uL of pENTR and 0.75 uL of insert. The Gibson mix (NEB HIFI Assembly Mix) is 2x. So you would add 3.75 uL of the assembly mix to the plasmid and insert mix. Following the assembly directions, place at 50°C for 15 minutes (1-2 inserts), followed by transformation in competent cells.