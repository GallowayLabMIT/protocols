=======================
On Terminals and Shells
=======================

Motivation
==========
Knowing the basics of using a command line interface is occasionally helpful. While
a lot of software has nice GUI interfaces, making these interfaces
takes a large amount of work. Software written by a small number of people
(like research groups!) often are only accessible via a CLI.
In many cases, a command line interface can also be a faster way to do certain operations.

Even if you avoid using a terminal in daily computing, a terminal is often the only
way that you can access high performance computing clusters.


The basics
==========
Lots of words get thrown around: CLI, terminals, bash, shells, command prompts.
For these purposes:

* A **terminal** is the program that runs on your computer and
  handles all of the low-level input output details. It is responsible
  for drawing to the screen, getting keyboard input, handling the clipboard,
  selecting fonts, and so on.

  Common terminals might be the programs *Terminal*  or *iTerm2* on MacOS or
  *Windows Terminal*, *Powershell*, and *Command prompt* on Windows (more on this later).

* A **shell** is a command-line program (e.g. instead of interacting with us through a
  graphical interface, you type stuff in line by line) that lets the user take actions like
  modify files, view program output, run other command-line programs, and so on.

  Inside a terminal, you run a shell. Somewhat confusingly, the default terminals
  on both MacOS and Windows run a default shell, so that the shell and terminal appear
  identical.

  Common Unix shells (runnable on MacOS and Linux) are the original shell, ``sh``, along
  with ``bash`` (common default on Linux), ``zsh`` (recent default on MacOS), and others
  like ``csh`` and ``dash``. The two major Windows shells are ``cmd`` (old-school, going
  back to DOS) and ``powershell`` (Windows' modern shell).


.. figure:: img/shell_terminal.png
    :width: 80%

    An example of the difference between terminals and shells [#]_



When a shell starts it, it displays a **prompt**, showing that it is ready for input. Once you are done
typing in your command, you hit enter to run that command.

When you run a command line program, the shell will show the prompt again when it's ready for more input.
In these notes, we will use ``$`` to represent generic prompts (and ``>`` for the default Powershell prompt);
lines without the ``$`` are example output of what you will see when you enter the command.
When typing in commands, you should *not* type in the dollar sign! Your specific shell may display
a more complicated prompt than a dollar sign, such as showing the current directory that you are currently
in.

An example is:

.. code-block:: console

    $ echo "test"
    test

If we have an operating-system specific command to show, we'll show them in specific
boxes, and we'll use the Powershell prompt symbol ``>`` for the Powershell examples.

.. code-block:: console
    :class: bash-console

    $ echo "test"
    test

.. code-block:: console
    :class: powershell-console

    > echo "test"
    test


Finally, throughout this we will talk about **files** and **directories**. Directories are more
commonly known as **folders**, but **directory** is the slightly more precise terminology,
used here for easier googling if you run into problems.


Commands
--------
In a shell, you enter commands to run them. When processing a line, the line you entered is
first separated by the spaces present. Consecutive spaces are treated as a single space, with
text in quotes being represented as a single "word".

Then, the first word is taken as the command name, and looked up in the list of installed
command-line programs (e.g. see if it is present in ``PATH``). The rest of the line is
given to that program as it's **command line arguments**.

By convention, command line arguments that start with dashes are normally **options**.
By convention, these options typically either have long names and start with two dashes,
or have a "shorthand" form with a single dash and a single letter. Arguments that don't start with dashes are typically user-specified.

For example, in the following commands:

.. code-block:: console

    $ git commit --message "Testing out a commit"
    $ git commit -m "Testing out a commit"

the command ``git`` is called in both cases, and is given the argument list:

(``commit``, ``--message``, ``Testing out a commit``) in the first case or
(``commit``, ``-m``, ``Testing out a commit``) in the second. These two calls
are identical in this case, because ``-m`` is shorthand for ``--message``.

.. admonition:: Demo

    For the command line commands:

    .. code-block:: console

        $ python -m venv env
        $ git add testing.py module.py "explanation revised.docx"
    
    what command is called in each case? What arguments are given to
    that command?

    .. raw:: html

        <details>
        <summary>Show/hide answer</summary>
        
    In the first example, the program ``python`` is ran with arguments (``-m``, ``venv``, ``env``).
    
    In the second example, the program ``git`` is ran with arguments (``add``, ``testing.py``, ``module.py``, ``explanation revised.docx``).

    .. raw:: html

        </details>

Starting off at home
--------------------
When you first open a terminal, your shell will likely start off in your **home directory**, also known in shorthand
as ``~``. Each user has its own home directory. All of the user directories that you are used to accessing through
Windows Explorer or Finder, such as ``Desktop``, ``Downloads``, or ``Documents`` are subdirectories of your home directory.

The actual location of your home directory differs,
but is typically something like ``C:\Users\Username`` on Windows, ``/users/Username`` on MacOS, and
``/home/Username`` on most Linuxes.

So that we don't have to type that large thing every time, ``~`` is short-hand notation for whatever your home
directory is. That is, the location of your downloads folder could be written either as ``C:\Users\Username\Downloads``
or more simply as ``~\Downloads``

.. note::
    You may have noticed earlier that these directory paths have been written differently between the
    two operating systems. In short, due to backwards compatibility, Windows uses the backslash ``\``
    as the path separator (written between directory names), whereas all Unix-derived operating systems
    including MacOS and Android use the forward slash ``/`` as the path separator.

    Most of the time you can just use the forward slash without worry; ``powershell`` on Windows will auto-convert
    from forward slashes to backslashes if you use forward slashes, but when programming you should keep this in
    mind and not manually use slashes when constructing paths to filenames. It still may work, but you should
    ideally use filesystem-aware techniques, like using ``os.path`` or ``pathlib`` in Python.

The shell has a current location; imagine it as having a Finder/Explorer window open to some directory
on your computer. This current location is called the (current) **working directory**. This is 
How do we know what folder we are in while using the shell? Our first command we will learn is ``pwd``:

.. admonition:: Command: ``pwd``

    ``pwd`` stands for **print working directory**, and does just that; it tells you what your current
    location is, in full detail (e.g. the entire path, not in shorthand). If you ever get lost, just type ``pwd``!


    This output is similar across operating systems; it is a little more verbose in Powershell.

    Example output right after launch, so that you are starting in your home directory:

    .. code-block:: console
        :class: bash-console

        $ pwd
        /users/username

    .. code-block:: console
        :class: powershell-console

        > pwd                                                                                     

        Path
        ----
        C:\Users\Username

If we want to know what is inside the current directory, we can use ``ls``:

.. admonition:: Command: ``ls``

    ``ls`` stands for **list**, and lists every file and folder inside the current working
    directory.

    If you were to run it in your home directory, you might get something like:

    .. code-block:: console

        $ ls
        Desktop    Downloads  Pictures
        Documents  Music      Videos
    
    If you want to see what is inside one of these directories, ``ls``
    takes command line arguments specifying which directory you'd like the view:

    .. code-block:: console

        $ ls Documents
        10-50     10-40   10-34
        research
    
    To view **hidden files** (on MacOS/Linux, these are files/directories that start with a period;
    on Windows, these are files/directories with a hidden attribute set), we need to pass
    ``ls`` a command line option. This differs between shells, but on bash/zsh/etc, you use ``--all`` or ``-a``
    to show hidden files as well:

    
    .. code-block:: console
        :class: bash-console

        $ ls -a
        .        Desktop    Music     Videos
        ..       Documents  Pictures
        .bashrc  Downloads  .profile
    
    In Powershell, we pass the option ``-Force``:

    .. code-block:: console
        :class: powershell-console

        > ls -Force
        Directory: C:\Users\username

        Mode                LastWriteTime          Length Name
        ----                -------------          ------ ----
        d--h--         1/11/2021   7:19 PM                .git
        d-----         1/11/2021   7:19 PM                Desktop
        d-----         1/11/2021   7:19 PM                Documents
        d-----         1/11/2021   7:19 PM                Downloads
        d-----         1/11/2021   7:19 PM                Music
        d-----         1/11/2021   7:19 PM                Pictures
        d-----         1/11/2021   7:19 PM                Videos


Moving away from home
---------------------
To move what directory we are in, we can use ``cd``:

.. admonition:: Command: ``cd``

    ``cd`` stands for **change directory**, and switches the current working directory
    to whatever directory you give it. This is the major way that you move around
    the various directories to find files.

    .. code-block:: console

        $ pwd            # Start off in your home directory
        /Users/username/
        $ cd Downloads   # move into the Downloads folder
        $ pwd
        /Users/username/Downloads
        $ cd ~           # return the the home directory
        $ pwd
        /Users/username


Relative and absolute paths
---------------------------
The earlier examples have hinted at the existence of two types of paths/ways
to reference files. 

The first is using an **absolute path**; this is what we call specifying
the entire path from the filesystem "root" to the file of interest. On Windows,
this means paths like ``C:\Users\username\Downloads``, where we specify the
drive followed by every path component.

On MacOS and Linux, absolute paths start at the root, which is the special
name given to the path ``/``, so absolute paths look like ``/Users/username/Downloads``.

In contrast, **relative paths** allow you to more concisely reference files and directories,
as the paths are calculated relative to the current working directory.

It is fairly intuitive how this works for going into subfolders; just specify the
subfolder name. To be able to reference folders "above" yourself in the tree, we need some
way to reference these parent folders.

Luckily this is standardized; there are two special pseudo-directories accessible everywhere
on the filesystem; the 'current folder' ``.`` and the 'parent folder' ``..``. The current folder
is always a sort of empty operation, but is useful if you want to run scripts in the same directory
as yourself.

When these are passed to a command, they are evaluated starting at the current working directory.

Say that we start off in our downloads folder, ``/Users/username/Downloads``. Then changing directory
to relative directory `..` means going one step "up", to ``/Users/username``

.. code-block:: console

    $ pwd
    /Users/username/Downloads
    $ cd ..
    $ pwd
    /Users/username

We can go up multiple layers at a time by combining these pseudo-directories together. For example,
to go up two directories to ``/Users`` from ``/users/username/Downloads``, you could just write
``cd ../..``.

You can actually combine absolute and relative paths; the parent directory ``..`` will always 
go "up" a directory, effectively removing what comes to the left if combined in this way. For example,
the paths ``/users/username`` and ``/users/username/Desktop/..`` both point to the same thing.

.. admonition:: Demo

    If your shell starts in the Downloads folder ``/Users/amanda/Downloads``, which of the following will
    navigate to the folder ``/Users/amanda/data``? ``/Users/amanda`` is your home folder. [#]_

    1. ``cd .``
    2. ``cd /``
    3. ``cd /Users/amanda/data``
    4. ``cd ../../``
    5. ``cd home/data``
    6. ``cd ../data``
    7. ``cd ~/data``

    .. raw:: html

        <details>
        <summary>Show/hide answer</summary>
        
    The 3rd, 6th, and 7th examples will navigate to the proper folder.

    1. ``.`` will stay in the same directory, ``/Users/amanda/Downloads``
    2. ``/`` is an absolute path to the filesystem root, not the correct folder.
    3. ``/Users/amanda/data`` is the full absolute path to the desired folder, so this works.
    4. ``../../`` evaluates to ``/Users``, the wrong folder.
    5. ``home/data`` will give an error, as it tries to navigate to ``/Users/amanda/Downloads/home/data``
    6. ``../data`` evaluates to ``/Users/amanda/Downloads``, the correct path.
    7. ``~/data`` also works, as ``~`` expands to ``/Users/amanda``

    .. raw:: html

        </details>

File operations
---------------

To finish off our brief intro, we need to talk about moving 
mkdir
cp
mv
nano

.. [#] MacOS image from https://ohmyz.sh/
.. [#] Inspired by the `Software Carpentry examples <https://swcarpentry.github.io/shell-novice/02-filedir/index.html>`__,
       license CC-BY-4.0

Exercise
--------

What directory did you unzip into?