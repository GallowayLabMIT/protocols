=========
CUT&Tag
=========

This protocol is modified from the Active Motif protocol.

Background
==========
CUT&Tag relies on a protein-A/protein-G conjugated Tn5 to tagment DNA
based on primary/secondary antibody binding. The advantage
of this is a higher signal-to-noise ratio, relative to CUT&RUN, which
relies on protein-A conjugated MNase, CUT&Tag libraries are directly tagmented
wtih PCR-compatible adapters, which allows you to skip the library ligation
step.

However, Tn5 has a related accessibility bias (like the bias you are measuring
in ATAC-seq!). CUT&Tag buffers do the tagmentation in a higher-salt buffer
than ATAC-seq, which increases electrostatic screening and thus disrupts
nucleosome and chromatin interactions, which lessens the accessibility signal.

This protocol is most sanely split over three days.

- Day 1: cell counting, bead binding, primary antibody binding overnight. This step is fairly short: 32 samples took ~4 hours. 
- Day 2: secondary antibody binding, tagmentation, DNA cleanup, test PCR. This is a very long day! Nearly ~11 hours for 32 samples.
- Day 3: PCR amplification, library quantification.

Experimental setup
==================

Active Motif does _not_ recommend using an IgG control antibody condition. Instead,
use a common histone mark (H3K27me3, H3K27ac) as your control. If your experiment
already calls for one of these histone marks, then you do not need an explicit
separate control.

Select primary antibodies that have the same species, either rabbit or mouse. Then,
order a spike-in nuclei kit from Active Motif with the matching species. 


.. warning:: 

    Do **NOT** store Concanavalin A beads below 4C. These beads are 
    extremely sensitive to freezing and should never be stored below 4C.

    Some protocols tell you not to vortex ConA beads, to avoid shearing
    the ConA from the beads, so we avoid vortexing the beads in the initial
    steps.

Preparation (N days before)
============================
- Seed cells and split your conditions so that you have a bit in excess
  of **500k cells per antibody** you wish to use. For example, if you have
  four antibodies, seed cells such that you have more than 2M cells.
- Check the Concanavalin A (ConA) beads for aggregation. To do so, after pipetting
  to resuspend the beads, dilute 1 uL of beads with 9 uL of 0.1x TE (or water).
  You should not see large clumps of beads with the hemocytometer. If so, you
  should order more. If you got the beads from Active Motif, contact customer support:
  they will ship you new beads overnight for free.

Day 0
=====
- Check for ConA bead aggregation if you did not previously. This is your last chance to order beads!
  Cell Signaling Technologies sells ConA beads and will overnight ship to you.

Day 1
======
1. Disassociate your target cells **without using trypsin** or other enzymatic methods.
   For iPSCs, this means using Gentle Cell Disassociation Reagent.
2. Resuspend your cells in some FBS-containing media (for iPSCs: DMEM/F12 + 1% FBS). Count your cells, using Trypan Blue.
3. After counting, take spike-in nuclei out of the -80C freezer and defrost on ice. Combine enough nuclei
   for your required reactions together into a single tube.
4. Calculate the volume of cells needed to reach 500k cells per CUT&Tag reaction.
   If you are running multiple antibodies per sample, you can "master mix"
   and combine conditions together (e.g. calculate for 2M cells if you have 4 antibodies).

.. note:: 

    If you do not have 500k cells per reaction, you can resuspend fewer cells.
    However, you need to adjust the amount of spike-in nuclei for each reaction!
    It is very important that the cell-to-spike-in-nuclei ratio is constant.

    For example, if most of your conditions have 500k cells, but one only has 400k cells,
    then you should spin down the entire 400k while only adding in 4/5th of the amount of spike-in
    nuclei. Normally, we use 40 uL of spike-in nuclei per 500k cells, so this would
    mean reducing this to 32 uL of spike-in nuclei.

5. While spinning down the cells as described, activate the ConA beads. You can activate the ConA beads
   in larger batches (e.g. activate 8 reactions worth in 1.7 mL tubes).

   1. Resuspend ConA beads via trituration, and aliquot 10 uL per sample.
   2. Place the beads on the magnet and, once clear, remove the supernatant.
   3. Add 100 uL of activation / binding buffer per 10 uL sample. Let sit at room temperature for 10-15 minutes.
   4. Place the beads on the magnet, remove the supernatant.
   5. If using the Cell Signaling Technology beads, repeat this 100 uL wash step, because CST provides
      enough reagents for two washes.
   6. Resuspend beads in 10 uL of activation/binding buffer per sample.

6. Transfer the calculated amount of cells to a new tube to spin down. Spike in 40 uL of nuclei
   per CUT&Tag reaction. Spin down the cells and resuspend / wash in PBS + 1% FBS.
7. Spin down the cell + nuclei pellete, and resuspend in 100 uL of complete Dig-Wash (Dig-Wash plus protease inhibitor cocktail).
8. Aliquot 10 uL of activated ConA beads into PCR tubes.
9. Add the 100 uL of cells to the beads. Incubate on the Nutator for 10 minutes at room temperature.
10. 
