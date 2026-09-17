Nanobody-MNase production for GapRUN
====================================

This protocol describes how to produce the anti-GFP nanobody-MNase fusion protein required for :doc:`GapRUN</protocols/biochem_and_analytics/genomics_sequencing/gap_run>`.
It is based on the work of [Longo2024]_ and [Koidl2021]_.

Required materials
------------------
In addition to the buffer components listed below, we use the following kits and other components:

- B-Per: bacterial lysis kit (Thermo Fisher 78248)
- EDTA-free protease inhibitors (Thermo Fisher A32965)
- Glutathione spin columns (Thermo Fisher 16106)
- Biotin-tagged thrombin protease (Sigma-Aldrich SAE0147-5KU)
- T1 streptavidin beads (Thermo Fisher 65601)
- 10 kDa MWCO protein concentrator spin columns (Thermo Fisher 88513)

Stock buffer preparation
-------------------------

1. Prepare and check that there is sufficient amounts of the following :doc:`shared genomics buffers </recipes/biochem_and_analytics/shared_genomics_buffers>`:
  
  - 1M Tris-HCl, pH 7.5
  - 0.5M EDTA, pH 8.0
  - 5M NaCl

2. 1 mL of **1M IPTG**:

   ==============================    ================ ========  ====================
   Component                          Concentration    g / L     Amount / 1 mL
   ==============================    ================ ========  ====================
   IPTG                                  1 M           238.3     0.238 g
   Elga water                           to 1 mL
   Sterile filter, 0.22μm filter
   ==============================    ================ ========  ====================

3. 200 mL of **Protein purification buffer**:

   ==============================    ================ ========  ====================
   Component                          Concentration    g / L     Amount / 200 mL
   ==============================    ================ ========  ====================
   Tris-HCl                                125 mM      19.70     3.94 g
   NaCl                                    150 mM      43.83     8.77 g
   NaOH                                to pH 8.0
   Elga water                           to 200 mL
   ==============================    ================ ========  ====================

4. 50 mL of **0.1M K2PO4 (pH 7.0)**:

   ==============================    ================ ========  ====================
   Component                          Concentration    g / L     Amount / 50 mL
   ==============================    ================ ========  ====================
   K2PO4                               100 mM          17.42     0.871 g
   HCl                                 to pH 7.0
   Elga water                           to 50 mL
   ==============================    ================ ========  ====================


Day -n
------

It is best practice to start protein production cultures from single colonies. Either:

    a. Transform the plasmid encoding GST-LaG16-MNase (`Addgene 170978 <https://addgene.org/170978>`_, miniprep from pKG03872) into BL21 (DE3) cells.
    b. Or, streak directly from the pKG03873 glycerol stock (GST-LaG16-MNase in BL21 (DE3) cells) onto LB-Amp plates.

Day 0
-----

1. From one colony, start two 5 mL overnight cultures in LB-Amp media.
2. Autoclave four baffled 1L flasks, each filled with 200 mL of freshly prepared LB media.
3. After the flasks have cooled to room temperature (or the following day before starting), spike-in Amp.
4. Prepare fresh **sample buffer**. Sample buffer made within the last month or two can also have fresh
   β-mercaptoethanol spiked in lieu of making fresh buffer.

   =======================    ==================== ==========================
   Component                   Concentration        Amount / 10 mL
   =======================    ==================== ==========================
   50% glycerol                  10%                  2 mL
   1M Tris (pH 7.5)              50 mM                500 μL
   0.5M EDTA (pH 8.0)            20 mM                400 μL
   10% SDS                       2%                   2 mL
   β-mercaptoethanol             1%                   100 μL
   Bromophenol blue             to desired color
   Elga water                   to 10 mL              5 mL
   =======================    ==================== ==========================


Day 1
-----
1. Take a sample of the LB-Amp flasks for blanking the NanoDrop.
2. Inoculate each flask (containing 200 mL of media) with 2 mL of the overnight culture.
3. Incubate the flasks at 37C, shaking at 200 rpm, until it reaches an OD600 of 0.5, about two hours.
4. Take a 1.5 mL "pre-induction" sample, spin it down, and resuspend in 300 μL of sample buffer, storing it at -20C
   for future analysis.
5. Induce protein production by adding 200 μL of 1M IPTG to each flask. Lower the incubator
   temperature to 18C (or, whatever room temperature is) and let flasks grow overnight.

Day 2
-----
1. Measure the OD of the flasks by diluting a sample five-fold. The OD600 should have reached at least 6.0.
2. Take a 500 μL "post-induction" sample, spin it down, and resuspend in 300 μL of sample buffer, storing it at -20C
   for future analysis.
3. Split the bacterial culture into 50 mL tubes, not exceeding 40 mL per tube (to prevent spillage upon centrifugation in the fixed rotor).
4. Pellet the cells at maximum speed (14000 g) using the fixed-angle rotor. Combine the pellets together and mass them.
5. Prepare 100x protease inhibitor cocktail (1 EDTA-free protease inhibitor tablet dissolved in 500 uL) if there is not enough.
   The tablet will not fully dissolve: pipette up and down to resuspend settled particles.
6. Prepare 4 mL of complete B-Per (4 mL B-Per buffer, 2 μL lysosome, 2 μL DNAse I, both included in the B-Per kit, plus 40 μL of 100x protease inhibitor cocktail) per 1g of cell mass.
7. Resuspend the pellet in the B-Per. Use a 5 mL serological pipette to fully resuspend the pellet. 
8. After incubation at room temperature for 15 minutes, subject the slurry to two freeze thaw cycles to -80C and back to room temperature.
9. Clarify the lysate by spinning at 14000 g in a fixed-angle rotor for 30 minutes at 4C.
10. Take a 50 μL sample of the clarified lysate, dilute it to 300 μL in sample buffer, and store it at -20C for later analysis.
11. Dilute the clarified lysate 2:1 in protein purification buffer.
12. Prepare two 0.2 mL glutathione spin columns, by washing it twice with two column volumes of wash buffer.
13. Load the clarified lysate onto the columns. This takes many, many spins because our vacuum manifold isn't strong enough.

.. note::

   When you spin the columns, don't screw on the caps! Leave the red caps off the columns.

14. Once the lysate has been loaded, wash the columns with successive washes (2 column volumes: 400 μL) until
    the A280 absorbance drops to background levels. This takes about 10 total washes (20 CVs).
15. Cover the bottom of the columns with parafilm.
16. To each column, combine 100 units of biotin-tagged thrombin protease diluted to 200 μL in wash buffer to each column.
    Incubate overnight at 4C.

.. note::

   You can likely reduce the amount of protease; I used excess to ensure cleavage worked well. 

Day 3
------
1. Prepare 400μL fresh 1M dithiothreitol (DTT). This is much in excess, but we are limited by balance accuracy.

   ==============================    ================ ========  ====================
   Component                          Concentration    g / L     Amount / 400 μL
   ==============================    ================ ========  ====================
   DTT                                 1M             154.25     0.077 g
   Elga water                           to 400 μL
   ==============================    ================ ========  ====================

.. warning:: DTT stock should be collected as a separate waste stream.

2. Prepare 5 mL of sterile filtered, PIC-spiked fresh Buffer A:

   =======================    ==================== ==========================
   Component                   Concentration        Amount / 5 mL
   =======================    ==================== ==========================
   0.1M K2PO4 (pH 7.0)               20 mM               1 mL
   50% glycerol                  10%                   1 mL
   0.5M EDTA (pH 8.0)            0.5 mM                5 μL
   1M DTT                          1 mM                  5 μL
   Elga water                     to 5 mL                3 mL
   0.22 micron filter
   100x PIC                                           50 μL
   =======================    ==================== ==========================

2. Spin the columns, collecting "elution 1". Wash with 1 CV (200 μL) for two successive elutions.
3. Combine elutions that have significant A280 absorption: typically, the first two elutions are combined. 
4. Wash 60 μL of T1 streptavidin beads three times with PBS. Wash with 200 μL each time.
5. Combine the elutions with the washed streptavidin beads. Rotate the elutions at 4C for 30 minutes.
6. Remove the streptavidin beads with a magnet, and transfer the elution fraction to fresh low-binding tubes.
7. Take a 10 μL sample of the combined elution, dilute to 20 μL in sample buffer, and store at -20C for future analysis.
8. Load the elution fraction to 10 kDa MWCO protein concentrator spin columns, and concentrate to a volume of around 100 μL.
9. Buffer exchange by adding prepared Buffer A. Buffer exchange by adding 100 μL of Buffer A on top, re-concentrating to 100 μL. Repeat this four times.
10. Concentrate the protein to a volume of around 37.5 uL per column. Combine the two volumes to around 75 μL, diluting with
    Buffer A as needed.
11. Add 75 μL of 100\% glycerol on top, to reach 150 μL of purified protein. Aliquot and store at -20C.
12. Confirm the correct protien product by load each of the accumulated samples in sample buffer into a :doc:`prepared denaturing protein gel </protocols/protein_production/denaturing_protein_gel>`. Look for a single elution band
    corresponding to the nanobody-MNase.

To benchmark protein activity, proceed to the :doc:`GapRUN protocol </protocols/biochem_and_analytics/genomics_sequencing/gap_run>`.