============================
Koch Flow Core FACS Training
============================

Sorting Machines
----------------

There are currently two types of FACS machines available at the Koch Flow Core.

1.  Sony MA-900 (recommended)

     * Easy to use.
     * Doesn’t require extra training on an analyzer.
     * However, the green + red lasers and the blue + far-red lasers are collinear (not spatially separated), meaning if you want to use green with red or blue with far-red at the same time, you will want to learn how to use the compensation wizard.

2.  Aria

     * You need to be trained on an analyzer first, then you can be trained on the Aria.
     * However, lasers are spatially separated like on the Attune.


Training
========

You will need to do several meetings and trainings before you can use the flow core independently, expect it to take a few weeks to get fully trained. The main steps are:

1.	Submit the biohazard form on iLabs
2.	1-hour consultation meeting with Glenn
3.	1-hour startup and QC training
4.	2-hour flow sort training (you need to bring your own samples)
5.	1-hour flow sort with supervision (this can be part of an experiment)


Training Details
~~~~~~~~~~~~~~~~

.. note::
    Much of this training information is also on iLabs or you will hear about it during your consultation meeting with Glenn.

1.	Make sure you have an iLabs account and PO for payment: https://mit.ilabsolutions.com/account/login
2.	In iLabs, under Core Facilities, you can find the Flow Cytometry Core.
3.	Go to Schedule equipment tab.
4.	Fill out the linked biohazard form.

     *	You only need to do this once unless your biosafety requirements change.

5.	Schedule a consultation meeting with Glenn.

     *	1 hour long
     *	Typically M-F from 11am-12pm
     *	Under Staff Calendars for Training and Assisted Work heading, book yourself on Glenn’s calendar.
     *	You will need to know what fluorophores and cell types you plan to use during your training.
     *	He will go over a lot of the information about flow sorting and the flow core.

6.	After the consultation meeting, you will be given access to the instrument calendar to book your training with the staff.
7.	Next you will need to sign up for a time for Startup & QC training.

     *	This is 9-10am W-F on days when someone is signed up to use that FACS machine (which is most days).

8.	Next you will sign up for a 2-hour time block to actually be trained how to sort.

     *	The staff are usually available for training from 10:30am-12:30pm and 1-3pm each day.
     *	Since training takes extra time, it is not recommend to use this time to sort cells for an important experiment since you might not have enough time to sort everything.
     *	You will need the following samples:

         * Unstained - same cell type as samples without any fluorophores. Needed for autofluorescence.
         * Single color - one for each fluorophore in your experiment. Needed for spectral overlap (compensation).
         * FMO - all fluorophores minus one. Important for dim populations and gating.

9.	Finally, you will sign up for a 1-hour assisted sorting. After this, you can sort on your own anytime.

     * If you need to do a longer sort for an experiment, you could sign up for the 1-hour assisted use, then separately sign up for more time immediately after to finish your sort.

Sony MA-900
-----------

The Sony MA900 cell sorter has a `SOP <https://docs.google.com/document/d/1toqMY_qnDy0_YDkcEr2ktDJWcteKe0Pj42_scukqT5s/edit>`__ that you can follow for startup and shutdown.

Startup
~~~~~~~

You only need to start up the Sony if you want to use it over the weekend, on holidays, or outside of normal hours.
During the week, core staff will do the start up in the morning.
The Sony is generally very easy to startup once you've seen how to; you mostly follow automated prompts and switch out the sorting chip. However, the auto-alignment and equivilant of the Attune performance test takes around 45 minutes.

1.	Empty the waste container. Put it in the sink and add 1 bleach tablet. Wait at least 20 minutes before emptying. They have labels to the right of the sink if you want to label with the time.
2.	Refill sheath fluid. Boxes can be found in the closet and on a rolling cart. Ethanol the tip of the tube before putting in the sheath fluid reservoir.

     * Sony 3 rubber O ring often falls off, so be cautious.

3.	Turn on the air (blue valve) if it is not already open, then wait 1-2 minutes.
4.	Open the BSC and turn on Sony with power button.
5.	Log into computer (login info is on the monitor) and open the Sony software.
6.	Select User 1.
7.	Scan chip QR code.

     * Each chip is good for 24 hours, so write time and date on package after opening it.
     * You don’t need to change out the chip if it has been less than 24 hrs since it was opened (e.g. someone used it at 5pm on a Saturday and you are using it at 9am on a Sunday)

8.	Push to open the top of the Sony. Take out the old chip and put new one in. It's like an SD card, so push gently on top of chip and eventually the instrument will pull it in.
9.	Follow prompts on screen.

     * May need to change out tube holder from 15 mL to 5 mL.
     * Beads are run in 5 mL tubes.

10.	Beads are located in the mini fridge near the sink in a brown cardboard box tray.

     * They make new tubes every week.
     * New beads can be found in the white boxes on the right side of the fridge. Make sure the bead lot matches if you get a new dropper bottle.
     * Sony 2 and 3 needs about ~10 drops.
     * Sony 1 needs ~15-20 drops.

11.	Shake the dropper bottle well and vortex tubes before use.
12.	On software during QC, make sure the droplets look good (e.g. no vibrations or fuzzy looking drops).

     * If droplets look weird, you can try a chip exchange and just put the same chip back in. If you do this, you need to skip autocalibration and then calibrate later after the chip exchange.

13.	Sony 2 and 3 takes ~30 minutes to start up, and the Sony 1 takes ~45 minutes to start up

     * The calibration step takes ~20 minutes.
     * You don’t need to include startup time when signing up to sort on weekends/holidays (e.g. don’t pay for startup time).

Sample Prep and Sorting
~~~~~~~~~~~~~~~~~~~~~~~

1. Get ice. Keep your samples on ice as much as possible after dissociation.
2. Dissociate cells using appropriate method. Centrifuge the cells to pellet them.
3. Aspirate the supernatant and resuspend cells in ~5-10 million cells / mL of media.

    .. tip:: Start with resuspending in 0.5-1 mL of media per 6-well. For reprogramming, try 1 mL for proliferative conditions and 0.5 mL for less proliferative conditions.

4. Gather useful items to bring to the sort:

     * Your samples
     * 5 mL round bottom tubes with strainer caps (at least 1 per sample, plus some extra)
     * Collection tubes of appropriate size
     * Extra media if you need to further dilute cells prior to sorting
     * FBS or 5% BSA for collection tubes
     * P1000 pipette with filter tips
     * Gloves
     * Lab markers

5. Head over to the Koch flow core.
6. On the computer, open a workspace for sorting.

     * If you don't have a template yet, you can select **File** > **New** and then Blank or Existing template. If you have sorted before and saved a template, you can import that instead.
     * You can uncheck any unused fluorophores (e.g. FL1 through FL4) if needed. If you need to use the compensation wizard, then you *must* uncheck the unused fluorophores.
     * The 488-nm laser *must* stay on, but other unused lasers can be unchecked. It may be easiest to just keep all lasers on.
     * Click Create Experiment.

7. Set gates by running some of your controls and samples. If needed, start the compensation wizard and run your single color controls.

     * Select begin experiment and start collecting first filtered tube.
     * You can make a new plot from the button in the upper left or by double clicking the gate.
     * As needed, adjust the Gain Settings (voltages) under **Detector & Threshold Settings**.
     * Add sort gates and rename them as needed.
     * The compensation wizard will give you prompts for getting it set up.

8. Place labeled collection tubes (with BSA or FBS) in the tube holder in the collection chamber and close the door.

     * You may need to change the tube holder to fit the tube size you wish to sort into.
     * Vortex your collection tube to allow BSA or FBS to coat the sides of the tube. This is supposed to help with recovery.

9. Under **Sort Control**, click **Load Collection**.

.. tip::
     Remember to click **Load Collection** *before* starting to run your sample.
     If you start running your sample first, you have to stop or pause it, click **Load Collection**, then restart running the sample.
     You can only begin to sort when the collection tube has been loaded.

10. Set the desired settings under Sort Control.

     * **Method** should match the collection tube size.
     * Set the sort **Mode** to your desired option (e.g. Normal, Purity, or Yield). There is a tradeoff between the two (e.g. better purity leads to lower yield and vice versa).
     * Under **Sort Settings**, select the location and gate for each collection tube, and optionally add a stop count. A stop count of 0 leads to non-stop sorting.
     * Also set your desired recording conditions (e.g. stop recording after 100k events). It is recommended to have Auto Record checked.

11. Filter your sample and load tube. Make sure the filter cap is off!
12. Click start and verify your gates.
13. Once the flow rate is stable, click **Sort & Record Start**.
14. You can change the **Sample Pressure** to adjust the flowrate and events/second.

     * Do not go over 5k events/second.
     * AMB recommended to run at ≤2-2.5k/sec for MEFs because he had issues at higher event rates.
     * Sample pressure of 4 is standard.
     * Increasing sample pressure can decrease sort efficiency. Aim for a sort efficiency of 80% or greater.

.. warning::
    Watch out for the event rate suddenly dropping quickly. This can mean the tube is close to running dry which can damage the machine.

    Always keep an eye on sample volume!

1.  If you did not set a stop condition for the sort, once you have sorted the desired number of cells, click Stop.
2.  If you have more samples to sort, click **Next Tube** to create a new sample. You can rename each sample to reflect your condition name.
3.  After you have sorted all your samples:
    
     a. If there is a user signed up after you, run **Bleach Cleaning** (~6 min) and then **DI Rinse** (~6 min) and follow the software's prompts for each step.
        You don't have to stay while the DI Rinse if there is another user after you.
     b. If you are the last user of the day, from the **Cytometer** tab, select **Hardware and Software Shutdown** to start the cleaning wizard.
        Follow the prompts to complete the Bleach Cleaning and DI Rinse. Then select Shutdown to turn off the instrument.

4.  Export your FCS files to the computer. There should be a data folder on the desktop with a folder for each month of the year, and you can add a folder with your name for the month.

     * Right-click on the experiment (at the top of all the tube names) and select **Export as FCS Files**.
     * A PDF of the experiment layout can be saved by clicking **Custom Print** (in **Worksheet Tools** ribbon).
     * To export the entire experiment, go to **File** > **Database**, then click on the experiment you want to export, then on the arrows to move it to the export window on the right.
       This will save the data, plots, and gates into one file.

5.  Optionally, save your workspace as a template for future experiments.
6.  Login and then upload your data and/or template to the Galloway Lab Onedrive under instruments/data/koch_flow_core.

.. note::
    * Each droplet is 1 nL, and you have 2 droplets per sorted cell. (e.g. 100k sorted cells = ~200 µL)
    * Sorting at 5k cells / sec is a safe rate, but you will lose more cells the more you put through.
    * You want your BSA or FBS to be at least 20-30% of the final volume after sorting.
      For example, if you want to sort 300k events, the sorted volume will be ~600 µL, and therefore you want to put ~200-300 µL of BSA or FBS into your collection tube.
    * Don't use a larger collection tube than needed. You can lose cells on the sides of your tube.
    * Leave 1-2 cm at the top of the collection tube to reduce cell loss.
    * The Sony can keep your sample and collection tubes cold, just remember to turn on that feature.
    * Strain cells *immediately* prior to sorting. This prevents clogs. If you get a clog, you can lose all your sorting time.
    * Use polypropylene tubes; this material is less "sticky" compared to polystyrene and can reduce cell loss.
    * DO NOT run the sample tube dry! This will damage the machine!
    * If fluorophores are dim, a live/dead stain is recommended.
    * It takes ~30 seconds from clicking start for cells to begin appearing in plots.

.. tip::
    How long should you sign up for flow sorting?

    Example: I have 6 samples to sort, and I want ~100k sorted cells.
    
    1. Assuming 40% yield (could expect between 30-50%), I want to sort at least 250k events in order to get 100k live cells after my sort.
    2. From my gating, I expect 50% of events to be Live Cells, 90% of those to be Single Cells, and 60% of those to be positive for my fluorophore.
    3. I plan to run at ~2000 events / second. Based on the percentages above I expect to sort ~540 events / second.
    4. Therefore, to collect 250k sorted events, it will take about 8 minutes to run each sample.
    5. For 6 samples, it may take about 48 minutes of just sorting time.
    6. Add on extra time for setting up the workspace, setting voltages and gates, swapping samples, the final Bleach Cleaning and DI Rinse steps, and exporting your data.

Shutdown
~~~~~~~~

Follow the shutdown SOP, with the exception that on step 7 ("Turn off the air compressor and blue switch on the air-line"), 
do **not** turn off the blue switch on the air-line, 
and turn off the air compressor by turning off the power strip that is below you to the left, when sitting at the computer. 
**Do not** turn off the air compressor by turning off the switch on the back of it.
