======================
Protein expression
======================

.. time:: 2 days


Protocol
=========
.. note::
    The BL21 strain of *E. coli* is best for protein production. It has several proteases knocked
    out, among other modifications. There are several sub-strains that can be relevant:

    - **BL21**: The classic, useful if your promoter is a standard *E. coli* promoter
      such as *lac, tac, trc, ParaBAD, PrhaBAD,* or *T5*.
    - **BL21(DE3)** : A strain with integrated T7 polymerase. Can be used in place of **BL21**
      but is required if using the *T7* or *T7-lac* promoters.
    - **BL21-RIL** : A strain with extra copies of certain tRNAs, in order to correct for the
      rarity of some codons in *E. coli*. This can be helpful in upping protein titers,
      especially when expressing some mammalian proteins.

1. In the morning, start a **5 mL** culture of your strain, in LB/antibiotic media.
2. Prepare :ref:`TB media <tb_media>` in Erlenmeyer flasks. For proper aeration,
   flasks should be filled to at most 30% the listed volume. 
3. Before leaving for the day, incoluate **20 mL** LB/antibiotic cultures with **400 uL** of the 5 mL culture.
4. The following morning, use the NanoDrop to calculate the OD of the overnight cultures. Inoculate large
   flasks to an OD of ???? (this should be around a 1:50 dilution).
5. Grow cultures until an OD of 0.6. Sample every half hour to an hour.
6. Induce with 0.5 mM sterile-filtered IPTG.