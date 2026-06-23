=================
Plasmid prepping 
=================

To obtain plasmids for cloning steps or use in tissue culture, we amplify them in bacteria and purify the resulting plasmid DNA.
We can prep at several scales (mini, midi, or maxi, even larger versions also exist) depending on the culture volume.

Miniprep
---------
This protocol is adapted from instructions for the NEB Monarch® Spin Plasmid Miniprep Kit (`NEB T1110L <https://www.neb.com/en-us/products/t1110-monarch-spin-plasmid-miniprep-kit>`_). 
**Minipreps yield ~40 uL of DNA at ~100-400 ng/uL.**
High copy, large plasmids like those with the LentiX backbone can reach ~400 ng/uL, while smaller plasmids like pPVs may remain <100 ng/uL.

When receiving a new kit: store RNase A in Anna -20ºC in the dedicated box, and the remaining reagents at room temp.

When opening a new bottle of buffer:

- Buffer B1: add RNase A (1 vial per bottle, stored in Anna -20ºC in a dedicated box), then store at 4ºC 
- Buffer BZ: add 18 mL isopropanol
- Buffer WZ: add 104 mL ethanol

1. Under a flame, aliquot 3-5 mL of LB media with antibiotic matching the plasmid antibiotic resistance.
   Use 14-mL culture tubes, placing the cap on securely but not airtight (the bacteria need aeration to grow).
2. Pick a single colony or dab a glycerol stock with a toothpick or pipette tip. Place the toothpick or pipette tip in the liquid culture.
3. Let the bacteria grow in the shaker overnight, ideally 12-16 hours and no longer than 24 hours.

    .. note::
        Grow viral plasmids in 30ºC to reduce the chance of recombination. Non-viral plasmids may be grown at 37ºC for better yield.

4. Spin the liquid cultures at 4800xg (max speed in bucket rotors) for 5 minutes, using the large centrifuge by shakers.
5. Pour or aspirate the supernatant into a cells/media waste flask.

    .. warning::
        Do not add media/cells into the miniprep waste or vice versa! If this occurs, talk to the EHS rep.
        Add bleach to the affected flask in the fume hood and allow fumes to disperse. 
        A black precipitate may form; dispose of the solids in the biowaste and drain the liquid in the sink. 

6. Resuspend the cell pellet in 200 uL Buffer B1 (stored in the 4ºC deli fridge) and transfer to a 1.7-mL tube.
7. Add 200 uL Buffer B2 and gently invert 5-6 times to lyse the cells. Incubate at room temp for 1 minute.
8. Add 400 uL Buffer B3 and invert until uniformly yellow (no pink). Incubate for 2 minutes at room temp.

    .. note::
        MC adds 250 uL of B2 and immediately after addition starts a time for 90 seconds, inverts for 30 seconds, and adds 500 uL of B3 at 90 seconds.

9. Spin down on a benchtop centrifuge at max speed (16,000xg) for 5 minutes.
10. While samples are spinning, place a filter column in a collection tube for each sample.
    
    .. important::
        Be sure to use the provided Monarch **Spin S2D columns**, not the Spin S1A ones that come with the PCR cleanup kit.
        The binding capacity of the Spin S2D column is 20-100 ug, but only 5 ug for the Spin S1A columns.

11. Transfer the lysate to the column. Discard the pellet.
12. Spin the lysate at max speed for 1 minute.
13. Aspirate the lysate from the collection tube into the miniprep waste.
14. Add 200 uL of Buffer BZ (Wash 1).
15. Spin at max speed for 1 minute.
16. Add 400 uL of Buffer WZ (Wash 2).
17. Aspirate the flow-through from the collection tube into the miniprep waste.
18. Spin at max speed for 1 minute. This dry spin helps remove traces of buffer from the column.
19. Transfer the column to a fresh 1.7-mL tube.
20. Add 40 uL of Elga water to the column and incubate for at least 1 minute at room temp.
    
    .. tip::
        Pre-warm Elga water in a 55ºC water bath for better elution.

21. Spin at max speed for 1 minute to elute the DNA.
22. To quantify yield, measure 1.5-2 uL of sample on the Nanodrop.

    - Concentrations <20 ng/uL are unreliable and indicate a poor prep.
    - The A260/280 ratio should be 1.80-2.00. Lower values indicate protein contamination.
    - The A260/230 ratio should be >2.00 (>1.80 is okay). Lower values indicate salt contamination from the buffers used in the kit.


.. _midiprep:

Midiprep
---------
This protocol is adapted from instructions for the QIAGEN Plasmid Plus Midi Kit (`Qiagen 12945 <https://www.qiagen.com/us/products/discovery-and-translational-research/dna-rna-purification/dna-purification/plasmid-dna/qiagen-plasmid-plus-kits?catno=12945>`_),
following the **high-yield protocol** (suitable for high-copy plasmids, which applies to most of ours). 
**Midipreps yield ~200 uL of DNA at ~500-2,000 ng/uL.**
Midipreps are preferred for transfections with large volumes of DNA (e.g., for virus production) because the kit better removes 
endotoxins (bacterial outer membrane components that induce an immune response in mammalian cells).

When opening a new bottle of buffer:

- Buffer P1: add RNase A and LyseBlue reagent (1 vial each per bottle), then store at 4ºC 
- Buffer PE: add 40 mL ethanol (confirm volume on bottle)

1. Under a flame, aliquot 40-50 mL of LB media with antibiotic matching the plasmid antibiotic resistance.
   Use a 250-mL flask for optimal aeration of the culture (125-mL flasks can be used in a pinch).
2. Pick a single colony or dab a glycerol stock with a toothpick or pipette tip. Place the toothpick or pipette tip in the liquid culture.
3. Let the bacteria grow in the shaker overnight, typically ~24 hours.

    .. note::
        Grow viral plasmids in 30ºC to reduce the chance of recombination. Non-viral plasmids may be grown at 37ºC for better yield.
        
4. Transfer the culture to a 50-mL conical and spin at 4800xg (max speed in bucket rotors) for 10-15 minutes, using the large centrifuge by shakers.

    .. note::
       The midiprep protocol recommends spinning at 6000xg and 4ºC for 15 minutes, but KL has had successful preps with the parameters written above.

    .. important::
       If spinning at 6000xg, the fixed rotor is required (stored in the cabinet below the centrifuge). 
       To avoid spilling culture into the rotor, fill the 50-mL conical with **up to 40 mL** of culture.

5. Pour off the supernatant into one of the empty flasks.
6. Safely dispose of the supernatant and disinfect your glassware: Add bleach to a final concentration of 10% to the supernatant, wait 20 minutes, and pour down the sink. 
   To the remaining empty flasks, add enough 10% bleach to cover the surfaces, swirl, and wait 20 minutes. 
   Then, thoroughly rinse the disinfected flasks and place them next to the Elga machine to be dishwashed.

    .. note::
        Collecting the supernatant (cells/media) waste in flasks and bleaching it yourself keeps the aspirator waste from filling up quickly!

        While waiting for the flasks to disinfect, keep them at your bench rather than in the sink, if possible. This keeps the sinks clear for others to use.

7. Resuspend the cell pellet in 4 mL of Buffer P1 (stored at 4ºC in the deli fridge).
8. Add 4 mL of Buffer P2 and gently invert 5-6 times to lyse cells. Incubate at room temp for 3 minutes. The suspension should turn blue and will become viscous. 
9.  While you wait, place a large filter column in a new 50-mL conical for each sample.
10. Add 4 mL Buffer S3 and mix 4-6 times, or until the lysate is completely colorless.
11. Transfer the lysate to the filter column (pouring is fine) and incubate for 10 minutes.
12. During incubation, place the small spin columns on the vacuum manifold and add tube extenders. Connect the vacuum manifold to the miniprep aspirator.
13. Gently insert a plunger into the filter column to filter the lysate into the 50-mL conical.
14. Add 2 mL Buffer BB to the cleared lysate and invert 4-6 times.
15. Transfer the solution to the spin column + tube extender on the vacuum manifold. Turn on the vacuum to draw all the liquid through.

    .. admonition:: Troubleshooting the vacuum manifold
        
        Sometimes, the vacuum pump is not strong enough to effectively filter the solution through the column. 
        
        - Double check all the tubing connections and ensure caps seal unused spots on the manifold.
        - If the solution is not flowing through, you can try the other miniprep vacuum pump, or directly connect each column to the aspirator tube.
        - Alternatively, you can add 700 uL of lysate to the spin column at a time and centrifuge at max speed (16,000xg) for 1 minute, 
          aspirating the supernatant from the collection tube after each spin.

16. With the vacuum still on, remove the tube extender and add 700 uL Buffer ETR to the spin column.
17. Once all the liquid flows through, add 700 uL Buffer PE and allow the vacuum to draw all the liquid through the column.
18. Remove the spin column from the vacuum manifold and transfer to a collection tube. Spin at max speed (16,000xg) for 1 minute.
    This dry spin helps remove traces of buffer from the column.
19. Transfer the column to a fresh 1.7-mL tube.
20. Add 200 uL of Buffer EB and incubate at room temp for at least 2 minutes.

    .. note::
        Elga water can also be used to elute the DNA. However, Buffer EB (10 mM Tris-Cl, pH 8.5) helps stabilize the DNA for long-term use.
        Since Buffer EB doesn't contain EDTA, it shouldn't interfere with downstream reactions, if you later use the midiprep for cloning.

    .. tip::
        Pre-warm Buffer EB in a 55ºC water bath for better elution.

21. Spin at max speed for 1 minute to elute the DNA.
22. To quantify yield, measure 1.5-2 uL of sample on the Nanodrop.

    - Concentrations <200 ng/uL indicate a poor midiprep, but the DNA is still fine to use.
    - The A260/280 ratio should be 1.80-2.00. Lower values indicate protein contamination.
    - The A260/230 ratio should be >2.00 (>1.80 is okay). Lower values indicate salt contamination from the buffers used in the kit.
  
23. Store midiprepped plasmids at -20ºC for best long-term stability.


Maxiprep
---------
This protocol is adapted from instructions for the QIAGEN Plasmid Plus Maxi Kit (`Qiagen 12963 <https://www.qiagen.com/us/products/discovery-and-translational-research/dna-rna-purification/dna-purification/plasmid-dna/qiagen-plasmid-plus-kits?catno=12963>`_),
following the **high-yield protocol** (suitable for high-copy plasmids, which applies to most of ours).
**Maxipreps yield ~400 uL of DNA at ~500-2,000 ug/uL.**
This protocol is essentially identical to midipreps, just with larger volumes. We typically only maxiprep the packaging and envelope plasmids for viral production, which require sequencing after every prep given 
the likelihood of recombination.

When opening a new bottle of buffer:

- Buffer P1: add RNase A and LyseBlue reagent (1 vial each per bottle), then store at 4ºC 
- Buffer PE: add 24 mL ethanol (confirm volume on bottle)

1. Under a flame, aliquot 100 mL of LB media with antibiotic matching the plasmid antibiotic resistance.
   Use a 500-mL flask for optimal aeration of the culture.
2. Pick a single colony or dab a glycerol stock with a toothpick or pipette tip. Place the toothpick or pipette tip in the liquid culture.
3. Let the bacteria grow in the shaker overnight, typically ~24 hours.

    .. note::
        Grow viral plasmids in 30ºC to reduce the chance of recombination.

4. Transfer the culture to several 50-mL conicals and spin at 4800xg (max speed in bucket rotors) for 10-15 minutes, using the large centrifuge by shakers.

    .. note::
       The midiprep protocol recommends spinning at 6000xg and 4ºC for 15 minutes, but KL has had successful preps with the parameters written above.

    .. important::
       If spinning at 6000xg, the fixed rotor is required (stored in the cabinet below the centrifuge). 
       To avoid spilling culture into the rotor, fill the 50-mL conical with **up to 40 mL** of culture.

5. Pour off the supernatant into one of the empty flasks.
6. Safely dispose of the supernatant and disinfect your glassware: Add bleach to a final concentration of 10% to the supernatant, wait 20 minutes, and pour down the sink. 
   To the remaining empty flasks, add enough 10% bleach to cover the surfaces, swirl, and wait 20 minutes. 
   Then, thoroughly rinse the disinfected flasks and place them next to the Elga machine to be dishwashed.

    .. note::
        Collecting the supernatant (cells/media) waste in flasks and bleaching it yourself keeps the aspirator waste from filling up quickly!

        While waiting for the flasks to disinfect, keep them at your bench rather than in the sink, if possible. This keeps the sinks clear for others to use.

7. Resuspend the cell pellet in 8 mL of Buffer P1 (stored at 4ºC in the deli fridge). You can split the volume across the conicals, resuspend each, then recombine into a single conical.
8. Add 8 mL of Buffer P2 and gently invert 5-6 times to lyse cells. Incubate at room temp for 3 minutes. The suspension should turn blue and will become viscous. 
9.  While you wait, place a large filter column in a new 50-mL conical for each sample.
10. Add 8 mL Buffer S3 and mix 4-6 times, or until the lysate is completely colorless.
11. Transfer the lysate to the filter column (pouring is fine) and incubate for 10 minutes.
12. During incubation, place the small spin columns on the vacuum manifold and add tube extenders. Connect the vacuum manifold to the miniprep aspirator.
13. Gently insert a plunger into the filter column to filter the lysate into the 50-mL conical.
14. Add 5 mL Buffer BB to the cleared lysate and invert 4-6 times.
15. Transfer the solution to the spin column + tube extender on the vacuum manifold. Turn on the vacuum to draw all the liquid through.

    .. admonition:: Troubleshooting the vacuum manifold
        
        Sometimes, the vacuum pump is not strong enough to effectively filter the solution through the column. 
        
        - Double check all the tubing connections and ensure caps seal unused spots on the manifold.
        - If the solution is not flowing through, you can try the other miniprep vacuum pump, or directly connect each column to the aspirator tube.
        - Alternatively, you can add 700 uL of lysate to the spin column at a time and centrifuge at max speed (16,000xg) for 1 minute, 
          aspirating the supernatant from the collection tube after each spin.

16. With the vacuum still on, remove the tube extender and add 700 uL Buffer ETR to the spin column.
17. Once all the liquid flows through, add 700 uL Buffer PE and allow the vacuum to draw all the liquid through the column.
18. Remove the spin column from the vacuum manifold and transfer to a collection tube. Spin at max speed (16,000xg) for 1 minute.
    This dry spin helps remove traces of buffer from the column.
19. Transfer the column to a fresh 1.7-mL tube.
20. Add 400 uL of Buffer EB and incubate at room temp for at least 2 minutes.

    .. note::
        Elga water can also be used to elute the DNA. However, Buffer EB (10 mM Tris-Cl, pH 8.5) helps stabilize the DNA for long-term use.

    .. tip::
        Pre-warm Buffer EB in a 55ºC water bath for better elution.

21. Spin at max speed for 1 minute to elute the DNA.
22. To quantify yield, measure 1.5-2 uL of sample on the Nanodrop.

    - Concentrations <200 ng/uL indicate a poor midiprep, but the DNA is still fine to use.
    - The A260/280 ratio should be 1.80-2.00. Lower values indicate protein contamination.
    - The A260/230 ratio should be >2.00 (>1.80 is okay). Lower values indicate salt contamination from the buffers used in the kit.
  
23. If prepping common stocks of viral packaging and envelope plasmids, dilute the plasmids to 500 ng/uL and aliquot 500 uL each in fresh 1.7-mL tubes.
    Send each prep for whole plasmid sequencing to confirm the plasmids have not recombined/mutated.
24. Store maxiprepped plasmids at -20ºC for best long-term stability.

