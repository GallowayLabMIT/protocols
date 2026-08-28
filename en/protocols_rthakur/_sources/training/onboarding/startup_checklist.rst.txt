================================================
Startup checklist when working with repositories
================================================

When both creating a new repository or cloning (creating a local copy) of an
existing repository, certain "startup tasks" need to be completed. These typically
only have to be performed once, when you create the local copy, not every time you
work with the repository.

..  _new_repository_python:

New repository (Python)
-----------------------

1. Create a new repository (aka repo) on Github, likely inside the GallowayLabMIT organization, by going to:
   https://github.com/organizations/GallowayLabMIT/repositories/new

   - When creating the repository, you likely want to check **Add a README file**. You should update this later with
     a description of the repository contents, as well as any non-standard setup instructions.
   - You should select **Python** as the ``.gitignore`` template. Setting the ``.gitignore`` means 
     that Git will start off by ignoring all Python-related temporary files. You can update and
     modify the ignore list later.
   - Unless you know what you are doing, you can leave the License field set to None initially.

   .. image:: img/new_python_repo.png
       :width: 80%
       :align: center

..  _clone_and_venv:

2. Clone the repository to some local folder.

   .. note::
      A common pattern is to put all of your git repositories in a ``repo`` folder in your home directory.
      Importantly, don't put git repositories inside OneDrive or another cloud-synced folder; in addition to duplicated version control,
      ``git`` tracks lots of small files internally which means a lot of syncing effort.

   First, find the URL to the repository. You can get the link at the repository online under the green "Code" button.
   It probably looks something like ``https://github.com/GallowayLabMIT/YourRepoName.git``

      .. image:: img/clone_url.png
         :width: 80%
         :align: center

   Then, *clone* (make a local copy of) the repo. There are several ways to do this, including the following:

   - In a terminal:
         
     1. Navigate (``cd``) to the local folder you want to put the repo in.
     2. Run ``git clone URL``, replacing ``URL`` with the one you found above.

   - In VS Code:

     1. Open the Command Palette (``ctrl-shift-p`` or ``command-shift-p``) and select "Git: Clone".
     2. Paste the URL you found above, or search within your repos.
     3. In the pop-up file explorer, select the local folder you want to put the repo in.

3. Open a terminal in the repository folder (i.e., ``cd`` into the folder). It's easiest to do this and the following steps inside VS Code.
4. Create a **virtual environment** for this project.

   Virtual environments enable standardization by creating local copies of packages. That way, the correct package versions are 
   associated with your code, allowing for reproducibility by running in the same "container" each time. This only needs to be 
   performed when you first clone the repo. If weird package errors happen later, you can always delete the environment folder and recreate it.
   
   From the root of the repository (i.e., the folder containing ``README.md``) create the environment using the ``venv`` Python module,
   passing the name of the virtual environment as an argument. In the command below, we give it the customary name ``env``, but you can 
   choose anything.

   .. code-block:: console

      $ python -m venv env  # On Windows, most Linuxes
      $ python3 -m venv env # On modern macOS

5. **Activate** the virtual environment. This typically has to be done every time you open a new terminal or when you switch between projects 
   with different virtual environments. Once the environment has been activated, any Python changes you do (installing packages, etc.) will only
   affect this environment.

   .. code-block:: console
      :class: bash-console

      $ source env/bin/activate # On macOS, Linux

   .. code-block:: console
      :class: powershell-console

      > .\env\Scripts\activate # On Windows

   Now, the prompt in terminal should begin with ``(env)``, indicating your environment is active.

   .. note::

      If you are working inside VS Code, right after you create the virtual environment,
      you may get a popup that says something akin to "New virtual environment detected.
      Do you want to set this environment as your project environment?" Answering yes
      means that all launched Python instances will use that environment by default. (Convenient!)

      If you don't see the popup, you can also set the Python environment through
      the Command Palette. Press ``ctrl-shift-p`` or ``command-shift-p``,
      search for "Python: Select Interpreter", and click the Python installation in your
      newly created virtual environment.

      .. image:: img/vscode_venv_select.png
         :width: 80%
         :align: center

6. Install the packages you need. For data analysis projects, this is likely
   ``pip install ipykernel matplotlib nb-clean numpy pandas rushd scipy seaborn``

   These packages are useful for computing with arrays and statistics (``numpy``, ``pandas``, ``scipy``);
   plotting (``matplotlib``, ``seaborn``); and running Jupyter notebooks (``ipykernel``, ``nb-clean``), 
   an interactive computing workspace that combines sections of code with text.
   Finally, ``rushd`` is a package developed by the lab for common tasks related to data loading,
   analysis, and plotting.
   
   If you are using ``nb-clean``, in the terminal run ``nb-clean add-filter``. From
   then on, this package will automatically run alongside Git as a filter to remove extraneous notebook 
   metadata.

7. Save your environment into a ``requirements.txt`` file using ``pip freeze > requirements.txt``.
   This means other people can reproduce exactly the set of packages you just installed.
   If you install or update packages later, remember to update the requirements file by repeating
   ``pip freeze > requirements.txt``.

8. If you will eventually load data from Smithsonian, create a ``datadir.txt`` file in the top-level folder
   of the repository. This file should contain one line with the full, absolute path to where Smithsonian syncs locally on your computer.
   You don't need any quotes or other characters around the path.

   For instance, a path on macOS might look something like: 

   .. code-block:: text
      
      /Users/username/Library/CloudStorage/Nextcloud-kerberos@mit.edu@smithsonian.mit.edu/data
   

9. Mark items that Git should not track by adding them to your ``.gitignore`` file.
   This means adding a line in ``.gitignore`` (usually at the top) for each file or directory.

   Typically, this includes your virtual environment ``env`` and any output files you save in a directory like ``output``, as you can always re-create 
   these later. Other files like ``datadir.txt``, ``.DS_store`` (on macOS), and ``.vscode`` save information relevant only to your local computer,
   so these should not be tracked by Git.

   Here's an example:
   ::
      
      # custom
      env/
      datadir.txt
      output/
      .vscode
      .DS_store

      # defaults continue below
      ...

.. _git_commit:

10. This is a good time to commit your changes, probably with a commit message like "repo setup".

   You can do this in the terminal with ``git commit -m "Your message"``, or in VS Code in the "Source Control" pane. For the latter, 
   stage changes first by clicking the plus icon next to each change, type your commit message in the box, and click the blue "Commit" button.

   .. image:: img/git-commit-vscode.png
      :width: 50%
      :align: center


New repository (Julia)
----------------------

1. Follow steps 1-3 above for creating a new repository. Except, select **Julia** as the ``.gitignore`` template.
2. Start a Julia instance inside a local virtual environment by typing ``julia --project=.`` into a terminal.
   Unlike Python, you do not have to pre-create a virtual environment, and you specify a virtual environment
   at launch using the ``--project`` syntax.
3. Inside the Julia prompt, press ``]``. The prompt should change to ``(folder_name) pkg>``. Type ``add pkg1 pkg2``
   to install packages (replacing ``pkg1``, etc. with package names) into the virtual environment.

   .. image:: img/julia_create_environment.png
      :width: 80%
      :align: center

   .. note:: 
      When you add or update packages later, be sure to commit the ``Manifest.toml`` and ``Project.toml`` files!
      These describe how others can reproduce your set of packages.

4. Once you have ``.jl`` files, VS Code should auto-select your local virtual environment. If it doesn't, you
   can open the command palette (``ctrl-shift-p`` or ``command-shift-p``) and search for "Julia: Change Current Environment"
   and select your newly created environment.

   .. image:: img/julia_pick_environment.png
      :width: 80%
      :align: center


New repository (R)
------------------
.. warning::

   TBD. R does not have a virtual environment system built-in, and this system is also bad compared to others.
   It is really hard to decouple system state in a reproducible way in R compared to Julia and Python.

   A possible best practice environment (Dockerized containers) is currently under beta testing.


.. _existing_repo_setup:

Existing repository (Python)
----------------------------

1. Follow steps 2-5 for "New repository (Python)" :ref:`above <clone_and_venv>` to clone the repo, create a virtual environment, and activate it.
2. Install the current package versions for this project using ``pip install -r requirements.txt``.
3. If using Jupyter notebooks, run ``nb-clean add-filter`` to register the cleaning filter with Git.
4. If using ``rushd``, add a ``datadir.txt`` file to the root folder of the repository. This file should contain one line with the full, absolute path 
   to where Smithsonian syncs locally on your computer. You don't need any quotes or other characters around the path.

   For instance, a path on macOS might look something like: 

   .. code-block:: text
      
      /Users/username/Library/CloudStorage/Nextcloud-kerberos@mit.edu@smithsonian.mit.edu/data

5. Any additional setup should be described in the ``README.md`` file of the repository.


Existing repository (Julia)
---------------------------

1. Clone the repository, following steps 2-3 for "New repository (Python)" :ref:`above <clone_and_venv>`.
2. Start Julia within the virtual environment using ``julia --project=.``
3. Enter package mode by pressing ``]``
4. Run ``instantiate`` to automatically install the reproducible list of packages in the Manifest and Project files.
5. Any additional setup should be described in the ``README.md`` file of the repository.
