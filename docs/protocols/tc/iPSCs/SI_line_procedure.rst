=================================
STRAIGHT-IN Line Procedure
=================================

This protocol describes the step-by-step integration of Donor plasmids using the STRAIGHT-IN (Dual) platform to generate genetically modified hiPSC lines. The procedure begins with a STRAIGHT-IN hiPSC acceptor line, derived from either LU99 (from Leiden) or iPS11 backgrounds.
We currently possess two types of acceptor lines:

* **Single landing pad lines:** iPS11 background only
* **Dual landing pad lines:** iPS11 at CLYBL and LU99 at either CLYBL or AAVS1

Two landing pad systems are used:

* **Bxb1-GT landing pad**
  
  * Confers zeocin (bleomycin) resistance upon integration
  * Carries CAG-BFP (bright blue signal in iPS11 Single GT line or iPS11 Dual line) or PGK-BFP (silenced in both LU99 lines)
  * Auxiliary sequences (BFP, BleoR, plasmid backbone) are excised using Cre recombinase
  
* **Bxb1-GA landing pad**
  
  * Confers puromycin resistance upon integration
  * Carries CAG-GFP (bright green signal in iPS11 Single GA line) or CAG-mScarlet (bright red signal in iPS11 Dual line) or PGK-mScarlet (silenced in both LU99 lines)
  * Auxiliary sequences (GFP/mScarlet, PuroR, plasmid backbone) are excised using Flp recombinase


**Key Reagents (TC Supplies)**

* 24-well plates
* `rhLaminin-521 <https://www.thermofisher.com/order/catalog/product/A29248>`_: aliquots are in Grand Paddie (-20°C) and stocks in Sven (-20°C).
* `PBS +/+ <https://www.thermofisher.com/order/catalog/product/14040141>`_: we keep the stock in cell culture fridge and in Oaken (4°C). 
* PBS -/-
* `Gentle Cell Dissociation Reagent <https://www.stemcell.com/products/gentle-cell-dissociation-reagent.html>`_
* `Penicillin/Streptomycin <https://www.thermofisher.com/order/catalog/product/15140122>`_: aliquots and stocks are in Olaf (-20°C).
* `StemFlex medium <https://www.thermofisher.com/order/catalog/product/A3349401>`_: aliquots and stocks in Sven (-20°C). It is aliquoted without Penicillin/Streptomycin but once the aliquot of the medium has been thawed, add Penicillin/Streptomycin (1:100). Do not thaw StemFlex medium at 37°C, do it at room temperature or preferably at 4°C overnight.
* Neutralization medium: `DMEM/F12 <https://www.thermofisher.com/order/catalog/product/21331020>`_  + `1% FBS <https://www.geneseesci.com/product/genclone-fetal-bovine-serum/?srsltid=AfmBOor2lSkkxAJVdk6msyt0Qf2OimomtjZPynUMimF1uXJhaVFGI_mn>`_
* `RevitaCell Supplement <https://www.thermofisher.com/order/catalog/product/A2644501>`_: used at 1:200. Aliquots are in Grand Paddie (-20°C) and stocks in Sven (-20°C).
* `OptiMEM <https://www.thermofisher.com/order/catalog/product/11058021>`_: aliquots and stocks are in Oaken (4°C). 
* `Lipofectamine Stem Transfection Reagent <https://www.thermofisher.com/order/catalog/product/STEM00008>`_: stocks are in Oaken (4°C).
* `Zeocin™ selection reagent <https://www.thermofisher.com/order/catalog/product/R25001>`_: aliquots are in Grand Paddie (-20°C). Stock is at 100 mg/mL and the working solution is 15 µg/mL (1:6666).
* `Puromycin <https://www.invivogen.com/puromycin>`_: aliquots are in Grand Paddie (-20°C). Stock is at 1 mg/mL and the working solution is 1 μg/mL (1:1000).
* `DNeasy Blood and Tissue kit <https://www.qiagen.com/us/products/discovery-and-translational-research/dna-rna-purification/dna-purification/genomic-dna/dneasy-blood-and-tissue-kit>`_
* STRAIGHT-IN acceptor lines: LU99 CLYBL Dual, LU99 AAVS1 Dual, iPS11 CLYBL Single GT, iPS11 CLYBL Single GA and iPS11 CLYBL Dual


**Key Reagents (Plasmids and modRNA)**

* eeBxb1 plasmid (pKG3466) or eeBxb1 modRNA (pKG3471). Miniprep fresh plasmid or preferably use modRNA. Frozen aliquots of the modRNA should be stored at -80°C (Elsa) in the box with the rest of the recombinases.
* p53DD modRNA (pKG3199). Frozen aliquots of the modRNA should be stored at -80°C (Elsa) in the box with the recombinases.
* Flp-T2A-BleoR modRNA (pKG3212). Frozen aliquots of the modRNA should be stored at -80°C (Elsa) in the box with the recombinases.
* `TAT-Cre protein <https://www.sigmaaldrich.com/US/en/product/mm/scr508?srsltid=AfmBOorSWM6-h4vYbK-_i-tZ0wl-9yYkrzKFuSHoKG7e7a7mbvmy0fzr>`_: aliquots can be found at -80°C (Elsa) in the box with the recombinases.
* Cre modRNA (pKG1779, pKG3213, pKG3214 or pKG3717). Frozen aliquots of the modRNA should be stored at -80°C (Elsa) in the box with the recombinases.
* Donor plasmids containing attB-GT or attB-GA and the desired DNA cargo

**General Preparation**

Before starting any step, pre-warm all culture media for 15 to 30 minutes at room temperature.

Pre-warm:

* StemFlex (with or without antibiotics)
* Neutralization medium
* OptiMEM

STRAIGHT-IN Integration Protocol
=================================

**Two Days Before Transfection (d -2)**
----------------------------------------

1.	Dilute rhLaminin-521 at 1:20 in PBS +/+.
2.	Add 300 µl per well to a 24-well plate (15 µl rhLaminin-521 + 285 µl PBS +/+).
3.	Seal with Parafilm and incubate overnight at 4 C.
  * Alternatively, coat on the day of splitting and incubate for 2 hours at 37°C.

**Day Before Transfection (d -1)**
------------------------------------

1.	Warm the coated plate at 37 C for 10 minutes.
2.	Select a hiPSC well that is approximately 80% confluent.
3.	Aspirate StemFlex.
4.	Rinse once with 1 mL PBS -/-.
5.	Rinse again with 1 mL PBS -/-.
6.	Add 300 to 500 µl of Gentle Cell Dissociation Reagent.
7.	Incubate 5 minutes at 37°C with 5% CO2.
8.	Aspirate the dissociation reagent and add 1 mL StemFlex + RevitaCell (1:200).
9.	Gently triturate 5 to 10 times to obtain a single cell suspension and transfer to a tube containing 1.5 to 2 mL neutralization medium.
10. Centrifuge at 300g for 3 minutes.
11. Aspirate supernatant and resuspend in 0.5 mL StemFlex.
12. Count cells and seed 100K cells per well (24-well scale) on rhLaminin-521 coated wells.
    * This number works well for our lines, but can be optimized between 150K-300K.
13.	Plate cells and distribute evenly by gentle rocking. Incubate at 37°C and 5% CO2.

**Day of Transfection (d0)**
----------------------------

1.	Confirm cells are approximately 30 to 40% confluent.
  * If too confluent, re-seed.
  * If too sparse, feed and wait until they reach the appropriate density.
2.	Prepare transfection mixes. Per well:
  * 600 ng Donor plasmid
  * 400 ng eeBxb1 modRNA
  * 400 ng p53DD modRNA
  * 3 µl Lipofectamine Stem reagent
  * Prepare Lipofectamine master mix based on n + 0.5 wells.
  * Add DNA mix to Lipofectamine mix (not the reverse).
3.	Incubate 50 µl Lipofectamine:DNA mix for 10 minutes at room temperature.
4.	Aspirate StemFlex, rinse once with PBS -/- and add 0.5 mL OptiMEM.
5.	Add 50 µl transfection mix dropwise and gently shake.
6.	After 4 hours, add 0.5 mL StemFlex without removing OptiMEM.

**Lipofectamine Stem Transfection Overview (24-well format)**

+------+--------+------------------------------+----------------------------------------------+
| Step | Tube   | Components                   | Amount per Well                              |
+======+========+==============================+==============================================+
| 1    | Tube 1 | OptiMEM\                     | 22 µL\                                       |
|      |        | Lipofectamine Stem Reagent   | 3 µL                                         |
+------+--------+------------------------------+----------------------------------------------+
| 2    | Tube 2 | OptiMEM\                     | 25 µL - DNA volume\                          |
|      |        | DNA                          | 600 ng donor + 400 ng Bxb1 + 400 ng p53DD    |
+------+--------+------------------------------+----------------------------------------------+
| 3    | Add Tube 2 into Tube 1 and mix well                                                  |
+------+--------+-----------------------------------------------------------------------------+
| 4    | Incubate 10 minutes at room temperature                                              |
+------+--------+-----------------------------------------------------------------------------+
| 5    | Rinse cells with PBS -/- and add 0.5 mL OptiMEM                                       |
+------+--------+-----------------------------------------------------------------------------+
| 6    | Add 50 µL complex to each well and swirl to distribute                               |
+------+--------+-----------------------------------------------------------------------------+
| 7    | Incubate 4 hours at 37°C with 5% CO₂                                                 |
+------+--------+-----------------------------------------------------------------------------+
| 8    | Add 0.5 mL warm StemFlex per well and incubate overnight                             |
+------+--------+-----------------------------------------------------------------------------+


**One Day After Transfection (d1)**
------------------------------------

1.	Aspirate media, rinse once with PBS -/-, add 0.5 mL StemFlex.
2.	Expect some cell death due to plasmid toxicity.
3.	Assess fluorescence if applicable.

**Two Days After Transfection (d2)**
---------------------------------------

1.	Begin antibiotic selection if cells are healthy and above 50% confluent.
  * Zeocin 1:6666 for Bxb1 GT
  * Puromycin 1:1000 for Bxb1 GA
2.	Prepare at least 1.5 mL antibiotic medium for multiple refreshments. Keep at 4°C for up to one week.

**Three to Four Days After Transfection (d3 to d4)**
------------------------------------------------------

1.	Rinse once with PBS -/- and add 0.5 mL antibiotic medium.

.. note::
    A lot of cell death during selection is expected.


**Five Days After Transfection (d5)**
-------------------------------------

1.	Look for clear colonies. If present, stop antibiotic selection.

.. note::
  * Three days of selection are usually sufficient.
  * Include a negative control lacking eeBxb1 and p53DD to confirm full lethality.

2.	Replace with 0.5 mL StemFlex without antibiotic.

**Six to Eight Days After Transfection (d6 to d8)**
------------------------------------------------------

1.	Refresh medium every other day.
2.	Proceed to the STRAIGHT-IN Excision Protocol.

STRAIGHT-IN Excision Protocol
=================================

The excision strategy depends on the landing pad:

* **GA landing pad:** excised using Flp recombinase
* **GT landing pad:** excised using Cre recombinase
 
Each system has two workflow options: A (no replating) and B (replate cells).

Flp-Mediated Excision (GA Landing Pad)
---------------------------------------

**Option A: Direct Transfection (d6 to d8)**

1.	Once colonies are large and healthy, transfect with Flp-T2A-BleoR modRNA.
2.	Per well, use:
  * 500 ng Flp-T2A-BleoR modRNA
  * 2 µl Lipofectamine Stem
3.	Prepare Lipofectamine master mix based on n + 0.5 wells. Add RNA mix to Lipofectamine.
4.	Incubate 10 minutes at room temperature.
5.	Aspirate medium, rinse with PBS -/-, add 0.5 mL OptiMEM.
6.	Add 50 µl Lipofectamine:RNA mix.
7.	After 4 hours, add 0.5 mL StemFlex without removing OptiMEM.
8.	After another ~2-4 hours, add 0.5 mL StemFlex containing Zeocin (1:6666).
  * Selection may also begin the next day if needed.

**Option B: Replate and Transfect (d6 to d8)**

1.	Replate cells into two rhLaminin-521 coated wells, splitting evenly.
2.	When wells reach 30 to 40 % confluency, proceed.
3.	Transfect only one well with Flp-T2A-BleoR modRNA. Keep the other as a contingency.
4.	Follow steps from Option A, starting at step 2.

Cre-Mediated Excision (GT Landing Pad)
---------------------------------------

**Option A: Replate and Use TAT-Cre Protein (d6 to d8)**

1.	Replate cells into two rhLaminin-521 coated wells.
2.	When cells reach 30 to 50% confluency, proceed.
3.	Prepare a 0.5 mL StemFlex mixture containing 2.25 µl TAT-Cre (1 µM final).
  * Mix the components in a separate protein low-bind/retention tube before adding to cells.
4.	Add the mix to one well. Keep the second well as a backup.
5.	The next day, rinse with PBS -/- and replace with 0.5 mL StemFlex.
6.	Allow cells to grow until confluent, typically 2 days. Refresh every other day.
7.	Passage cells and collect samples for gDNA extraction and CNV ddPCR assays for BleoR and EBFP2/EGFP.
  * Typical excision efficiency is 50 to 60%.
  * Additional rounds of TAT-Cre may further increase excision rates.

**Option B: Replate and Use Cre modRNA (d6 to d8)**

1.	Replate cells into two rhLaminin-521 coated wells, splitting evenly.
2.	When wells reach 30 to 40% confluency, proceed.
3.	Transfect only one well with Cre modRNA. Keep the other as a contingency.
4.	Follow steps from Option A, starting at step 2.
5.	The next day, rinse with PBS -/- and replace with 0.5 mL StemFlex.
6.	Allow cells to grow until confluent, typically 2-3 days. Refresh every other day.
7.	Passage cells and collect samples for gDNA extraction and CNV ddPCR assays for BleoR and EBFP2/EGFP.
  * Typical excision efficiency is 30%.
  * Additional rounds of Cre modRNA transfection may further increase excision rates.
