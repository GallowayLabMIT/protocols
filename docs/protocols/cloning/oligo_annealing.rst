======================================
Oligo annealing for ligation cloning
======================================

This protocol describes how to anneal and phosphorylate oligos to add short sequences to plasmids via ligation cloning. 
This could be useful to make new microRNA target sites or CRISPR guide RNAs, for instance.

Oligo phosphorylation
---------------------------------
1. Order desalted oligos (e.g., from Azenta/Genewiz) and reconstitute as usual to 100 µM.
2. Combine the following in a PCR tube:

    ============================== ===========================
    Reagent                          Amount
    ============================== ===========================
    Oligo (**100 µM**)              1 µL
    10X T4 DNA ligase buffer        1 µL
    T4 PNK (polynucleotide kinase)  0.5 µL
    Water                           7.5 µL
    **Total**                       **10 µL**
    ============================== ===========================

    .. important::
        Use the *original 100 µM stock* of oligos, not a diluted working stock, in the reaction.

    .. note::
        The PNK buffer that comes with the PNK enzyme does not include ATP, so T4 ligase buffer is used instead. If you want to use the PNK buffer, also add 1 mM ATP.

3. Run the reaction on a thermocycler at 37°C for 1 hr, then heat inactivate the PNK at 65°C for 20 min.
4. Phosphorylated oligos can be stored at -20°C.


Oligo annealing
---------------------------------
1. Combine 1 µL of each phosphorylated oligo (i.e., forward and reverse oligos from the reaction above) in a PCR tube with 18 µL water, for a total volume of 20 µL.
2. In a thermocycler, heat at 95°C for 3 min then cool to room temperature over ~30-60 min. There should be a temperature step function on the thermocycler, 
   e.g., cool by 0.1°C every second.
3. Store annealed oligo fragments at -20°C so they remain annealed.

.. important:: 
    Make sure you design your fragments to have sticky ends appropriate for your ligation!

Combined oligo phosphorylation and annealing
--------------------------------------------
To save time, the phosphorylation and annealing steps can be combined as follows:

1. Order desalted oligos (e.g., from Azenta/Genewiz) and reconstitute as usual to 100 µM.
2. Combine the following in a PCR tube:

    ========================= ===========================
    Reagent                   Amount
    ========================= ===========================
    Forward oligo (100 µM)    1 µL
    Reverse oligo (100 µM)    1 µL
    10X T4 DNA ligase buffer  2 µL
    T4 PNK                    1 µL
    Water                     15 µL
    **Total**                 **20 µL**
    ========================= ===========================

3. Run the reaction on a thermocycler: 37°C for 1 hr, heat at 95°C for 3 min, then cool to room temperature over ~30-60 min. There should be a temperature step function on the thermocycler, 
   e.g., cool by 0.1°C every second.
4. Store phosphorylated and annealed oligo fragments at -20°C.

.. note:: 
    When combined protocol is used, a 1:10 dilution of annealed oligos may be more effective in a downstream ligation reaction.

.. note::
    Measuring the concentration of annealed oligos on a Nanodrop can be done, but is not necessary. 1 µL of the final annealed and phosphorlyated product (~0.5 µM) is typically relevant for ligation asssemblies.
