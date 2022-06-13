===============================
Computational environment check
===============================

Many of the tools, including this protocols website,
depend on Python. Contributing to analysis code and to protocols
also requires that your ``git`` install is working as expected.

There is a repository at https://github.com/GallowayLabMIT/environment-check
that contains a Python script that checks for installation problems by
checking that simple commands can succeed.

This page does not give specific, copy-and-pastable instructions, as these
will slightly differ. See :doc:`day_0_setup` for instructions on installing both
Python and Git, and :doc:`git_intro` for ``git`` help.

Initial environment check
-------------------------
If you run into errors, ask someone who has their environment fully setup!

1. Clone the **environment-check** repository at https://github.com/GallowayLabMIT/environment-check.
   You can put this repository wherever you like. This is intentionally a private repository, which means
   that you will have to be in the GallowayLabMIT Github organization and have your local Github credentials
   working.

.. note::
   A common pattern is to put all of your
   git repositories in a ``repo`` folder in your home directory. Importantly, don't put
   git repositories inside OneDrive or another cloud-synced folder; in addition to duplicated effort
   , ``git`` tracks lots of small files internally which means a lot of syncing effort.

2. Create a **virtual environment** within the environment-check repository; see :ref:`python_setup`
   for help creating this environment. Remember to add your virtual environment folder to the ``.gitignore``
   so it is not tracked by ``git``! [KEG: This just involves adding the file 'env' to the ".gitignore' file]
3. Activate the virtual environment, and install the listed dependencies with ``pip install -r requirements.txt``. [Note: "requirements.txt" can be found in the protocol repo]
4. Create and switch to another branch (e.g. ``cjohnsto``). [KEG: I found the easiest way to do this is via Github Desktop. Branch > New branch]
5. Install ``rushd``, a package for sane data management, using ``pip install rushd``. Because you
   added new packages, update the requirements file by using ``pip freeze > requirements.txt`` so someone else could
   use the same package versions.
6. Create a ``datadir.txt`` file that contains the path to your locally-synced OneDrive. [KEG: Just make a text file and copy the path to your OneDrive (aka SharePoint) folder for the Galloway lab so you can link directly to your data using "rushd".]
7. Commit your changed files and push your new branch to Github. [KEG: Stage changes by clicking on the '+' in the 'Changes' tab. Then types some message on what you will commit into the space for 'Source Control'. By clicking ont the check mark, you will commit changes.]
8. Run ``python check.py`` or ``python3 check.py`` (MacOS) to see if you get all green checks! [KEG: This only works if you are in the 'environment-check' folder]

.. note::
   Some tips from Katie on getting going.
      1. Your virtual environment is basically a container for projects that will help you track packages, versions, ectera. So you need one for spaces you'll be running python ( for instance in /protocols ) 
      2. Don't have permissions to run scripts, see here: https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.2
      3. If something isn't working, try restarting VS Code. Sometimes it just needs to restart. 
      4. To install reStructuredText, click here: https://marketplace.visualstudio.com/items?itemName=lextudio.restructuredtext
      5. Are you sure you installed Sphinx? https://pypi.org/project/Sphinx/
      6. Visually confirming the protocols' preview is working is encouraging. Try 'Ctrl+Shift+P' or 'Ctrl+Shift+R' 
      7. If you get stuck, ask for help!

Protocols check
---------------
After getting all green checks, clone the protocols repo (https://github.com/GallowayLabMIT/protocols)
and edit this file (``docs/bootcamp/iap/environment_check.rst``), adding your name to the completion list.
Commit and push those changes and you are done! [KEG: To save, "Ctrl+S"].


Completion date
---------------
- Christopher Johnstone (2022-06-01)
- Katie Galloway (2022-06-13)
