Possible build/install errors
=============================

Virtual environment install errors
----------------------------------
When doing ``pip install -r requirements.txt``, you might (after a long time "collecting build dependencies") get an error
saying that it is unable to compile / build a wheel. What's happening here?

There are two ways to distribute Python packages:

- As source code, which requires a working compiler if there are any non-Python code
  included (like C++ code). This is the same on all computers and operating systems.
- As a "binary wheel", e.g. a pre-compiled version of the package. Separate "wheels"
  have to build for every combination of Python version, operating system, and computer architecture.

Likely what happened is you are trying to install version-pinned packages that are **too old for your version of Python**. Because
the package developer has to make wheels for all Python versions, this means that old package versions will not have wheels for versions
of Python released after the package version.

The solution is generally simple; just update those packages that are trying to install from source code. Newer packages are typically
backwards compatible to older versions of Python.

E.g, if `pandas` is trying to install from source and failing, you can do:

.. code-block:: console
    
    $ pip install -U pandas # update pandas
    $ pip freeze > requirements.txt # re-freeze dependencies

No PDF is generated when I push
-------------------------------

If the PDF link is broken in the protocols page, then something broke the LaTeX build.

There are two ways to fix this:

1. Find someone with LaTeX locally installed (e.g. TeX Live). Have them run:

   .. code-block:: console

        $ python build.py --latex
  
   This should show you the LaTeX error.
2. Go to the build logs. You get to it by going to the `"Actions" tab <https://github.com/GallowayLabMIT/protocols/actions>`__ in the Github repo,
   finding the latest "CI" run, and then scrolling through the logs to find the LaTeX error.

My screenshots aren't visible
-----------------------------
Check that you don't have an uppercase ``.PNG`` either in the actual filename or wherever
you are loading the image.

On Windows, filenames are case-insensitive, that is ``some_file.txt`` is "the same file" as ``sOmE_fiLe.TXT``.
This is not true on MacOS or Linux, which means if there is a mismatch between the filename case,
the website build (which runs on Linux) will fail.