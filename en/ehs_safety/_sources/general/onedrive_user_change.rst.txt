
=====================================
Replacing the logged-in OneDrive user
=====================================

IST does not provide "service users", so one of us has to be logged into the lab computers
in order for OneDrive syncing to work. Occasionally, someone will graduate or swap roles,
so we need to change the logged in user.

.. important::
    Make sure that the OneDrive is fully synced, e.g. shows no pending files, before
    swapping users!

1. Select "Free up space" on the entire OneDrive, and on any folders still present. This both confirms
   that the files are uploaded and frees up space on the disk.
2. Wait for the OneDrive to finish syncing these changes.
3. Confirm with `WinDirStat <https://windirstat.net>`__ that none of the files are actively present (e.g. not taking up space).
   WinDirStat should already be downloaded on the lab computers.
4. Logout the old user out of OneDrive, by clicking through the OneDrive settings, accessible via the blue cloud icon.
5. Close OneDrive, and exit out of any file explorer windows.
6. Using Powershell, rename the old OneDrive and Sharepoint folders, as stored in the data directory.

.. code-block:: console
    :class: powershell-console

    > cd D:
    > mv "./Massachusetts Institute of Technology" "./Massachusetts Institute of Technology - old"
    > mv "./OneDrive - Massachusetts Institute of Technology" "./OneDrive - Massachusetts Institute of Technology - old"

7. Login as the new user. It will ask you where to put the new OneDrive folder. **You have to select the D drive**, such that
   the OneDrive path is ``D:\OneDrive - Massachusetts Institute of Technology``
8. Uncheck the backup syncing options (e.g. backup local documents / pictures).
9. Hit the Sync button in the web GUI for both the `main OneDrive <https://mitprod.sharepoint.com/sites/GallowayLab/Shared%20Documents/Forms/AllItems.aspx>`__ and the `timelapse OneDrive <https://mitprod.sharepoint.com/sites/GallowayLab-Timelapse/Shared%20Documents/Forms/AllItems.aspx>`__. It should create a new ``D:\Massachusetts Institute of Technology`` folder that the ``D:\data`` symlink points at.
10. After confirming that the new user has the same synced view of the OneDrive, you can delete the ``- old`` folders you created in the above step.
