====================================
Chitin-binding protein purification
====================================

.. warning::

  This protocol was attempted for Tn5 purification. This was unsuccessful,
  though possibly not because of this protocol.

Required solutions
-------------------
* **Chitin Lysis buffer**:

  ===================== ================   ========================
  Component             Concentration        amount/L final volume
  ===================== ================   ========================
  DI water              89.8%                     898 mL
  HEPES                 20mM                    4.766 g
  NaCl                  800 mM                  46.762 g
  EDTA                  1 mM                    0.292 g
  Triton-X100           0.2%                    2 mL
  Glycerol              10%                     100 mL
  KOH                    to pH 7.2
  ===================== ================   ========================

* **Chitin cleavage buffer**:

  ===================== ================   ========================
  Component             Concentration        amount/L final volume
  ===================== ================   ========================
  Chitin lysis buffer      Base                 898 mL
  DTT                     100 mM                15.423 g
  ===================== ================   ========================

* **Chitin stripping buffer**:

  ===================== ================   ========================
  Component             Concentration        amount/L final volume
  ===================== ================   ========================
  Chitin lysis buffer      Base                 898 mL
  SDS                      1%                   10 g
  ===================== ================   ========================


* **2x Dialysis buffer**:

  ===================== ================   ========================
  Component             Concentration        amount/L final volume
  ===================== ================   ========================
  DI water              79.8%                     798 mL
  HEPES                 100mM                    23.83 g
  NaCl                  200 mM                  11.69 g
  EDTA                  0.2 mM                   0.0584 g
  DTT                     2 mM                   0.3085 g
  Triton-X100           0.2%                    2 mL
  Glycerol              20%                     200 mL
  KOH                    to pH 7.2
  ===================== ================   ========================

* **10% PEI**:

  ======================= ================   ============================
  Component                Concentration       amount/10 mL final volume
  ======================= ================   ============================
  Branched PEI (50% w/v)           10%           2  mL
  DI water                 -                    8 mL
  HCl                       -                   to pH 7.2
  ======================= ================   ============================


.. note::
  Use *branched* PEI. Any branched PEI should technically work,
  though the product mentioned in the literature is `Sigma P3143 <https://www.sigmaaldrich.com/US/en/product/sial/p3143>`__.


Protocol
--------
1. Resuspend the cell pellet in lysis buffer plus cOmplete protease inhibitor, on ice. For every gram of cell pellet, use 10 mL lysis buffer.
2. Sonicate the resuspended cells, using 5 cycles of 30-second, medium-amplitude 50% duty-cycle sonication.
3. Spin to clarify the lysate using maximum centrifuge speed (14600 xg) for 30 minutes.
4. If the protein of interest has DNA-binding activity, add 1.2 mL/10mL **10% PEI** dropwise while stirring.
   This should be **branched PEI** as noted above.
   Centrifuge at maximum speed for 30 minutes to remove bound DNA.
5. Incubate the supernatant with 10 mL chitin resin / 500 mL original culture. Tube rotate for 1 hour at 4C.
6. Wash with 10-20 CVs of lysis buffer.
7. Add cleavage buffer. Incubate at 4C for 48 hours.
8. Elute into separate 1 mL fractions.
9. Proceed to dialysis and concentration.

Dialysis and concentration protocol
-----------------------------------

.. note:: 

  Both the dialysis tubing and the protein concentration columns come with a molecular weight cutoff!
  Make sure that both the tubing and columns are sufficiently sized so that the protein cannot leave
  through the tubing but also gets concentrated on the column!


1. Prepare dialysis tubing, long enough to hold the desired volume, plus about a 20% headspace.
   You can look up length calculators, or try it out with water first.
2. For easy filling, soak the tubing in water to make it more pliable.
3. Clip the bottom of the tubing shut with the dialysis tubing clips.
4. Set the tubing in a clean glass beaker, in case you spill in the next step.
5. Using a seriological pipette, transfer each elution buffer fraction into segment of tubing. Close the tubing
   with a second dialysis tubing clip on the top.
6. Check that the tubing is watertight, over/inside the clean glass beaker. 
7. Transfer the tubing to a large plastic beaker, filled with 2x dialysis buffer. Place the beaker + tubing
   on a stir plate and let the dialysis proceed at 4C in the deli fridge for around 4-8 hours.
8. Replace the dialysis buffer with fresh buffer, and let it stir for an additional 24 hours.
9. Further dialysis steps can be added on if desired purity not reached.
10. Follow the instructions on the protein concentrator columns to concentrate the resulting 
    Look up length calculators, or try it out with water to determine the correct length.


Regeneration Protocol
---------------------
1. Wash the resin with 3CVs of stripping buffer.
2. Stop the flow, and soak the resin in stripping solution for 30 minutes.
3. Wash with an additional 10 CVs of stripping buffer.
4. Rinse with 20 CVs of water.
5. Equilibrate with 5 CVs of 20% ethanol.
6. Store the resin in 20% ethanol at 4C.
