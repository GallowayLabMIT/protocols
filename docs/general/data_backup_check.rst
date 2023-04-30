====================================
Checking data backups
====================================

Onedrive backups
================
The OneDrive and timelapse OneDrive are the main place
we store data. Each OneDrive has 10TB of storage. We
can create more OneDrives, but eventually storing much greater than 20TB
will run into logistical issues because of all of the OneDrive juggling.

Files in the OneDrive are chiefly backed up for us, through the normal interface.
Deleted files stay in a special OneDrive recycle bin for around 90 days, after which they are deleted.

What happens if someone accidentally deletes data after it expires, or we need to get an older version of data?
We now have a Network Attached Storage (NAS) with about 18TB of storage space. The Keyence
computer has a sync client that duplicates both OneDrives onto this storage device. This means
we have a secondary backup of everything in the OneDrive.

Once a year checks
------------------
Once a year, during the IAP infrastructure day(s), you should check and restore an older version of a file using the NAS,
just for practice.

- Login to the NAS at https://ashurbanipal.mit.edu and ???
- Using the Synology sync client on the Keyence computer, test recovering a file by ???

NGS backups
============
When we do next generation sequencing, we can easily generate terabytes of data.
Storing this in the OneDrive would quickly exceed the space available. To safely keep
raw sequencing data, we duplicate this data onto pairs of physical hard drives, and use a
backup helper to store *parity* data, which allows for recovery in the case of file corruption.

The pairs of hard drives are stored in fireproof/waterproof safe boxes. Ideally, we store
one of the safe boxes somewhere in lab/in an office, and store another one offsite (with Katie).

Which NGS datasets are stored on which pair of hard drives is listed in a
`spreadsheet in the OneDrive <https://mitprod.sharepoint.com/:x:/s/GallowayLab/ERLZeBrX4OVIpMRjG9Q5foIBV0iK1xhWT1DEF2Qg1dgGCA?e=0OhHi8>`__

Adding a new NGS dataset checklist
----------------------------------
- Compress the dataset, either into a ``.tgz`` or a ``.zip``.
- Check the hard drive spreadsheet, and determine if the dataset fits on one of the existing disk pairs (including an extra 3-5% for parity data).
- If there is not enough room, order a new pair of hard drives.
  There are suggestions listed in the `backup helper instructions <https://github.com/GallowayLabMIT/cold_backups>`__;
  as of 2023, it is recommended to get 6TB Western Digital Blue CMR (conventional magnetic recording) hard drives. This might
  change in the future, so read the instructions!
- Locate and bring both fireproof safes to lab. One is likely with Katie or otherwise offsite from 66.
- Copy the dataset onto both drives, into the `data` folder.
- Follow the `backup helper instructions <https://github.com/GallowayLabMIT/cold_backups>`__

Once a year checklist
---------------------
The main instructions on how to use the backup helper are available at https://github.com/GallowayLabMIT/cold_backups

In short, once a year you should:

- Bring both fireproof safes to lab. One is likely with Katie or otherwise offsite.
- For each pair of drives, load each into the external hard drives enclosures and connect to the same computer.
- Follow the `backup helper instructions <https://github.com/GallowayLabMIT/cold_backups>` to run the auto-verification.
- Do the suggested spot-check manual check on one of the files both as practice and to make sure the automated helper is working.
- Check the desiccant packs. You can either weigh them to see how much water they have absorbed, or look at the color of the bead.
  You can regenerate the desiccant by microwaving the packs for the listed time (or until they lose water mass).
