=================================
KAPA SYBR\ |registered| FAST qPCR
=================================

Protocol
---------------------------------

Any existing qPCR assay performed efficiently using standard cycling conditions may be converted to a fast qPCR assay with KAPA SYBR FAST qPCR Kits. Typically, re-optimization of reaction parameters is required.

qPCR is performed  at the MIT BioMicro Center on a Roche LightCycler 480 using SYBR Green MasterMix. Roche's documentation is `here <../../_static/files/roche_light_cycler-manual.pdf>`__.

1. Master Mix Preparation
---------------------------------

#. Ensure all reaction components are properly thawed and mixed.
#. Prepare a master mix containing the appropriate colume of all reaction components common to all or a subset of reactions to be performed.
#. Always include a No Template Control (NTC) to allow for detection of contamination of reaction components.
#. Calculate the required volume of each component based on the following tables:


+------------------------+-----------+-----------+-------------+
| Component              |  ROX      |   No ROX  | Final conc. |
+========================+===========+===========+=============+
| PCR-grade water        |Up to 20 μL|Up to 20 μL|  N/A        |
+------------------------+-----------+-----------+-------------+
| KAPA SYBR FAST         | 10 µL     | 10 µL     | 1X          |
| qPCR Master Mix (2X)   |           |           |             |
| Universal              |           |           |             |
+------------------------+-----------+-----------+-------------+
| 10 µM forward primer   | 0.4 µL    | 0.4 µL    | 200 nM      |
+------------------------+-----------+-----------+-------------+
| 10 µM reverse primer   | 0.4 µL    | 0.4 µL    | 200 nM      |
+------------------------+-----------+-----------+-------------+
| Template DNA           | As        | As        | <20 ng      |
|                        | required  | required  |             |
+------------------------+-----------+-----------+-------------+
| 50X ROX High/Low       | 0.4 µL    |    \--    | 1X          |
| (as required)          |           |           |             |
+------------------------+-----------+-----------+-------------+

2. Reaction Setup
---------------------------------

#. Transfer the appropriate volumes of qPCR master mix, template, and primers to each well of a PCR plate/tube(s).
#. Cap or seal the reaction plate/tube(s) and centrifuge briefly.

3. qPCR
---------------------------------

#. If applicable, select fast mode on the instrument.
#. Confirm that the qPCR protocol to be used conforms to the following parameters:

+--------------------+---------------------------------+------------------------------------+
| Detection Format   | Block Type                      |   Reaction Volume                  |
+====================+=================================+====================================+
| SYBR Green         | 96 well                         |  10 - 25 µL                        |
|                    +---------------------------------+------------------------------------+
|                    | 384 well                        |  3 - 20 µL                         |
+--------------------+---------------------------------+------------------------------------+
| **Program Name**   |  **Cycles**                     |  **Analysis Mode**                 |
+--------------------+---------------------------------+------------------------------------+
| Pre-incubation     | 1                               |  None                              |
+--------------------+---------------------------------+------------------------------------+
| Amplification      | 40                              |  Quantification                    |
+--------------------+---------------------------------+------------------------------------+
| Melting Curve      | 1                               |  Melting Curves                    |
+--------------------+---------------------------------+------------------------------------+
| Cooling            | 1                               |  None                              |
+--------------------+---------------------------------+---------------------+--------------+
| **Program Name**   | **Target (**\ |degree|\ **C)**  | **Aquisition Mode** | **Hold**     |
|                    |                                 |                     | (hh:mm:ss)   |
+--------------------+---------------------------------+---------------------+--------------+
| Pre-incubation     | 95                              |  None               | 00:03:00     |
+--------------------+---------------------------------+---------------------+--------------+
| Amplification      | 95                              |  None               | 00:00:10     |
|                    +---------------------------------+---------------------+--------------+
|                    | Primer dependent                |  None               | 00:00:20     |
|                    +---------------------------------+---------------------+--------------+
|                    | 72                              |  Single             | 00:00:01     |
+--------------------+---------------------------------+---------------------+--------------+
| Melting curve      | 95                              |  None               | 00:00:05     |
|                    +---------------------------------+---------------------+--------------+
|                    | 65                              |  None               | 00:01:00     |
|                    +---------------------------------+---------------------+--------------+
|                    | 97                              |  Continuous         | 5-10 acq/    |
|                    |                                 |                     | \ |degree|\ C|
+--------------------+---------------------------------+---------------------+--------------+
| Cooling            | 40                              |  None               | 00:00:10     |
+--------------------+---------------------------------+---------------------+--------------+

4. Data Analysis
---------------------------------
#. Data analysis is dependent on experimental design. Refer to the instrument guidelines for more information on how to perform the appropriate data analysis.

.. |registered| unicode:: U+00AE
.. |degree| unicode:: U+00B0