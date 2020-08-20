=============================
His-tag protein purification
=============================

Required solutions
-------------------
* **Lysis buffer**:
* **10% PEI**: pH to 7.2

.. note::
    Do not use the cOmplete running and elution buffers with normal Ni-NTA His-tag resin!
    They contain chelating agents that will remove the nickel ions! cOmplete His-tag
    resin is resistant to small concentrations of chelating agents.

* **cOmplete running buffer (native)**:

  ===================== ================   ==================
  Component             Concentration        g/L final volume
  ===================== ================   ==================
  DI water              90%
  HEPES                 20mM                    4.766 g
  NaCl                  800 mM                  46.762 g
  Imidazole             20 mM                   1.362 g
  EDTA                  1 mM                    0.292 g
  DTT                   2 mM                    0.3085 g
  Glycerol              10%                     
  NaOH                  to pH 7.2
  ===================== ================   ==================

.. note::
  Perform the pH after all components have been added.

* **cOmplete elution buffer (native)**: 

  ===================== ================   ================== ================================================================
  Component             Concentration        g/L final volume  Purpose
  ===================== ================   ================== ================================================================
  DI water              90%
  HEPES                 20mM                    4.766 g       Main buffer component
  NaCl                  800 mM                  46.762 g      High salt maintains protein solubility
  Imidazole             300 mM                  20.42 g       Prevents non-specific binding to column.
  EDTA                  1 mM                    0.292 g       Chelating agent, deactivates proteases and other enzymes.
  DTT                   2 mM                    0.3085 g      Reducing agent, prevents nonspecific cystine crosslinking.
  Glycerol              10%                                   Prevents hydrophobic protein-protein interactions.
  NaOH                  to pH 7.2
  ===================== ================   ================== ================================================================

.. note::
  Perform the pH after all components have been added.

* **NI-NTA running buffer (native)**:

  ===================== ================   ================== ===================================================================
  Component             Concentration        g/L final volume Purpose
  ===================== ================   ================== ===================================================================
  DI water              90%
  NaH2PO4               50mM                    6.90 g        Main buffer component.
  NaCl                  800 mM                  46.762 g      High salt maintains protein solubility.
  Imidazole             15 mM                   1.022 g       Prevents non-specific binding to column.
  beta-mercaptoethanol  5 mM                                  Weaker reducing agent, prevents nonspecific cystine crosslinking.
  Glycerol              10%                                   Prevents hydrophobic protein-protein interactions.
  NaOH                  to pH 8.0
  ===================== ================   ================== ===================================================================

.. note::
  Perform the pH after all components have been added.
 
Protocol
--------
 
Protocol
--------
1. Resuspend the cell pellet in lysis buffer, on ice. For every gram of cell pellet, use 10 mL lysis buffer.
2. Sonicate the resuspended cells, using 5 cycles of 30-second, medium-amplitude 50% duty-cycle sonication.
3. Spin to clarify the lysate using maximum centrifuge speed (14600 xg) for 30 minutes.
4. If the protein of interest has DNA-binding activity, add 1.2 mL/10mL **10% PEI** dropwise while stirring.
   Cetnrifuge at maximum speed for 30 minutes to remove bound DNA.
5. Fill a column with roughly 1.0 mL resin per gram of cell lysate.

.. note::
    When using affinity columns, the volumes required will be listed as Column Volumes (CVs).
    The amount of resin is the CV. For a gram prepration, this would mean the CV is 1 mL.

5. Equilibrate the column with 3 CVs of running buffer.
6. Flow the clarified cell lysate across the column, collecting the flow-through.
7. Rinse the column with 8 CVs of running buffer, collecting flow-through fractions.
8. Elute with four separate 0.5 CV washes of elution buffer.
9. Run all collected samples on a SDS-page gel to confirm successful purification.