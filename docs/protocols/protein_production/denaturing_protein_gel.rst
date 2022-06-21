=======================================
Denaturing protein gel run and staining
=======================================

Solutions required
-------------------
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
  1x running buffer before filling the gel tank.

  =================   ===================  ==========================
  Component           Final concentration  g/L to final concentration
  =================   ===================  ==========================
  Sodium bisulfite      1 M                 104.061 g
  =================   ===================  ==========================


* **200 mM Tris-HCl stock**:

  =========== =================== ==========================
  Component     Concentration     g/L to final concentration
  =========== =================== ==========================
  Tris-HCl      200 mM                 31.52 g
  NaOH          Add to pH 6.8
  =========== =================== ==========================

* **10% SDS stock**: At low temperatures, the SDS may fall out of solution, but will redissolve
  when mixed with the other ingredients. Mix well before transferring.
* **0.1% bromophenol blue**

  ================  ====================================
  Component         amount/50 mL to final concentration
  ================  ====================================
  bromophenol blue  50 mg
  DI water          50 mL
  ================  ====================================

.. note::

  The bromophenol blue solution will not be blue. It is more brown
  at this concentration. It will be blue when you add it into
  other things.

* **2x sample buffer**: Used to denature and solubilize protein samples. Can be stored

  ===========================  ======================  ================
  Component                     Final concentration     Volume / 10 mL
  ===========================  ======================  ================
  200 mM Tris-HCl stock         100 mM                  5 mL
  Glycerol                      20%                     2 mL
  10% SDS stock                 2%                      2 mL
  0.1% bromophenol blue stock   0.01%                   1 mL
  ===========================  ======================  ================
* **Coomassie staining dye**:
  When preparing this dye, pour the 10% methanol first, using it to dissolve the R-250.
  Then, add water. Add the glacial acetic acid last to prevent aggregation.

  ================  ===================
  Component         Final concentration
  ================  ===================
  Coomassie R-250    0.2% (2g/L)
  Methanol           10%
  Acetic acid        10%
  Water              80%
  ================  ===================

* **Coomassie destain solution**

  ================  ===================
  Component         Final concentration
  ================  ===================
  Acetic acid        10%
  Water              90%
  ================  ===================


Running procedure
-----------------
1. Dilute enough **20x MES-SDS running buffer** to fill the gel tank,
   adding fresh **200x running buffer reductant** if a gel has not been recently run.
2. Add **2x sample buffer** to the protein sample of interest. Add 2-mercaptoethanol to a
   final concentration of 1%.

.. warning::

    2-mercaptoethanol smells awful; always add it inside a fume hood.

3. Briefly heat the protein sample to above 80C for one minute, to ensure full protein
   denaturation.
4. Place a :doc:`prepared bis-Tris protein gel <bis_tris_protein_gels>` in the gel-runner,
   and fill both chambers with the prepared 1% MES-SDS running buffer.
5. Carefully load samples, including a protein standard.
6. Run the gels at constant current, about 30 mA per mini-gel. The dye band runs around 3-5 kDa, so
   it is typically ok to run the dye band to the bottom of the gel unless very small proteins are
   of interest.


Staining (Coomassie)
--------------------

1. Fill a small dish (the top of a pipette tip box works great!) with DI water.
2. Carefully separate the gel plates from each other, without ripping the delicate gel.
   Invert the gel over the dish of water, and gently move the gel into the dish.
3. Place the gel dish on a rocker for 5 minutes to remove any unbound proteins.
4. Drain the water, and replace it with a roughly half-inch layer of Coomassie stain.
5. Either gently shake, while covered, for several hours, or microwave until the solution
   just reaches boiling (for accelerated diffusion). If microwaving, cover with Kimwipes
   to prevent spattering!
6. Drain the Coomassie stain off, replace with DI water, and rock for 5 minutes.
7. Drain the DI water, and replace with destaining solution.
8. Cover the gel with Kimwipes, and either shake, while covered, for several hours or microwave as before.
9. When the destain solution seems substantially blue or purple, replace it with fresh destain solution.
