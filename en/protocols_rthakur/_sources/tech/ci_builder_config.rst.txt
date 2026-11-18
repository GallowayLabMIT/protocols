Builder config and update
=========================

This repository is automatically built and pushed to https://gallowaylabmit.github.io/protocols
using Github Actions. `Github Actions <https://docs.github.com/en/actions>`__ is a "continuous integration" (CI)
service built into Github that is free for public repositories (like this one!)

It lets us programmatically define build steps, such as building the website and PDF versions of the protocols,
automatically whenever someone pushes to Github.

A special YAML file defines how this build works. If you edit this file through Github's interface, it will
give you nice suggested completions. The general (annoying) workflow for editing CI jobs is thus:

1. Edit in the online interface.
2. Commit your changes.
3. Wait for the Github Actions job (at https://github.com/GallowayLabMIT/protocols/actions) to complete.
4. Check for errors, and so on.

Current CI jobs
---------------
Github Actions runs jobs that are in the special ``.github/workflows`` folder. The only current one is
``.github/workflows/build_helper.sh``:

.. literalinclude:: ../../.github/workflows/build_docs.yaml
    :language: yaml
    :linenos:


This job is run sequentially on a Linux virtual machine. 

As an explanation of what each of these jobs are doing:
1. checkout: checks out a *full* (``fetch-depth = 0``, e.g. unlimited) version of the repo so we can render all active branches.
2. install dependencies: installs LaTeX so that we can build the PDF.
3. setup Python: installs a specific Python version.
4. Python dependencies: install the specific packages listed in the ``requirements.txt``
5. Build: calls the build helper script that builds and deploys the website.


Updating the CI job
-------------------
From time to time, you may have to update the CI job. This is good practice to do, so that the documentation
jobs don't get horribly out of date.

1. Start by looking at the YAML file and see if the `setup-python` or `checkout` functions have updates by checking the "Actions Marketplace".

   - The ``actions/checkout`` step is viewable at https://github.com/marketplace/actions/checkout
   - The ``actions/setup-python`` step is viewable at https://github.com/marketplace/actions/setup-python
   
   Change the pinned version (the thing after the ``@``) if necessary.
2. If a new stable version of Python has been released, first make sure that you are running it on your local computer.
   Then, change the ``python-version`` line to the new version.
3. If Python has been updated, update the requirements file by doing:
   
   - Create a **fresh virtual environment** and activate it.
   - Remove the version specifier from every package in the ``requirements.txt`` file (the ``==1.2.3`` part)
   - ``pip install -r requirements.txt`` to fetch the latest versions of all packages.
   - Run ``python build.py --force-rebuild`` and **check the output in ``output/html`` carefully**.

   If nothing in the built output is broken, then you can commit your changes!
4. Commit the changes to both the ``requirements.txt`` and ``build_docs.yaml`` files, and see if it works on Github.
5. Monitor progress through https://github.com/GallowayLabMIT/protocols/actions