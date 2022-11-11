
=====================================
Replacing the logged-in OneDrive user
=====================================

.. important::
    Make sure that the

1. Logout the old user out of OneDrive.
2. Close OneDrive, and exit out of any file explorer windows.
3. Using Powershell, rename the old OneDrive and Sharepoint folders

.. code-block:: console
    :class: powershell-console

    > cd D:
    > mv "./Massachusetts Institute of Technology" "./Massachusetts Institute of Technology - old"
    > mv "./OneDrive - Massachusetts Institute of Technology" "./OneDrive - Massachusetts Institute of Technology - old"

4. Login as the new user. It will ask you where to put the new OneDrive folder. **You have to select the D drive**, such that
   the OneDrive path is ``D:\OneDrive - Massachusetts Institute of Technology``
5. Uncheck the backup syncing options.
6. Hit the Sync button in the web GUI. It should create a new ``D:\Massachusetts Institute of Technology`` folder that the ``D:\data`` symlink points at.

