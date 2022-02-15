============
Western Blot
============

Lysis
=====

Materials:
----------
* 10X Cell Lysis Buffer from CST
* 200mM PMSF (200X concentrated)
* Cell Scraper
* Blunt 21 gauge needles
* Lock-joint syringe
* Cells to lyse

.. note::
   * If 10X cell lysis buffer will be continually used, it is recommended that the 10x buffer be kept at 4°C for 1-2 weeks.
     For longer periods of time, buffer should be stored at -20°C. Aliquoting of 10x buffer is recommended if many small experiments are to be performed.
   * PMSF is unstable in water and should be added to lysis buffers or other aqueous solutions just prior to use.
     Typically, a final concentration of 1 mM provides sufficient protease protection. Store lyophilized at RT for 24 months protected from direct light.
     Once in solution, PMSF can be stored at -20ºC for up to 3 months, protected from light.

Protocol:
---------

.. important:: All reagents and lysates must be kept cold.


1. Cool microcentrifuge to 4°C for 20-30 minutes.
2. Dilute 10X Cell Lysis Buffer to a 1X solution using Elga water.
3. Chill 1X buffer on ice and add PMSF just prior to use.
4. Wash plate with ice-cold PBS to remove residual media.
5. Add 400 uL of 1X lysis buffer to the 10cm dish of cells.
6. Incubate on ice for 5 minutes.
7. Scrape cells with a cell scraper and transfer lysed solution to a centrifuge tube.
8. Use 21 gauge needles to shear the cells 5-6 times.
9. Spin extract 10-12 minutes at 14,000 x g in the 4°C microcentrifuge.
10. Remove supernatant for use.


.. note::
   * Use prepared lysates as quickly as possible, and store for as short a time as possible. 
   * Store lysates at -80℃ for as long as possible. For lysates that will need to be kept around long term,
     transfer freshly prepared tubes to an available -80℃ freezer to prevent degradation.
   * Lysates have a shorter shelf life when stored at -20℃; long-term storage at this temperature is not recommended.
     CST recommends that lysates are stored at -20℃ for no longer than 3 months.
   * Minimize your freeze/thaw cycles as much as possible. Instead, aliquot into smaller volumes.





Bradford Assay
==============

Introduction
------------

The Bradford Assay is used for protein concentration quantification.
It utilizes Coomassie Brilliant Blue G-250 dye which binds to proteins and shifts the maximum absorption from 470nm to 595nm.
This absorption at 595nm can be measured using the NanoDrop.
The protein concentration can be estimated by creating a standard curve and using Beer's law.

Materials
---------

* Bradford Assay Reagent
* BSA Standard (2 mg/mL)
* Lysis Buffer
* Lysate Samples

.. important::
   Ensure that the Bradford assay kit is compatible with the lysis buffer.
   
   For example, the Bradford assay should be compatible with RIPA lysis buffer but is not compatible with the CST Cell Lysis Buffer due to high amounts of Triton.

   See `Bradford Assay Documentation <https://geneseesci.com/shop-online/product-doc/18-442?doc_id=1>`_ for the full list of compatible reagents.

Protocol
--------

1. Remove Bradford Protein Assay Reagent from the refrigerator and gently mix by inverting the bottle several times.
2. Aliquot the required volume of the dye reagent and allow it to equilibrate to room temperature before use.
3. Prepare diluted BSA protein standards. Be sure to dilute the supplied BSA standard (2000 ug/mL) in the same buffer as the test samples (e.g. 1x lysis buffer).
   Use the tables below as a guide for preparing a set of protein standards.

For a working range of 100 to 1500 ug/mL:

====== ======================== ================================ ===================
Tube # Buffer/Diluent Vol. (uL) BSA Standard (2 mg/mL) Vol. (uL) Final Protein Conc.
====== ======================== ================================ ===================
Blank   80                          0                               0
1       0                           80                              2000 ug/mL
2       20                          60                              1500 ug/mL
3       40                          40                              1000 ug/mL
4       50                          30                              750 ug/mL
5       60                          20                              500 ug/mL
6       70                          10                              250 ug/mL
7       75                          5                               125 ug/mL
8       79                          1                               25 ug/mL
====== ======================== ================================ ===================

For a working range of 1 to 25 ug/mL:

====== ======================== ================================ ===================
Tube # Buffer/Diluent Vol. (uL) BSA Standard (2 mg/mL) Vol. (uL) Final Protein Conc.
====== ======================== ================================ ===================
Blank   800                          0                                 0
1       790                          10                                25 ug/mL
2       792                          8                                 20 ug/mL
3       794                          6                                 15 ug/mL
4       796                          4                                 10 ug/mL
5       798                          2                                 5 ug/mL
6       799                          1                                 2.5 ug/mL
7       799.5                        0.5                               1.25 ug/mL
====== ======================== ================================ ===================

1. Combine each standard and unknown sample with the Bradford Reagent.
   
   * For a working range of 100-1500 ug/mL, pipette 1 uL of each standard or unknown sample into a labeled tube and add 20 uL of the Bradford Protein Assay Reagent and mix well.
   * For a working range of 1-25 ug/mL, pipette 10 uL of each standard or unknown sample into a labeled tube and add 10 uL of the Bradford Protein Assay Reagent and mix well.

2. Incubate at room temperature for 10 minutes.
3. On the NanoDrop, select the Proteins tab and then Bradford Assay.
4. Enter the concentrations of each BSA standard and select the number of replicates.
5. Measure the absorbance of of each BSA standard as directed by the NanoDrop to construct the standard curve.
6. Measure the absorbance of each sample. The NanoDrop will automatically calculate the protein concentration for you based on the standard curve.





Protein Gel Casting
===================

Modified for a Western Blot from `this protocol <https://gallowaylabmit.github.io/protocols/en/latest/protocols/protein_production/bis_tris_protein_gels.html>`_.

Required stock solutions
------------------------

* **40% Acrylamide stock solution**: Solution of monomers for gel polymerization.
  
  We find it cheaper to buy premixed 40% stock solution, with a acrylamide:bis-acrylamide
  ratio of 29:1 (3.3%). Stocks with a 37.5:1 ratio also work, and are typically used
  for resolving larger proteins.

* **3x bis-Tris gel buffer**: Ion buffer used in gel casting.

  =========== =================== ==========================
  Component     Concentration     g/L to final concentration
  =========== =================== ==========================
  bis-Tris      1 M                 209.242
  HCl          Add to pH 6.5-6.8
  =========== =================== ==========================

* **10% APS**: One of the polymerization initiators. Only a small quantity
  needs to be prepared; each gel only requires 25 uL. Make fresh each time by dissolving in water.

  ======================== =================== ===========================================
  Component                 Concentration      g/L to final concentration
  ======================== =================== ===========================================
  Ammonium persulfate       10%                 100 (For example: 10mg/100uL or 100mg/1mL)
  ======================== =================== ===========================================
  
Casting protocol
----------------

.. warning::

    The acrylamide monomers used here are toxic. Read the
    `SDS <https://www.fishersci.com/store/msds?partNumber=BP14081&productDescription=ACRYLAMIDE%3ABISACRYLAMIDE+29%3A1&vendorId=VN00033897&countryCode=US&language=en>`_.

    Perform polymerization steps with a lab coat in a fume hood, and collect rinse waste in
    a waste container.
..

1. Prepare 1X resolving and stacking buffers. These buffers can be stored
   in the refrigerator for several weeks. Recipes given here for enough for 2 0.75mm gels.

   **Resolving buffer:** ~3 mL per gel (6.5 mL total). Final acrylamide concentration depends on desired protein size:

   ============  ==============  ===========================  ===============  =============================
   Protein Size  Gel Percentage  Volume 40% Acrylamide Stock  Volume DI Water  Volume 3x bis-Tris gel buffer
   ============  ==============  ===========================  ===============  =============================
     4-40 kDa     20%               3.25 mL                       1.05 mL        2.2 mL
     12-45 kDa    15%               2.44 mL                       1.86 mL        2.2 mL
     10-70 kDa    12.5%             2.03 mL                       2.27 mL        2.2 mL
     15-100 kDa   10%               1.63 mL                       2.67 mL        2.2 mL
     25-100 kDa   8%                1.30 mL                       3.00 mL        2.2 mL
   ============  ==============  ===========================  ===============  =============================

   **Stacking buffer:**  ~1.2 mL per gel (2.5 mL total):

   =======================    ===========  =============================
   Component                   Volume       Final concentration
   =======================    ===========  =============================
   3x bis-Tris gel buffer       0.83 mL         1x
   40% Acrylamide stock         0.32 mL        5%
   DI water                     1.36 mL
   Bromophenol blue                         50 uL (enough to give color)
   =======================    ===========  =============================


Gel casting setup
-----------------
In-lab, we have the ability to cast two gels simultaneous; this is recommended even if you only
need one, so that you have a backup in case of pouring mishaps. Our gel runner also requires two
poured gels to properly seal.

1. Locate two 0.75mm spacer plates and two short glass plates.
2. Use ethanol and a Kimwipe to clean both glass surfaces.
3. Assemble them in the green alignment device.
4. Lock the two gels into the transparent gel pouring device.

Resolving gel
~~~~~~~~~~~~~

1.  Measure 6.5 mL of **1x resolving buffer** per gel to pour.
2.  Add 50 uL of **10% APS** per gel, mix well.
3.  Add 20 uL **TEMED**, mixing quickly. Pour both gels to the resolving gel height (3 mL per gel).
    Lightly tap and tilt the gel to remove any bubbles.
4.  Once done pouring, quickly but carefully fill the remaining height with isopropyl alcohol, making sure the gel-water
    interface stays undisturbed. This is to ensure the resolving-stacking interface is straight and level.
5.  Wait for the polymerization reaction to finish (noticeable by a change in refractive index).
6.  Drain the water by tilting the gel past 90 degrees, and wicking away with a Kimwipe.

.. tip::
   The resolving gel can polymerize within a just minute or two, especially at higher percentages of acrylamide.
   Therefore, pour the gel quickly using a P1000 pipette.

   It is best to pour the gel from the edges of the gel mold to avoid bubbles.
..

Stacking gel
~~~~~~~~~~~~

1.  Measure 2.5 mL of **1x stacking buffer** to pour.
2.  Add 20 uL of **10% APS**, mix well.
3.  Add 10 uL **TEMED**, mixing quickly. Fill the top of the gels until
    just before overflowing. Insert the comb into the top, letting it rest on the spacers.
4. Wait for the stacking gel to polymerize.
5. Rinse with water to remove unpolymerized acrylamide.
6. If removing the combs prior to storage, slowly remove the comb, ensuring that wells are not broken.

.. tip::
   Insert the comb starting from one end and moving slowly to the other.
   Once the comb is fully inserted, lift the first end and add additional stacking gel to remove bubbles.

   After removing the comb, gently rinse the wells with isopropyl alcohol to remove residual, un-polymerized gel.
..





Loading and Running the Gel
===========================

Modified for a Western Blot from `this <https://gallowaylabmit.github.io/protocols/en/latest/protocols/protein_production/denaturing_protein_gel.html>`_ protocol.

Solutions required
------------------
* **20x MES-SDS running buffer stock solution**: Suitable for separating proteins with a molecular weight less than 75 kDa.
  
  It is also generally cheaper to order this as a pre-mixed 20x stock solution. If you need to make it yourself, the recipe is:

  =========   ===================  ==========================
  Component   Final concentration  g/L to final concentration
  =========   ===================  ==========================
  MES           1 M                  195.2 g
  Tris          1 M                  121.13 g
  EDTA          20 mM                5.845 g
  SDS           2%                   N/A
  =========   ===================  ==========================

* **200x running buffer reductant**: Ensures that the gel remains under reducing conditions when run. Add directly to
  1x running buffer before filling the gel tank. Dissolve sodium bisulfite in DI water.

  =================   ===================  ==========================
  Component           Final concentration  g/L to final concentration
  =================   ===================  ==========================
  Sodium bisulfite      1 M                 104.061 g
  =================   ===================  ==========================


* **200 mM Tris-HCl stock**: Dissolve components in DI water.

  =========== =================== ==========================
  Component     Concentration     g/L to final concentration
  =========== =================== ==========================
  Tris-HCl      200 mM                 31.52 g
  NaOH          Add to pH 6.8
  =========== =================== ==========================

* **20% SDS stock**: At low temperatures, the SDS may fall out of solution. Therefore, warm in a water bath to dissolve. Mix well before transferring.

  ======================= =================== ================================
  Component                Concentration      To make final concentration
  ======================= =================== ================================
  Sodium dodecyl sulphate          20%          2g / 10 mL DI water
  ======================= =================== ================================

* **0.1% bromophenol blue**: 1 mg / mL
* **2x Loading Buffer (Laemmli Buffer)**: Used to denature and solubilize protein samples. Can be stored.
  
  ===========================  ======================  ================
  Component                     Final concentration     Volume
  ===========================  ======================  ================
  200 mM Tris-HCl stock         100 mM                  5 mL
  Glycerol                      20%                     2 mL
  20% SDS stock                 4%                      2 mL
  0.1% bromophenol blue stock   0.01%                   1 mL
  2-mercaptoethanol             10%                     1.1 mL
  ===========================  ======================  ================

.. warning::

    2-mercaptoethanol smells awful; always add it inside a fume hood.

Running procedure
-----------------
1. Add **2x Laemmli Buffer** to an equal volume of lysate in PCR tubes.
   This is recommended unless the online antibody datasheet indicates that non-reducing and non-denaturing conditions should be used.
2. Use a PCR machine to reduce and denature the lysate samples at 95℃ for 5 minutes.
3. Dilute enough **20x MES-SDS running buffer** to fill the gel tank,
   adding fresh **200x running buffer reductant** if a gel has not been recently run.
4. Place a prepared bis-Tris protein gel in the gel-runner. Fill both chambers with the prepared 1% MES-SDS running buffer.
   Fill the inner chamber to the top of the stacking gel, and the outside chamber to the top of the resolving gel.
   You will need about 1 liter of the 1% MES-SDS running buffer.
5. Carefully load equal amounts of protein samples, including a protein standard, into the wells of the gel. Each well can be loaded with a maximum of 25 uL.
   20-30 ug of total protein from cell lysate is generally used unless further optimization is needed for the desired protein(s).
6. Run the gels at constant current, about 30 mA (~43V) per mini-gel for approximately 125 minutes. The dye band runs around 3-5 kDa, so
   it is typically ok to run the dye band to the bottom of the gel unless very small proteins are
   of interest.




Coomassie Staining
==================

Solutions required
------------------

* **Coomassie staining dye**:
  When preparing this dye, pour the 10% methanol first, using it to dissolve the R-250.
  Then, add water. Add the glacial acetic acid last to prevent aggregation.

  ================  ===================  ==================
  Component         Final concentration  Amount per 1 liter   
  ================  ===================  ==================
  Coomassie R-250    0.2% (2g/L)          2g
  Methanol           10%                  100 mL
  Water              80%                  800 mL
  Acetic acid        10%                  100 mL
  ================  ===================  ==================

* **10% Acetic Acid**: Used as a destain solution.
  
  .. Warning:: Do not microwave pure acetic acid.


Procedure
---------

1. Pour water into a plastic tray (tip box lid), about half a centimeter deep.
2. Very carefully separate the gel plates without breaking the gel. The gel will stick to one side or the other. 
3. Invert the plate/gel over the water and "convince" the gel to fall into the dish. It can help to put the gel and plate into the water and let the solution help the gel release.
   Using a green gel scraper can also help with this process.
4. Place the gel on a rocker for 2-5 minutes to remove excess free proteins.
5. Drain the water without dropping your gel in the sink, and cover with ~0.5 cm of Coomassie staining dye.
6. Place the gel in stain in the microwave and microwave on high until the solution just begins to boil (this step greatly accelerates the procedure and allows you to see you bands in a minute or so).
   This only takes 20-30 seconds in the microwave.
7. Remove from the microwave and place on a rocker for a few minutes. Once you see the gel filled with Coomassie, it's done.
8. Drain the Coomassie and cover the gel with water, rock for about 5 minutes, drain.
9. Cover with **10%** acetic acid, place a couple folded Kim-wipes over the gel, and microwave again until the solution begins to boil (20-30 seconds).
10. Remove from microwave and rock to remove Coomassie not bound to protein.
    If there is excess stain, replace the 10% acetic acid and Kim-wipes and continue to rock until the gel is clear with dark purple protein bands.



Transferring the protein from the gel to the membrane
=====================================================

.. note:: To Do

Antibody Staining
=================

.. note:: To Do
