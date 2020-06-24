# documentation
Galloway Lab protocols and media recipes.

This is build with Sphinx. To build locally, you must install Python, then do:
```
pip install sphinx sphinx-rtd-theme
```

After Sphinx and the main theme are installed, build with
```
python build.py
```

This builds both the HTML and the PDF versions.

To skip PDF building (for example, if you do not have a local LaTeX install), run
```
python build.py --skip-latex
```
