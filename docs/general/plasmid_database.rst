Plasmid Database
================

Quartzy
-------

The shared lab plasmid database is hosted on `Quartzy <https://app.quartzy.com/groups/190392/inventory?sort=-name>`_. 
Each item is assigned a five-digit ``pKG`` number, in order. 

.. tip:: 
    
    To make sure you add new plasmids with the correct next number, click the "Item Name" column header to sort by this field.
    (It should now have a downward arrow icon.) Alternatively, use the following URL: 
    `https://app.quartzy.com/groups/190392/inventory?sort=-name <https://app.quartzy.com/groups/190392/inventory?sort=-name>`_


To add a new plasmid to the database, click the the "Add Item" button in the top left corner of the Quartzy page. Then, 
click "Skip Lookup" in the top right of the pop-up that appears.

Fill out fields as follows:

=============================== ======================================================================
Field                           Instructions 
=============================== ======================================================================
Vendor                          Company that the plasmid was purchased from (e.g., Addgene)
Catalog #                       Addgene number OR secondary plasmid name/ID (e.g., pGEEC100)
Item Name                       ``pKGNNNNN``, where ``NNNNN`` is the unique five-digit ``pKG`` number
Upload File                     Upload the plasmid map
Type                            Bacterial Stock
Date Stored                     Date glycerol stock made
Plasmid                         Short description of construct (e.g., pLentiX1-EF1a-mGL-bGH)
pKG#                            ``NNNNN``
Plasmid type                    Select from options
Resistance markers              Select from options
Species                         Bacterial cell type (e.g., NEB Stable)
CAS # (under "Specs")           Copy "Plasmid" field
=============================== ======================================================================

Then, click the "Add Item" button in the lower left corner to add the item to the database. 

.. important::

    Double check that all the fields are correct, especially "Item Name", "pKG#", and "Upload File"! These are the most common sources
    of entry errors, particularly when adding a many plasmids at the same time.


Plasmid website
---------------

In addition to hosting the database on Quartzy, we also export plasmid information to a separate 
`website <https://gallowaylabmit.github.io/plasmids/en/latest/>`_. This way, we can group plasmids by alternate names, search plasmid 
names more easily, and add error/warning flags to improperly formatted entries.

The website displays plasmids with errors/warnings by ``pKG`` number, but it is often useful to group these entries by user so that 
the errors/warnings can be fixed. This list can be generated from the same project that builds the website: 
`https://github.com/GallowayLabMIT/plasmids <https://github.com/GallowayLabMIT/plasmids>`_

1. Clone the git repo, then create and activate a virtual environment. See 
   :doc:`Startup checklist when working with repositories <../bootcamp/iap/startup_checklist>` for instructions.
2. In the terminal, run ``python -m quartzy_parser`` to print a list of ``pKG`` numbers with errors and warnings by user.

   - To print only errors or only warnings, add the flag ``--only-errors`` or ``--only-warnings``, respectively.
   - To print only for a subset of users, add the flag ``--users`` followed by the list of users (full names).
   - The numbers printed are the values in the ``pKG`` field, not the "Item Name" field.

.. note::

    This code takes a while (>5 min) to run, since it has to scrape thousands of items from Quartzy.