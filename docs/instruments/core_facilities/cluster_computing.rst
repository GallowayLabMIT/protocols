==================
Cluster Computing
==================


MIT houses several computing clusters that are available for the lab to use. As of 2025, we use the Engaging cluster, though this may change in the future.

The most common use case in our lab is RNA-seq analysis because reading and aligning millions of transcripts is computationally intensive, as you can imagine.
The general workflow (in detail below) is using a Snakefile to execute a list of commands for trimming, aligning, and/or analyzing transcripts.
These commands may point to RNA-seq-related packages or to user-defined python scripts that run analysis.
At a high level, you upload your raw reads and your project repo housing your Snakefile, run snakemake on the cluster, the cluster will compute, 
and then you will extract the data you need (usually gene counts and/or differentially expressed genes) to make plots locally.

First-time setup
================

0. Create an account
~~~~~~~~~~~~~~~~~~~~

Following the instructions on the `MIT ORCD docs page <https://orcd-docs.mit.edu/orcd-systems/#how-to-get-an-account-on-engaging>`_,
log in to the Engaging cluster through the web portal using your Kerberos ID and password (`instructions here <https://orcd-docs.mit.edu/accessing-orcd/ondemand-login/>`_).
This will automatically trigger a new account to be created.

.. note::

    There may be a delay of a day after creating your account before you can start any jobs. However, you should still be able to log in. 

Confirm you can log in to Engaging via your terminal or PowerShell using ``ssh``. Replace ``[your-kerberos]`` with your Kerberos ID:
   
.. code-block:: console

    $ ssh [your-kerberos]@orcd-login.mit.edu

This will prompt you for your Kerberos password and Duo authentication.


1. Add an ``ssh`` shortcut
~~~~~~~~~~~~~~~~~~~~~~~~~~

Once you've confirmed that you can log in, create an ``ssh`` shortcut to the cluster.

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

    You can't use ``nano`` on Windows. Instead, navigate to the folder directly in the File Explorer and edit your config file with a text editor:

    1. In PowerShell, run ``cd ~/.ssh`` 
    2. Get the directory path by ``pwd``
    3. Copy this path into "File Explorer". This might look like ``C:\Users\ChemeGrad2025\.ssh``
    4. Once you've located the hidden .ssh directory, edit the config file with "Notepad" (or "VSCode", etc.) and add in the above.

See `MIT ORCD docs SSH key setup <https://orcd-docs.mit.edu/accessing-orcd/ssh-setup/>`_ for help.

Now, check to confirm that the shortcut runs:

.. code-block:: console

    $ ssh engaging

This should generate the same prompt for your Kerberos password and Duo authentication as above, just via a simpler command.


2. Set up an SSH key with forwarding
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Based on `MIT ORCD docs "SSH key setup" <https://orcd-docs.mit.edu/accessing-orcd/ssh-setup/#__tabbed_1_2>`_ and
`GitHub docs "Using SSH agent forwarding" <https://docs.github.com/en/authentication/connecting-to-github-with-ssh/using-ssh-agent-forwarding>`_.

At a high level: SSH agent forwarding can be used to make deploying to a server simple.
It allows you to use your local SSH keys instead of leaving keys (without passphrases!) sitting on remote servers, like the Engaging cluster.

You can set up ``ssh-agent`` for your local computer which runs in the background and keeps your SSH key loaded into memory so you don't need to enter a passphrase every time
you need to use the key. Then, you can give remote servers, like the Engaging cluster, access to your local ``ssh-agent`` as if they were running on the server.
This is sort of like asking a friend to enter their password so that you can use their computer.

The end result basically means you get use ``git clone`` and other things without having to re-enter passphrases every time while on the Engaging cluster.

We'll start with `GitHub docs "Using SSH agent forwarding" <https://docs.github.com/en/authentication/connecting-to-github-with-ssh/using-ssh-agent-forwarding>`_.
Check to see if your own SSH key is set up and working by entering ``ssh -T git@github.com`` in the terminal. If successful it will look like:

.. code-block:: console

    $ ssh -T git@github.com
    # Attempt to SSH in to github
    > Hi USERNAME! You've successfully authenticated, but GitHub does not provide shell access.

If not, next make sure your local computer has an SSH public key for GitHub.

1. Check for an existing SSH key on your local computer:  `GitHub docs "Checking for existing SSH" <https://docs.github.com/en/authentication/connecting-to-github-with-ssh/checking-for-existing-ssh-keys>`_ 
2. If no key exists, then generate and add a new SSH key: `GitHub docs "Generating a new SSH key and adding it to the ssh-agent" <https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent>`_  
3. Now add the SSH key from your local computer to your Github account: `GitHub docs "Adding a new SSH key to your GitHub account" <https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account>`_
4. Confirm that the SSH key works by entering ``ssh -T git@github.com`` in the terminal. You should see the message above.

.. note:: 
    Your public key is likely ``id_ed25519.pub`` but may alternatively be ``id_rsa.pub`` or ``id_ecdsa.pub``.
    

Now GitHub has your public key but you still need to let ``ssh-agent`` get access to your private key. This way, when a remote server with ``ForwardAgent true``
needs to sign something with your private key, the request gets funneled back to your ``ssh-agent`` which returns the signed request so the private key never
leaves your local computer. By copying the public key onto remote systems---such as copy-pasting onto Github like we just did or using 
``ssh-copy-id``---your public key gets pre-loaded onto remote systems but you can still control access to your private keys for each individual remote server.


To make your key available to ``ssh-agent``:

1. Check that your key is visible to ``ssh-agent`` by running the following command on your local computer: ``ssh-add -L``
2. If the command says that no identity is available, you'll need to add your key with the following command: ``ssh-add`` . This will add any "default" keys. You can also add a specific key. For NBW this looks like ``ssh-add ~/.ssh/id_rsa`` which is different than the public key, ``~/.ssh/id_rsa.pub``!
3. On macOS, ``ssh-agent`` will "forget" this key, once it gets restarted during reboots. But you can import your SSH keys into Keychain using this command: ``ssh-add --apple-use-keychain YOUR-KEY``

Great! You should be done now! The secret was in something we added before:

.. code-block::

    Host engaging
        HostName orcd-login.mit.edu
        User [your-kerberos]
        ForwardAgent yes

The ``ForwardAgent yes`` tells your ``ssh-agent`` to let the Engaging cluster use your local keys. This is known as "SSH agent forwarding".

Check to make sure it's set up correctly:

1. Log in to the Engaging cluster using ``ssh engaging``, enter your Kerberos password, and authenticate with Duo.
2. On the Engaging cluster, test to see if the SSH key is set up and working with Github by entering ``ssh -T git@github.com`` in the terminal. It should show the same successful response as above.

If it's not working, check `GitHub docs "Using SSH agent forwarding: Troubleshooting SSH agent forward" <https://docs.github.com/en/authentication/connecting-to-github-with-ssh/using-ssh-agent-forwarding#troubleshooting-ssh-agent-forwarding>`_
for tips.


3. Link the shared data directory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We have a 20-TB shared data directory on the Engaging cluster. It is located at ``/orcd/data/katiegal/002``, which is an
annoying path to type. Instead, it is convenient to put a link in your home directory, which is the place where you start when you SSH in.

You only have to create this symbolic link (symlink) once. To make the symlink, run:

.. code-block:: console

    $ ln -s /orcd/data/katiegal/002 ~/katiegal_shared

The relevant directories here are:

- ``data/raw_reads``: where we put all our raw data
- ``projects``: where we clone git repos for analysis pipelines, etc.
- ``hpc_infra``: infrastructure scripts and other useful items.

.. code-block::

    katiegal_shared/
    ├── data/
    │   └── raw_reads/
    ├── hpc_infra/
    └── projects/


.. note::

    Before December 2025, we used to have another directory at ``/orcd/pool/003/katiegal_shared/``. If something is missing in the main shared folder,
    it is likely here. You should symlink each set of data into the new directory, e.g.: 

    .. code-block:: console

        $ ln -s /orcd/pool/003/katiegal_shared/data/raw_reads/250425Gal/ ~/katiegal_shared/data/raw_reads/250425Gal


Per-project setup
=================

.. admonition:: TODO 

    Needs description of other files in the suggested repo layout. Pipeline templates are in progress.

After getting your ``ssh-agent`` set up as described above, you should clone your project repo into ``~/katiegal_shared/projects/``.
This will let you edit your script files locally or on the server, and track changes.
You will want to make a new directory to house all of your Engaging cluster files. You can either copy a ``cluster`` folder from someone else's pipeline (CJ is working on an incoming template repo) or make a new one. 


To clone your repo:

1. Log in to the Engaging cluster via ``ssh engaging``
2. Navigate to the projects directory by ``cd katiegal_shared/projects``
3. Clone your project repo by using the ``ssh`` URL, which you can get from GitHub. This might look like: 

   .. code-block:: console

       $ git clone git@github.com:GallowayLabMIT/your_repo.git

Next, make a new cluster directory in your ``your_repo`` (if not using an existing template) and symlink the raw reads:

.. code-block:: console

    $ mkdir ~/katiegal_shared/projects/your_repo/cluster
    $ mkdir ~/katiegal_shared/projects/your_repo/cluster/data
    $ ln -s ~/katiegal_shared/data/raw_reads/ ~/katiegal_shared/projects/your_repo/cluster/data/raw_reads

Ultimately, your cluster file structure should look something like this:

.. code-block::

    katiegal_shared/
    ├── data/
    ├── hpc_infra/
    └── projects/
        └── your_repo/
            ├── ...             # everything else in your repo, like Python data analysis, figures, etc.
            └── cluster/
                ├── config      # TODO DESCRIPTION - Metadata for configuring
                ├── data/       # Data you don't want tracked, like genomes
                │   └── raw_reads
                ├── envs/       # TODO DESCRIPTION
                ├── inputs/     # Inputs that should be tracked, like transgenes or metadata
                ├── profiles/   # TODO DESCRIPTION
                ├── scripts/    # Scripts for analysis
                ├── .gitignore  # TODO DESCRIPTION
                └── Snakefile   # Runs pipeline


.. Upload raw data to the cluster
.. ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. .. admonition:: TODO

..     This section is incomplete/has errors!

.. Next we will upload the raw reads from smithsonian to the cluster using rclone.
.. Once per SSH session, you need to activate the rclone module. You do this by running our HPC-infastructure activate
.. script and adding the module:

.. .. code-block:: console

..     $ . ~/katiegal_shared/hpc-infra/modules/activate.sh
..     $ module add rclone

.. Then, you can use ``rclone``. See the `rclone documentation <https://rclone.org/docs/>`_ for more details, but a simple
.. copy command between files stored in Smithsonian to the cluster could be:

.. .. code-block:: console

..     $ rclone copy smithsonian:data/NGS/raw_reads/251204_Plasmidsaurus ~/katiegal_shared/data/raw_reads/251204_Plasmidsaurus


.. Be sure to ``unzip`` your files if they are zipped. 

.. Next we want to symlink in the raw_reads so you can easily access it:

.. 1. Run ``ln -s ~/katiegal_shared/data/raw_reads/ ~/katiegal_shared/projects/project_repo/cluster/data/raw_reads``

.. .. .. warning::
.. ..     Below needs to be updated

.. .. TODO: suggested project folder structure

.. .. .. code-block::

.. ..     cluster
.. ..     - data/
.. ..     - raw
.. ..     - envs/
.. ..     - inputs/
.. ..     - profiles/
.. ..     - scripts/
.. ..     - Snakefile
.. ..     - .gitignore

.. .. | cluster
.. .. | ├── config
.. .. | │   ├── samplesheet.csv 
.. .. | ├── data
.. .. | │   ├── raw
.. .. | ├── envs
.. .. | │   ├── deseq2.yaml
.. .. | │   ├── salmon.yaml
.. .. | │   └── trim_reads.yaml
.. .. | ├── inputs
.. .. | │   └── transgenes
.. .. | │       ├── transgenes-eGFP.fna
.. .. | │       └── transgenes-eGFP.gtf
.. .. | ├── load_snakemake.sh
.. .. | ├── profiles
.. .. | │   └── default
.. .. | │       └── config.yaml
.. .. | ├── scripts
.. .. | │   └── run_deseq2.R
.. .. | └── Snakefile 3



.. Run pipeline
.. ~~~~~~~~~~~~

.. .. admonition:: TODO

..     This section is incomplete/has errors!

.. 1. in your project folder on the cluster, do `git pull` to confirm you are up-to-date
.. 2. do `tmux new` to activate a [terminal multiplexer](https://github.com/tmux/tmux/wiki)
.. 	- this will keep things running in the background even if you close your computer
.. 3. Add modules:
   
.. .. code-block::

..     . ~/katiegal_shared/hpc-infra/modules/activate.sh
..     module add snakemake

.. 4. do a dry run to check for errors in the structure of snakemake calls (note: this will not catch all errors)
   
.. .. code-block::

..     snakemake --dry-run

.. 5. (optional) create the conda environment (long step) using a compute node

.. .. code-block::

..     salloc --mem 20G -c 10 -p mit_normal
..     snakemake --conda-create-envs-only

.. 6. run the pipeline! (do this when you know your pipeline is good, otherwise just do snakemake inside the folder with your Snakefile)
   
.. .. code-block::

..    snakemake --default-resources slurm_partition=mit_preemptable --keep-going --retries 3

.. 7. to exit the tmux window, type ``ctrl-b d`` (dettaches, keeps running in background), and to check on progress, do `tmux attach`
.. 8. When the job is finished, download to smithsonian using rclone.

.. .. code-block::

..     $ . ~/katiegal_shared/hpc-infra/modules/activate.sh
..     $ module add rclone
..     $ rclone copy ~/katiegal_shared/data/[data of interest] smithsonian:data/NGS/processed_reads/[new folder for your data]


.. Troubleshooting
.. ---------------
.. - if your snakemake is failing and nothing appears in a log for a rule involving a python script, 
..   ensure you have made the script executable by typing ``git update-index --chmod=+x cluster/scripts/pythonfile.py`` in the VS Code terminal

.. KL notes
.. --------



.. **Run pipeline**

.. - in your project folder, do `git pull` to confirm you are up-to-date
.. - do `tmux new` to activate a [terminal multiplexer](https://github.com/tmux/tmux/wiki)
.. 	- this will keep things running in the background even if you close your computer
.. - add modules
.. 	- `. ~/katiegal_shared/hpc-infra/modules/activate.sh`
.. 	- `module add snakemake`
.. - do a dry run to check for errors
.. 	- `snakemake --dry-run`
.. - tip: create the conda environment (long step) using a compute node
.. 	- `salloc --mem 20G -c 10 -p mit_normal`
.. 	- `snakemake --conda-create-envs-only`
.. - then, run your pipeline
.. 	- `snakemake --default-resources slurm_partition=mit_preemptable --keep-going --retries 3`
.. 	- do this when you know your pipeline is good, otherwise just do `snakemake` inside the folder with your `Snakefile` 
.. - to exit the tmux window, type `ctrl-b d` (dettaches, keeps running in background)
.. - to check on progress, do `tmux attach`

.. ### Download plots, etc from cluster
.. - navigate to the directory where you want to download the data
  
.. 	- e.g., your computer downloads folder, some output folder in your local project repo
  
.. - log in to the cluster using `sftp`
  
.. 	- `sftp engaging`
.. 	- approve the Duo request (note that nothing will pop up)
  
.. - navigate to what you'd like to transfer
  
.. 	- e.g., `cd katiegal_shared/projects/YourProject`
  
.. - download the data using the `get` command
  
.. 	- `get -R PathToFolderToCopy`
.. 	- [sftp manual](https://man.openbsd.org/sftp.1)