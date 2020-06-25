# Galloway Lab protocols and media recipes.

Installation and building
=========================
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

Contributing
============
Protocol files are written in the [reStructuredText format](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html), a relatively lightweight markup language. See the linked primer for details on how to make tables, link images, or link to other protocols.


License
=======
These protocols are available under the Creative Commons 4.0 Attribution International license. Use, share, and modify freely, with attribution!
