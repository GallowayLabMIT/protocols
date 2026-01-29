===============================
Computational environment check
===============================

Most of the data analysis we do in lab depends on Python and uses Git for version control and collaboration.
Additionally, lab infrastructure like this protocols site and our plasmid website rely on these tools. It's 
important to get these set up early so your labmates can help troubleshoot any issues that arise. That way, you
can begin contributing and start off with best practices.

Following the instructions below serves as a minimal test of basic functionality. It's normal to run into issues
as you work to complete it---your labmates are happy to help you troubleshoot and understand what's going on!

Before you begin
-----------------

1. Double check that you've completed everything in :doc:`day_0_setup`. Specifically, you'll want to have
   Python, Git, and VS Code installed, and OneDrive and Nextcloud synced locally to your computer.

2. If you aren't very familiar with the terminal, check out :doc:`the_shell` for explanations of some basic
   commands. You might want to try completing the :ref:`exercises <shell-exercise>` at the end to double-check your understanding.
   
3. It's *highly recommended* that you read through :doc:`git_intro` or a similar tutorial before beginning.
   Understanding why and how we use Git will help you complete the steps below. Don't worry about being an 
   expert yet, but a refresher before you begin is always a great idea.

.. tip::
   General tip: If things really aren't working (especially during the very initial setup) try quitting and restarting the application,
   restarting your computer, or uninstalling and reinstalling the software. Sometimes things need a reboot, and it doesn't hurt to try
   if you're really stuck.


Initial environment check
-------------------------

1. Clone the ``environment-check`` repository at https://github.com/GallowayLabMIT/environment-check.
   
   To do so, follow the instructions in the "Existing repository" section of 
   :ref:`Startup checklist when working with repositories <existing_repo_setup>`. You should follow 
   the instructions for a Python repo, but you do not need to add the ``nb-clean`` filter. Wait to commit your changes until later.

   .. note::
      This is intentionally a private repository, which means that you will have to be in the GallowayLabMIT Github organization 
      and have your local Github credentials working in order to clone it.
   
   .. tip::
      If you get an error message about not having permission to run scripts, you may need to change your execution policy.
      
      On Windows:
   
      1. Open PowerShell on administrator mode
      2. Run ``set-ExecutionPolicy RemoteSigned``
      3. Select "Y" to confirm
   
      Now you should be able to run scripts. For more explanation, see
      `here <https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.5&viewFallbackFrom=powershell-7.2>`_.

2. In the ``environment-check`` repo, create and switch to another branch. Name the branch with something like your name (for example, ``cjohnsto``). See :ref:`this section <git-branches>` of the Git intro for instructions.
3. Install ``rushd``, a package for sane data management, using ``pip install rushd``. Because you
   added new packages, update the requirements file by using ``pip freeze > requirements.txt`` so someone else could
   use the same package versions in the future.
4. For this training, modify the ``datadir.txt`` file (or create one if you haven't yet) to contain the path to your locally synced lab OneDrive/SharePoint
   (*not* the Nextcloud for this repo).
   
   For example, the path might look like this (on MacOS):

   .. code-block:: text

      /Users/username/Library/CloudStorage/OneDrive-SharedLibraries-MassachusettsInstituteofTechnology/GallowayLab - Documents

   You don't need any quotes or other characters around the path.

   .. note::

      The environment-check script expects that you point the data directory at the *root* of the OneDrive,
      i.e., the folder with subdirectories like ``projects``, ``instruments``, etc.

5. Commit your changed files and push your new branch to Github. See step 10 on the "New respository (Python)" section of :doc:`/training/onboarding/startup_checklist`.
6. From a terminal inside the repo, run ``python check.py`` or ``python3 check.py`` (MacOS) to see if you get all green checks! Fix any errors until you do.


Protocols check
---------------

Getting all green checks above means that you can now clone repos and run Python! The next step is to make sure you can contribute to our lab protocols 
(this website). At base, this site is a collection of formatted text files that is built into a website and pdf using Python. Specifically, protocols 
are written in `reStructuredText <https://docutils.sourceforge.io/rst.html>`_, a lightweight markup language that enables useful formatting in a 
relatively straightforward manner. These ``.rst`` files areconverted into a nice-looking website via the Python package `Sphinx <https://www.sphinx-doc.org/en/master/>`_. 
For more details on how we use this system here, check out the :doc:`/contributor_guide`. Don't worry about knowing the ins and outs of all this now.

Instead, to start, it's good to check that you can edit one of the files. 

1. Confirm that you have installed the "reStructuredText" and "reStructuredText Syntax highlighting" extensions in VS Code, as directed in :doc:`/training/onboarding/day_0_setup`.
2. Clone the protocols repo (https://github.com/GallowayLabMIT/protocols), using your new knowledge. (Hint: Begin with the 
   :ref:`Startup checklist when working with repositories <existing_repo_setup>`.)

3. Edit this file (``docs/training/onboarding/environment_check.rst``), adding your name to the completion list.
4. Save, commit, and push those changes, and you are done!

.. tip::
   Some specific tips for working with the protocols site:

      - Use :ref:`contrib_local_preview` to see how the reStructuredText is rendered on the website as you edit.
      - Check out the :ref:`contrib_rst_basics` for a primer on formatting in reStructuredText.
      - Follow the :ref:`contrib_standard_workflow` when editing protocols.


**Completion date**

   - Christopher Johnstone (2022-06-01)
   - Katie Galloway (2022-06-13)
   - Emma Peterman (2022-06-13)
   - Kasey Love (2022-06-17)
   - Nathan Wang (2022-06-17)
   - Christian Otero (2022-06-17)
   - Brittany Lende (2022-06-17)
   - Conrad Oakes (2022-06-20)
   - Kei Takahashi (2022-06-20)
   - Adam Beitz   (2022-06-21)
   - Patrick Han (2022-06-21)
   - Sneha Kabaria (2022-06-21)
   - Joji Teves (2023-02-24)
   - Deon Ploessl (2023-06-27)
   - Mary Ehmann (2024-01-15)
   - Diya Godavarti (2024-06-03)
   - Eliska Liang (2024-06-24)
   - Yunbeen Bae (2024-08-08)
   - Zahmiria Johnson (2025-01-07)
   - Maria Castellanos (2025-01-07)
   - Derin Gumustop (2025-01-09)
   - Rachel Lee (2026-01-22)
   - Paulina Naydenkov (2026-01-29)


The next frontier
-----------------

Now that your computational environment is set up, you're ready to move on to *the next frontier*: analyzing your data.
This belongs separately in its own training, but there are a few things you can do to get started with the knowledge you
have from this one.

1. Create a new repository in the GallowayLabMIT organization for your project. (Hint: See 
   :ref:`Startup checklist when working with repositories <new_repository_python>`.)

   Call it something descriptive related to the project (but probably not your name/initials, as collaborators may contribute to it).
   You can always change this later on Github under the "Settings" tab in the repo.
   
   The repo can be private for now, but you'll make (a version of) the final code public when you publish!

2. Test that you can run a Jupyter notebook by creating a new file anywhere in the repo called ``test.ipynb``.

   The easiest way to do this is probably with the "New file" icon (paper with plus sign) on the left-side Explorer panel in VS Code.

   .. image:: img/new-file-vs-code.png
      :align: center
      :width: 40%

3. Make a plot in the notebook! 
   
   - The first time you run a code cell in the Jupyter notebook, VS Code will prompt you to select a kernel. Choose the Python instance from your virtual environment.
   - Don't worry about loading data for now; generate some random values or use one of the sample datasets from 
     `seaborn <https://seaborn.pydata.org/tutorial/introduction.html>`_.
   - Consider checking out the seaborn `gallery <https://seaborn.pydata.org/examples/index.html>`_ or `tutorials <https://seaborn.pydata.org/tutorial.html#>`_ 
     to get inspired about the cool plots you can make!
