=======================================
Transient HEK293T Transfection
=======================================

.. note::
	If performing transient transfection for virus production: please use the updated :doc:`/protocols/tc/virus/virus_production` protocol for lentivirus production via HEK293Ts, and the :doc:`/protocols/tc/virus/platE_prod` protocol for Plat-E retrovirus production.

	If performing transient transfection for an experiment, continue to the protocol below.

.. _transfection-calcs:

Calculations
------------

For all calculations you can refer to the most updated transfection template in the `shared projects folder <https://mitprod.sharepoint.com/sites/GallowayLab/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2FGallowayLab%2FShared%20Documents%2Fprojects%2Fshared&viewid=a7b740fe%2D9cf6%2D4f23%2D823f%2D41f507975686>`_ of the Galloway Lab sharepoint, example `here <../../_static/files/2021.08.31_TransfectionTemplate.xlsx>`_.

To scale per well amounts according to plate size, divide by number of wells with the total amount per entire plate constant (e.g., 1 10cm-dish = entire 6-well plate = entire 96-well plate).
For instance, each well in a 6-well plate would use :math:`\frac{1}{6}` the per-plate DNA and knockout DMEM amounts.

For conditions with multiple wells, make 110% of the calculated amount to account for pipetting loss.
Additionally, make 120% KO DMEM + PEI MM to ensure there is enough extra.

**Knockout (KO) DMEM + PEI Master Mix (MM) Calculations**

Overall parameters:

=========================================== ===============
**Parameter**    							**Value**
=========================================== ===============
	Titrated PEI ratio						Specific for each PEI batch (e.g., 5 ug PEI : 1 ug DNA). The PEI concentration itself is 1mg/mL.
	DNA/plasmid/well						10.8 ug/plate
	KO DMEM/plasmid/well					1.33 mL/plate
=========================================== ===============

Example MM calculation (make 120% for extra):

============================================== =====================================================================================================
**Value**    					    			**Example in a 96-well plate**
============================================== =====================================================================================================
	Number plasmids/well						2 plasmids (*example*)
	Total wells									50 wells (*example*)
	Titrated PEI ratio							5 ug PEI : 1 ug DNA (*example*)
	KO DMEM/well								(1.33 mL/plate/plasmid) / (96 wells/plate) * (2 plasmids) = **27.7 uL/well**
	PEI/well									(10.8 ug DNA/plate) / (96 wells/plate) * (5ug PEI / 1ug DNA) / (1 ug/uL PEI) = **0.56 uL/well**
	**Total KO DMEM (120%)**					(27.7 uL/well) * (50 wells) * 1.2 = **1.663 mL**
	**Total PEI (120%)**						(0.56 uL PEI/well) * (50 wells) * 1.2 = **33.75 uL**
============================================== =====================================================================================================

Example condition mix calculation (make 110% for extra):

============================================ ===============
**Value**    					    			**Example**
============================================ ===============
	Plasmid concentration						100 ng/uL (*example*)
	Wells/condition								3 wells (*example*)
	**Plasmid volume/condition (110%)**			(10.8 ug/plate) / (96 wells/plate) / (0.100 ug/uL) * (3 wells) * 1.1 = **3.71 uL**
	**Master mix/condition (110%)**				(~ 27.7 uL/well KO DMEM) * (3 wells) * 1.1 = **91.41 uL**
============================================ ===============

Protocol
--------

1.	Seed healthy 293T cells 1 day prior to transfection.  Cells must be ~80% confluent at time of transfection for highest efficiency. Recommended cell counts are:

=============== ================= ===============
**Cell Type**    **Well Size**     **# Cells/Well**
=============== ================= ===============
HEK293T        	96-well             25-40K
HEK293T        	10-cm               7.5M
Plat-E         	6-well              800K
=============== ================= ===============

2.	Make a mastermix (MM) of PEI and Knockout DMEM according to the calculations :ref:`above <transfection-calcs>`.

.. important::
	Ensure that you add PEI to KO DMEM, *not the other way around!*
	Mix master mix well, then let sit for minimum 10 minutes.

3.	For each condition, combine the DNA and the PEI+KO DMEM MM according to the calculations, then mix and wait 10-15 minutes. These are the "condition mixes."

4.	Gently add the calculated amount of condition mix to each desired well on **TOP** of the existing growth media using the 100% NOT the 110% volumes. For larger well (anything above 24-well), add the condition mix *dropwise* and evenly around the plate, rocking the plate back and forth, side to side to mix.
5.	*After 18-24 hours* (1 day post transfection, dpt), aspirate and replace with :doc:`fresh media <adherent_cell_culture>` (e.g., DMEM + 10% FBS for HEK293T). Typically, any small-molecule inducers are added at this step (e.g., doxycycline).
6.  It is standard to image and flow cells at 2 dpt (1 day after fresh media change). If small-molecule inducers were added at 1 dpt, it is common to flow at 3 dpt to allow the expression levels to reach steady state.
