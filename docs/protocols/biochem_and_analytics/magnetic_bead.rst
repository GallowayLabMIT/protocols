=============================================
Magnetic bead clean-up for genomics libraries
=============================================
(Adapted from USC Epigenome Center)

.. note:: This protocol describes two methods to clean up libraries following various adapter ligations. Most recently, I (Katie) used this workflow to clean up samples from 10X 3'RNAseq before sequencing. 

.. warning::
  INCOMPLETE! Part of 10X Genomics workflow; the rest of the protocol needs to be added. This section separates DNA by size in preparation for sequencing.

Uses
---------------------------------
* Clean-up Samples or Libraries (buffers, salts, NTPs, or other undesirable fragments)
* Condense / Concentrate into lower volume

Determine Bead Volume to use by size range you wish to recover:
---------------------------------------------------------------

* To recover ALL nucleic acids regardless of size use bead volume of 1.8x sample volume.

* To recover nucleic acids >50bp - use bead volume of 1.5x sample volume.

* To remove Primer-dimers & recover everything >100 bp - use bead volume of 1.0x sample vol.

* To remove Adaptor-dimers & recover everything >200bp - use bead volume of 0.8x sample vol.

* To remove very HMW bands, see the :ref:`2-step <two_step>` protocol modification below.

Preparations:
---------------------------------

* Locate a strong rare-earth-metals magnet

* Bring AMPure XP Beads to RT (from 4\ |degree|\ C), vortex vigorously to mix
* If using a plate or strip-tubes & trough add volume of beads needed + 300-500µL extra

* Mix fresh EtOH  at 75%.

  * For large double stranded DNA can use 70%
  * For very small &/or single stranded RNA use 80%

Basic Bead Clean Protocol:
---------------------------

1. Measure volume of samples.

2. Calculate bead volume for desired size range

3. Add beads to sample & mix well -- if some splashes onto tube lid or sides do a quick pulse centrifuge to collect at bottom of tube.

4. Incubate 5 m @ RT.

5. Place tube on magnet to condense beads into pellet (1 – 15 minutes, depending on magnet strength)

.. important::
  **Keep beads pelleted throughout washes!**

6. Draw off supernatant & discard

7. Wash with 200µL of fresh 70%-80% EtOH 2x.

8. Draw off EtOH & discard each time

9. After 2nd wash allow residual EtOH to evaporate

10. Before pellet overdrys & starts to “crack” or “flake off” elute in volume of reagent appropriate for next step in protocol (typically diH2O or EB).

11. Mix well, pellet beads on magnet, draw off supernatant with your sample

12. Pipette into new, labeled tube.

.. _two_step:

2-step "Big" bead clean to remove large fragments >~350bp.
-----------------------------------------------------------

**1st clean:**

1. 0.7x Bead:lib vol, incubate 5m, pellet beads with everything >350bp.
2. Transfer soup into clean tube containing	 2nd bead volume.

**2nd clean:**

1. 1.1x Bead:original lib vol, for total ratio of 1.8x PEG+NaCl  to original lib vol.
2. Mix well & incubate up to 15m, pellet beads well (8-10 min’s), EtOH wash 2x
3. Allow to air dry & elute back into desired vol of diH2O or EB.

.. |degree| unicode:: U+00B0