==================
Cluster Computing
==================


MIT houses several computing clusters that are available for the lab to use. As of 2025, we use the Engaging cluster, though this may change in the future.


Creating and setting up an account
==================================

**Create an account**

Following the instructions on the `MIT ORCD docs page <https://orcd-docs.mit.edu/orcd-systems/#how-to-get-an-account-on-engaging>`_,
log in to the Engaging cluster through the web portal using your Kerberos ID and password (`instructions here <https://orcd-docs.mit.edu/accessing-orcd/ondemand-login/>`_).
This will automatically trigger a new account to be created.

.. note::

    There may be a delay of a day after creating your account before you can start any jobs. However, you should still be able to log in. 

Confirm you can log in to Engaging via your terminal or PowerShellusing ``ssh``. Replace ``[your-kerberos]`` below with your Kerberos ID.
   
.. code-block:: console

    $ ssh [your-kerberos]@orcd-login.mit.edu

This will prompt you for your Kerberos password and Duo authentication.


First-time setup
----------------

**Add an ``ssh`` shortcut**

Once you've confirmed that you can log in, create an ``ssh`` shortcut to the cluster:

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

See `MIT ORCD docs SSH key setup <https://orcd-docs.mit.edu/accessing-orcd/ssh-setup/>`_ if stuck.

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

.. code-block::

    katiegal_shared
    ├── data
    │   └── raw_reads
    ├── hpc_infra
    └── projects


.. note::

    2025.12.12 - NBW: We used to have another folder at ``/orcd/pool/003/katiegal_shared/``. If something is missing it is likely there.
    You should symlink it, e.g. ``ln -s /orcd/pool/003/katiegal_shared/data/raw_reads/250425Gal/ ~/katiegal_shared/data/raw_reads/250425Gal``

**Setup and SSH key to make Git repo's easier to access**

Based on `MIT ORCD docs "SSH key setup" <https://orcd-docs.mit.edu/accessing-orcd/ssh-setup/#__tabbed_1_2>`_ and
`GitHub docs "Using SSH agent forwarding" <https://docs.github.com/en/authentication/connecting-to-github-with-ssh/using-ssh-agent-forwarding>`_ 

At a high level: SSH agent forwarding can be used to make deploying to a server simple.
It allows you to use your local SSH keys instead of leaving keys (without passphrases!) sitting on remote servers, like the Engaging cluster.

You can set up ``ssh-agent`` for your local computer which runs in the background and keeps your SSH key loaded into memory so you don't need to enter a passphrase every time
you need to use the key. Then, you can give remote servers, like the Engaging cluster, access to your local ``ssh-agent`` as if they were running on the server.
This is sort of like asking a friend to enter their password so that you can use their computer.

The end result basically means you get use ``git clone`` and other things without having to re-enter passphrases every time while on the Engaging cluster.

We'll start with `GitHub docs "Using SSH agent forwarding" <https://docs.github.com/en/authentication/connecting-to-github-with-ssh/using-ssh-agent-forwarding>`_ .
Check to see if your own SSH key is set up and working by entering ``ssh -T git@github.com`` in the terminal. If successful it will look like:

.. code-block::

    $ ssh -T git@github.com
    # Attempt to SSH in to github
    > Hi USERNAME! You've successfully authenticated, but GitHub does not provide shell access.

If not, next make sure your local computer has an SSH public key for GitHub based on `GitHub docs "Adding a new SSH key to your GitHub account" <https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account>`_ 

1. Check for an existing SSH public key on your local computer:  `GitHub docs "Checking for existing SSH" <https://docs.github.com/en/authentication/connecting-to-github-with-ssh/checking-for-existing-ssh-keys>`_ 
2. If no key exists, then add generate a new SSH public key: `GitHub docs "Generating a new SSH key and adding it to the ssh-agent" <https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent>`_  

After confirming you have an SSH public key on your local computer, you will then give this SSH key to Github so Github can identify you without having to log in everytime.
To do so:

1. Copy the SSH public key to your clipboard ``pbcopy < ~/.ssh/id_ed25519.pub``. If your SSH public key file has a different name than the example code, modify the filename to match your current setup. When copying your key, don't add any newlines or whitespace. For example, NBW's key is located at ``~/.ssh/id_rsa.pub``.
2. In the upper-right corner of any page on GitHub, click your profile picture, then click "Settings".
3. In the "Access" section of the sidebar, click  "SSH and GPG keys".
4. Click "New SSH key" or "Add SSH key".
5. In the "Title" field, add a descriptive label for the new key. For example, if you're using a personal laptop, you might call this key "Personal laptop".
6. Select the type of key, either authentication or signing. For more information about commit signing, see About commit signature verification.
7. In the "Key" field, paste your public key.
8. Click "Add SSH key".
    
Check to see if your own SSH key is set up and working again with Github by entering ``ssh -T git@github.com`` in the terminal. 

Now GitHub has your public key but you still need to let ``ssh-agent`` get access to your private key. This way, when a remote server with ``ForwardAgent true``
needs to sign something with your private key, the request gets funnel back to your ``ssh-agent`` which returns the signed request so the private never
leaves your local computer. By copying the public key onto remote systems like copy-pasting onto Github like we just did or using ``ssh-copy-id``,
your public key gets pre-loaded onto remote systems but you can still control access to your private keys for each individual remote server.


To make your key available to ``ssh-agent``:

1. Check that your key is visible to ``ssh-agent`` by running the following command on your local computer: ``ssh-add -L``
2. If the command says that no identity is available, you'll need to add your key with the following command: ``ssh-add`` . This will add any "default" keys.  You can also add a specific key. For NBW this looks like ``ssh-add ~/.ssh/id_rsa`` which is different than the public key, ``~/.ssh/id_rsa.pub``!
3. On macOS, ssh-agent will "forget" this key, once it gets restarted during reboots. But you can import your SSH keys into Keychain using this command: ``ssh-add --apple-use-keychain YOUR-KEY``

Great! You should be done now! The sercret was in something we added before:

.. code-block::

    Host engaging
        HostName orcd-login.mit.edu
        User [your-kerberos]
        ForwardAgent yes

The ``ForwardAgent yes`` tells your ``ssh-agent`` to let the Engaging cluster use your local keys. This is known as "SSH agent forwarding".

Check to make sure it's set up correctly:

1. Log into Engaging cluster using ``ssh engaging`` and sign in
2. On the Engaging cluster, test to see if the SSH key is set up and working again with Github by entering ``ssh -T git@github.com`` in the terminal. Like before, if successful it should say ``Hi USERNAME! You've successfully authenticated, but GitHub does not provide shell access.``

If it's not working, check `GitHub docs "Using SSH agent forwarding: Troubleshooting SSH agent forward" <https://docs.github.com/en/authentication/connecting-to-github-with-ssh/using-ssh-agent-forwarding#troubleshooting-ssh-agent-forwarding>`_.
for more tips.

Per-project setup
-----------------

.. admonition:: TODO 

    - .gitignore? 

**Set up project Git repo**

After getting your ``ssh-agent`` set up as described above, you should clone your project repo into ``~/katiegal_shared/projects/``.
This will let you edit your script files locally or on the server, and track changes. The end result should look something like this:

.. code-block::

    katiegal_shared
    ├── data
    ├── hpc_infra
    └── projects
        └── project_repo
            ├── analysisFile.ipynb
            ├── datadir.txt
            └── cluster
                ├── config      # Metadata for configuring
                ├── data        # Data you don't want tracked, like genomes
                │    └── raw_reads
                ├── envs        # TODO DESCRIPTION
                ├── inputs      # Inputs that should be tracked, like transgenes or metadata
                ├── profiles    # TODO DESCRIPTION
                ├── scripts     # Scripts for analysis
                └── Snakefile   # Runs pipeline

Clone the project repo:

1. ``ssh engaging`` and log into the Engaging cluster
2. Navigate to the projects directory by ``cd katiegal_shared/projects``
3. Clone your project repo by using the ``ssh`` url which you can get from GitHub. This might look like ``git clone git@github.com:GallowayLabMIT/project_repo.git``

At the end of this, you should get something like this

.. code-block::

    katiegal_shared
    ├── data
    ├── hpc_infra
    └── projects
        └── project_repo
            ├── analysisFile.ipynb
            └── datadir.txt

**Set up data folder in project Git repo**

You will want to make a new directory to house all of your Engaging cluster files. You can either copy a ``cluster`` folder from someone else's pipeline or make a new one. 
To make a new one:

1. Run ``mkdir ~/katiegal_shared/projects/project_repo/cluster``
2. Run ``mkdir ~/katiegal_shared/projects/project_repo/cluster/data`` . This will house any untracked data, like genomes and raw_reads

It should look like this

.. code-block::

    katiegal_shared
    ├── data
    ├── hpc_infra
    └── projects
        └── project_repo
            ├── analysisFile.ipynb
            ├── datadir.txt
            └── cluster
                └── data        # Data you don't want tracked, like genomes

Next we want to symlink in the raw_reads so you can easily access it:

1. Run ``ln -s ~/katiegal_shared/data/raw_reads/ ~/katiegal_shared/projects/project_repo/cluster/data/raw_reads``
   
It should look like this

.. code-block::

    katiegal_shared
    ├── data
    ├── hpc_infra
    └── projects
        └── project_repo
            ├── analysisFile.ipynb
            ├── datadir.txt
            └── cluster
                └── data        
                    └── raw_reads   # Symlink to ~/katiegal_shared/data/raw_reads/




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

Then, you can use ``rclone``. See the `rclone documentation <https://rclone.org/docs/>`_ for more details, but a simple
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

| cluster
| ├── config
| │   ├── samplesheet.csv 
| ├── data
| │   ├── raw
| ├── envs
| │   ├── deseq2.yaml
| │   ├── salmon.yaml
| │   └── trim_reads.yaml
| ├── inputs
| │   └── transgenes
| │       ├── transgenes-eGFP.fna
| │       └── transgenes-eGFP.gtf
| ├── load_snakemake.sh
| ├── profiles
| │   └── default
| │       └── config.yaml
| ├── scripts
| │   └── run_deseq2.R
| └── Snakefile 3


**Upload data to Engaging**

TODO

then, symlink data to your project folder

.. code-block::

    ln -s /orcd/data/katiegal/002/data/raw_reads YourPath



**Uploading RNA-seq data from Plasmidsaurus**

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
--------



**Run pipeline**

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