=================
Attune operation
=================


.. note::

    "10% bleach" refers to a final concentration of 0.525% sodium hypochlorite (5250ppm chlorine).
    Use ELGA water instead of DI water to dilute the bleach.

    This was originally a 10x dilution of 5.25% sodium hypochlorite bleach, but in lab we typically
    stock higher concentration bleach.

    ====================    ===============     =====================   ========================
    Concentration           Dilution            Vol bleach (100mL)       Vol ELGA water (100mL)
    ====================    ===============     =====================   ========================
    5.25%                       1:9                 10 mL                   90 mL
    6%                          1:10.4              8.8 mL                  91.2 mL
    8.25%                       1:14.7              6.4 mL                  93.6 mL
    ====================    ===============     =====================   ========================

Procedure descriptions
----------------------

Through the **instrument tab**, several different user-runnable procedures are listed. From left to
right in the instrument tab, these are:


- **Rinse**: Rinses the sample loop and connecting sample lines with focusing fluid.
- **Sanitize SIP/Sanitize Autosampler SIP**: Washes and sanitizes the Sample Injection Port (SIP) on the Attune
  or on the autosampler. Use this especially after running sticky samples, including the performance beads.
- **Deep clean**: Cyclicly runs Wash solution and 10% bleach through the flow cell and sample lines. This is
  the wash steps done in the shutdown step, without the final flush with shutdown fluid.
- **Startup**: Flushes the shutdown solution from all fluidic lines, replacing it with focusing fluid.
- **Shutdown**: Uses bleach to backflush the flow cell and all sample lines, rinses all lines with water,
  then runs Wash solution and 10% bleach cyclicly through all lines. *Quick* does 5 cycles/10 minutes, *standard* does
  15 cycles/40 minutes, *thorough* does 25 cycles/60 minutes.
- **Debubble**: Clears bubbles in the fluidics lines.
- **Unclog**: Backflushes the sample probe and flow cell.
- **Decontaimate system**: Runs bleach through all backend and frontend fluidic lines. The focusing fluid filters
  must be replaced after decontamination.


Weekly system cleaning
------------------------

The proprietary "flow cell cleaning solution" is actually a `Hellmanex solution <https://www.fishersci.com/shop/products/fisherbrand-hellmanex-iii-liquid-cleaning-concentrate/14385864>`__.
Hellmanex is an alkaline, viscuous detergent for cleaning glass. It can be corrosive to metals; make sure to clean up spills!

1. Dilute 1 mL of Hellmanex with 2 mL of DI water (3 mL total).
2. Run Deep Clean - Standard (40 min) with 1:2 diluted Hellmanex (instead of standard 10% bleach)
3. Run Deep Clean - Quick (10 min) with 10% bleach to ensure that any Hellmanex is flushed out of the system.


.. note ::

    10% bleach or diluted Hellmanex can also be used with the debubble protocol instead of debubble solution to
    clean the flow cell (however, don't expect it to debubble! We just use the debubble procedure because
    it washes and backflows the flow cell). If you use Hellmanex, however, run a debubble with 10% bleach after to flush it out.


Every ~3-6 month system decontamination
---------------------------------------

.. time:: 2.5 hours


   This is not a "fire and forget" protocol; you will have to be actively doing things for nearly two hours!

.. warning::
   The focusing fluid filters must be replaced after decontamination, so ensure we have replacements before beginning!

.. note ::
   The `Attune maintenance manual <../../_static/files/attune_maintenance_guide.pdf>`__ (page 21) is no longer up-to-date
   with what the Attune decon protocol is!

   When in doubt, always follow the on-screen prompts. There is only one divergence from the on-screen prompts that makes
   replacing the focusing fluid filters easier.

.. note ::

   Over the course of the decontamination, all of the fluid is poured out. You may save some of the fluids if they are
   not contaminated, but it is good to fully remove all liquids somewhat regularly to prevent reservoir contamination.

   It is helpful to run the bottles closer to empty before performing the decontamination to waste less fluid.


1. Sanitize

   a. Rinse out the focusing fluid bottles (internal and autosampler) and the shutdown bottle with deionized water.
      Fill the focusing fluid bottles with 500 mL of fresh 10% bleach and fill the shutdown bottle with 100 mL of fresh 10% bleach.
   b. Make sure the wash bottle is filled with at least 100 mL of wash solution.
   c. Ensure all fluid connections are connected securely.
   d. Hit **Next** in the software.
   e. Load a clean, empty tube onto the tube lifter and load a clean 96 well plate into the autosampler.
   f. Hit **Next** in the software to start phase 1.

2. Rinse
   a. Lower the tube lifter, and remove the plate from the autosampler.
   b. Hit **Next** in the software.
   c. Remove all liquids from all fluid bottles. Rinse all with deionized water.
   d. Replace the normal liquids in the fluid bottles.
   e. Hit **Next** in the software.
   f. Replace the focusing fluid filters, as detailed in :doc:`user_replacements`.

   .. note::

      Replacing the focusing fluid filters before reconnecting the bottles, as suggested here, makes your life much easier.

   g. Clean the Attune with ethanol (wipe up any spills inside the cabinet, clean the metal parts, etc).
   h. Replace all bottles and reconnect all fluid connections.
   i. Hit **Next** in the software to start phase 3.

3. Run 3 startup procedures, 2 debubble procedures, and 2 rinse procedures while observing for leaks
   from the newly replaced filters.


Focusing fluid refill
--------------------------

Empty focusing fluid bottles should be kept and placed on top shelf over the attune.
No other bottles should be kept (e.g., throw away shutdown bottles when empty).

.. important ::

    Once you get to the last 1X focusing fluid bottle, follow this procedure so we aren't refilling with contaminated solutions.


1. Rinse sides of bottles with 10% bleach squeeze bottles. Let sit for 15 min.
2. Rinse out bleach.
3. Rinse bottles with Alconox.
4. Rinse out the Alconox with tap *until no more soap*. MAKE SURE NO SOAP REMAINS AND GETS INTO ATTUNE.
5. Rinse bottles with DI water. Let dry overnight.

.. important ::

    Wash large 1X focusing fluid reservoir spigot with Alconox and DI water before using to prevent refilling with contaminated focusing fluid.

6. Refill bottles with 1X fcocusing fluid from the large reservoir using the *clean* spigot.


Full Attune guides
------------------

You can download the `Attune software manual <../../_static/files/attune_software_guide.pdf>`__ or the
`Attune maintenance manual <../../_static/files/attune_maintenance_guide.pdf>`__.