=================
Attune operation
=================


.. note::

    "10% bleach" refers to a final concentration of 0.525% sodium hypochlorite (5250ppm chlorine).
    Use ELGA water to dilute instead of DI water to dilute the bleach. 

    This was originally a 10x dilution of 5.25% sodium hypochlorite bleach, but in lab we typically
    stock higher concentration bleach.

    ====================    ===============     =====================   ========================
    Concentration           Dilution            Vol bleach (100mL)       Vol ELGA water (100mL)
    ====================    ===============     =====================   ========================
    5.25%                       1:9                 10 mL                   90 mL
    6%                          1:10.4              8.8 mL                  91.2 mL
    8.25%                       1:14.7              6.4 mL                  93.6 mL
    ====================    ===============     =====================   =========================

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

1. 1 mL of Hellmanex with 2 mL of DI water.
2. Run Deep Clean - Standard (40 min) with 1:2 diluted Hellmanex (instead of standard 10% bleach) 
3. Run Deep Clean - Quick (10 min) with 10% bleach to ensure that any Hellmanex is flushed out of the system.


.. note ::

    10% bleach or diluted Hellmanex can also be used with the debubble protocol instead of debubble solution to
    clean the flow cell (however, don't expect it to debubble! We just use the debubble procedure because
    it washes and backflows the flow cell). If you use Hellmanex, however, run a debubble with 10% bleach after to flush it out.


Every ~3-6 month system decontamination
---------------------------------------

See page 21 in the `Attune maintenance guide <../../_static/files/attune_maintenance_guide.pdf>`__ for full details.

1. Remove liquid from all fluid containers. These can be poured out into clean glassware or plastic for reuse (as long as they
   are not visibly contaminated).
2. Rinse all fluid containers with deionized water, reconnecting them to the system while empty.
3. Click decontaminate system to start decontamination phase 1 (backend fluidics bleach flush)

   a. Fill both the internal and external focusing fluid bottles with **500 mL of 10% bleach** each. Leave all
      other bottles empty!

4. Click next to start phase 2 (user fluidics bleach flush)

   a. Load a clean 96-well plate into the autosampler. Load a clean empty tube onto the tube lifter.

5. Click next to start phase 3 (water rinse)

   a. Empty all fluidics bottles, rinsing with DI.
   b. Fill both the internal and external focusing fluid bottles with **500 mL of DI** each.
   c. Reconnect all lines.
   d. Load a clean empty tube onto the tube lifter.

6. Click next to start phase 4 (filter replacement, return to system fluidics)

   a. Replace the focusing fluid filters, as detailed in :doc:`user_replacements`.
   b. Remove, empty, and rinse all fluidics bottles with DI.
   c. Refill all bottles with proper solutions.
   d. Reconnect all lines, then remove the tube from the tube lifter and the plate from the autosampler.

7. Run 3 startup procedures, 2 debubble procedures, and 2 rinse procedures while observing for leaks
   from the newly replaced filters.


.. important ::

    Do this whenever the 1X focusing fluid bottles need to be refilled so we aren't refilling with contaminated solutions.


Full Attune guides
------------------
You can download the `Attune software manual <../../_static/files/attune_software_guide.pdf>`__ or the
`Attune maintenance manual <../../_static/files/attune_maintenance_guide.pdf>`__.