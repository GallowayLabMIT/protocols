==========
Test PCRs
==========
Before amplifying an entire DNA library for sequencing, we often perform a **test PCR**, amplifying a fraction of the library 
to estimate the number of amplification cycles required for the remainder. This helps ensure that we do not over-amplify the library, 
which would reduce library complexity and bias it towards shorter fragments.

Test PCRs have three key variables that depend on the upstream genomics technique:

- **The desired amount of product**. A common sequencing minimum is 15 µL of a 2-nM library. For a ~500-bp library, this is 5 ng. 
  Normally, you want to amplify to reach 50-500 ng per library. This variable sets the number of test cycles that need to be performed.
  Our protocols for each genomics technique suggest cycle counts for the test PCR based on expected yield (and previous results).
- **Choice of primers** based on how the library was constructed. Libraries created via adaptor ligation use one set (``ligation_fwd`` and ``ligation_rev``); 
  libraries created via Tn5 transposition use another set (``tagmentation_fwd`` and ``tagmentation_rev``).
  Other methods might have custom primers. These primers bind to a common sequence after the unique sample indexes, so you can use the same ones for all your samples.

   ====================== ==========================================================================
      Primer                  Sequence
   ====================== ==========================================================================
   ``ligation_fwd``        AATGATACGGCGACCACCGAGATCTACACTATAGCCTACACTCTTTCCCTACACGACGCTCTTCCGATC*T
   ``ligation_rev``        CAAGCAGAAGACGGCATACGAGATCGAGTAATGTGACTGGAGTTCAGACGTGTGCTCTTCCGATC*T
   ``tagmentation_fwd``    AATGATACGGCGACCACCGAGATCTACACTATAGCCTTCGTCGGCAGCGTCAGATGTG*T
   ``tagmentation_rev``    CAAGCAGAAGACGGCATACGAGATCGAGTAATGTCTCGTGGGCTCGGAGATGTG*T
   ====================== ==========================================================================

   \*T is an internal phosphorothioate.
  
- **Ratio between input volumes**. The suggested protocol uses 3 µL of pre-amplification library as input for the test PCR. Typical upstream elution volumes vary from 25 to 50 µL. The ratio
  between the volume used in the test PCR and the volume used in the real PCR is important; it defines how the optimal cycle count is converted from the test to the real amplification.

Protocol 
--------

1. Thaw the primers (Sven –20ºC, "Library prep reagents" box) at room temperature.
2. Prepare the PCR Master Mix using the NEBNext Ultra II DNA Library Prep Kit (`NEB E7645 <https://www.neb.com/en-us/products/e7645-nebnext-ultra-ii-dna-library-prep-kit-for-illumina>`__). 
   You will need 27 µL of mix per reaction; prepare 10% excess. You can use either undiluted 100 µM
   primers or diluted 10 µM primers.

   **PCR Master Mix (27 µL / reaction)**

   ================================== =========================   ======================
   Component                          Volume (100 µM primers)     Volume (10 µM primers)
   ================================== =========================   ======================
   2x NEBNext Ultra II Q5 Master Mix  15 µL                       15 µL
   DEPC-treated water                 11.85 µL                    10.5  µL
   forward primer                     0.075 µL                    0.75 µL
   reverse primer                     0.075 µL                    0.75 µL
   ================================== =========================   ======================
  
   .. note::

     We use 1/4 of the amount of primers that the NEBNext protocol suggests. Empirically, this works great!
     Pick the dilution that makes sense for the number of samples you are running. For example, use the
     diluted primers if you only have 3-4 conditions.

3. In fresh PCR tubes, add 3 µL of the pre-amplification library per condition to 27 µL of PCR Master Mix. There will be one tube per library.
   
  .. note::
     It is fine if your input samples contain streptavidin or other magnetic beads. They do not interfere with the PCR or downstream steps.

4. Set up the thermocycler protocol as written below (``lib_prep/test_pcr``). Decide on the number of cycles you wish to test, generally N, N+2, and N+4.
   Rather than preparing 3 tubes for each reaction, there are holds in the thermocycler protocol after N 
   and N+2 cycles during which sub-samples are removed (explained below).
     
     ==========  =============  ==============================================
     Temp (°C)   Time (MM:SS)   Description
     ==========  =============  ==============================================
     72          5:00           Polymerase activation
     98          0:30           Initial denaturation
     --          --             *N cycles of:*
     98          0:10           Denaturation
     65          1:15           Extension
     --          --             *[end cycle]*
     42          Hold           Remove 7 µL Qubit sample and 7 µL gel sample
     --          --             *2 cycles of:*
     98          0:10           Denaturation
     65          1:15           Extension
     --          --             *[end cycle]*
     42          Hold           Remove 7 µL gel sample
     --          --             *2 cycles of:*
     98          0:10           Denaturation
     65          1:15           Extension
     --          --             *[end cycle]*
     42          Hold           Remove 7 µL gel sample
     ==========  =============  ==============================================

5. Run the thermocycler protocol. While the initial cycles of the PCR are running (~30 min), prepare a normal DNA gel (e.g., 1.5% agarose with ethidium bromide) and 
   four sets of fresh PCR tubes (4 new tubes per reaction). For **three** of the sets of tubes, pipet 3 µL of Orange Loading Dye in each tube.

   .. note::
     We use Orange Loading Dye rather than Purple because the dye overlaps less with the DNA fragments we expect from the PCR. 
     This makes it easier to visualize bands in the imager. Orange Loading Dye is stored at room temperature in or next to the genomics hood.

6. When the hold step is reached, do not hit enter to continue. Instead, pause the run, press the "Lid open" button, and
   briefly take the tubes out. Use the multi-channel P10 to take a 7-µL subsample, combining it with the pre-prepared 3 µL of Orange Loading Dye for the gel.
   For the Qubit subsamples, place the 7-µL sample into empty tubes.
7. Place the tubes back in the thermocycler, close the lid, press "Lid close", press "Resume", then hit enter to continue past the hold. Repeat the subsampling at the next hold and at the end of the protocol.
8. Once the test PCR is complete, run the three subsamples per reaction on the prepared DNA gel. It is convenient to group the three subsamples per condition together, rather than grouping by cycle count.

   .. note::
     After removing the first subsamples, you can start loading the gel. Just don't forget to return to remove the next subsample 
     at the second hold.

9. When the gel has finished running, image it on both on our imager and the ChemiDoc in the Niles lab for better quantification.
10. While waiting on the gel to run, clean up the fourth set of subsamples (without loading dye) using SPRI beads.
    Follow the instructions for general :doc:`magnetic bead cleanup for genomics </protocols/biochem_and_analytics/genomics_sequencing/magnetic_bead>`, with these parameters:
   
      - Use 0.9x volume of beads (6.3 µL beads into the 7-µL subsample)
      - Elute in 20 µL of 0.1x TE
    
    .. note:: 
      You can alternatively use Ampure beads instead of SPRI beads if you plan to use these to clean up your final amplified libraries.
      Allow the Ampure beads to equilibrate to room temperature beforehand.

   ..   a. Vortex the Ampure beads well.
   ..   b. Add 0.9x (6.3 µL) of Ampure beads to each 7 µL Qubit sample, mix well via pipetting.
   ..   c. Incubate at room temperature for 15 minutes.
   ..   d. Place tubes on the magnetic rack. Remove the supernatant, and wash twice with 200 µL of freshly-prepared 80% EtOH
   ..      without disturbing the beads (e.g. keep the tubes on the magnet).
   ..   e. After the last wash step, remove residual EtOH using a P10.
   ..   f. Air-dry the beads until the shiny-to-matte transition happens, not longer than 5 minutes.
   ..   g. Add 20 µL of 0.1x TE to elute. Mix well via pipetting and incubate off-magnet for 2 minutes at room temperature.
   ..   h. Place the tubes back on the magnet and transfer the supernatant to new PCR tubes.

11. Quantify the cleaned-up samples on the Qubit in the BMC. Follow the Qubit protocol (TODO).

.. If you are unsure about the concentration, prepare both a 1 µL samples and a 10 µL sample.

..         a. Dilute the Qubit light-sensitive reagent 1:200 in Qubit dilution buffer to make working buffer. For 8 samples + 2 standards, this is 10 µL reagent + 1.990 dilution buffer.
..         b. In Qubit tubes, dilute 10 µL of Standard 1 and Standard 2 with 190 µL of working buffer.
..         c. In Qubit tubes, dilute 1 / 10 µL of each sample with 199 / 190 µL of working buffer.
..         d. Vortex all tubes to mix well.
..         e. Measure at the BMC. Multiply the given concentration by the dilution factor (20x or 200x).

Determine the optimal cycle counts
----------------------------------

Use the data from the gel and the Qubit to determine the number of cycles for amplifying each full library. Use the calculations below to convert 
test PCR cycle counts from the optimal conditions to "real" PCR cycle counts. Since the Qubit measurement can saturate, prefer the gel quantification results
over the Qubit ones if in conflict.

This calculation should be performed for each library (sample) individually, meaning that the cycle counts for the "real" PCR may vary across samples.
This helps ensure that the final libraries end up with similar total DNA amounts.

Gel-based quantification
~~~~~~~~~~~~~~~~~~~~~~~~

1. Identify the optimal band on the gel.
   
   Call the test PCR cycle count corresponding to this band :math:`N_{test}`.

   Look for a band with a visible fragment smear that is not over-amplified. Depending on genomics method, you may see smears corresponding 
   to mononucleosome, dinucleosome, and/or trinucleosome fragments.
   
   .. admonition:: Example

      In the example below, something between the first and second lanes appears optimal, since the reaction saturates in the third and fourth lanes.
      Here, the cycle counts were 12, 14, 16, 18, so we'll say :math:`N_{test} = 13`.

      .. image:: /img/rcmc_test_pcr_gel.jpg
         :align: center
         :height: 7cm

2. Calculate the volume of the pre-amplification library in the gel subsample, :math:`V_{test}`:
   
   .. math:: V_{test} = V_{input} \times \frac{V_{subsample}}{V_{reaction}}
   
   where:
   
   - :math:`V_{input}` is the volume of the pre-amplification library used as input to the test PCR reaction, here 3 µL as written in step 3 above
   - :math:`V_{reaction}` is the total volume of the test PCR reaction, here 30 µL 
   - :math:`V_{subsample}` is volume of the test PCR reaction subsampled for the gel, here 7 µL 
   
   .. admonition:: Example
      
      For the amounts suggested in the protocol above, we have:

      .. math:: V_{test} = 3\ \text{µL} \times \frac{7\ \text{µL}}{30\ \text{µL}} = 0.7\ \text{µL}

3. Compute the relative cycle count :math:`\Delta N` for the "real" PCR compared to the test PCR. 

   This is related to the ratio of the input volumes
   for the test PCR (:math:`V_{test}`) and the "real" PCR (:math:`V_{real}`). 
   As you increase the amount of starting material, you'll need fewer cycles to obtain the same amount of product. 
   For instance, if you start with twice the starting material, you'll need one fewer cycle, since the product 
   doubles each cycle in a PCR. More generally, the change in amount of product for the "real" PCR compared to the test 
   PCR is set by the ratio of input volumes, which must be compensated for by a change in cycle count:

   .. math:: 
      {\frac{V_{test}}{V_{real}}} = 2^{\Delta N} \\

   which gives:

   .. math::
      \Delta N = \log_2({\frac{V_{test}}{V_{real}}}) \\

   .. admonition:: Example

      If the total pre-amplification library volume was 23 µL and we'll use the entire remaining volume in the "real" PCR, we have:

      .. math:: 
         \Delta N &= \log_2({\frac{0.7}{23 - 3}}) \\
         &= -4.84

4. Finally, combine these values to find the cycle count for the "real" PCR, :math:`N_{real}`:

   .. math:: 
      N_{real} &= N_{test} + \Delta N \\
      &= N_{test} + \log_2({\frac{V_{input} \times \frac{V_{subsample}}{V_{reaction}}}{V_{real}}}) \\
      &= N_{test} + \log_2({\frac{V_{input}\ V_{subsample}}{V_{real}\ V_{reaction}}})

   .. admonition:: Example

      Continuing the example above, we have:

      .. math:: 
         N_{real} &= N_{test} + \Delta N \\
         &= 13 - 4.84 \\
         &= 8.16 \\
         &\approx 9\ \text{cycles}

      While we don't want to excessively over-amplify, diluting the final library is better than undershooting, which would then require an 
      additional PCR step before submission. So we'll round up to **9 cycles** for the "real" PCR.
   
Qubit quantification
~~~~~~~~~~~~~~~~~~~~

The calculation with the Qubit data is similar in concept, except it uses masses instead of volumes.

1. Calculate the final mass of the test PCR subsample used in the Qubit reaction, :math:`m_{test}`.

   This is the volume of the cleanup elution (from step 10 in the above protocol) times the measured Qubit concentration, accounting for the dilution factor:

   .. math::
      m_{test} = V_{cleanup} \times C_{Qubit} \times \text{dilution factor}

   .. admonition:: Example

      Let's say the Qubit measured a concentration of 10 ng/mL when the sample was diluted 1:200. Following the protocol above, we eluted the cleanup 
      of the Qubit subsample in 20 µL. Since ng/mL is equivalent to pg/µL, we have:

      .. math::
         m_{test} &= 20\ \text{µL} \times 10\ \text{pg/µL} \times 200 \\
         &= 40,000\ \text{pg} \\
         &= 40\ \text{ng}

2. Compute the expected mass of the "real" PCR, if the same cycle count is used.

   This is the final mass of the test PCR subsample scaled by the change in input volume. Use the volume of the pre-amplification library in the gel subsample (:math:`V_{test}`)
   calculated in step 2 of the gel quantification.

   .. math::
      m_{expected} = m_{test} \times \frac{V_{real}}{V_{test}}

   .. admonition:: Example

      Using the same example, with :math:`V_{test} = 0.7\ \text{µL}` as before and 20 µL as the input to the "real" PCR, we find

      .. math::
         m_{expected} &= 40\ \text{ng} \times \frac{20\ \text{µL}}{0.7\ \text{µL}} \\
         &= 1143\ \text{ng}

3. Determine the target mass for the "real" PCR, :math:`m_{real}`.

   This will depend on the genomics technique but is typically 50-500 ng. Note that the BMC sequencing minimum for a mid-yield sequencer is 
   15 µL of a 2-nM library, which is 5 ng for a library with an average fragment size of ~500 bp. This means there will be plenty of extra of each library, 
   in case they need to be re-sequenced later (or something goes wrong with library pooling).

4. Compute the relative cycle count :math:`\Delta N` for the "real" PCR compared to the test PCR.

   This is set by the ratio of expected and target masses, which must be compensated for by a change in cycle count:

   .. math:: 
      {\frac{m_{real}}{m_{expected}}} = 2^{\Delta N} \\

   which gives:

   .. math::
      \Delta N = \log_2({\frac{m_{real}}{m_{expected}}}) \\

   .. admonition:: Example

      If we want the final library to be 100 ng, we'll need to reduce the cycle count for the "real" PCR:

      .. math::
         \Delta N &= \log_2({\frac{100\ \text{ng}}{1143\ \text{ng}}}) \\
         &= -3.51

5. Finally, the cycle count for the "real" PCR (:math:`N_{real}`) is simply:
   
   .. math:: 
      N_{real} = N_{test} + \Delta N
      
   where :math:`N_{test}` is the cycle count for the test PCR subsample that was cleaned up for Qubit.

   .. admonition:: Example

      If the Qubit subsample was taken after 12 cycles of the test PCR, then for the "real" PCR we should use

      .. math::
         N_{real} &= 12 - 3.51 \\
         &= 8.49 \\
         &\approx 9\ \text{cycles}

The Qubit quantification should agree with the gel quantification for the same test PCR.
Additionally, the cycle count for the "real" PCR should match expected values in the genomics protocol.