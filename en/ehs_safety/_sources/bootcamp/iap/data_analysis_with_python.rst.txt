=========================
Data analysis with Python
=========================


Why do data analysis with Python?
=================================

There's many GUI tools out there that do various types of data analysis: Excel, FlowJo, GraphPad Prism, and others.
These are useful, but ultimately are only variably reproducible. "Reproducible" can mean a lot of things, but ideally
scientific data analysis is:

1. Data reproducible: your raw data should be freely accessible and easy to load into analysis software. 
2. Computer/OS reproducible: anyone on a reasonably modern computer should be able to do your analysis.
3. Tool reproducible: anyone can freely access the tools to do your analysis.
4. Minimally "artisanal": the final product of your analysis—graphs, tables, figures—should be as close to the analysis output as possible.

A related ideal is that of **transparency**, or how clear your data analysis is to your readers.


Introduction: the research problem
==================================

For the purposes of this, we are interested in a 

- Introduce a research problem that will use both flow cytometry data.
- Generate some synthetic data for this


Good file layout practices
==========================
- All data in the OneDrive
- All analysis code in a git repo, setup reproducibly.

How do we deal with the fact that we are storing information in different locations?
If we look carefully, there are really only three types of files here:

1. synced raw data in the OneDrive
2. Code to do the analysis and generate output.
3. Output, like figures, that you can regenerate by re-running the code.

- All notebooks in a `notebooks` folder.
- All temporary/regeneratable output in an `output` folder that is `.gitignore`'d
- Large cache data that takes a long time to regenerate may belong in the OneDrive.

The location of the OneDrive is going to change from computer to computer! We fix this by
using a 

.. note::

    Ideally, at the end of the day, you should be able to take your laptop and throw it into the Charles River and lose
    no data and lose no progress. How do we practically make this the case?

    If you store data in the OneDrive, it gets persisted. We also have a separate backup
    process that runs every day.

    If you store your analysis code in a git repository (and sync with e.g. Github from time to time),
    then you will always retain a complete version history of your work, and also persist it.

    There are some caveats that apply when dealing with extremely large datasets, e.g. next gen sequencing datasets that involves fun heavy boxes full of hard drives. If you are curious or need to do something with it, ask around.

To start, navigate to where you want your repository to be (with `cd` and `ls`). A common place create a new git repository, and create a Python virtual environment.

.. code-block:: console

    $ mkdir data_analysis_tutorial
    $ cd data_analysis_tutorial
    $ git init
    $ python -m venv env
    $ . ./env/bin/activate   # on MacOS, Linux
    $ ./env/Scripts/activate # on Windows

We need to install the base packages we use, which are `pandas`, `seaborn`, and `rushd`. We will also be using Parquet files, which means we need to install `pyarrow`. Installing these packages also installs the other packages we use as dependencies (`matplotlib`, `numpy`, etc). You can also specify these explicitly if you want; it does not make a difference.

After we install packages, we snapshot the state into a `requirements.txt` file so that other people (or your future self) can exactly recreate your computational environment.

.. code-block:: console
    
    $ pip install pandas seaborn rushd pyarrow
    $ pip freeze > requirements.txt


The first time you open a notebook, it will want to pick a kernel and install ipykernel. Let it do this

Oh yaml, my yaml
================
- Let's start analyzing some flow data! 
- Whoops, we have metadata we want to attach to these files.
- Time to write a yaml file!

- `learn YAML in Y minutes <https://learnxinyminutes.com/docs/yaml/>`__
- Example of special things, 


- Example
- Using the YAML metadata visualizer in rushd.


Loading flow data
=================

Introduction to Pandas
======================

Tidy data
---------
- Every data point / observation / cell is a _row_, with every measured variable in a column.


Indicies
--------
Certain columns can be made into an index/multi-index. The indicies are special, because they allow for efficient (amortized constant time!) lookups into the dataframe, but are immutable and must be unique.

By default, none of the columns in your loaded data will be an index. Instead, each row gets a numeric index. This is still helpful! It means that even after a lot of dataframe slicing, you can still lookup that datapoint in the original dataframe!

For the purposes of analyzing flow data, we don't care to lookup specific columns in the dataframe, so we spend a lot of our time resetting the index. 

Saving cache files
------------------
- Cache file example

Downsampling data for kdeplots
------------------------------
-

Common data cleaning/manipulation approaches
--------------------------------------------
Use the `Pandas visual cheat sheet <https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf>`__

Merging in extra metadata
~~~~~~~~~~~~~~~~~~~~~~~~~
(use this by defining a "plasmid" field to merge over in the fake data)

- The `join` function is only used for index joins
- Otherwise, you use the `merge` function.

Auto-selecting  gates
~~~~~~~~~~~~~~~~~~~~~

Summarizing data
~~~~~~~~~~~~~~~~
(e.g. group by)

Computing "condition means" to normalize by
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
(use of xs)


Plotting with Seaborn
=====================