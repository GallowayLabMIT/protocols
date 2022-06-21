======================================
Oligo annealing for ligation cloning
======================================

This protocol describes how to anneal and phosphorylate oligos to add short sequences to plasmids via ligation cloning. 
This could be useful to make new microRNA target sites or CRISPR guide RNAs, for instance.

Oligo phosphorylation
---------------------------------
1. Order desalted oligos and reconstitute as usual (e.g., order from Genewiz)
2. Combine the following in a PCR tube:

========================= ===========================
Reagent                   Amount
========================= ===========================
Oligo (100 uM)            1 uL
10X T4 DNA ligase buffer  1 uL
T4 PNK                    0.5 uL
Water                     7.5 uL
========================= ===========================

T4 PNK = T4 polynucleotide kinase

.. important::
    Use *original 100 uM stock* of oligos, not working stock, in the reaction.

.. note::
    The PNK buffer that comes with the PNK enzyme does not include ATP, so T4 ligase buffer is used instead. If you want to use the PNK buffer, also add 1 mM ATP.

3. Run the reaction on a thermocycler: 37°C for 1 hr, then heat inactivate the PNK at 65°C for 20 min.

.. note:: 
    Phosphorylated oligos can be stored at -20°C


Oligo annealing
---------------------------------
4. Combine 1 uL of each phosphorylated oligo (i.e., forward and reverse oligos from reaction above) in a PCR tube with 18 uL water, for a total volume of 20 uL.
5. In a thermocycler, heat at 95°C for 3 min then cool to room temperature over ~30-60 min. (There should be a temperature step function on the thermocycler, e.g. cool by 0.1°C every second.)

.. note:: 
    Annealed oligo fragments can be stored at -20°C

6. Nanodrop annealed fragments and use in ligation reaction.

.. important:: 
    Make sure you design your fragments to have sticky ends appropriate for your ligation!

Combined oligo phosphorylation and annealing
--------------------------------------------
To save time, the phosphorylation and annealing steps can be combined as follows:

1. Order desalted oligos and reconstitute as usual (e.g., order from Genewiz)
2. Combine the following in a PCR tube:

========================= ===========================
Reagent                   Amount
========================= ===========================
Forward oligo (100 uM)    1 uL
Reverse oligo (100 uM)    1 uL
10X T4 DNA ligase buffer  2 uL
T4 PNK                    1 uL
Water                     15 uL
========================= ===========================

3. Run the reaction on a thermocycler: 37°C for 1 hr, heat at 95°C for 3 min, then cool to room temperature over ~30-60 min. (There should be a temperature step function on the thermocycler, e.g. cool by 0.1°C every second.)
4. Nanodrop annealed fragments and use in ligation reaction.

.. note:: 
    When combined protocol is used, a 10X dilution of annealed oligos may be more effective in ligation reaction.
