================================
Genomics and sequencing methods
================================

.. toctree::
   :maxdepth: 1
   :glob:
   
   *

Genomics methods give us a way to interrogate any DNA you can place adaptors on, at very high scale and resolution.
Short-read sequencing is increasingly a commodity; it costs roughly $1000 for 500 million reads, and even less
per-read for billions of reads.

Genomics methods are very "mix and match", as they all follow the overall trend of:

1. **Generating fragments.** These steps take in all of the chromatin (or intact nuclei, or cells) and somehow fragment the DNA. Alternatively, when doing an RNA method, the transcripts are already fragments.
2. **Post-fragment methods.** Fragments of interest (transcripts, chromatin, etc) can be selected and enriched.
3. **Adding PCR adaptors.** To the fragments, adaptors are added, enabling downstream PCR steps. Tagmentation methods combine fragment generation 
   and PCR adaptor addition.
4. **Library generation.** Using the adaptors, just enough PCR is performed to reach submission minimums without over-amplified the library
   (which biases towards smaller fragments). These library PCRs also tend to add per-condition barcodes.
5. **Post-library methods.** Specific library members can be selected and enriched.
6. **Library pooling, QC, and submission.** Multiple libraries with different barcodes can be combined into the same sequencing run.

We can break down our in-lab protocols in the following way:

=========   ============================= ======================= =======================  ==============
Protocol    Fragment generation           Post-fragment           Adaptors                 Post-library
=========   ============================= ======================= =======================  ==============
ATAC-seq    Tn5 transposition                                     N/A: Tn5 adds adaptors
ChIP        Sonication                    Antibody pulldown       Ligation    
CUT&RUN     Targeted MNase digestion                              Ligation
CUT&Tag     Targeted Tn5 transposition                            N/A: Tn5 adds adaptors
GapRUN      GapR-targeted MNase digestion                         Ligation
MicroC      MNase digestion               Proximity cross-linking Ligation
RCMC        MNase digestion               Proximity cross-linking Ligation                 ROI capture
RNA-seq     RNA isolation, cDNA synthesis                         Ligation    
=========   ============================= ======================= =======================  ==============

Single-cell genomics methods take one of two paths:

1. **Droplet-based methods** like 10X encapsulates individual cells in droplets that have all of the required components for the assay.
2. **Combinatorial/Split-pool methods** which do successive rounds where cells are split across multiple PCR plates, then re-pooled and split again.
   These rely on combinatorial indexing to statistically add single-cell barcodes.

The following protocols we have done in lab fall into these categories:

=============  =====================   =====================
Method         Single-cell technique   Effort
=============  =====================   =====================
sci-ATAC-seq   Combinatorial           Very high
sc-RNA-seq     Droplet                 Low (core submission)
=============  =====================   =====================


Sequencing technologies
=======================

"Last generation" sequencing
-----------------------------
The original sequencing technology that you may be familiar with is Sanger sequencing.
Sanger sequencing works by running a normal PCR reaction for a single cycle,
starting from a primer binding site and using a low percentage of fluorescent, chain-terminating modified
nucleotides. The molar fraction of modified nucleotides is chosen so that, across an entire population
of plasmids, the chain reaction stops, on average, at every base pair for some member of the population.

This results in a mixture of PCR products of different lengths. Every product
terminates with a fluorescent base pair. Then, the mixture is run through a chromatography column that separates
the fragments based on length, with the resulting fluorescent measurements as a function of column running time
being the ``ab1`` file that you load into Snapgene.

Next generation sequencing
---------------------------
Next generation sequencing (NGS) is also a "sequencing by synthesis" and also uses fluorescent base pairs,
but measures the data in a fundamentally different way. Instead of measuring a single species for ~1000 base pairs,
like Sanger sequencing, NGS uses a patterned flow cell that reads millions to billions of DNA molecules
simultaneously.

However, NGS is a "short-read" sequencing method because each of the molecules are not read in full; only
the outer ~50-100bp edges are sequenced. One company, Illumina, invented this technique, but other companies like
Element Biosciences have innovated on the design. Element (AVITI Cloudbreak) is currently the most cost-effective
up to about a billion reads, whereas Illumina (NovaSeq X Plus) is the most cost-effective for billions of reads.

There is a lot of quality control that goes into these libraries, but the convienent thing is that, as the user,
you are only responsible for providing a library (e.g. mixture) of DNA molecules that contain known DNA anchors
at the end. Core facilities are responsible for actually loading and running the chip. 

The high-level process of what the core facility does is:

1. Does additional QC on your sample to confirm library concentrations, low contamination, etc.
2. Loads your library onto a "flow lane" of a "flow chip". Loading binds individual DNA molecules to
   binding sites on the patterned flow chip.
3. The bound DNA molecules are amplified, leading to small clusters of identical DNA molecules, spread spatially
   along the chip.
4. Primers and fluorescent bases, added in successive wash/binding steps, allows sequences of each cluster to be read out base-by-base.

Long-read sequencing
--------------------
Long-read sequencing is (currently) dominated by nanopore technology. These methods sequence DNA by forcing individual
DNA or RNA molecules through a small pore. A known adapter sequence is still needed to bind a DNA fragment to the pore to start
sequencing.

Given a library with a known sequence, these methods allow for sequencing of the entire fragment length, using a flowcell
with thousands of nanopores that measure the electrical properties of each base as it passes through the pore.

These techniques are more expensive per-read than short-read sequencing, but give full-length sequence information that
is especially important for examinig long spliced transcripts and other complicated fragments.
