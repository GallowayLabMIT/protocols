=====================
CellBaum User's Guide
=====================

A practical guide to CellBaum for those who want to live track cells but know absolutely nothing about computers.

.. note::
    You can use CellBaum either on your computer or the MIT Supercloud.

Local Usage
===========

Getting started
---------------

1. Follow Chris's instructions for getting CellBaum set up on your computer and update this protocol with those instructions. (I don't remember how to do this - I think you need to clone the CellBaum repository or something?)
2. Make sure you have CellProfiler and Fiji installed on your computer.
3. Download all the timelapse images to your computer so they can be accessed quickly. This can be done by right clicking on the folder and selecting "Always keep on this device".
   After you are done analyzing the images you can remove them from your computer by right clicking on the folder and selecting "Free up space".
4. Complete the cellbaum_config.yml file for your specific experiment. This can be done using VS Code. See more detailed instructions below.
5. Open up a terminal in the CellBaum folder. You may open the terminal using VS Code.
6. Activate the virtual environment by typing conda activate ./cenv in the terminal::
        
        conda activate ./cenv

7. To do a dry-run the CellBaum pipline, type snakemake - -dry-run in the terminal. This is to double check that everything is configured correctly::

        snakemake --dry-run

8. To run CellBaum, type snakemake into the terminal. To assign a set number of cores on your computer, add the -j# flag after snakemake. For example, to use 7 cores on your computer to run CellBaum, type snakemake -j7::

        snakemake -j7

9.  Let CellBaum run. This may take many hours. The typical order of jobs is:
   
   1. folder merging (if needed, e.g. you stopped and re-started the timelapse)
   2. grayscaling
   3. find focus (if z-stacking was used)
   4. stitching (if stitching was used)
   5. run Cell Profiler pipeline to collect cell data and locations (nuclei_masking.cppipe)
   6. btracking (for more information on Bayesian Tracking see `GitHub <https://github.com/quantumjot/BayesianTracker>`_ and their `User's Guide <https://btrack.readthedocs.io/en/latest/>`_)
   7. Add cell data to HDF tracks file


.. tip::

  If you want to stop CellBaum from running, hit ctrl+C while in the terminal and CellBaum will stop running after it finishes all the jobs it is currently running.
  
  If you are too impatient to wait for CellBaum to finish running or it is stuck on the btracking step, you can kill the terminal.
  However, if you kill the terminal, you will need to unlock it before you can run again::

    snakemake --unlock

  You may also need to use the rerun-incomplete flag after unlocking if you stopped CellBaum partway through a job such as grayscaling::

    snakemake -j7 --rerun-incomplete


CellBaum Config File
--------------------

If you have not completed a config file previously, copy the cellbaum_config.yml.template file and remove ".template" from the file name. This will be your config file.
If you have a previous config file, you may simply edit that one.

Complete the config file with the following information:

* directories

  * Put the path on your computer to each item.
  * data_dir = Keyence data folder
  * cp_dir = CellProfiler app
  * fiji_dir = Fiji app
  * pipe_dir = pipeline for CellBaum (in CellBaum repository)
  * output_dir = where you want to save all output files
  * log_dir = where to save logs, usually this can be in an output_dir/Logs folder
  * cell_config = btrack config file, under the models folder in CellBaum repository
  * See examples below::
  
        data_dir: C:\Users\ChemeGrad2020\Massachusetts Institute of Technology\GallowayLab-Timelapse - Brittany\2022.12.16_Hb9-Activation\
        cp_dir: C:\Program Files\CellProfiler
        fiji_dir: C:\Users\ChemeGrad2020\Documents\Fiji.app
        pipe_dir: C:\Users\ChemeGrad2020\Documents\GitHub\CellBaum\cp_files
        output_dir: C:\Users\ChemeGrad2020\Documents\CellBaum_Analysis\2022.12.16_Hb9-Activation
        log_dir: C:\Users\ChemeGrad2020\Documents\CellBaum_Analysis\2022.12.16_Hb9-Activation\Logs
        cell_config: C:\Users\ChemeGrad2020\Documents\GitHub\CellBaum\models\cell_config.json

* folder_merging_needed

  * false if all your images are in a single folder from the Keyence
  * true if you need to merge two or more folders, for example you re-started the timelapse on the Keyence.
  * If true, you must include list under folders_to_merge

* gray_channels

  * list of channels you want to grayscale and which grayscale method to use.
  * 'max' uses the RGB channel in which the maximum pixel value occurs (I think)
  * 'avg' uses the average of all three RGB channels (I think)
  * using a list of 3 ratios lets you choose the weight of each RGB channel (I think)
  * For example::

        gray_channels:
            CH2: max
            CH3: max
            CH4: avg
            Overlay: avg

* focus_finding_needed

  * True if you used z-stacking during your timelapse.
  * If true, you also need to include focus_channels.

* image_regex

  * A regular expression that extracts data from image names such as time, well, stitching position, z-stack, and channel.
    You can check if your regular expression fits your file names using https://regex101.com/. For example, your regular expression could be::

        image_regex: (?P<prefix>.*)_(?P<time>T\d{4})_(?P<well>XY\d{2})_(?P<position>\d{5})_Z(?P<stack>\d{3})_(?P<channel>.*)\.tif

* focus_channels

  * List of channels for which you want to find the most in-focus z-slice. For example::

        focus_channels:
         - CH2
         - CH3
         - CH4
         - Overlay

* example_image_name

  * An example name of your image to check your regular expression above. You can just copy paste a file name of an image from your data folder::

        example_image_name: 10x_T0001_XY01_00001_Z001_CH2.tif

* pre_stitch_correction_needed

  * True if you want to make some kind of correction to your images before stitching.
    For example you could apply a threshold filter to the image and reduce noise.
  * If doing pre-stitch corrections, you will need to update the img_processing.cppipe in CellProfiler to make the desired pre-stitch corrections to your images.

* stitching / prefix / template

  * Needs to be included if you used stitching during your timelapse.
  * grid_width and grid_height are how many images are in each dimension of your stitching grid.
  * Prefix is a list of which channels you want to stitch.
  * Template is which channel in the list you want to use as a template (zero indexed!). It is probably best to use a channel with the most "information" as a template.
  * Example usage::

        stitching:
            grid_width: 3
            grid_height: 4
            Prefix: 
            - CH2
            - CH3
            - CH4
            - Overlay
            Template: 3

* minsize/maxsize

  * The expected minimum and maximum size of objects/nuclei being tracked (pixel diameter). For example::

        minsize: 7
        maxsize: 45

* Update_method

  * Which method to use when tracking objects (EXACT or APPROXIMATE).
    It is recommended to start with the default EXACT. This option considers all possible combinations of linking objects, so it can be slow for very large datasets.
    If there are issues converging to switch to APPROXIMATE.
  * In general, for cell datasets with <1000 cells per time point we recommend EXACT. If you have larger datasets, we recommend APPROXIMATE.
  * Example usage::

        Update_method: APPROXIMATE

* Max_search_radius

  * The maximum search radius for the tracking algorithm in isotropic unit of the data. This parameter can be used to prevent very large displacements when linking objects.
  * Example usage::

        Max_search_radius: 100

* Volume

  * An estimate of the dimensions of the imaging volume, used to define the edges of the field of view for generating hypotheses and labeling tracks as lost.
  * This is pretty much the dimensions of the stitched images in pixels.
  * It is recommend to use 'auto' which automatically calculates these values based on the size of the images.
  * Example usage::

        Volume: auto

  * OR::

        Volume:
            x: 
            - 0
            - 4577
            y: 
            - 0
            - 5427
            z: 
            - 0
            - 2

* Step_size

  * Not really sure what this does. It doesn't seem to affect anything. You can just put like 100 or something::
  
        Step_size: 100

* CP_Data_Keep

  * List of which CellProfiler data to keep, or you can just put 'all' for simplicity::
      
        CP_Data_Keep: 'all'

* time_interval_to_track

  * This feature is useful if the btracker isn't converging you want to change the parameters in the btracker config file (models/cell_config.json).
  * Choose which time points to track. For example, if you have 181 time points and you want to see if you can get it to converge on the subset of time points from 0 to 50 you could put::

        time_interval_to_track:
            min: 0
            max: 50


Getting the btracker to Converge
--------------------------------

The best way to make sure CellBaum will converge is by carefully choosing the conditions of your timelapse. Two recommendations are:

1. Adding a population of dark cells and/or seeding cells sparsely will help with tracking. Many tracking issues are due to simply way too many cells in the field of view.
2. Imaging more frequently can help when cells move around a lot. However, you may start worrying about photo bleaching or computer storage space restrictions if you image too frequently.


Ensure your nuclei masking pipeline works well with your stitched images.

* It is required that you always re-do the CellProfiler pipeline nuclei_masking.cppipe for your specific images AFTER they have been stitched.
* You will probably need to stop CellBaum partway through in order to update the pipeline and use stitched images.
* Stitching will affect the RegEx used in your CellProfiler pipeline.
* You may use different channels between experiments, nuclei will be different size ranges, there may be weird background luminance, etc.


Change the btrack model parameters (models/cell_config.json)

* You can read more about the btrack config models `here <https://btrack.readthedocs.io/en/latest/user_guide/configuration.html#>`_.
* The output of the tracking is very sensitive to the choice of parameter values. The global optimization step can take a very long time to complete if you have a poor choice of model parameters.
* Changing the Motion Model probably won't help much.
* Brittany has found that increasing the values for lambda_link and lambda_branch helped most with converging.


MIT Supercloud Usage
====================

Getting Access to the MIT Supercloud
------------------------------------

1. Follow the directions `on the MIT Supercloud website <https://supercloud.mit.edu/requesting-account>`_ for getting access to the MIT supercloud.
2. First you will need to fill out the Account Request Form.
3. Then you will need to send an email to supercloud@mit.edu and CC Katie.
4. Then you might have to do some other setup stuff. Ask Chris for help and then add those instructions to this protocol.

.. hint::

    You may use this as a template for your email:
    
    Hello,

    I have submitted an account request form so I can get access to the MIT Supercloud for my research project. I will be using the Supercloud to analyze and generate data from time-lapse microscopy images. I have Cc’d my PI, Katie Galloway, so she can confirm that I will need access for my work.

    Thanks,

    Tony Stark


Upload Timelapse Files from the Keyence to the Supercloud
---------------------------------------------------------

1. Open a terminal **in your Keyence Timelapse Ondrive folder** (shift + right click then choose Open Terminal).
2. Use rclone to copy your experiment folder to the supercloud. Rclone uses the following command to copy files::

    rclone copy (--dry-run) (--progress) source:sourcepath dest:destpath

3. It is recommended to first do a dry run to ensure everything will transfer correctly::

    ~/downloads/rclone-v1.60.1-windows-amd64/rclone-v1.60.1-windows-amd64/rclone.exe copy --dry-run 2022.12.16_Hb9-Activation supercloud-blende:/home/gridsan/blende/galloway_shared/data/2022.12.16_Hb9-Activation

4. Then when you are ready to transfer the files, include the progress flag to see upload progress::

    ~/downloads/rclone-v1.60.1-windows-amd64/rclone-v1.60.1-windows-amd64/rclone.exe copy --progress 2022.12.16_Hb9-Activation supercloud-blende:/home/gridsan/blende/galloway_shared/data/2022.12.16_Hb9-Activation


.. note:: 

    rclone is safe to interrupt at any point.

    On the Keyence computer, rclone isn’t in the Path, so you need to do the whole path for rclone.exe in the Downloads folder.

    Remember to include add supercloud-blende: (or your equivalent) before the dest path to specify you are using a remote path.

    It can take several hours for all the files to transfer to the supercloud.


Using the MIT Supercloud
------------------------

1. Open powershell.
2. In the terminal type::

    ssh supercloud

3. You may need to type your password. If you don't want to type your password every time you can use ssh-add to use an agent to control authentification.
4. Navigate to the CellBaum folder::

    cd ~/galloway_shared/CellBaum

5. Do a git pull to update CellBaum::

    git pull

6. If you have your own branch in CellBaum, switch to your branch. For example::

    git checkout KTRs

7. Update the supercloud_config.yml file for your specific timelapse. You can update the file in VS Code on your computer, push it to GitHub, and then do git pull on the supercloud. Or you can use nano::

    nano supercloud_config.yml

8. You might also need to update the snakefile to use the supercloud_config.yml instead of the cellbaum_config.yml file::

    nano snakefile

    # Then change

    configfile: "cellbaum_config.yml"

    # to

    configfile: "supercloud_config.yml"

9. Update any CellProfiler pipelines that are used. You can copy files to the supercloud via `scp <https://supercloud.mit.edu/accessing-and-transferring-data-and-files>`_, or you can git push the file from your computer and then git pull from the supercloud.

10. To run CellBaum you need to run the submission bash script::
 
     LLsub sub_script.sh

11. To see what is running, you can type::
 
     LLstat

12. When you want to leave the supercloud, just type exit::

     exit

13. You can view the files on the supercloud using the Powershell and ls. Or you can log into the online web portal: https://txe1-portal.mit.edu/


Supercloud Config
-----------------

This config file is virtually the same as the cellbaum_config.yml file, except you will want to change all the directories to locations on the supercloud. For example::

    data_dir: /home/gridsan/blende/galloway_shared/data/2022.12.16_Hb9-Activation/2022.12.16_Hb9-Activation
    cp_dir: /home/gridsan/blende/galloway_shared/cluster_infrastructure/conda_envs/cellbaum/bin/
    fiji_dir: /home/gridsan/blende/galloway_shared/bin/Fiji.app
    pipe_dir: /home/gridsan/blende/galloway_shared/CellBaum/cp_files
    output_dir: /home/gridsan/blende/galloway_shared/data/2022.12.16_Hb9-Activation/CellBaum_results
    log_dir: /home/gridsan/blende/galloway_shared/data/2022.12.16_Hb9-Activation/CellBaum_results/Logs
    cell_config: /home/gridsan/blende/galloway_shared/CellBaum/models/cell_config.json


Data Analysis
=============

To add later

How to open HDF files and understand LBEPR format.