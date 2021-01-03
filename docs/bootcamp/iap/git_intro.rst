=======================
An introduction to Git
=======================

Motivation
----------
Even if you haven't used version control software before, you have probably encountered two
types of version control:

1. Linear time-based snapshots. This can either be manually done (e.g. you append a
   date to documents and copy files when you want to make a new version), or automatically
   done (e.g. you are storing documents in Dropbox, and it stores time snapshots for the
   last 30 days automatically).
2. Online, live multi-person editing, like in Overleaf and Google Drive.

These techniques are useful, but have limitations. Time-based snapshots often fail if you want
to have multiple people editing simultaneously without massive headaches, and online live editing
only works if you have permanent internet access, intermediate states are meaningful (e.g. saving
mid-sentence is fine for manuscripts, but would throw a syntax error for code), and you don't
actually care about saving a detailed history.

For us, having robust version control without these limitations makes our coding work easier to share,
easier to reproduce (how do you regenerate a plot made with a previous code version you
didn't know you needed?), and easier to do shared work.

In the CS community, this is a solved problem; the field has coalesced around using the 
version control system called ``git``. There are competing version control systems, including
Subversion, Mercurial, and Fossil, but ``git`` has emerged as the clear winner with the emergence
of supporting webservices Github, Sourceforge, GitLab, and others.

Unfortunately for us, ``git`` is also by far the most powerful and complicated version control system,
so before jumping into ``git`` commands, let's consider an example:


    Git is a simple, but extremely powerful system. Most people try to teach
    Git by demonstrating a few dozen commands and then yelling “tadaaaaa.”
    I believe this method is flawed. Such a treatment may leave you with the ability
    to use Git to perform simple tasks, but the Git commands will still feel like
    magical incantations. Doing anything out of the ordinary will be terrifying.
    Until you understand the concepts upon which Git is built, you’ll feel like a
    stranger in a foreign land.

    -- Tom Preston-Werner, `The Git Parable <https://tom.preston-werner.com/2009/05/19/the-git-parable.html>`__

Say you are trying to do version control for files related to a paper manuscript.
You have some figures, and a main ``.docx``

.. code-block::
    :class: box-spacing-override

    .
    ├─ figure1.ai
    ├─ figure2.ai
    └─ manuscript.docx

How should you track the version history of this? First create a new directory/folder, which is
called ``working`` here, as it is the directory you would be actively working on/editing.

.. code-block::
    :class: box-spacing-override

    .
    └─ working
       ├─ figure1.ai
       ├─ figure2.ai
       └─ manuscript.docx

After some hacking in Illustrator, you're happy with the way the figures look. To save this version, you
just copy the entire working folder to a ``snapshot-01`` folder and promise yourself that you won't further
edit what is inside the snapshot folders.

.. code-block::
    :class: box-spacing-override

    .
    │─ snapshot-01
    │  ├─ figure1.ai
    │  ├─ figure2.ai
    │  └─ manuscript.docx
    └─ working
       ├─ figure1.ai
       ├─ figure2.ai
       └─ manuscript.docx

After you do some more work, (some directories are shown collapsed, without showing content), such
as adding new figures, you might have lots of snapshots:

.. code-block::
    :class: box-spacing-override

    .
    │─ snapshot-01
    │─ snapshot-02
    │─ snapshot-03
    │─ snapshot-04
    │  ├─ figure1.ai
    │  ├─ figure2.ai
    │  ├─ figure3.ai
    │  └─ manuscript.docx
    └─ working
       ├─ figure1.ai
       ├─ figure2.ai
       ├─ figure3.ai
       └─ manuscript.docx

How are you supposed to remember what we changed in each of these? To help yourself,
you decide to add a new file, ``message.txt`` to each snapshot created. Inside the message,
you decide to add the date, our name, and some free-form message that describes what happened
in that version snapshot. A ``message.txt`` might look like:

::

    Author: Christopher Johnstone <cjohnsto@mit.edu>
    Date:   Jan 11 2021

        Made Figure 3 300% more aesthetic!

The snapshots now look like the following.
Note that we add the ``message.txt`` after we copy the working folder to a new snapshot folder.

.. code-block::
    :class: box-spacing-override

    .
    │─ snapshot-01
    │─ snapshot-02
    │─ snapshot-03
    │─ snapshot-04
    │─ snapshot-05
    │  ├─ message.txt
    │  ├─ figure1.ai
    │  ├─ figure2.ai
    │  ├─ figure3.ai
    │  └─ manuscript.docx
    └─ working
       ├─ figure1.ai
       ├─ figure2.ai
       ├─ figure3.ai
       └─ manuscript.docx


After some more work, you end up revising the manuscript while also trying out a new
revision of ``figure1.ai``. You want to save your updated manuscript version, but the
figure isn't quite ready yet. How do we save the manuscript edits into a snapshot while
leaving the in-progress figure edits out of the snapshot? There isn't an obvious
way to do this with this folder setup, so you decide to make another special directory
called ``stage`` (as in a stage to set and later snapshot).

With the edits marked with a ``*``, we initially have:

.. code-block::
    :class: box-spacing-override

    .
    │─ snapshot-01
    │─ snapshot-02
    │─ snapshot-03
    │─ snapshot-04
    │─ snapshot-05
    │  ├─ message.txt
    │  ├─ figure1.ai
    │  ├─ figure2.ai
    │  ├─ figure3.ai
    │  └─ manuscript.docx
    │─ stage
    │  ├─ figure1.ai
    │  ├─ figure2.ai
    │  ├─ figure3.ai
    │  └─ manuscript.docx
    └─ working
       ├─ *figure1.ai
       ├─ figure2.ai
       ├─ figure3.ai
       └─ *manuscript.docx

Now instead of directly copying the ``working`` folder into a snapshot, we first
copy the changes we want into ``stage``, while leaving files we are still actively
editing in ``working``. Copying the modified manuscript to ``stage``:

.. code-block::
    :class: box-spacing-override

    .
    │─ snapshot-01
    │─ snapshot-02
    │─ snapshot-03
    │─ snapshot-04
    │─ snapshot-05
    │  ├─ message.txt
    │  ├─ figure1.ai
    │  ├─ figure2.ai
    │  ├─ figure3.ai
    │  └─ manuscript.docx
    │─ stage
    │  ├─ figure1.ai
    │  ├─ figure2.ai
    │  ├─ figure3.ai
    │  └─ *manuscript.docx
    └─ working
       ├─ *figure1.ai
       ├─ figure2.ai
       ├─ figure3.ai
       └─ *manuscript.docx

then we make a new snapshot from ``stage``:

.. code-block::
    :class: box-spacing-override

    .
    │─ snapshot-01
    │─ snapshot-02
    │─ snapshot-03
    │─ snapshot-04
    │─ snapshot-05
    │  ├─ message.txt
    │  ├─ figure1.ai
    │  ├─ figure2.ai
    │  ├─ figure3.ai
    │  └─ manuscript.docx
    │─ snapshot-06
    │  ├─ message.txt
    │  ├─ figure1.ai
    │  ├─ figure2.ai
    │  ├─ figure3.ai
    │  └─ *manuscript.docx
    │─ stage
    │  ├─ figure1.ai
    │  ├─ figure2.ai
    │  ├─ figure3.ai
    │  └─ *manuscript.docx
    └─ working
       ├─ *figure1.ai
       ├─ figure2.ai
       ├─ figure3.ai
       └─ *manuscript.docx



Finally, this whole setup seems to be working well, and you want to go share your work
with fellow lab-mates. While you could just copy the entire folder and share created
snapshots, this would be inherently linear; only one person could work on this at a
certain time! To solve these issues, among others, you decide to assign arbitrary, unique
names to snapshots, such as ``2a8aba``. With these arbitrary names, it's hard to tell what
order you made the snapshots in, so you also add a ``parent`` field.


.. code-block::
    :class: box-spacing-override

    .
    │─ snapshots
    │  ├─ c3612a
    │  │─ 86ac2d
    │  │─ acd748
    │  │─ fb9742
    │  │─ 12d276
    │  │  ├─ message.txt
    │  │  ├─ figure1.ai
    │  │  ├─ figure2.ai
    │  │  ├─ figure3.ai
    │  │  └─ manuscript.docx
    │  └─ 2a8aba
    │     ├─ message.txt
    │     ├─ figure1.ai
    │     ├─ figure2.ai
    │     ├─ figure3.ai
    │     └─ *manuscript.docx
    │─ stage
    │  ├─ figure1.ai
    │  ├─ figure2.ai
    │  ├─ figure3.ai
    │  └─ *manuscript.docx
    └─ working
       ├─ *figure1.ai
       ├─ figure2.ai
       ├─ figure3.ai
       └─ *manuscript.docx

After this renaming, the most recent ``message.txt`` (in ``snapshot-06``, renamed to ``2a8aba``)
could read:

::

    Snapshot: 2a8aba
    Parent: 12d276
    Author: Christopher Johnstone <cjohnsto@mit.edu>
    Date:   Jan 12 2021

        Updated the manuscript with method details.


We're almost ready to jump into Git; the last thing to note from this example is that specifying
parents of snapshots means that we no longer (necessarily) have a linear history; instead,
the history forms a tree (a graph without cycles). Trees have nice properties, like always being
able to determine all of your ancestors.