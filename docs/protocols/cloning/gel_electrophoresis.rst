Gel electrophoresis and extraction of DNA
==========================================

Gel electrophoresis
-------------------

Gel electrophoresis is a technique used to separate DNA fragments by size. DNA is negatively charged, so when an electric field is applied, DNA fragments will migrate towards the positive electrode. Smaller fragments migrate faster than larger ones, allowing for size-based separation.

1. Prepare a 1% agarose gel by mixing 0.5 g of agarose powder with 50 mL of 1X TAE buffer.

.. note::
    50 mL is needed for a 2 comb gel, whereas 30 mL is sufficient for a 1 comb gel. To detect smaller fragments, higher concentrations of agarose (up to ~3% for ~100 bp fragments) can be used.

2. Heat the mixture in a microwave until the agarose is completely dissolved (~1 min).
3. Allow the solution to cool slightly before pouring it into a gel casting tray with a comb in place to create wells. 
4. Let the gel solidify at room temperature for ~30 minutes.


.. _gel_extract: 

Gel extraction
--------------

Gel electrophoresis can also be used to select and purify DNA fragments by size.

1. Perform gel electrophoresis as described above. Load the **entire volume** of your reaction into a single well, if possible, 
   with the appropriate volume of 6X Loading Dye (e.g., 10 µL Loading Dye plus 50 µL reaction). 

    .. note:: 
        Since you will be running a larger volume, you should use the gel comb that creates larger wells (6 wells in a row for the small gels).
        Also, be careful to adequately fill the mold so that the well is deep enough.

2. After the gel is finished running, use the UV imager to identify the desired band on the gel. Using a razor blade, cut out a 
   fragment of gel containing your product. Do your best to cut the **smallest** gel fragment that includes your product.
   Cut the gel while still in the acrylic loader, don't cut it directly on the backlight.

   .. important:: 
    To avoid UV exposure while cutting your gel at the imager, it is recommended to wear a blue lab coat (if you are not already wearing long sleeves).

3. Place the gel fragment into an eppendorf tube.
4. Weigh the fragment (tare the scale on an empty tube first) and record the weight in mg.
5. Add agarose dissolving buffer to the tube. Use a 3:1 ratio of buffer in µL to gel fragment in mg (e.g., add 300 µL buffer for a 100 mg gel fragment). 

    .. tip:: 
        You should always use the 3:1 ratio. However, you should try to cut your gel chunks so that you are
        using less than 400 µL gel dissolving buffer. Larger volumes will introduce more contaminants into your
        final DNA cleanup and reduce the quality of DNA.
        In many cases, using a standard 250 µL of gel dissolving buffer works well, assuming a reasonably sized gel fragment.

6. Incubate in the water bath at 56ºC for ~10 minutes, or until the gel looks dissolved.
7. Follow the steps in the `NEB Monarch PCR DNA Cleanup Kit <https://www.neb.com/en-us/protocols/2024/07/16/standard-cleanup-protocol-using-the-monarch-spin-pcr-and-dna-cleanup-kit-and-centrifugation>`_
   to purify DNA from this solution. 

   - In the first step, you do NOT need to add binding buffer; you can directly load the solution into the spin column.
   - Perform **3 washes** instead of the two listed in the protocol, followed by a dry spin. If you had to use more ADB, you can add a fourth or fifth wash. This will help improve the purity of the final product.
   - In the final step, elute into ~15 µL of pre-warmed Elga water.

8. To confirm effective purification, measure the concentration of the final product on the Nanodrop.
   Concentrations below ~25 ng/µL are unreliable and indicate poor purification, but may still be used in downstream reactions at lower efficiency.