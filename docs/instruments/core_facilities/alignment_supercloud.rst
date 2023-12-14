===========================================================
Running Genomic pre-analysis using SnakePipes in Supercloud
===========================================================

We have snakePipes module set-up in the Galloway Supercloud account. 
To read more: https://snakepipes.readthedocs.io/en/stable/. 
This protocol aims to guide the user how to create an alignment script using the SnakePipes module and instructions on running it in Supercloud. 

1.	Log in to your SuperCloud from Terminal. 
2.	Navigate to ``~/galloway_shared/data/NGS_DATA/raw_reads`` and confirm the path to the FASTQ files that you intend to analyze. 
3.	Go back to your local directory and create a bash script using


    .. code-block:: text

        vim alignment.sh

4.	 Type the following lines into the bash script, and don’t forget to modify the directory paths, organism genome , Read_1 and Read_1 extensions , accordingly.
    
    
    .. code-block:: bash

        #!/bin/bash
        # SBATCH --output=snakePipes-%j.txt
        # Loading the required module
        source /etc/profile
        module load anaconda/2023a
        # Activate local conda module
        eval "$(conda shell.bash hook)"
        conda activate /home/gridsan/groups/galloway/conda_envs/snakepipes
        ## SnakePipes for DNA mapping command ##
        DNA-mapping -i ~/galloway_shared/data/path/to/FASTQ_files -o ~/galloway_shared/data/path/to/output_files -v --ext ".fastq" --reads '_1_sequence' '_2_sequence' mm10_gencodeM19 

5.	Save and exit from script by pressing ``:wq`` . You can always open and edit the script using ``vim alignment.sh``
6.	To run the script in Supercloud, you need to submit to SLURM via LLsub (See Supercloud user guidelines ) using the following command: 
    .. code-block:: text
        LLsub -i alignment.sh
7.	Once submitted, you can check the status of the run via ``LLstat``. To verify the success/failure of the run, you can check the log ``file—alignment.sh.logXXXXX `` for more details. Usually the log file contains the progress of the alignment run and/or the details if the alignment failed. 