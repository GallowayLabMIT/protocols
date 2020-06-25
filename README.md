# Galloway Lab protocols and media recipes.

## Installation and building
This documentation is build with Sphinx. To build locally, install Python 3,
then do:
```
pip install sphinx sphinx-rtd-theme
```

Then, the HTML and PDF documentation can be build with:
```
python build.py
```

To skip PDF building (for example, if you don't have a local LaTeX install),
run:
```
python build.py --skip-latex
```

Build output is in the folder `output`. The HTML version can be loaded by clicking on `output\html\index.html`

This documentation is also automatically build and published to [](gallowaylabmit.github.io/protocols) on every push.

## Contributing
Protocol files are written in the [reStructuredText format](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html), a relatively lightweight markup language. See the linked primer for details on how to make tables, link images, or link to other protocols. All protocols are located in the `docs` folder.

This project has one custom directive: an estimated time directive. To use it, simply write:
``
.. time:: 35 billion years

``
The empty line after the directive is important! Remember that reStructuredText directives need that empty line to distinguish them from other text.

### Adding a new protocol
When adding a new protocol, ensure that it has a title so it shows up properly in the table of contents! The title is the first piece of text surrounded by equal signs. An example protocol:
```
=================
The best protocol
=================

.. time:: 3 hours

Protocol
========
  1. Prep the cool science.
  2. Do the cool science.
  3. Clean up the cool science.

.. note::
  1. Make sure to read this before starting!
```

### Adding a new subsection
If you want to add additional structure to the protocols, the easiest way to do it is to add a new subfolder. Inside that folder, add a file `index.rst` with the following:
```
=================
Subsection name
=================

.. toctree::
   :maxdepth: 2
   :glob:
   
   *
```
This will auto-include all other `*.rst` files present in the same directory. If you are doing further nesting, you may want to include the glob `*/index` to include all subdirectories as well. An example of this is in [docs\protocols\index.rst](docs\protocols\index.rst).




License
=======
These protocols are available under the [Creative Commons 4.0 Attribution International license](https://creativecommons.org/licenses/by/4.0/). Use, share, and modify freely, with attribution!
