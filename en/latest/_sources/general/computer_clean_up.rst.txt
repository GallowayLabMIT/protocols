=============================
Regular computer maintenance
=============================

One of the quarterly lab jobs is to do regular computer maintenance. This makes sure our lab computers
stay up to date and aren't accumulating junk.

1. Run Windows Update. Go to the Start menu / hit the Windows key and search for "Windows update" or "Check for updates".
   Do not update to Windows 11 (yet), but install any other required/recommended updates.
   You do not have to install optional driver updates unless that piece of hardware is causing problems.
2. Reboot if necessary to install updates.
3. Check the disk storage available on each computer. You can use `WinDirStat <https://windirstat.net/>`__
   to easily check how much storage is actually being locally used for the synced OneDrive folders.

   - Make sure that the boot drive (``C:\``) is not filling up. If it is, see what is causing this and correct it (e.g. do stuff like clear unneeded downloads)
   - See if there are unnecessary files locally synced, such as large timelapses. Right click and hit "Free up space"
     to remove them from the local cache.

4. Check for data files stored e.g. on the desktop, on the ``C:\`` drive, really anywhere besides the OneDrive. Move
   all such files you find into a folder and inform people about this. Delete these files after a week or so so we keep
   stuff tidy and all contained in the OneDrive folder.
5. Clean up the "quick access" menu on each computer (the top most part of the explorer window).
   If there are too many e.g. personal folders pinned here so that you can't see the main "keyence" / "attune" ones,
   unpin some of them.
6. Compare the Attune software version with that `available online <https://www.thermofisher.com/us/en/home/global/forms/attune-nxt-software-download-registration.html>`__.
   You have to fill out the form to get to the software page: I recommend using "this-is-a-dumb-requirement@mit.edu" as your email :)
   Do **not install** this update yourself; send a message to the lab and plan when to do this.
   

Installing Attune software updates
----------------------------------
The Attune software updates takes a while, and can, in the worst case, temporarily leave you with a non-functioning Attune.

While that sounds scary, we do need to keep the software up to date, and we can always have a service call if we
really break the software. **Do not ignore these software updates**, just plan them around non-critical experiments.

1. Before beginning, make sure that everyone has exported their FCS files into the OneDrive. Go into the software About page and write down the current software versions.
2. Close the Attune software, if it is open. Make sure the Attune is in the sleeping/idle mode.
3. Launch the "Attune Database Utility"; search in the Start Menu for it. Login with user account ``admin``.
4. Go to the Backup tab and hit "Backup user data". Choose a folder outside the OneDrive to backup to.
5. When the backup is complete, close the database utility and unzip the software update installer.
6. Read the PDF inside the update installer package. **This is not optional**.
7. Run the installer and follow the prompts. This could involve doing many different things, which is why the instructions are important.
8. If the update fails, it is sometimes possible to downgrade by rerunning an earlier installer. You can use the Attune Database Utility to restore your userdata backup as well.
9. If all else fails, ask for a service call to fix it.