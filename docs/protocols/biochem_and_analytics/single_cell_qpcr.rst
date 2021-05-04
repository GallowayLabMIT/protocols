=================
Single cell qPCR
=================

Single-cell acquisition
-----------------------
.. time:: 3-5 minutes per cell.

.. important:: All work should be performed with RNase free reagents!


1.	Cells should be plated on the lids of electrophysiology dishes to prevent interferences of dish sides with micromanipulator angle of approach. 
2.	Label PCR tube strips with numbers to correspond to the number of the cell picked.
3.	Add 5 ul of Cells Direct 2X rxn (Cells Direct One-step qRT-PCR kit , Life, Cat# 11753-100) mix to each PCR tube. 
4.	Pull glass micropipettes with the machine in the Chow lab. Pipettes pulled with 1st T=61.2 °C and 2nd T=47 °C is most optimal. 

.. admonition:: TODO

	Speicfy glass micropipette diameter and describe machine used in this step.

5.	Obtain dry ice in a cooler box for immediate freezing of cell following acquisition. 
6.  Setup fluorescence on an inverted microscope, imaging at 40X.
7.	Identify isolated GFP+ cells with neuronal morphology using bright field and FITC. 
8.	Use RNAse inhibitor (~3 ul per 30 cells picked) to be placed in each glass micropipette prior to use in single-cell picking.
9.	Place pipette in micromanipulator. Position so that the tip comes into the field of view. Careful not to break the tip by lowering the Z position too far. 
10.	Carefully move the tip to the edge of the cell and aspirate, scooping the cell off the dish and retrieving as much of the cell body and dendrites as possible. 
11.	Crush pipette tip into 5 ul of 2X Rxn mix to capture cell in solution. 
12.	Immediately place on dry ice to freeze. Keep on dry ice until ready to store in -80 °C freezer. 

.. note::
	Cells dissociate from plate more easily with greater amount of time out of incubator. Average time to acquire a single cell runs from 3-5 minutes. 
	


Lysis, reverse transcription (RT), and specific target amplification (STA)
--------------------------------------------------------------------------
1.	Prepare primer mix

	a.	Each primer stock should be 200 uM. (e.g. If primer is 40.4 nM, add 202 uL of RNAse free water (DEPC treated or other).  
	b.	For bookkeeping it is helpful to label each primer with a letter and keep in order (e.g  A- Z then AA- AZ ). 
	c.	Make 20uM stock of forward and reverse primer together (e. g  “A  F+R” for gene A. ) For 250 ul F+R mix, add 25 ul F and 25 ul R and 200 ul of RNAse free water	. 
	d.	For 200 nM (each primer at 200 nM) RT and STA primer mix of 1 mL, add 10 ul of each 20 uM F+R mix and bring to 1000 uL. For 48 genes (480 ul of primer), add 520 ul RNAse free water. 

.. time:: 1 hour for steps 2 through 7

2.	Remove cells from -80°C and immediately place on ice.
3.	Move quickly to 50 oC water bath for 15 sec defrost, then place back on ice. 
4.	Make RT/STA mix:

=============================   ==============  =================
Component                        Volume/ 1rxn    Volume / 100 rxn
=============================   ==============  =================
Superscript III/Platinum Taq     0.2 uL         20 uL
200 uM Primer Mix                2.5 uL         250 uL
RNAse-free water                 1.3 uL         130 uL
*Total*                          *4 uL*         *400 uL*
=============================   ==============  =================

5.	Add 4 ul of RT/STA mix per tube. 
6.	Spin down samples in minifuge to collect all liquid. 
7.	Place in thermocycler.

8.	Run thermocycler program (1 hr and 55 min)

==== =======  ==================    =========================
 #    Time     Temperature (°C)      Name
==== =======  ==================    =========================
 1   15 min    50                    Reverse transcription
 2    2 min    95                    Initial denature
 3     -      Cycle 4&5 18 times     Cycle
 4   15 sec    95                    Denature
 5    4 min    60                    Annealing and elongation
 6    Hold     4                     Chill, end
==== =======  ==================    =========================

9.	Spin down samples in minifuge to collect all liquid. Steps i- n = 1 hr and 40 min)
10.	Make Exonuclease I and SAP (Shrimp Alkaline Phosphotase) mix:

=============================   ==============  =================
Component                        Volume/ 1rxn    Volume / 100 rxn
=============================   ==============  =================
 Exonuclease I                    0.5 uL         50 uL
 SAP                              1.0 uL         100 uL
 RNAse-free water                 2.5 uL         250 uL
 *Total*                          *4 uL*         *400 uL*
=============================   ==============  =================
	
11.	Add 4 ul of Exonuclease I SAP mix per tube. 
12.	Place in thermocycler, running the following program:

==== =======  ==================    =========================
 #    Time     Temperature (°C)      Name
==== =======  ==================    =========================
 1   20 min    37                    Digest primers, dNTPs
 2   15 min    80                    Denature
 3    Hold     4                     Chill, end
==== =======  ==================    =========================

13.	Store @ -20 oC. 

Single-cell qPCR on Fluidigm Biomark
------------------------------------
.. time:: 2 hours for steps 1 through 8

1.	Defrost samples on ice.
2.	Dilute 5x by adding 52 ul of H20 to 13 ul of sample to make 65 ul of single-cell amplified cDNA (13 ul is standard volume size following above procedure). 
3.	Make Sso Fast Evagreen super mix (Bio-rad) with 20X DNA binding dye (Fluidigm, green cap):

====================================   ==============  =================
Component                               Volume/ 1rxn    Volume / 96 rxn
====================================   ==============  =================
Sso Fast Evagreen super mix, low ROX     2.5 uL         480 uL
20X DNA binding dye loading reagant      0.25 uL        48 uL
RNAse-free water                         2.75 uL        264 uL
*Total*                                 *5.5 uL*        *528 uL*
====================================   ==============  =================

.. admonition:: TODO

	Check if the above mixture is diluted with water as written here

i.	….2.5 uL/ rxn….96 rxn+ over= 480 uL
ii.	20X DNA binding dye sample loading reagent…0.25 uL/rxn...96 rxn+ over= 48 uL 
iii.	Total…………………………………….……5.5uL/rxn………….96 rxn+ over =528 uL

4.	Mix samples in 96-well qPCR plate.  Place samples in well corresponding to number to order correctly (e.g.  Sample 1= A1, Sample 2= A2… Sample 13= B1, Sample 14= B2…Sample25= C1 etc). 

i.	Sso Fast/DNA binding Dye mix………….……5.5uL/well
ii.	Single-cell STA cDNA samples………………….4.5 ul/well

5.	Cover with qPCR sticky lid.  Vortex lightly to mix. Spin down in plate spinner and place on ice.
6.	Prepare assays with 2X loading reagent (Fluidigm), F+R primers, and water. Place samples in well corresponding to number to order correctly (e.g.  Assay 1 (Gene A)= A1, Assay 2 (Gene B)= A2… etc). 
7.	?

i.	2X Assay Loading reagent ………….2.5 uL/ rxn……….4 rxn= 10 uL
ii.	20 uM F+R  for each assay.……………0.25 uL/rxn…………4 rxn= 5 uL
iii.	RNAse-free water…..2.25 uL/rxn………….4 rxn=5 uL 

8.	Cover assay lids with qPCR sticky lid.  Vortex lightly to mix. Spin down in plate spinner and place on ice.
9.	PRIME Chip: Add fluid to accumulators by depressing springs and O-rings and injecting control line fluid. Tilting the plate will ensure the fluid goes into the accumulators. Run “Prime” script on Fluidigm Mixer (HX for 96.96 and MX for 48.48.) 

 
Consult Chip Pipetting Map (PN 68000130, REV B) to optimize efficiency of set-up for pipetting with multi-channel pipette.  More detail on Page 5 and 6. 
 (ref: http://openwetware.org/images/5/52/Fluidigm_96.96_RT-_PCR_Quick_Reference_.pdf)

10.	Use electronic multi-channel pipette to add 5 uL to each well. 
11.	Note:  Special thin tips are to be used on this device compatible with loading 384-well plates. Using the 96-well plate spacing for tips more compatible with 96 well plates assays and sample preparation and requires using the Chip pipetting map to quickly and correctly load the assays and sample inlets.  It is recommended to aspirate 5.2 uL and dispense 5 uL to avoid introducing air bubbles. By preparing extra assay and sample mix in the 96 well plate, air bubbles should be avoided using this pipetting method. 

12.	Following addition of all samples and assays, follow the detailed protocol for loading the Chip on the IFC mixer and then running the Chip on the Biomark HD.  (See below).  Note:  The Camera requires time to turn on (~20 min) make sure to turn on early.  Also, loading the Chip takes ~ 1 hr 20 min and running the chip takes ~1 hr and 30 min. 

IV.	Pipetting Map for 48.48 









V.	Pipetting Map for 96.96
 
