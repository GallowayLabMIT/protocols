================================
293T Rogi2 single LP V4 (cKG087)
================================


Line summary
------------


V4 Rogi2 dual LP single site integrase line:

=========       ===============      ================      ===============================              ===============================
locus            pHA for cargo        recombinase          positive selection (gene, drug)               counterselection (gene, drug)

=========       ===============      ================      ===============================              ===============================
Rogi2 LP            pKG03560          Bxb1 or eeBxb1             PuroR, Puromycin                           HSV-TK SR39h, GCV or PCV
=========       ===============      ================      ===============================              ===============================

.. note::
    The Rogi2 v4 is our current version. DO NOT use the pKG02180 donor plasmid, which contains an SV40 promoter which will replicate the plasmid in HEK293Ts. Use pKG03560.

.. note::
    Any Bxb1 or eeBxb1 expression plasmid can be used. Past plasmids used were pKG0570 for Bxb1 and pKG03466 for eeBxb1. The eeBxb1 is a higher efficiency recombinase variant.

Integration protocol
----------------------------------

Day -1
~~~~~~~
Seed cells at 100k per 24 well.

.. note:: 
    SRK typically plates 200k per 24 well which boosts cell health post-delivery of the plasmids.

Day 0
~~~~~~
Co-transfect your donor plasmid and Bxb1 expression plasmid at a 1.5:1 ratio, ie., following our standard PEI protocol.

.. note::
    An example that has worked well for SRK is 850 ng of donor plasmid and 565 ng ofBxb1 expression plasmid per 24-well.

.. note::
    Keep one well with no donor plasmid to be used as a negative control for puromycin selection.

Day 1
~~~~~
Visualize cells to verify efficient transfection and check cell health. 

.. note:: 
    DSP doesn't observe toxicity from PEI/Bxb1 expression, and therefore, does not media change. 
    SRK typically does a media change at this step to improve cell health.

Day 2
~~~~~~
Passage entire 24-well to 6-well plate.

Day 3
~~~~~~
Verify cells have adhered/look healthy and begin Puromycin selection @ 1 ug/mL (standard concentration). 

.. note:: 
    If cells do not look healthy, wait another 1-2 days to start selection. However, do not wait too long. At maximum, cells should be less than 40% confluent, otherwise selection may not perform as well. Include at least one condition with no integration to be used the monitor the puromycin selection.

Day 6
~~~~~~
Check well for survivors. At a minimum, you should see single cells/small colonies with normal morphologies. 

.. note:: 
    Larger cargoes will result in less efficient recombination, and thus, fewer survivors. Depending on your experimental timeline, you can transfect multiple wells with the same condition so you don't have to wait as long for outgrowth.

Day 8
~~~~~~
Media change, removing puromycin. DSP recommends a PBS wash to remove cell debris.

Day 9 + n
~~~~~~~~~~
Monitor cells and passage once confluent. DSP recommends passaging 1:10 at 6-well scale to let the cells recover and dilute out any residual plasmid before proceeding with downstream experiments.

.. note::
    SRK has noticed some outgrowth of non-integrated cell lines over time. Therefore, she recommends maintaining puromycin selection (1 ug/mL) in the media (or at least occasionally adding it) for downstream experiments.
    
Excision protocol

This is a placeholder until Deon ascertains a robust protocol.
------------------------------------------------------------------
=================   =============   ========
Counter-selection   Concentration   Dilution
=================   =============   ========
GCV                 10 µM           1000x
=================   =============   ========

