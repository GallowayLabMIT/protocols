
===================================================================
Sample Prep and Confocal Imaging at the Koch Microscopy core
===================================================================

This protocol aims to guide users on how to prepare samples for imaging using the Leica Sp8 confocal microscope at the Koch Institute. 
This protocol is only supplemental to the mandatory training provided by KI microscopy core and would only cover important tips and tricks 
learned over trial and error on sample preparation and cell-specific imaging process that have proven to improve the confocal imaging acquisition.

Confocal access and Experimental planning:
------------------------------------------
.. important:: 
    Before starting make sure you have undergone or have requested for training to access the Leica Sp8 microscope. 
    The training will cover mostly the instructions on how to operate the hardware and software components of the microscope, 
    as well as, practical advise on lasers based on your specific fluorophore needs. 

1.	Carefully plan your Fluorophore-conjugated secondary Abs, (for example the Cy7 detection is weak unless your signal is very bright) 
and use no more than 1:10000 for both Hoechst and DAPI for counterstaining, as these channels tends to be very bright.  
If in doubt consult Jeff for Fluorophore-Laser compatibility. 
2.	All cells to be used for  confocal imaging have to be cultured on glass-bottom plates. 
Before plating your cells, try to position them as close to the center as possible, leaving at least 2 outer rows and columns blank. 
If imaging Hb9::GFP cells, have 1 well close to the edge to be used as background control (uninfected, non-treated and unstained). 
This is because Hb9::GFPs tend to be very bright causing halo and grainy effect on higher magnifications, so you need to use this well for black balance correction. 
3.	Make sure you coat the glass bottom plate appropriately (i.e. Laminin - Neurons and Intermediate 4dpi cells, Matrigel- mature neurons, or gelatin- MEFs) 
so that cells will adhere all throughout the fixation, permeabilibilization and washes. 
4.	During storage or transport to KI, always cover the plate with foil and do not let wells dry. 

.. important:: 
    Filter-sterilize the PBS and gelatin to be used to have less debris at high-resolution imaging. 


Confocal imaging 
-------------------

1.	Book a time at iLabs  and take your sample to KI for confocal imaging
2.	Go through the proper log-ins in the Leica computer and turn on the microscope in proper sequence (will be instructed during training). 
3.	Open LasX software, load a configuration (this will be set-up during training) or start a new one, if using different lasers than in your training. 
4.	Once inside the LasX software, navigate to the Acquisition panel on the Left-hand side and make sure to use 1024x1024 Image format and Line average of 2. 
5.	You can switch on the lasers you need (this will be instructed during training) or the lasers are automatically turned on if you’ve loaded a configuration. 
Use only a minimum of 1 for Laser Power during the start-up, this can be modified as needed in Step 9 or with consultation with Jeff.  
6.	Once the lasers are turned on, you can start setting up your plate in the scope. Begin by selecting the desired magnification (I’ve only used 100x) then add 2 drops of Oil into the objective. 
Select the plate adapter for the sample holder (or slide adapter, if needed), then place your plate into adapter. 
Make sure all sides of the plate are evenly pushed into the adapter before plaing it in the microscope. 
7.	Start navigating into your target wells using the joysticks. Use the focus to find an initial Z-stack of cells. 
8.	Go back to the software and press Live at the bottom left. The Image panel on the right should display a Live acquisition of all your target Fluorophores (lasers). 
Don’t worry if nothing shows up right away, this usually takes a few minutes to load. 
9.	Refine the quality of the acquisition depending on your target fluorophore by tuning the Laser Power. Less is always recommended to avoid artefacts. 
10.	To capture several stacks, press Fast Live and navigate to the Z-stack option, turn the Z-stack knob to either direction and Set the start and end-point of the Z-stacks to be captured. 
11.	Press Start to begin Image acquisition. More Z-satcks and channel sequences takes longer time. 

Saving and Export of files
------------------------------
1.	Navigate to the Open Projects Panel in LasX and verify that the image-sets per well that you have acquired are all displayed. 
You can either save all of them in one go or save them individually. 
2.	To save and export, right click either the Entire Project or the Individual image acquisitions and click Export.
 It should redirect you to a file path in the D-drive of the microscopy core, where you can save files in a folder under your name. 
3.	This can later on be accessed and analyzed using one of the Workstations in the Core. 

