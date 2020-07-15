Contributor guide
=================
Protocols and recipes are written in reStructuredText, a lightweight markdown
language that allows usu to use plain text to describe relatively complicated intent,
letting us make tables, cross-links between different files, image inclusion, and so on.

The Python package Sphinx is used to automatically take this information and make a `searchable
website <https://gallowaylabmit.github.io/protocols>`_, in addition to a printable
PDF version of all of the protocols and recipes,
available `here <https://gallowaylabmit.github.io/protocols/galloway_lab_protocols.pdf>`_.


If you want to make small edits or prefer the browser interface, you can skip all
local setup and go directly to :ref:`contrib_online_edit`.

If you already are familiar with text editors and have an editing/programming environment
already setup, you can go directly to :ref:`contrib_local_build`.

.. _contrib_environ_setup:

Local environment setup
-----------------------


.. _contrib_local_build:

Local building
--------------

.. _contrib_online_edit:

Online editing through Github
-----------------------------
When editing directly through the Github website, you won't be able to check for Sphinx build
errors or fully preview the generated PDF and website until you commit to the branch. For this reason,
doing :ref:`local builds <contrib_local_build>` is preferred.

.. _contrib_repo_layout:

Repository layout
------------------


.. _contrib_rst_basics:

Basics of reStructuredText
--------------------------