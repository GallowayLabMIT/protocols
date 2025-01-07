======
PCR
======

Polymerase chain reaction, or PCR, is a method to amplify sequences from template DNA using custom short oligonucleotides (primers).
The primers can additionally add short new sequences to the 5\' or 3\' ends of the DNA product. 

The identity of the polymerase used
in the reaction determines the speed and fidelity of product generation. In lab, we have the following polymerases:

- **Q5**: relatively efficient with high fidelity, recommended for generating fragments for cloning
- **PrimeSTAR**: extremely fast with slight compromises in fidelity, recommended for difficult-to-amplify sequences
- **Taq**: slow with lower fidelity, recommended for screening bacterial colonies (:doc:`colony PCR </protocols/cloning/colony_pcr>`) or other large-batch screening

Protocols for each polymerase are below. After running the reaction, :ref:`confirm and purify <pcr_confirm_purify>` the product.


Q5
----

.. note::
    To run the reaction, you'll need an annealing temperature (Ta) specific to your primers. The `NEB Tm Calculator <https://tmcalculator.neb.com/#!/main>`_ is a helpful tool for this.

Reaction mix:

======================= ============== ==========================
Reagent                 Amount (µL)     Notes
======================= ============== ==========================
DNA template            1               Dilute the DNA template to ~5 ng/µL to add ~5 ng
Primer 1                1.25            Use 10 µM primers diluted from stocks 
Primer 2                1.25            Use 10 µM primers diluted from stocks 
Q5 5X mix               5               Thaw from small cold block in Anna (-20ºC)
dNTPs                   0.5             10 mM, aliquots in Anna (-20ºC)
Q5 polymerase           0.25            Stored in small cold block in Anna (-20ºC) --- keep cold!
GC enhancer (optional)  5               Use for difficult or high GC templates
Elga water              15.75 (10.75)   Without (with) GC enhancer
**Total**               **25**
======================= ============== ==========================

Thermocycler protocol:

+----------------------+------------------+------------+
| Step                 | Temperature (ºC) | Time       |
+======================+==================+============+
| Initial denaturation | 98               | 30 sec     |
+----------------------+------------------+------------+
|| 1. Denaturation     || 98              || 10 sec    |
|| 2. Annealing        || Ta              || 10 sec    |
|| 3. Extension        || 72              || 30 sec/kb |
|| x 25 cycles         ||                 ||           |
+----------------------+------------------+------------+
| Final extension      | 72               | 2 min      |
+----------------------+------------------+------------+

.. note::
    There is no need to set at 4ºC infinte hold at the end of the reaction. DNA is quite stable, so it is fine to sit at room temp overnight. For longer-term storage, keep at 4ºC.


Source: `NEB Q5® High-Fidelity DNA Polymerase <https://www.neb.com/en-us/protocols/2013/12/13/pcr-using-q5-high-fidelity-dna-polymerase-m0491>`_


PrimeSTAR
----------

.. note:: 
    While changing the annealing temperature is an optimization strategy, most reactions will run well at the default 55ºC.

Reaction mix:

======================= ============== =======
Reagent                 Amount (µL)    Notes
======================= ============== =======
DNA template            1               Dilute the DNA template to ~5 ng/µL to add ~5 ng
Primer 1                1.25            Use 10 µM primers diluted from stocks
Primer 2                1.25            Use 10 µM primers diluted from stocks
PrimeSTAR Max 2X Premix 12.5            Stored in small cold block in Anna (-20ºC)
Elga water              9              
**Total**               **25**
======================= ============== =======

Thermocycler protocol:

+----------------------+------------------+-----------+
| Step                 | Temperature (ºC) | Time      |
+======================+==================+===========+
| Initial denaturation | 98               | 30 sec    |
+----------------------+------------------+-----------+
|| 1. Denaturation     || 98              || 10 sec   |
|| 2. Annealing        || 55              || 5 sec    |
|| 3. Extension        || 72              || 5 sec/kb |
|| x 30 cycles         ||                 ||          |
+----------------------+------------------+-----------+
| Final extension      | 72               | 2 min     |
+----------------------+------------------+-----------+

Source: `Takara Bio PrimeSTAR® Max DNA Polymerase <https://www.takarabio.com/documents/User%20Manual/R045Q/R045Q_e.v1108Da.pdf?srsltid=AfmBOoqYaK51A1XbVEkvskFbtibSTPU9uN4hpuIgiBXUMyP3nXMId-J9>`_


Taq
----

See the full :doc:`colony PCR protocol </protocols/cloning/colony_pcr>` for steps beyond running the reaction itself.

Reaction mix:

========== ============== =======
Reagent     Amount (µL)    Notes
========== ============== =======
Primer 1    0.75           Use 10 µM primers diluted from stocks
Primer 2    0.75           Use 10 µM primers diluted from stocks
Taq 2X MM   7.5            Thaw from Anna (-20ºC)
Elga water  6              
**Total**   **15**         Scale up as needed
========== ============== =======

Thermocycler protocol:

+----------------------+------------------+-----------+
| Step                 | Temperature (ºC) | Time      |
+======================+==================+===========+
| Initial denaturation | 95               | 30 sec    |
+----------------------+------------------+-----------+
|| 1. Denaturation     || 95              || 15 sec   |
|| 2. Annealing        || Ta              || 15 sec   |
|| 3. Extension        || 68              || 1 min/kb |
|| x 30 cycles         ||                 ||          |
+----------------------+------------------+-----------+
| Final extension      | 68               | 5 min     |
+----------------------+------------------+-----------+

Source: `APExBIO 2X Taq PCR <https://www.apexbt.com/downloader/document/K1034/Protocol.pdf>`_


.. _pcr_confirm_purify:

Confirm and purify
------------------

**DpnI digest**

If you plan to use your PCR product in a cloning reaction, it is helpful to perform a DpnI digestion on your PCR product before purification. 
DnpI is a restriction enzyme that recognizes dam methylation, which is found only on cell-derived DNA --- i.e., your plasmid template.
This chops up any of the original template from your PCR reaction, which is particularly useful if the template plasmid has the same antibiotic
resistance as the new, final plasmid product of the downstream assembly reaction.

1. Add 0.5 µL DpnI directly to your PCR reaction (for a 25 µL reaction; scale up the DpnI for larger reactions).
2. Pipet up and down or flick the tube to mix.
3. Incubate at 37ºC (water bath) for 1 hour. Avoid prolonged incubation, as the enzyme may promiscuously cut non-methylated GATC sites in your PCR product.


**Confirm**

To check that your PCR reaction was successful, you can run a portion of the product on a gel (:doc:`gel electrophoresis </protocols/cloning/gel_electrophoresis>`) to confirm that the product is the correct size.
This can be performed in parallel with a DpnI digestion.

- Combine ~2 µL of your PCR product with 0.5-1 µL of 6X Loading Dye. This can be done in a small droplet on a piece of parafilm.
- **For amplicons >500 bp:** Use a 1% gel (100 mg agarose per 10 mL 1xTAE buffer) and run at 100V for 25 min.
- **For amplicons <500 bp:** Use a 2% gel and run at 90V for 30-40 min.


**Purify**

We use the NEB Monarch PCR DNA Cleanup Kit to purify PCR products. If the gel shows a single band at the size you expect for your PCR product, you can purify the remaining product directly.

- **For amplicons <2 kb:** Use a 5:1 ratio of binding buffer to sample. For a 25 µL PCR reaction (where you ran a portion on a gel), you should use ~100 µL binding buffer.
- **For amplicons >2 kb:** Use a 2:1 ratio of binding buffer to sample. For a 25 µL PCR reaction (where you ran a portion on a gel), you should use ~40 µL binding buffer.
- In the final step, elute in 15-20 µL of pre-warmed Elga water.

Sometimes, PCR reactions will result in off-target amplification, which will likely cause problems in downstream cloning steps.
If this is the case, you can run the *entire volume* of the PCR product on a gel and cut out the band of the correct size. See the 
:ref:`gel extraction protocol <gel_extract>` for details. 