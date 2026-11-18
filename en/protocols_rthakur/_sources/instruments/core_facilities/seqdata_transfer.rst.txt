
===================================================================
Data Transfer of Sequenced files from BioMicro Center to Supercloud 
===================================================================

FASTQ files for Samples submitted for sequencing at the BioMicro center are stored in the BMC drive Luria. We usually transfer these files to our Supercloud account for processing and analysis. To transfer sequenced files from the BioMicro center to the Galloway Lab Supercloud account, do the following steps. 
    
1.	Log in to your SuperCloud from Terminal. 
2.	Navigate to ``~/galloway_shared/data/NGS_DATA/raw_reads``
3.	Create a folder for your sequenced files in the ``raw_reads`` directory. This is where you’ll copy the sequenced files.
4.	Load and configure Rclone using the following commands:


    .. code-block:: text

        module load ~/galloway_shared/modules/rclone_module
        rclone config

5.	Make sure that ``BMC`` is listed in the current remotes
6.	To begin copying files from BMC, navigate first to newly created folder and use the following command:


    .. code-block:: text

        rclone copy –progress BMC:~/path/to/sequenced_folder/ .

7.	You can do a test run of the copying process by adding in ``--dry-run`` .


    .. code-block:: text
        
        rclone copy --progress --dry-run BMC:~/data/230717Gal/ .

8.	Confirm that the data transfer is successful by checking the accuracy of copied files. 
