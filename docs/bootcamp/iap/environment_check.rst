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
   You can put this repository wherever you like.

.. note::
   A common pattern is to put all of your
   git repositories in a ``repo`` folder in your home directory. Importantly, don't put
   git repositories inside OneDrive or another cloud-synced folder; in addition to duplicated effort
   , ``git`` tracks lots of small files internally which means a lot of syncing effort.

2. Create a **virtual environment** within the environment-check repository; see :ref:`python_setup`
   for help creating this environment. Remember to add your virtual environment folder to the ``.gitignore``
   so it is not tracked by ``git``!
3. Activate the virtual environment, and install the listed dependencies with ``pip install -r requirements.txt``.
4. Create and switch to another branch (e.g. ``cjohnsto``).
5. Install ``rushd``, a package for sane data management, using ``pip install rushd``. Because you
   added new packages, update the requirements file by using ``pip freeze > requirements.txt`` so someone else could
   use the same package versions.
6. Create a ``datadir.txt`` file that contains the path to your locally-synced OneDrive.
7. Commit your changed files and push your new branch to Github.
8. Run ``python check.py`` or ``python3 check.py`` (MacOS) to see if you get all green checks!

Protocols check
---------------
After getting all green checks, clone the protocols repo (https://github.com/GallowayLabMIT/protocols)
and edit this file (``docs/bootcamp/iap/environment_check.rst``), adding your name to the completion list.
Commit and push those changes and you are done!


Completion date
---------------
- Christopher Johnstone (2022-06-01)
