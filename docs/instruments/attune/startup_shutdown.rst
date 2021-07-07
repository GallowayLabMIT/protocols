===========================
Attune startup and shutdown
===========================


Quick startup checklist
------------------------------

1. Make sure fluid bottles are full except for waste bottles. If necessary, empty waste bottle and refill with 10% bleach (100 mL for Attune, 200 mL for Cytkick)
2. Fluid lines are all plugged in correctly (especially Cytkick autosampler waste!! should hear double click)
3. Log in and run start up procedure
   
   a. If the Attune has not been run for > 3 days, run another startup procedure to further flush the lines (don't shutdown, just immediately hit startup again).
   b. If the Attune has not been run for > 1 week, run Debubble with the debubble solution.

4. Run performance test
   
   a. Make sure optical filter config is correct (no red-stripes, order is correct)
   b. Verify bead lot number
   c. Put 3 drops of performance beads in 2 mL of focusing fluids (should be ~100 ev/s)
   d. If Delta PMT is high (>10-20), check Attune maintenance guide pg. 41

5. Run SIP sanitize to wash beads out


Quick shutdown checklist
------------------------------------------------

1. Place a clean 96 well plate into the autosampler (or reuse an old plate with no salt crusts - remove with water/toothpick if there is).
2. Empty the waste containers and refill with 10% bleach (100 mL for Attune, 200 mL for Cytkick).
3. Refill the shutdown and wash solution bottles if needed.
4. Fill a clean tube with **3 mL of 10% bleach** and load it into the tube lifter.
5. Run the following depending on how quickly the next user will be using it:
   
   a. *DEFAULT* If next user will be using it > 1 hr, run Shutdown - standard (40 min)
   b. If next user will be using it < 1 hr, run Deep Clean - quick (10 min)
   c. If last user of the day, run Shutdown - thorough (60 min)

6. Log out of the software but do *not* close the software or log out of the INSTR-ADMIN Windows user or shutdown will fail.


Initial inspection and startup
------------------------------

.. time:: 30 minutes

1. Visually inspect the Attune.

   a. Check the main fluidics syringe for the presence of a salt ring.

   .. figure:: img/attune_syringe.jpg
        :align: center
        :height: 5cm

        A normal syringe without salt ring. The salt ring would be visible at the bottom
        of the syringe travel, e.g. near the printed label.

   b. Check the internal and external fluid bottles for any leaks or salt residue. Clean up any
      salt residue with ethanol and a Kimwipe.
   c. Check that other components are in good order (focusing fluid filters, SIP, etc).

.. warning::
    
    Always grip fluid bottle and data connections by the connector, e.g. as close to the connection as possible.
    This prevents stress on both the fluid and data lines!

2. Check that all internal fluidics bottles except waste are reasonably full. 

   a. If the waste bottle needs to be emptied, empty it into the sink, and refill with **100 mL of 10% bleach**.
      See :doc:`attune_operation` for definition of 10% bleach.
   b. The focusing fluid bottle can be refilled by **carefully** moving the focusing fluid bottle forward
      just enough to be able to take the cap about, without disconnecting the fluid or data lines.

   .. figure:: img/refill_focus_fluid.jpg
        :align: center
        :height: 5cm

        The focusing fluid bottle can be moved slightly out for refilling without
        stressing the fluid or data line.

   c. If disconnecting fluid bottles, the connectors have disconnect "buttons" that must be pressed Before
      disconnecting the bottle. After pushing the disconnect button, carefully remove the line, gripping 
      at the **connector**, not the fluid line itself to prevent putting stress on the system.
   d. If a fluid line does not reconnect with a click sound, do not force the connection. Check to make sure
      the instrument-side connector has not been tripped. If it has, press down on the top connector button
      to reset.
    
.. figure:: img/attune_connector_reset.png
    :align: center
    :height: 4cm

    Visual appearance of tripped and normal connectors.

3. Check that the autosampler focusing fluid bottle is full and the waste bottle is empty.
 
   a. The focusing fluid bottle has a single click lock.
   b. The waste fluid bottle requires a double "click" for locking purposes.
   c. After emptying the waste bottle, fill with **200 mL of 10% bleach**.

4. If the instrument is off, turn on the Cytkick first, wait ten seconds, then turn on the Attune.
5. Remove all plates from the Cytkick.
6. Login to the **INSTR-ADMIN** user, start the software, then login to your specific software user.
7. Run the startup procedure.

   a. If the Attune has not been run for > 3 days, run another startup procedure to further flush the lines.
   b. If the Attune has not been run for > 1 week, run Debubble with the debubble solution.

Performance test
----------------

.. time:: 10 minutes, run before the first flow run of the day.

1. Open the top of the Attune, to check the optical filter setup. Replace any red-stripe filters with their
   stock filters.

2. Click the performance test button in software.
3. Verify the bead lot # of the performance beads.
4. Add 3 full drops of performance beads to a new, clean tube. Dilute with 2 mL of focusing fluid.
5. Run the performance test. In the first part of the performance test, the events per second should be
   near 100 ev/sec.
6. After performance test, wash the beads out of the sample loop by running **SIP sanitize**.


================= ===========================
Delta PMT         Status
================= ===========================
> 10                   Run Cleaning
> 20                   Indicates an issue
> 50                   Performance will fail
================= ===========================


.. important ::

    The bead lot number changes roughly every four years and requires a new set of parameter files to be downloaded.

    Bead lot changes also requires a new baseline reference to be set.

    Instructions for the install/baseline reference and bead lot data files can both be downloaded from
    `ThermoFisher <https://www.thermofisher.com/order/catalog/product/4449754>`__.

Shutdown
--------

.. time:: 30 minutes total, ~2 minutes hands-on time.

1. Place a clean 96 well plate into the autosampler. If reusing a shutdown plate, make sure there are no salt
   crusts in wells; if so, they can be removed with a toothpick and water.
2. Fill a clean tube with **3 mL of 10% bleach** and load it into the tube lifter.
3. Empty the waste containers, refilling the shutdown and wash solution bottles if needed.
4. Run a **thorough shutdown** if this is the last run of the day. If it is going to be > 1 hour before
   the next user, run a **standard shutdown**.
5. Once the shutdown is started, you can log out of the software (but do *not* close the
   software or log out of the INSTR-ADMIN Windows user!).