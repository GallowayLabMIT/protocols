=============
Virus safety
=============

The highest hazard that we have in lab is likely human-infectable lentiviruses. The lentiviruses we make are
*replication-incompetent*, e.g. they do not make more virus after they infect, but they can still be dangerous
for two reasons:

1. Insertional mutagenesis: even a benign GFP is bad for you if it randomly inserts into a key gene and causes cancer.
2. Oncogene expression: expressing known oncogenes from your constructs can cause cancer. Known or suspected oncogenes
   made in human-infectable lentiviruses falls under BSL2+. Only graduate student and postdocs that have done the special
   BSL2+ training are allowed to work with these.

Other virus types are also potentially hazardous if they express oncogenes, even if they are non-integrating like AAVs.
The following still applies in those cases!

Control methods
===============

Elimination/Mitigation
----------------------
The easiest way to not be exposed to a human-infectable virus is to not make viruses! There are other integration techniques,
such as PiggyBac/transposon-insertion which may be suitable for your process.

Substitution
------------
If you need to make virus, we can reduce the hazard by using more modern viral vector systems or by reducing tropism.

We do this in two ways. First, we can use third-generation lentiviral vectors (which separate viral genes
across multiple plasmids *and* have self-inactivating LTRs.) which makes it less likely that inserted DNA can be re-recognized
via the LTRs. Second, you can use a different envelope plasmid. The VSVG envelope has broad tropism; it infects human cells,
mouse cells, and so on. If you are only targeting mouse cells, you can make virus in PlatE cells, which have a different
envelope that does not infect human cells.


Engineering controls
____________________
The key way that we separate virus particles from us using engineering controls is working with our equipment safely.
There are three main ways we do this:

1. Only do work in our BSCs, and work with the sash at the right height.
2. Only spin down cells in the virus centrifuge, and use the centrifuge caps when spinning.
3. Do not use sharps (or *glass aspirator pipettes*) when working with virus. If you think it is necessary
   to use sharps or glass, make sure you have a safety discussion.

PPE
---
When working with virus, we use disposable sleeves and double gloves. The proper order to put on your PPE is
first, your lab coat, then your first pair of gloves, then sleeves, then the second pair of gloves.

You can reuse your sleeves through a whole virus production, but **only** if you check for any droplets. Swap
sleeves if you got virus on your gloves, as the sleeves may be contaminated.

Virus protocols
===============
We have specific virus procedures in place, which change the way that we work in TC to protect us.
You should treat virus-infected cells or media using virus protocols until **both** two days and three media changes
have passed.

Specific protocols are:

Virus BSC setup
---------------

.. important::

    The **most important** rule to follow when doing virus work is **double glove and use sleeves**
    and 
    **never take your hands out of the BSC** until you have removed your second layer of gloves.
    If you forget something and need to exit the BSC to grab it, do a glove change.

1. When starting up your BSC hood to do virus work, make sure that you have enough seriological pipettes,
   tips, and other plastics. You want to make sure that you don't have to take your hands out. Add them
   now if needed.
2. Add a secondary plastic bag to the waste container, to catch any liquid on tips or pipettes.
3. Make sure that you have all of the plates, tubes, filters and other things that you need. You may want to
   do the gelatin coating before you add any virus to your hood.
4. Make sure you have enough media in the hood. You may want to aliquot out of your 500mL container.

Virus BSC cleanup
-----------------
1. For any liquid waste you have not aspirated (e.g. 10cm dishes you are done with), use a seriological
   pipette to add bleach to any waste plates/containers/tubes.
2. Spread the waste out slightly so all waste will get UV'd.
3. Remove your second pair of gloves, putting them in the biotrash container.
4. Remove any non-waste cells, collected virus, small molecules, etc from the hood
   (you may put on a fresh second pair of gloves, but the outside of these tubes should not be contaminated)
5. Leaving all trash inside, close the sash on the BSC. Set a fifteen minute alarm!
6. Fifteen minutes later, with full PPE (double gloves and sleeves), open the hood again.
   Aspirate bleached liquid waste, finish with another bleach rinse of the aspirator,
   and collect all trash. Take the trash bag out and throw it in the red waste containers.
7. Spray Preempt on the surface of the BSC. Wait one minute or longer, and then wipe up the Preempt by spraying ethanol.
   on the surface. Once the surface is looking nice, close the hood.
8. The hood is usable after the second UV cycle!

Exposure plan
=============
Our PPE and processes mean that it should not be possible to get virus-containing droplets on your skin
without needlesticking yourself, and it should not be possible to needlestick yourself if you do not use glass
or sharps when working with virus.

However, it is still possible that an exposure happens, especially if e.g. you have a pre-existing cut on your hand.
Simply having virus-containing media on unbroken skin is not a large concern, though you can and should discuss this
with a doctor if e.g. the virus was BSL2+ or if you are otherwise worried.

The main treatment is a 28-day course of HIV post-exposure prophylaxis drugs that interfere with lentivirus
retrotranscription, among other things. This is a prescription drug, so you are going to urgent care / somewhere else
to get it proscribed, then getting it from a pharmacy.

Lentiviruses are generally poor at infecting humans, even with direct puncture wounds (<20% of needlestick incidents
directly with HIV lead to infections). The post-exposure drugs are *very effective* if started within 3 days (ideally within 3-6 hours),
dropping this number to effectively 0%.

If you believe that you are exposed, you should:

1. Make sure the BSC is in a safe state, e.g. nothing in precariously perched on something else.
2. Wash your hands and/or the exposed area of skin for ten to fifteen minutes with bleach.
3. If possible while washing your hands, inform someone else in lab to contact.
   
   a. the EHS rep, Katie, or Brian Smith, to kick off the paperwork side of things. Do not worry about this paperwork now
      if you can't reach these people, it's not your job to deal with it.
   b. Anyone, to contact MIT Medical urgent care (617-253-1311) if inside business hours (8am-8pm M-F, 10am-4pm on weekends)
   c. If outside of business hours, any other urgent care that is open (or ER if everywhere is closed).

4. Tell the doctor that you were exposed to an HIV-derived lentiviral vector, and how you were exposed. If the virus
   was BSL2+, tell them that the vector encodes for an oncogene.
5. The prescription should be covered under even the base insurance that all students get.
6. Follow up with other people in lab to handle e.g. paperwork filling, finishing cleaning out the BSC, and so on.


Lessons learned from incidents
==============================

Spilled virus incident
----------------------

While a former member of the lab was filtering a human-infectable lentivirus encoding for a fluorescent protein, 
too much pressure was applied on the syringe. Their hold on the syringe slipped, and knocked over the tube containing
the filtered lentivirus. Most of the lentivirus-containing media stayed within the BSC, though some was knocked onto
the person's lab coat, around the mid-chest area.

**Response:** The person carefully removed their PPE, washed their hands, and asked other people in lab for advice.
Due to good PPE use and protocols, all virus-containing media ended up only on PPE, and the person decided that medical attention was not needed.

Katie filled out the incident paperwork. The lab coat was soaked in bleach and Preempt and sent out for laundering
after being decontaminated in lab.

**Lessons learned:** When filtering virus, if the filter gets too clogged with cells or other debris, it can be hard
to apply enough pressure to filter the virus. If this happens, you can transfer the remaining virus to filter back
into a separate tube, and use a second syringe. Do not apply more force than you can control.
