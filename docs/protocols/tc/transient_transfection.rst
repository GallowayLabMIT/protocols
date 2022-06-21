=======================================
Transient HEK293T Transfection
=======================================
.. note:: 
	If performing transient transfection for virus production: please use the updated :doc:`virus_production` protocol going forward for lentivirus product via HEK293Ts; the efficiency of the new protocol
	exceeds this protocol's efficiency by more than an order of magnitude! Plat-E retrovirus production
	should still use :doc:`/protocols/tc/platE_transfection`.

	If performing transient transfection for an experiment, continue to the protocol below.

Protocol
--------

For all calculations you can refer to the most updated transfection template in shared projects folder of the Galloway Lab sharepoint, example `here <../../_static/files/2021.08.31_TransfectionTemplate.xlsx>`_.

1.	Seed confluent 293T cells approximately 1-2 days prior to transfection.  Cells must be ~80-90% confluent for highest transfection effiency. If plating 1 day before, recommended cell counts are:

=============== ================= ===============
**Cell Type**    **Well Size**     **# Cells/Well**
=============== ================= ===============
HEK293Ts        96-well             25K-35K
HEK293Ts        10-cm               7500K
Plat-Es         6-well                800K
=============== ================= ===============

2.	Make a mastermix of PEI and Knockout DMEM as follows:

  		- Parameters needed (To scale to DNA/well in other size plates, divide by number of wells: 10cm-plate = 6-well plate = 24-well plate = 96-well plate): 
  	
			================================ ===============
			**Parameter**    					**Value**
			================================ ===============
			    **Titrated PEI ratio**			Specific for each PEI batch, ex. 5 ug PEI : 1 ug DNA. The PEI concentration itself is 1mg/mL.
				**DNA/well/plasmid**			10.8 ug / 10-cm plate
				**Knockout DMEM/well**			1.33 mL / 10-cm plate
				**DNA concentration**			ng/uL (for each plasmid from nanodrop)
			================================ ===============
  			
  		- Calculations
  
  			========================================= ===============
			**Parameter**    					    		**Example for 96-well plate**
			========================================= ===============
			  **110% PEI/well**						    	1.125ugDNA/well * 5ug PEI/1ugDNA * 1.1 = 0.62 ugPEI/well
			  **110% Total volume DNA/well/plasmid**			112.5 DNA(ng)/well/plasmid / 213 DNA concentration (ng/uL) * 1.1 = 0.56 uL DNA/well/plasmid
			  **110% KO DMEM/well/plasmid**					13.9 uL KO DMEM/well * 1.1 = 15.2 uL
			========================================= ===============

			- Depending on number of wells and plasmids/well, find how much KO DMEM and PEI total you will need for the experiment. Then, make the master mix.

.. important::
	*Ensure* that you add PEI to KO DMEM, *not the other way around!*
	Mix master mix well, then let sit for minimum 10 minutes. 

3.	Add DNA to the PEI+KO DMEM MM as calculated per each  conditions, then mix and wait 15 minutes. These are the "condition mixes."

	a. For *one 10cm retrovirus plate*, use 6.67ug viral plasmid + 6ug pIK-MLVgp + 0.667ug pHDMG.
	b. For *one 10cm lentivirus plate*, use 6.67ug viral plasmid + 6ug pPAX2 + 0.667ug VSVG.
	c. For one condition of a 96-well transfection (use 110% volumes from calculations): 
	
			========================================= ===============
			**Parameter**    					    	**Example**
			========================================= ===============
			  **110% Total volume DNA/well/plasmid**	112.5 DNA(ng)/well/plasmid / 213 DNA concentration (ng/uL) * 1.1 = 0.56 uL
			  **Number plasmids / well**					2 plasmids
			  **Wells**										3 wells
			  **Condition Mix**							(0.56 uL DNA/well/plasmid + 15.2 KO DMEM/well/plasmid) * (2 plasmids * 3 wells)  
			========================================= ===============

.. tip::
	It's more efficient to make a master mix of the structural and packaging vectors (e.g. PAX2/VSVG or IK-MLV/HDMG) and aliquot that out.


4.	Add amount of DNA+KO DMEM+PEI condition mix to desired well on **TOP** of growth media (DMEM + 10% FBS, see :doc:`media amounts </protocols/tc/adherent_cell_culture>`). (use the 100% NOT the 110% volumes.) For larger well (anything above 24-well), add the condition mix *dropwise* and evenly around the plate, rocking the plate back and forth, side to side to mix.
5.	*After 18-24 hours*, change with :doc:`fresh media </protocols/tc/adherent_cell_culture>` (i.e. DMEM + 10% FBS for HEK293Ts).

If making virus continue to further steps: 

		6.	Harvest media after another 24 hours and replace with another 6.5mls fresh media. Store media from each virus/vector in 50ml conical at 4°C (combine media from both plates into same tube!).
		7.	Harvest again after another 24 hours.  May add the media from the two plates into the 50ml conical already being stored at 4C.  After this second harvest, UV plates for about 30 minutes, then discard into biohazard.
		8.	Keep virus in 4°C until :doc:`ready to concentrate <virus_concentration>`!

		.. note::
			Retroviruses are stable at 4°C for 2-3 days, with lentiviruses being stable for 4-5 days.
