==========================================
Flow Cytometry
==========================================

.. _plate spinning:

96-well plate spinning
-----------------------

.. note::
    It is convenient to prep cells for flow cytometry in a 96-well plate because you can add media and do mixing with a multichannel pipette.

.. important::
    Make sure you have at least 2 autoclaved tips per well (1 for triturating, 1 for transferring to U-bottom). For a full 96-well, that means at least 2x200 µL boxes. Plus more for PBS washes and adding in dissociation media!


1. Wash, dissociate, and triturate cells in plate (swap out tips every time for the trituration).

   - You don't need to swap tips if you hover above the plate while adding in wash and dissociation buffer but you **must swap tips for trituration** (i.e. everytime you put the tip into the well)

2. Take the plate out of the BSC (**the plate is no longer sterile at this point**).

3. *Optional* Transfer contents of (flat bottom) plate to a 96-well U-bottom or V-bottom plate

   - A U-bottom plate is not necessary, but cells pellet better on U- or V-bottom plates, and lose less volume running flow.

4. Spin the plate at 400 rcf (g) for 5 min using the plate bucket rotor.

   - Balance with another 96-well plate filled with roughly equivalent amount of water (there's a balance plate near the centrifuge) but balancing doesn't have to be exact at this low speed

5. Aspirate supernatant.

   - Tilting the plate and aspirating from corner helps to avoid disturbing the cell pellet. Do NOT aspirate straight from the middle of well.

6. If performing any staining (e.g. Live/Dead, surface markers, intracellular, etc.), skip step 7 and proceed to :ref:`cell staining <Cell staining>`.

7. Resuspend in ~200 µL PBS and pipet up and down to mix well (must be single-cell suspension---no clumps!).

   - Swap tips in between each transfer to avoid contamination between wells!
   - If using flat-bottoms, decrease the Attune uptake volume settings so you don't create bubbles (i.e. you will lose more volume with flat-bottom wells)

8. Load plate into the Attune CytKick autosampler and run.

.. _Cell staining:

Cell staining (Live/Dead & surface markers)
-------------------------------------------

.. note::
    Cells are usually stained in U- or V-bottom 96-well plates but they can be stained in any container (e.g. test tubes, Eppendorf tubes, polystyrene round-bottom tubes, cluster tubes).

.. tip::
   It is recommended to stain with ice-cold reagents/solutions and at 4°C, since low temperature prevents modulation and internalization of surface antigens which can produce a loss of florescence intensity.

1. Begin with cell pellets, i.e. wash, dissociate, triturate, spin, and aspirate samples (e.g. :ref:`steps 1-5 above <plate spinning>` for a 96-well plate).
2. Resuspend cells in 100µL of staining solution.

   - Staining solution is made in FACS buffer (2% FBS in PBS).
   - Antibody dilutions will require optimization.
   - Primary antibodies are generally good at 1:500 dilution, Secondary antibodies ~1:1000, Live/Dead (e.g. Zombie) ~1:1000.

3. Incubate for ~30 min at 4°C in the dark, on ice or in 4°C fridge.

   - Timing will require optimization.

4. Wash plate 3 times by centrifugation at 400 rcf for 5 min. If stained with unconjugated antibodies, repeat steps 1-3 but with staining solution containing secondary antibodies.

If staining for intracellular/nuclear protein targets, proceed with the following. If not, skip to step 14.

5.	Remove supernatant and incubate cells in 3.7-4% paraformaldehyde (PFA) (in fume hood) for 15 min

   -  EU calls for 3.7% PFA

6.	Add 1 mL PBS and spin cold at 4°C to pellet cells

7. Aspirate solution and incubate cells in 0.5% Tween/PBS for 15 min to permeabilize

8.	Add 1 mL PBS and spin cold at 4°C to pellet cells

9.	Aspirate solution and incubate cells in 200 µL primary antibody (diluted in blocking solution) for 1 hr in the rotator at 4°C
.. note:: Some antibodies (e.g. Ki67) work better overnight in the rotator at 4°C

10.	Add 1 mL PBS and spin cold at 4°C to pellet cells

11.	Aspirate solution and incubate cells in 200 µL secondary antibody (diluted in blocking solution) for 30 min in the rotator at 4°C in the dark

12.	Add 1 mL PBS and spin cold at 4°C to pellet cells

13.	If doing a DNA stain, add Hoechst or DAPI diluted in PBS for 10 minutes at room temp, then wash with PBS
.. note:: All spins are performed at ~500 rcf for 5 min. Our centrifuge follows RCF = 1e-4*[rpm]^2 + 4e-2*[rpm] - 6e1, where 2200 rpm = 512 rcf. It is recommended to perform all spins at 4°C once the cells have been fixed to prevent pellet loss.

14. For immediate analysis:

   a. Resuspend in ~200 µL FACS buffer (or PBS), pipet up and down to mix well (must be single-cell suspension---no clumps!)

      - Swap tips in between each transfer to avoid contamination between wells!
      - If using flat-bottoms, decrease the Attune uptake volume settings so you don't create bubbles (i.e. you will lose more volume with flat-bottom wells)

   b. Load plate into the Attune CytKick autosampler and run.

15. To preserve cells for several days:

   a. Resuspend in 1-4% paraformaldehyde and incubate for 10-15 min at room temp.
   b. Centrifuge your samples at 400 rcf for 5 min and resuspend in 200 µL of PBS.
   c. Store plate at 4°C in the dark until analysis.