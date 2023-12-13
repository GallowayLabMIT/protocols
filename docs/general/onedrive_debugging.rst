
=======================================================
OneDrive sync problems and replacing the logged-in user
=======================================================

OneDrive sync problem debugging
-------------------------------

.. warning::

   The OneDrive sync client is very sensitive and does not like being logged into
   from multiple user accounts! Keep track of who is logged in on each computer.
   If you want to switch, following the instructions at the bottom.

   Unfortunately, after an authentication change that MIT made, we have to regularly
   log back into the computers to get them to sync, roughly once every other month.

Sometimes, the OneDrive client on the computers will either lose its sync connection or
get stuck in a state where files are not syncing.

The first debugging step is always to run the OneDrive reset. A OneDrive reset does not
change the logged-in user, it just clears the database that OneDrive uses to keep track of files.
After a reset, OneDrive will rescan **all** of the files in the synced folder and figure out which
it has to sync.

To reset:

1. Hit ``Win-R`` on the keyboard to open the run dialog. Enter ``%localappdata%\Microsoft\OneDrive\onedrive.exe /reset``
2. You should see the OneDrive client close and disappear from the taskbar.
3. After a few seconds, launch OneDrive again from the start menu. The first start after a reset does
   some additional reset stuff, so the client will close itself.
4. After a few more seconds, launch OneDrive again. This time, it should stay up.

.. note::

   A full resync takes a long time, upward of several hours. You can use the PowerToys toolbar
   icon and set it to "Keep computer awake -> Indefinitely" until it finishes.

It still doesn't work!
~~~~~~~~~~~~~~~~~~~~~~
If syncing is still not happening, or it is forcing users to login, then the user cache probably
needs to be fixed.

1. If possible, log out of the OneDrive client, unlinking it.
2. Run the OneDrive reset command from above (``%localappdata%\Microsoft\OneDrive\onedrive.exe /reset``), but do
   **not** start the client again.
3. Using Windows Explorer, navigate to ``%localappdata%/Microsoft`` (paste into the address bar). Delete the subfolders
   ``IdentityCache`` and ``OneAuth``
4. Start the OneDrive client.
5. Log back in. When it asks where to put the OneDrive folder, pick:
   
   - for the Keyence computer (Edward): ``D:\``
   - for the Attune computer (Jacob): ``D:\Users\INSTR-ADMIN``

   After making your selection, the dialog should read "Your onedrive folder is ``D:\OneDrive - Massachusetts Institute of Technology``"
6. Following the linking instructions from :ref:`the IAP sync instructions <OneDrive syncing>`. This involves hitting "Sync" in the web client.
7. The client should recognize that there is already data in the selected folder. Accept this by hitting "use this folder".

Unable to pin OneDrive folders to the quick access
--------------------------------------------------
If you are unable to re-pin folders like the Keyence or Attune folders, it may be
due to a corrupt Quick Access folder. The solution is documented on the `Microsoft forums  <https://answers.microsoft.com/en-us/windows/forum/all/cant-pin-images-and-documents-folder-to-quick/7c0380af-8d9b-4b85-ae0d-d7481dc67efe>`__

Using a **administrator command prompt** (search for command prompt in the windows-key / start menu, then right click and hit "Run as administrator". This won't work in Powershell) run the following:

1. ``del /F /Q %APPDATA%\Microsoft\Windows\Recent\*``
2. ``del /F /Q %APPDATA%\Microsoft\Windows\Recent\AutomaticDestinations\*``
3. ``del /F /Q %APPDATA%\Microsoft\Windows\Recent\CustomDestinations\*``
4. Reboot the computer


User replacement
----------------

IST does not provide "service users", so a lab member has to be logged into the lab computers
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