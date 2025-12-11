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

Confirm you can log in to Engaging via the terminal using `ssh`. Replace `[your-kerberos]` below with your Kerberos ID.
   
.. code-block::

    ssh [your-kerberos]@orcd-login.mit.edu

This will prompt you for your Kerberos password and Duo authentication.


**Add an `ssh` shortcut**

Once you've confirmed that you can log in, create an `ssh` shortcut to the cluster.
On your computer (not in the cluster), add the following to your config file (`nano ~/.ssh/config`):

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


**Set up folders on Engaging**

On Engaging, we have a shared folder for the lab data. You should create a symlink to this folder within your personal folder.
To do so, run

.. code-block::

    ln -s /orcd/data/katiegal/002 katiegal_shared

This creates the directory `katiegal_shared` in your cluster home directory.

The relevant folders here are:

- `raw_reads`: where we put all our raw data
- `projects`: where we clone git repos for analysis pipelines, etc.

So the next thing to do is to clone your git repo:

.. code-block::

    cd ~/katiegal_shared/projects
    git clone https://github.com/GallowayLabMIT/[your_project]
    git config --global --add safe.directory /orcd/data/katiegal/002/projects/[your_project]

TODO: suggested project folder structure


**Upload data to Engaging**

TODO

then, symlink data to your project folder

ln -s /orcd/data/katiegal/002/data/raw_reads YourPath


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