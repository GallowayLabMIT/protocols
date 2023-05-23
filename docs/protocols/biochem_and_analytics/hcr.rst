************
HCR RNA-FISH
************

Prepare necessary buffers as described in :doc:`/recipes/fish/fish_buffers`
Expected time: 3 days

.. note::
    All spins are performed at ~500 rcf for 4 min. Our centrifuge follows RCF = 1e-4*[rpm]^2 + 4e-2*[rpm] - 6e1, where **2200 rpm = 512 rcf**.
    It is recommended to perform all spins at 4°C once the cells have been fixed to prevent pellet loss. 

Solution Detection Stage
========================
1. Steps 1-5 of :doc:`antibody_staining`
2. Add 200 uL of probe hybridization buffer for 30 min at 37 degrees C
3. Prepare probe solution by adding 2 uL of 1 uM stock to 500 uL of probe hybridization buffer at 37 degrees C
4. Remove pre-hybridization solution and add 200 uL of probe/hybrid buffer solution
5. Incubate samples **overnight (12-16 h**) at 37 degrees Celsius
6. Remove excess probes by washing 1x 15 min with 200 uL of probe wash buffer at 37 degrees Celsius
7. Wash samples 1x 5 min with 200 uL of 5X SSCT at room temperature

Solution Amplification Stage
============================
1. Pre-amplify samples in 500 uL of amplification buffer for 30 min at room temperature
   While waiting, begin Hairpin Preparation:

      a. Prepare 30 pmol of hairpin h1 and h2 by snap cooling 10 uL of 3 uM stock at 95 degrees Celsius for 90 seconds
      b. Cool hairpins in the dark at room temperature for 30 minutes
      c. Prepare hairpin solution by adding h1 and h2 hairpins to 500 uL amplification buffer

2. Remove pre-amplification solution and 200 uL of the hairpin/amplification buffer solution
3. Incubate samples **overnight (12-16 h)** in the dark at room temperature
4. Remove excess hairpins by washing with 200 uL of 5X SSCT at room temperature for:

   a. 1x 30 min
   b. 1x 5 min

5. Store at 4 degrees C in the dark until imaging