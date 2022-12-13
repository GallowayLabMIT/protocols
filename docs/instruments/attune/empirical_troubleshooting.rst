======================
Attune troubleshooting
======================

The following troubleshooting tips and explanations are a result of empirical
observations and discussions with our support engineers. Additional troubleshooting
is available in the `Attune maintenance manual <../../_static/files/attune_maintenance_guide.pdf>`__.

Delay before events start running
---------------------------------
If you notice that there is a delay before events appear,
but the events appear normal (e.g. there isn't a clog), check
that the thumbscrew and screw at the top of the main sample syringe
are fully tight. You can add about a quarter-turn if they are loose.

**Explanation:** The main sample syringe is responsible for pushing liquid,
including your sample, through the fluidics system. If the two screws
that attach the servo motor to the syringe are loose, then when the servo
motor initially starts moving, that motion instead goes towards the slop
in the system and the main syringe doesn't start moving until after a delay.

This delay actually affects any procedure that starts from the fully-down
syringe position, but is most noticeable when capturing events. The delay
is not harmful in any way.

Fluid leak from the autosampler SIP onto a running plate
--------------------------------------------------------
First, take the plate out and clean up the spilled liquid.
Carefully, **while the Attune is idle or off**, you can open
the autosampler door and clean up any spilled liquid with a
paper towel.

Then, ensure that the two waste bottle connections are fully
connected. Make sure you re-seat the autosampler waste bottle connection
unti you hear **two clicks**.

**Explanation:** The autosampler fluidics are relatively simple.
The autosampler syringe directly pulls focusing fluid from the
autosampler focusing fluid bottle to use as sheath fluid. After
aspirating a sample, the sample syringe is actually *pushing*
fluid through the system to move your sample into position, with the
excess fluid "in front" of your sample redirected into the waste bottle.

If the autosampler waste bottle is not fully connected, you instead end
up with the syringe trying to push against a closed connection, which leads
to high backpressure. The fluid goes through the easiest escape route,
which is back out of the SIP onto your plate :(

Wells skipping and the autosampler fails to draw focusing fluid
---------------------------------------------------------------
If you directly observe that fluid is not successfully being taken up
by the autosampler syringe, or you observe that no events happen or
wells get entirely skipped, the autosampler is likely not taking up
focusing fluid correctly.

Check that the autosampler focusing fluid bottle connection is fully seated.
Also check that the autosampler waste bottle connection is fully seated (two clicks
on insertion).

**Explanation:** The syringe has to be able to hold suction. A leak on the focusing
fluid bottle side will prevent the syringe from getting fluid in (unless you elevate
the focusing fluid bottle). A not fully connected waste line will cause pressure
to build up in the system and prevent it from working.