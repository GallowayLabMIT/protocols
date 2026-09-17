=============================
Gating cells in FlowJo
=============================

Flow cytometers save data in ``.fcs`` files, one per sample. While it is possible to load these files in Python, it is (currently) easier to do an initial gating step 
in FlowJo, a paid flow cytometry analysis software from Waters Biosciences (formerly BD Biosciences). Follow the instructions below to gate single cells and save these 
as ``.csv`` files, one file per sample. The ``.csv`` files can then be loaded into Python as described in 
:doc:`Loading flow cytometry data </training/data_analysis/flow-data-analysis>`.

We use FlowJo to gate single cells, i.e., to select events on the cytometer that represent measurements from individual cells and to exclude debris 
and cell doublets or clumps. This is commonly done by first gating **cells**: in an FSC-A vs SSC-A plot, select the main cluster of events to remove debris (smaller) 
and obvious clumps (larger). Then, gate **single cells**: in an FSC-A vs FSC-H (or SSC-A vs SSC-H) plot of the gated cell population, exclude the population with similar 
height but larger area to remove doublets.

.. figure:: /img/gating-in-FlowJo.png
    :align: center
    :figwidth: 90%

    **Left:** Black polygon outline shows the cell population, labeled "cells", on an FSC-A vs SSC-A plot. 
    **Right:** Black polygon outline shows the single cell population, labeled "singlets", a subset of the "cells" population on
    an FSC-A vs FSC-H plot.

|

1. Load ``.fcs`` files.

    Open the FlowJo software and log in with the lab username and password. Do not download a new version of the software, if prompted. 
    Then, drag the ``.fcs`` files from your experiment into the new workspace.

2. Draw a gate to select cells.

    Double click on one of your samples. A new window should pop up with an FSC-A vs SSC-A plot. Use the **polygon gate** tool 
    (button at the top) to gate region representing the main cell population. Draw the gate by clicking to add vertices. 
    Call this population "cells" or something similar.

    .. figure:: /img/flowjo-draw-gates.PNG
        :align: center
        :figwidth: 50%

        Use the polygon gate tool to select cells from all events.

3. Draw a gate to select single cells.

    Double click within the cells gate to select this population. A new window will appear; change the axes to plot FSC-A vs FSC-H.
    Use the polygon gate tool to select single cells, excluding the subpopulation of events with larger FSC-A values. (See top image.)
    Call this population "singlets" or something similar.

4. Apply these gates to all samples.

    To apply the same gates uniformly to all samples, select the "cells" and "singlets" populations and drag them to the 
    "All Samples" group at the top of the workspace.

    Spot-check several samples to ensure the gates capture the desired populations across conditions.

    .. image:: /img/flowjo-drag-gates.PNG
        :align: center
        :width: 100%

5. *Optional:* Apply compensation.

    .. admonition:: TODO 

        Description of compensation to be added. 

6. Export the single cell populations as ``.csv`` files.

    Right click on the "All samples" group and select "Export / Concatenate Group".

    .. image:: /img/flowjo-export.PNG
        :align: center
        :width: 100%

    In the pop-up menu, select the "CSV -- scale values" format and a destination folder in Smithsonian, somewhere near the 
    original ``.fcs`` files.

    The default filename will be ``export_[wellID]_singlets.csv``, which is convenient for loading into Python later.
    However, you can change this in the "Advanced Options" tab if you added other metadata when flowing (usually only 
    relevant for tube experiments—additional metadata can be easily mapped later based on well IDs).

    The file structure in Smithsonian might look something like this:

        ::

            data/
            ├── attune/
            │   ├── your-name/
            |   |   ├── 2026.01.01_exp001/
            │   │   │   ├── fcs/
            |   |   |   |   ├── A1.fcs
            |   |   |   |   ├── A2.fcs
            |   |   |   |   └── ...
            │   │   │   ├── csv/
            |   |   |   |   ├── export_A1_singlets.csv
            |   |   |   |   ├── export_A2_singlets.csv
            |   |   |   |   └── ...
            │   │   │   ├── wells.yaml
            │   │   │   └── exp001.wsp
            │   |   └── ...
            │   └── ...
            └── ...

7. Save the FlowJo workspace.
   
    To keep a record of your gating, save the FlowJo workspace (``.wsp`` file) near the related files.
    Then, quit the software.

.. note::

    Because the FlowJo software requires a paid subscription, it is currently only available on the lab computers (e.g., Attune computer). 
    If possible, it is convenient to perform this single cell gating immediately after finishing your Attune run. 
    You can then do all subsequent data analysis steps on your own computer, beginning with 
    :doc:`Loading flow cytometry data </training/data_analysis/flow-data-analysis>`.