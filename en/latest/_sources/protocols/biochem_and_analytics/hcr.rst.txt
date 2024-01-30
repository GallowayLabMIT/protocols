************
HCR RNA-FISH
************

Prepare necessary buffers as described in :doc:`/recipes/fish/fish_buffers`. The total amount needed per sample (without technical replicates) is:

=====================   ========================
Buffer                  Total amount per sample
=====================   ========================
4% PFA                  100 µL
0.5% Tween              100 µL
Hybridization buffer    270 µL
Wash buffer             200 µL
Amplification buffer    270 µL
5x SSCT                 600 µL
=====================   ========================


.. time::
   3 days (3-4 hours Day 1, 2 hours Day 2, 1 hour Day 3)

.. note::
    All spins are performed at ~500 rcf for 4 min. Our centrifuge follows RCF = 1e-4*[rpm]^2 + 4e-2*[rpm] - 6e1, where **2200 rpm = 512 rcf**.
    It is recommended to perform all spins at 4°C once the cells have been fixed to prevent pellet loss. 

.. warning::
   Both PFA (used in the fixation) and Formamide (used in the hybridization and wash buffers) are hazardous, so all steps must be performed in the fume hood.


Day 1
========================
1. Dissociate cells and spin down. Resuspend in PBS and transfer to a 96-well V-bottom plate.
2. Spin down and aspirate PBS. Resusepnd in 100 uL of 4% PFA and incubate for 15 min at room temp.
3. Add 150 uL of PBS, spin down, and aspirate.
4. Resuspend in 100 uL of 0.5% Tween, and incubate for 15 min at room temp.
5. Add 150 uL of PBS, spin down, and aspirate.
6. Add 200 uL of probe hybridization buffer for 30 min at 37 degrees C.
7. Prepare probe solution by adding 1 uL of 1 uM stock to 70 uL of probe hybridization buffer (per sample) at 37 degrees C.
8. Spin down with reduced deceleration, and aspirate hybridization buffer.

.. important:: 
   The hybridization buffer is viscous, so the deceleration setting on the centrifuge should be lowered to 5 to get a good pellet.

9.  Add 70 uL of the prepared probe solution, and incubate samples **overnight (12-16 h**) at 37 degrees C.

Day 2
=========================
1. Spin down at reduced deceleration, and aspirate probe solution.

.. important:: 
   The hybridization buffer is viscous, so the deceleration setting on the centrifuge should be lowered to 5 to get a good pellet.

2. Resuspend in 200 uL of probe wash buffer, and incubate for 15 min at 37 degrees C.
3. Spin down, and aspirate wash buffer.
4. Resuspend in 200 uL of 5X SSCT, and incubate for 5 minutes at room temp.
5. Spin down, and aspirate 5X SSCT.
6. Pre-amplify samples in 200 uL of amplification buffer for 30 min at room temp.
   While waiting, begin *Hairpin Preparation*:

   a. Prepare 4.5 pmol each of hairpin h1 and h2 by snap cooling 1.5 uL of 3 uM stock (per sample) at 95C for 90 seconds. Snap cool each individual hairpin in **separate tubes**.
   b. Cool hairpins in the dark at room temperature for 30 minutes.
   c. Prepare hairpin solution by adding h1 and h2 hairpins to 70 uL amplification buffer (per sample).

7. Spin down, and aspirate amplification buffer.
8. Add 70 uL uL of the hairpin/amplification buffer solution, and incubate samples **overnight (12-16 h)** in the dark at room temperature.

Day 3
===========
1. Spin down, and aspirate hairpin solution.
2. Resuspend in 200 uL of 5X SSCT, and incubate for 30 min in the dark at room temp.
3. Spin down, and aspirate 5X SSCT.
4. Resuspend in 200 uL of 5X SSCT, and incubate for 5 min in the dark at room temp.
5. Spin down, and aspirate 5X SSCT.
6. Resuspend in 220 uL of PBS. Store at 4 degrees C in the dark until flow cytometry.