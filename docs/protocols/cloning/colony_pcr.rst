Colony PCR
==========

Colony PCR is one method to screen colonies after transformation to identify clones harboring the correct plasmid product.
(See the Cloning Workflow Overview :ref:`Step 4: Screen colonies <screening>` for more.)

Materials
---------

- Agar plate with colonies
- Fresh agar plate (with the same antibiotic)
- `Taq 2X Master Mix <https://www.neb.com/en-us/protocols/2012/09/13/protocol-for-taq-2x-master-mix-m0270>`_
- Elga water 
- Two primers, each diluted to 10 µM (typical working stock)
- PCR strip tubes, one tube per colony to be picked
- Toothpicks

Protocol
--------

1. **Identify a primer pair** to amplify a region unique to your desired plasmid product (i.e., distinct in length from any 
   reactants or incorrect products). 

   - It is usually convenient to choose two primers in the plasmid backbone, amplifying the entire new insert. For entry vectors
     or ``pShip`` plasmids, ``oSEQ043`` and ``oSEQ044`` work well.
   - Amplified regions (amplicons) can be large; at least 4 kb regions amplify sufficiently. This allows the entire insert to be amplified; 
     however, one con is that it takes much longer for the reaction to run.
   - For small inserts, or for inserts that vary only slightly in size from the original backbone vector, primer pairs should 
     instead be chosen to amplify as short a region as possible (that still captures the expected differences). This helps make small 
     size differences more readily apparent when analyzing the results.
   - Be sure to choose a primer pair with compatible annealing temperatures. To determine annealing temperatures, you can use the 
     `NEB Tm Calculator <https://tmcalculator.neb.com/#!/main>`_, specifying "Taq DNA polymerase" as the "Product Group" and selecting 
     "Taq 2X Master Mix" as the "Polymerase/Kit".


2. **Label colonies** to screen on your agar plate (e.g., circle, point an arrow) and number each colony.
   
   - Choose colonies that you can isolate with confidence, i.e., not touching or too close to other colonies.
   - The number of colonies to pick is determined by the estimated specificity of the assembly reaction. For reactions that rarely produce 
     incorrect products (e.g., Gateway with proper antibiotic selection), fewer colonies will be sufficient (2-3). For reactions 
     that often produce incorrect products (e.g., oligo annealing and ligation), more colonies will likely need to be screened (≥6).

3. **Prepare a fresh agar plate** by drawing many small regions, one for each colony to pick, on the bottom of the plate (a simple grid 
   works well). Label each region with a colony number.
4. **Make the reaction mix** according to the calculations below, scaling by the number of colonies to pick. Pipet the reaction mix into 
   PCR strip tubes, 15 µL per tube and one tube per colony.

   ========== ============== =======
   Reagent     1X (1 colony)  8X
   ========== ============== =======
   Elga water  6              48
   Primer 1    0.75           6
   Primer 2    0.75           6
   Taq 2X MM   7.5            60
   **Total**   15 µL          120 µL
   ========== ============== =======

   .. note::

      The reaction will run well with slightly more or less than 15 µL per colony. Therefore, rather than making extra mix to account for 
      pipetting loss, instead pipet 14-14.5 µL per tube.

5. **Pick colonies** one at a time under a flame: Touch the end of a sterile toothpick (or pipette tip) to the colony, swirl the toothpick 
   in the reaction mix of one of the PCR strip tubes, then streak the wet toothpick on the corresponding region of the prepared fresh agar 
   plate. Discard the toothpick and close the tube.

6. **Run the PCR reaction** by placing the tubes in a thermocycler. Set the correct annealing temperature (from the 
   `NEB Tm Calculator <https://tmcalculator.neb.com/#!/main>`_) and extension time (**1 min/kb** of amplified sequence). Run 30 cycles 
   to ensure sufficient amplification.

   +----------------------+--------------------+------------+
   | Step                 | Temperature (ºC)   |  Time      |
   +======================+====================+============+
   | Initial denaturation |  95                | 30 s       |
   +----------------------+--------------------+------------+
   | | Each cycle         | | 95               | | 15 s     |
   | |  x 30 cycles       | | {annealing temp} | | 15 s     |
   | |                    | | 68               | | 1 min/kb |
   +----------------------+--------------------+------------+
   | Final extension      |  68                | 5 min      |
   +----------------------+--------------------+------------+

7. **Run the PCR products on an agarose gel** to assess the results. Note colonies with the correct amplicon band size.

   - **For amplicons >500 bp:** Use a 1% gel (100 mg agarose per 10 mL 1xTAE buffer) and run at 100V for 25 min.
   - **For amplicons <500 bp:** Use a 2% gel and run at 90V for 30 min.
   - Load 5 µL of reaction mix. Note that the reaction mix already contains loading dye, so no additional dye needs to be added.

8. **Incubate the streaked plate** overnight at 30ºC. To start cultures from the streaked plate on the same day, instead grow for ~6 hours 
   at 37ºC. Once visible bacteria is growing for each colony, the plate can be used to inoculate cultures for plasmid preps and 
   :doc:`glycerol stocks <glycerol_stocking>`.
   Wrap the plate in parafilm and store at 4ºC for up to ~4 weeks.
