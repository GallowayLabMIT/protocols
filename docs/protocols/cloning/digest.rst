Restriction digest
==================

Restriction digest refers to the cutting of DNA fragments using restriction enzymes, which recognize particular DNA sequences (~4-6 bp).
We have a number of restriction enzymes in lab; a current list can be found `here <https://mitprod.sharepoint.com/:t:/s/GallowayLab/EafvG6wxMYtIldd_kYfRWuUBgfdTJmFjVKERHH2ouqYQIw?e=asZyuv>`_.
Most, if not all, of these enzymes have optimal activity in the NEB rCutSmart Buffer, but you can check `this NEB chart <https://www.neb.com/en-us/tools-and-resources/usage-guidelines/nebuffer-performance-chart-with-restriction-enzymes>`_ 
for details.


1. Combine the following in a PCR strip tube:

    =================== =========== =========
    Reagent             Amount      Notes
    =================== =========== =========
    DNA                 ~1 µg 
    rCutSmart buffer     5 µL 
    Enzyme(s)           1 µL each 
    rSAP (optional)     1 µL        Dephosphorylates 5\' DNA ends to prevent re-ligation of digested product
    Elga water          X µL        Add Elga water to reach total volume
    **Total**           **50 µL**
    =================== =========== =========

2. Incubate the mixture at 37ºC in the water bath for 1 hour.

    .. tip:: 
        If you'd like to run a digestion but can't come back in an hour, you can incubate the mixture in a thermocycler at 37ºC for 1 hour followed by 20 min at 65ºC
        (or 80ºC, `check <https://www.neb.com/en-us/tools-and-resources/usage-guidelines/nebuffer-performance-chart-with-restriction-enzymes>`_ the inactivation temperature for your enzyme).
        This way, you don't over-digest, which can lead to off-target cutting.

3. :ref:`Gel extract <gel_extract>` your desired digestion product.

    .. note:: 
        Depending on your use-case for the product, you may be able to skip the gel extraction step and instead purify the digestion directly.
        This will increase the concentration of the final product but may affect downstream assembly reactions.