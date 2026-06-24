===========
DNA cleanup
===========

When generating DNA fragments via an enzymatic reaction (e.g., PCR, restriction digest), we need to purify the resulting product 
and remove the leftover enzyme and buffer. That way, the product can be easily used in downstream cloning reactions.

To do so, we use the NEB Monarch® Spin PCR & DNA Cleanup Kit (`NEB T1130 <https://www.neb.com/en-us/products/t1130-monarch-spin-pcr-and-dna-cleanup-kit-5-ug>`_).
Actually, we source the components separately:

    - **Buffer BZ** (`NEB T1115 <https://www.neb.com/en-us/products/t1114-monarch-buffer-bz>`_): Binding buffer, add 72 mL isopropanol (or volume indicated on bottle) 
      when first opened; not required when using agarose dissolving buffer
    - **Spin S1A columns** (`NEB T2037L <https://www.neb.com/en-us/products/t2037-monarch-spin-columns-s1a-and-tubes>`_): 5-µg binding capacity, not the same as the columns for the miniprep kit
    - **DNA wash buffer**: made in-house, dilute from 10x stock as needed (:doc:`recipe </recipes/bacteria/dna_wash>`)


1. Add the appropriate volume of Buffer BZ to your sample and pipet to mix. 
   Note that the max volume in a PCR strip tube is 250 µL---transfer to a 0.6-mL Eppendorf tube if necessary.

   - **For larger fragments** (>50 bp dsDNA): Use 5 volumes of buffer (e.g., 125 µL buffer into 25 µL sample)
   - **For smaller fragments and oligos** (dsDNA 11-50 bp, ssDNA 16-200 nt): Use 2 volumes of buffer (e.g., 50 µL buffer into 25 µL sample)

   .. important:: If your sample already contains agarose dissolving buffer, you do **not** need to add Buffer BZ.

2. Transfer the solution into a Spin S1A column placed in a collection tube.
3. Spin at max speed (16,000xg) for 1 minute in a benchtop centrifuge.
4. Aspirate the flowthrough into the miniprep waste.

   .. warning::
        Do not add the flowthrough into the media/cells waste! If this occurs, talk to the EHS rep.
        Add bleach to the affected flask in the fume hood and allow fumes to disperse. 
        A black precipitate may form; dispose of the solids in the biowaste and drain the liquid in the sink. 

5. Add 200 µL of DNA wash buffer to the column. Spin at max speed for 1 minute.
6. Repeat the wash step for a total of 2-5 washes.

   - When cleaning up a reaction directly, 2 washes is sufficient.
   - When cleaning up a fragment extracted from a gel, additional washes help remove contaminants from the agarose dissolving buffer.
   - Aspirate the flowthrough into the miniprep waste after every 3 washes. This prevents the solution from touching the column (max fill is 800 µL).

7. Aspirate the flowthrough into the miniprep waste.
8. Spin at max speed for 1 minute. This dry spin helps remove traces of buffer from the column.
9.  Transfer the column to a fresh 1.7-mL tube.
10. Add 5-20 µL of Elga water to the column. Pipet the liquid directly onto the filter without touching it with the pipette tip.
    Incubate at room temperature for at least 1 minute.

    .. tip:: Pre-warm Elga water in a 55ºC water bath for better elution.

11. Spin at max speed for 1 minute to elute the DNA.
12. To quantify yield, measure 1.5-2 uL of sample on the Nanodrop.

    - Concentrations <20 ng/uL are unreliable measurements.
      However, the product can likely still be used in a downstream reaction if the spectrum has the correct shape.
    - The A260/280 ratio should be 1.80-2.00. Lower values indicate protein contamination.
    - The A260/230 ratio should be >2.00 (>1.80 is okay). Lower values indicate salt contamination from the buffers. Additional washes can reduce this contamination. 