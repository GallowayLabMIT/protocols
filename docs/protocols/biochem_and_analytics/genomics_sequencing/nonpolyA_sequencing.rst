=====================================
Non-pA and pA transcript sequencing
=====================================

This protocol allows you to do a targeted pulldown of
both polyadenylated and non-polyadenylated transcripts,
targeted to a set of genes or a region of interest. The resulting
transcripts can be reverse transcribed into cDNA or directly used for
long-read sequencing.

How do we do both this enrichment while maintaining the non-polyadenylated
transcripts? The overall process is:

1. Extract RNA from cells, following normal RNA isolation instructions.
2. Non-specifically ligating on a known DNA adapter to the 3' end of all RNA. This includes things like rRNA, miRNA, etc.
3. Using a biotinylated probe library, bind capture probes to the adapter-ligated library.
4. Select for the library by mixing with streptavidin magnetic beads.
5. Release the resulting transcripts from the beads. Perform cDNA synthesis with a custom primer targeting the adapter,
   or perform direct RNA sequencing.


Day -n
------
Prepare a 5'-phosphorylated adapter oligo. This can be stored at -20°C indefinitely.

.. note::

    A tested functional adapter oligo is oTA526, though you can use another if desired. For example, if your nanopore run
    or other downstream step is already using a specific sequencing primer, it might be good to use the reverse complement of that oligo as the adapter sequence.

    oTA526: ``CCTAATTCAGGTAACCGGAGGAG``

1. Prepare the following reaction mix for the adapter oligo. This can be scaled up or down as required.

   ==================   ================
   Component            Volume
   ==================   ================
   100 µM oligo         4 µL (400 pmol)
   T4 ligase buffer     1 µL
   PNK                  0.5 µL
   Water                4.5 µL
   ==================   ================

2. Run a phosphorylation program (37°C for 1 hour, 65°C for 20 minutes) on a thermocycler.
3. Cleanup using a DNA spin column. Use the "alternative / oligo" cleanup protocol that adds more IPA to reduce the size cutoff. Elute in 10 µL of 0.1x TE.

Make sure that enough genomics-grade stock solutions are available. These are common buffers shared across many protocols. In particular,
you will need less than 1mL of the following :doc:`shared genomics buffers </protocols/biochem_and_analytics/genomics_sequencing/shared_genomics_buffers>`:

- 1M Tris, pH 7.5
- 5M NaCl
- 0.5M EDTA

Day 0: Buffer preparation
------------------------------

- Make sure there is sufficient amounts of the following :doc:`shared genomics buffers </protocols/biochem_and_analytics/genomics_sequencing/shared_genomics_buffers>`:
  
  - 5M NaCl
  - 1M Tris-HCl, pH 7.5
  - 0.5M EDTA, pH 8.0


Ligation and target enrichment
------------------------------

Following RNA isolation, setup a ligation reaction. This reaction can be scaled up depending on the amount of recovered RNA.

1. Setup the following reaction. The components come with the T4 RNA Ligase 1 (NEB #M0204) 

   ============================ ================
   Component                    Volume
   ============================ ================
   10x T4 RNA ligase buffer     2 µL
   50% PEG                      9 µL
   1 mM ATP                     2 µL
   T4 RNA ligase I              1 µL
   Phosphorylated adapter oligo 100 pmol, ~2 µL
   RNA                          10 pmol
   Water                        to 20 µL
   ============================ ================
2. Incubate at 25°C for 2 hours.
3. While incubating, prepare the following buffers.  You either need to make the High EDTA buffer or High EDTA + formamide. Only the formamide-containing buffer needs to be made fresh; others can be stored.

   - Wash/binding buffer (5 mL)

     ========== =================   ========
     Target     Component           Volume
     ========== =================   ========
     0.5M NaCl  5M NaCl             500 µL
     20 mM Tris 1M Tris, pH 7.5     100 µL
     1 mM EDTA  0.5M EDTA           10 µL
     Water      DEPC water          4.39 mL
     ========== =================   ========

   - Option A: High EDTA buffer (500 µL)

     ========== =================   ========
     Target     Component           Volume
     ========== =================   ========
     0.5M NaCl  5M NaCl             50 µL
     20 mM Tris 1M Tris, pH 7.5     10 µL
     4 mM EDTA  0.5M EDTA           4 µL
     Water      DEPC water          436 mL
     ========== =================   ========


   - Option B: High EDTA buffer buffer + 15% formamide (500 µL)

     .. warning::

        Formamide is a suspected carcinogen and can damage fertility / fetuses!
        Don't work with this if you are pregnant, and work with both the 100% formamide buffer preparation and 
        capture steps up to the first wash in the actual fumehood, before moving back to the genomics hood.

        Collect used buffer, unused buffer, and the first wash after as chemical waste.

     =============  =================   ========
     Target         Component           Volume
     =============  =================   ========
     0.5M NaCl      5M NaCl             50 µL
     20 mM Tris     1M Tris, pH 7.5     10 µL
     4 mM EDTA      0.5M EDTA           4 µL
     15% formamide  formamide           75 µL
     Water          DEPC water          361 µL
     =============  =================   ========

   - Low Salt buffer (5 mL)

     ========== =================   ========
     Target     Component           Volume
     ========== =================   ========
     0.15M NaCl 5M NaCl             150 µL
     20 mM Tris 1M Tris, pH 7.5     100 µL
     1 mM EDTA  0.5M EDTA           10 µL
     Water      DEPC water          4.74 mL
     ========== =================   ========

   - Elution buffer (1 mL)

     ========== =================   ========
     Target     Component           Volume
     ========== =================   ========
     10 mM Tris 1M Tris, pH 7.5     10 µL
     1 mM EDTA  0.5M EDTA           2 µL
     Water      DEPC water          988 mL
     ========== =================   ========

4. Add 0.5 µL (50 pmol) of 100 µM biotinylated capture oligos to each sample.
5. Dilute each sample five-fold with high-EDTA buffer, with or without formamide, adding 80 µL to a final volume of 100 µL. The EDTA stops the ligase activity.

   - If using formamide, after mixing well, let the reaction sit at room temperature for 10-15 minutes.
   - If not using formamide, after mixing well, use a thermocycler to heat to 65°C for 5 minutes, followed by a slow ramp back to room temperature.
 
6. While waiting for capture oligo binding, wash 12.5 µL of MyOne Streptavidin C1 beads per sample. Wash a "master mix" of beads if possible to maintain consistent bead
   concentration. To wash, adding 10x volume (125 µL) of Wash/Binding buffer, magnetically separating the beads, removing the supernatant, and repeating the wash.
   After washing twice, resuspend the beads back in 12.5 µL of Wash/Binding buffer per sample.
7. Before beginning wash steps, warm an aliquot of Elution Buffer to 65°C. Keep at 65°C.
8. Add 12.5 µL of washed beads to each sample. Mix well with a pipette, and incubate at room temperature for 10 minutes. If beads settle, re-mix with a pipette.
9. Perform 2x wash steps with 100 µL of Wash/Binding buffer. After the second resuspension in wash buffer, move the beads to a fresh set of PCR tubes.
10. Perform one more wash with 100 µL of Wash/Binding buffer.
11. Wash the beads with 100 µL of Low Salt buffer.
12. After removing the supernatant from the Low Salt wash step, add 4 µL of warm elution buffer to the beads, mixing with pipetting. Once all samples are well mixed,
    put the tube back on the magnet and move the supernatant to a fresh set of PCR tubes.
13. At this point, you have properly ligated, target-enriched RNA. You should freeze the RNA or proceed to downstream uses, like cDNA synthesis.



cDNA synthesis
--------------
If doing cDNA synthesis, you can use the reverse complement of the ligation primer to only make cDNA of properly ligated RNA. You can follow
the ProtoScript First Strand cDNA Synthesis kit, whose instructions (for half-reactions, which work fine) are listed here for convenience.
This protocol uses 3 of the 4 µL eluted in the previous step, to correct for any losses.

1. Prepare the following reaction mix:
   
   ==================== ======
   Component            Volume
   ==================== ======
   RNA                  3 µL
   10 µM rev-com primer 1 µL
   M-MuLV reaction mix  5 µL 
   M-MuLV enzyme mix    1 µL
   ==================== ======

2. Incubate at 42°C for one hour, followed by inactivation at 80°C for 5 minutes. A thermocycler program exists for this.
3. Store at -20°C or colder. The sample can be used directly in downstream steps (qPCR, etc) as long as the volume of cDNA product
   does not exceed 10% of the downstream volume.