============
Plot Gallery
============

.. toctree::
   :maxdepth: 2
   :glob:

   *

Notes on reproducing examples
-----------------------------

All plots in the plot gallery have a set of implicit imports
and setup code that runs before any given code examples:

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   import seaborn as sns
   sns.set_theme(style="ticks")
   from statannot import add_stat_annotation
   import scipy
   from pathlib import Path
   from matplotlib import ticker as mticker

If you are reproducing the code on your own, make sure that these lines have been run!


All example data needed is available as a zip file: `plot_gallery_data.zip <../_static/files/plot_gallery_data.zip>`__.
