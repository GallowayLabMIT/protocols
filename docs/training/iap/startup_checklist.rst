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


1. Create a new repository on Github, likely inside the GallowayLabMIT organization, by going to:
   https://github.com/organizations/GallowayLabMIT/repositories/new

   When creating the repository, you likely want to check **Add a README file** and you
   should select **Python** as the ``.gitignore`` template. Setting the ``.gitignore`` means
   that Git will start off by ignoring all Python-related temporary files. You can update and
   modify the ignore list later.

   .. image:: img/new_python_repo.png
       :width: 100%

   Unless you know what you are doing, you can leave the License field set to None initially.
2. Clone the repository to some local folder, and open a terminal (or VS Code instance) into the repository folder.
3. Create a virtual environment (``python -m venv env``) for this project.
4. If in a terminal, activate the virtual environment (see :ref:`python_setup` for help activating)

.. note::

    If you are working inside VSCode, right after you create the virtual environment,
    you may get a popup that says something akin to "New virtual environment detected.
    Do you want to set this environment as your project environment?" Answering yes
    means that all launched Python instances should use that environment by default.

    If you don't see the popup, you can also set the Python environment through
    the Command Palette. Press ``ctrl-shift-p`` or ``command-shift-p``, type in ``select interpreter``,
    select ``Python: Select Interpreter`` and click the Python installation in your
    newly created virtual environment.

    .. image:: img/vscode_venv_select.png
        :width: 80%
        :align: center

5. Install packages you need. For data-analysis projects, this is likely
   ``pip install numpy scipy matplotlib seaborn rushd``

   a. If you are planning on using Jupyter notebooks, it is a best-practice to additionally
      install ``nb-clean`` via ``pip install nb-clean``. Then, run ``nb-clean add-filter``. From
      then on, ``nb-clean`` will automatically run alongside Git as a filter, making sure that
      extraneous notebook metadata does not get committed to version control.

6. Save your environment into a ``requirements.txt`` file using ``pip freeze > requirements.txt``.
   This means other people can reproduce exactly the set of packages you just installed.
   If you install or update packages later, remember to update the requirements file by repeating
   ``pip freeze > requirements.txt``.
7. If using data in the OneDrive/Sharepoint, create a ``datadir.txt`` file in the top-level folder
   of the repository that contains one line with the full, absolute path.

   a. Add ``datadir.txt`` to your ``.gitignore`` file. This means editing the ``.gitignore`` and adding
      a line anywhere, typically at the top, that contains just ``datadir.txt``.

New repository (Julia)
----------------------
1. Create a new repository on Github, likely inside the GallowayLabMIT organization, by going to:
   https://github.com/organizations/GallowayLabMIT/repositories/new

   When creating the repository, you likely want to check **Add a README file** and you
   should select **Julia** as the ``.gitignore`` template. Setting the ``.gitignore`` means
   that Git will start off by ignoring all Julia-related temporary files. You can update and
   modify the ignore list later.

   .. image:: img/new_julia_repo.png
       :width: 100%

   Unless you know what you are doing, you can leave the License field set to None initially.
2. Clone the repository to some local folder, and open a terminal (or VS Code instance) into the repository folder.
3. Start a Julia instance inside a local virtual environment by typing ``julia --project=.`` into a terminal.
   Unlike Python, you do not have to pre-create a virtual environment, and you specify a virtual environment
   at launch using the ``--project`` syntax.
4. Inside the Julia prompt, press ``]``; the prompt should change to ``(folder_name) pkg>``. Type ``add pkg1 pkg2``
   to install packages into the virtual environment.

   .. image:: img/julia_create_environment.png
       :width: 80%
       :align: center

   a. When you add or update packages later, be sure to commit the ``Manifest.toml`` and ``Project.toml`` files!
      These encode how others can reproduce your set of packages.

5. Once you have ``.jl`` files, VSCode should auto-select your local virtual environment. If it doesn't, you
   can open the command palette (``ctrl-shift-p`` or ``command-shift-p``) and search for "Julia: Change Current Environment"
   and select your newly created virtual environment.

   .. image:: img/julia_pick_environment.png
       :width: 80%
       :align: center

New repository (R)
------------------
.. warning::

    TBD. R's virtual environment system is non-built-in and is also bad compared to other systems.
    It is really hard to decouple system state in a reproducible way in R compared to Julia and Python.

    A possible best practice environment (Dockerized containers)
    currently under beta testing.


.. _existing_repo_setup:

Existing, non-data-driven repository (e.g. ``protocols``)
---------------------------------------------------------
1. Clone the repository to some local folder.
2. Start a terminal/VSCode isntance in the folder.
3. If using Python:

   a. Create a virtual environment using ``python -m venv env``.
   b. Activate the environment (see :ref:`new_repository_python` for details on activating in VSCode/terminal).
   c. Install the current package versions for this project using ``pip install -r requirements.txt``.

4. If using Julia:

   a. Start Julia within a local virtual environment with ``julia --project=.``.
   b. Enter package mode by pressing ``]``.
   c. Run ``instantiate`` to automatically install the reproducible list of packages in the Manifest and Project files.

5. Any additional setup should be described in the ``README.md`` file of the repository.


Existing, data-driven repository (e.g. ``tangles_model``)
---------------------------------------------------------
1. Perform the steps in the above section, :ref:`existing_repo_setup`.
2. If using Jupyter notebooks, run ``nb-clean add-filter`` to register the Jupyter notebook
   cleaning filter with Git.
3. If using ``rushd``, add a ``datadir.txt`` file to the root folder of the repository,
   containing the absolute path to the OneDrive/Sharepoint folder (e.g. the folder that *directly*
   contains the folders such as ``projects``, ``manuscripts``, etc).
