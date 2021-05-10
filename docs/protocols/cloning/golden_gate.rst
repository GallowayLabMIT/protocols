========================
Golden Gate assembly
========================

Golden Gate assembly allows us to create a construct using type II restriction enzymes.

Protocol
=========
1. Design the assembly. Online tools such as `NEB Golden Gate <https://goldengate.neb.com/>`_.

2. Recipe

* Total volume: **10 µL**

================================= =================================================
  Component                          Amount        
================================= =================================================
 75 ng/plasmid
 2:1 mol ratio for fragments
 10X T4 DNA ligase buffer          1 µL
 T4 DNA ligase (400 U/µL)          1.25 µL (500 U)
 Type II RE                        0.5 µL (increase to 1 µL if >10 inserts)
 H2O                               to 10 µL
================================= =================================================

.. note::
	Make sure to use 500 U T4 DNA ligase. NEB sells 400 and 2,000 U/µL T4 DNA ligase so scale volume accordingly.


3. Use the appropriate assembly protocol
   
================================= ==========================================================================
  Insert number                      Assembly protocol        
================================= ==========================================================================
 For 1 insert                      37°C, 5 (cloning) or 37°C, 1 hr (library preparation) -> 60°C, 5 min
 For 2-10 inserts                  (37°C, 1 min -> 16°C, 1 min) x 30 -> 60°C, 5 min
 For 2-10 inserts                  (37°C, 5 min -> 16°C, 5 min) x 30 -> 60°C, 5 min
================================= ==========================================================================

4. :doc:`Transform competent cells <transformation>` with 2 µL of the Golden Gate mixture.
5. Store unused Golden Gate assembly products at -20°C


Citations
---------
[1] https://www.neb.com/protocols/2018/06/05/golden-gate-24-fragment-assembly-protocol

[2] https://www.neb.com/-/media/nebus/files/manuals/manuale1601.pdf



