
===================================================================
Image analysis using the KI workstation - Nemo
===================================================================

.. important:: 
    Before starting make sure you have been trained by the core staff about Workstation access. 
    This protocol is supplemental only to training provided by the core staff, and aimed maily for basic 3D reconstruction using Z-stack images. 
    More advanced analysis can be consulted from the core staff. 
    
This protocol aims guide users how to perform basic image processing, specifically 3D reconstruction from Z-stacks, using softwares installed at the KI Microscopy core workstation – Nemo. 
At the time of my training, this workstation has 3 different softwares installed: Fiji, LasX and Imaris. 
All images acquired in Lecia Sp8, can be processed and analyzed by either of 3 softwares, 3D reconstruction from Z-stacks can be done better using LasX (Leica software) and Imaris. 
For simplicity, I've used the LasX 3D function to acquire Volume data, but use Imaris 3D visualization function for the representative reconstructed images. 

LasX 3D Image Viewer 
---------------------------------------

1. Log-in to the Workstation with your MIT credentials. 
2. Access the images acquired in Leica Sp8 by navigating into the D- drive.
3. Double click on your Project. It should automatically open in the LasX software (the same software used for Image acquistion in the Sp8).
4. On the Left-hand side, you can see your Project acquisitions, with the subfolders of the different wells you imaged. Click on the desired "condition" or "well" to display the acquired images and stacks in the viewing panel. 
5. Select on the image displayed on DAPI or Hoechst channel and click the Browse Workflow. Under this, you can click the "Z" tab. Check to make sure it is displaying all the stack that you've captured. 
6. On the Tool list, select 3D model. Adjust the parameters of 3D options accordingly. A preview will be display on the right-hand side. 
7. Once statisfied with the 3D model, you can click on the Measurement tab to obtain 3D metrics including Volume. 


Imaris 
--------

Imaris software is handy to use for obtaining the representative 3D image because it has a built-in function that can focus on only 1 nucleus per field.

1. Open the Imaris software and stage your LasX project. This has ``.lif`` file extension and you need to convert this to Imaris file extension ``.ims``. 
2. Once converted, you can double click to open into Imaris.
3. The loaded image is automatically Rendered in 3D, focus on the nuclei that you want to represent and crop around it. 
4. The cropped image will dislay the metrics such as Volume and Area which you can confirm from the data measured from LasX software. 
5. The displayed image can be saved as .png using the Export button. 
6. The 3D reconstructed image using Imaris is used mainly for representative image visualization and not for data processing. 
