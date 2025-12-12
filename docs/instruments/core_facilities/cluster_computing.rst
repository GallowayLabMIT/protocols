======================
Cluster Computing
======================

MIT houses several computing clusters that are available for the lab to use. As of 2025, we use the Engaging cluster, though this may change in the future.


Creating and setting up an account
==================================

**Create an account**

Following the instructions on the `MIT ORCD docs page <https://orcd-docs.mit.edu/orcd-systems/#how-to-get-an-account-on-engaging>`_,
log in to the Engaging cluster through the web portal using your Kerberos ID and password (`instructions here <https://orcd-docs.mit.edu/accessing-orcd/ondemand-login/>`_).
This will automatically trigger a new account to be created.

.. note::
    There may be a delay of a day after creating your account before you can start any jobs. However, you should still be able to log in. 

Confirm you can log in to Engaging via the terminal using ``ssh``. Replace ``[your-kerberos]`` below with your Kerberos ID.
   
.. code-block:: console

    $ ssh [your-kerberos]@orcd-login.mit.edu

This will prompt you for your Kerberos password and Duo authentication.


First-time setup
----------------

**Add an ``ssh`` shortcut**

Once you've confirmed that you can log in, create an ``ssh`` shortcut to the cluster. You can look at `MIT ORCD docs SSH key setup <https://orcd-docs.mit.edu/accessing-orcd/ssh-setup/>`_ for more info.
On your computer (not in the cluster), add the following to your config file using ``nano ~/.ssh/config``:

.. code-block::
    Host engaging
        HostName orcd-login.mit.edu
        User [your-kerberos]
        ForwardAgent yes

While you're at it, add a shortcut to the BioMicro Center cluster. This is where they'll temporarily store your sequencing data.

.. code-block::
    Host bmc
        HostName bmc-150.mit.edu
        User galloway_ill

.. important::
    You can't use ``nano`` on Windows. Instead, navigate to the folder directly in the File Explorer and edit your config file with a text editor.
    To do this, use PowerShell and navigate by ``cd ~/.ssh`` and get the directory path by ``pwd``. Then copy this path into "File Explorer".
    This might look like ``C:\Users\ChemeGrad2025\.ssh``. Then edit config file with "Notepad" or with VSCode and add in the above.


**Setup the link to the shared data folder**

We have a 20TB shared data folder on the Engaging cluster. It is located at ``/orcd/data/katiegal/002``, which is an
annoying path to type. Instead, we like to put a link in your home directory, which is the place where you start when you SSH in.

You only have to create this symbolic link (symlink) once. To make the symlink, run:

.. code-block::

    $ ln -s /orcd/data/katiegal/002 ~/katiegal_shared

The relevant folders here are:

- ``data/raw_reads``: where we put all our raw data
- ``projects``: where we clone git repos for analysis pipelines, etc.
- ``hpc_infra``: infastructure scripts and other useful items.

Per-project setup
-----------------

.. admonition:: TODO 

    - Talk about setting up SSH key forwarding, and making sure that you use the same SSH key
      for both Github and Engaging.
    - Talk about cloning your project repo into ``~/katiegal_shared/projects/``
    - Talk about creating a ``cluster/data`` folder and symlinking the raw_reads folder in


Transferring files
------------------
There are two major ways to transfer files: **rclone** for transferring files between Smithsonian or the BMC, and **sftp**
for transferring files from your local computer.

**rclone**
``rclone`` is an all-purpose tool for moving files between servers, and especially cloud providers. We have it setup
with two "remotes":

- ``bmc``: the BioMicroCenter data directory
- ``smithsonian``: our data storage.

Once per SSH session, you need to activate the rclone module. You do this by running our HPC-infastructure activate
script and adding the module:

.. code-block:: console

    $ . ~/katiegal_shared/hpc-infra/modules/activate.sh
    $ module add rclone

Then, you can use ``rclone``. See the `rclone documentation <https://rclone.org/docs/>`__ for more details, but a simple
copy command between files stored in Smithsonian to the cluster could be:

.. code-block:: console

    $ rclone copy smithsonian:data/NGS/raw_reads/251204_Plasmidsaurus ~/katiegal_shared/data/raw_reads/251204_Plasmidsaurus

This works bidirectionally! You can copy results back into Smithsonian directly.


**sftp**

To transfer local files, we use SFTP. On your local computer (not in the cluster), run:

.. code-block:: console

    $ sftp [your-kerberos]@orcd-login.mit.edu

This connects your local computer to the Engaging cluster. You should see ``katiegal_shared``. 
Then use ``put`` to upload the sequencing data to ``katiegal_shared\data\raw_reads``

.. code-block::

    put path/to/local/directory/filename.extension /path/to/remote/directory/newname.extension


Before you upload your data, making a new directory to hold the data using ``katiegal_shared\data\raw_reads\new_directory_name``
It should look something like this

.. code-block::

    mkdir katiegal_shared/data/raw_reads/251204_Plas
    put C:\Users\ChemeGrad2019\Downloads\4Y5Y7T_fastq.zip katiegal_shared/data/raw_reads/251204_Plas/4Y5Y7T_fastq.zip

Then unzip your files and delete the original zip.



.. important::
    We have multiple data folders from the Engaging cluster. Ideally everything should be symlinked into the current folder.
    TODO ADD MORE DETAILS `` /orcd/data/katiegal/003``

So the next thing to do is to clone your git repo:

.. code-block::

    $ cd ~/katiegal_shared/projects
    $ git clone https://github.com/GallowayLabMIT/[your_project]
    $ git config --global --add safe.directory /orcd/data/katiegal/002/projects/[your_project]

A convenient way to organize your project is to add a folder called ``cluster`` (or similar) in the root directory of your project repo.
Here, you can add pipelines to run on the cluster separate from the other data analysis (e.g., flow) for your project. 


.. warning::
    Below needs to be updated

TODO: suggested project folder structure

`cluster`
- `data/`
   - `raw`
- `envs/`
- `inputs/`
- `profiles/`
- `scripts/` 
- `Snakefile`
- `.gitignore`

cluster
├── config
│   ├── samplesheet.csv
├── data
│   ├── raw
├── envs
│   ├── deseq2.yaml
│   ├── salmon.yaml
│   └── trim_reads.yaml
├── inputs
│   └── transgenes
│       ├── transgenes-eGFP.fna
│       └── transgenes-eGFP.gtf
├── load_snakemake.sh
├── profiles
│   └── default
│       └── config.yaml
├── scripts
│   └── run_deseq2.R
└── Snakefile 3


**Upload data to Engaging**

TODO

then, symlink data to your project folder

.. code-block::

    ln -s /orcd/data/katiegal/002/data/raw_reads YourPath



**Uploading RNA-seq data from Plasmidsaurus **

We use ``sftp`` to copy data between servers, either remote (e.g. Engaging cluster) or local (your computer). 
You can look at `SFTPCloud docs <https://sftpcloud.io/learn/sftp/sftp-put-command>`_ for more info.

For **Plasmidsaurus**, download the fastq.zip file (e.g. "4Y5Y7T_fastq.zip" which contains fastq.gz files). Open a new terminal or PowerShell and run locally:

.. code-block::
    sftp [your-kerberos]@orcd-login.mit.edu

This connects your local computer to the Engaging cluster. You should see ``katiegal_shared``. 
Then use ``put`` to upload the sequencing data to ``katiegal_shared\data\raw_reads``

.. code-block::
    put path/to/local/directory/filename.extension /path/to/remote/directory/newname.extension


Before you upload your data, making a new directory to hold the data using ``katiegal_shared\data\raw_reads\new_directory_name``
It should look something like this

.. code-block::
    mkdir katiegal_shared/data/raw_reads/251204_Plas
    put C:\Users\ChemeGrad2019\Downloads\4Y5Y7T_fastq.zip katiegal_shared/data/raw_reads/251204_Plas/4Y5Y7T_fastq.zip

Then unzip your files and delete the original zip.








**Run pipeline**

TODO (KL has notes)


**Download output to local computer**

TODO (KL has notes)




KL notes
========

### Run pipeline
- in your project folder, do `git pull` to confirm you are up-to-date
- do `tmux new` to activate a [terminal multiplexer](https://github.com/tmux/tmux/wiki)
	- this will keep things running in the background even if you close your computer
- add modules
	- `. ~/katiegal_shared/hpc-infra/modules/activate.sh`
	- `module add snakemake`
- do a dry run to check for errors
	- `snakemake --dry-run`
- tip: create the conda environment (long step) using a compute node
	- `salloc --mem 20G -c 10 -p mit_normal`
	- `snakemake --conda-create-envs-only`
- then, run your pipeline
	- `snakemake --default-resources slurm_partition=mit_preemptable --keep-going --retries 3`
	- do this when you know your pipeline is good, otherwise just do `snakemake` inside the folder with your `Snakefile` 
- to exit the tmux window, type `ctrl-b d` (dettaches, keeps running in background)
- to check on progress, do `tmux attach`

### Download plots, etc from cluster
- navigate to the directory where you want to download the data
	- e.g., your computer downloads folder, some output folder in your local project repo
- log in to the cluster using `sftp`
	- `sftp engaging`
	- approve the Duo request (note that nothing will pop up)
- navigate to what you'd like to transfer
	- e.g., `cd katiegal_shared/projects/YourProject`
- download the data using the `get` command
	- `get -R PathToFolderToCopy`
	- [sftp manual](https://man.openbsd.org/sftp.1)