=========================
Self-hosted data storage
=========================

In 2025, we moved data off of the OneDrive to our own data storage system. This is because OneDrive is limited to 5TB,
and MIT has no current plans to make more space accessible to labs.

Self-hosting your data comes with certain problems that need to be solved: first, you need a server and a robust
way to store the data. Second, you need some way for lab members to login to access and sync the data. Third,
the data needs to be robustly backed up so that we don't lose data.

We solve each of these problems in turn by 1) placing the data on a Synology NAS, which provides a (more) user
friendly method for this type of data storage and redundancy than other alternatives, 2) hosting Nextcloud on the server
and linking it to MIT Touchstone, and 3) backing up all of the data to TSM / Spectrum Protect, a managed backup server
run by MIT. This server is accessible at https://smithsonian.mit.edu, with internal admin interfaces accessible at https://smithsonian-internal.mit.edu (only available within MIT).

Relevant passwords are stored in the Galloway Lab password database, which is in the Sharepoint, in the file ``logins/gallowaylab_main.kbdx``.
Install KeePassXC to access these passwords.

NAS setup
---------
The NAS is a Synology DS1825+. For storage, it currently (2025-11-26) has six 12TB hard drives (Seagate IronWolf) and two 2TB SSDs (Samsung 990 Pro).
The hard drives are are arranged in what is called a RAID: a redundant array of independent disks.
It using a RAID layout called **SHR-2**, which means that it can tolerate two drive failures. E.g., we don't lose any data
until three drives out of the six fail. However, if a drive fails, we do need to replace the failed drive as quickly as possible.

The two SSDs do not participate in the RAID; they are there as a read cache. Commonly accessed files will be automatically copied to the SSDs
for faster access. If the SSDs fail, there is no data loss.

Up to two more drives can be added, and drives can also be replaced with larger hard drives. I (CPJ) recommend using Samsung SSDs
and buying WD Red Pro or Seagate IronWolf hard drives. To replace a drive (either a failed one, or a in-use one in order
to expand available storage), follow the `Synology instructions <https://kb.synology.com/en-global/DSM/help/DSM/StorageManager/storage_pool_expand_replace_disk?version=7>`_.

The NAS user interface is accessible through a webbrowser at https://smithsonian-internal.mit.edu:5000 or over SSH
at ``gallowaylab@smithsonian-internal.mit.edu``. For both cases, the username and password are listed in the password database.


Of note, as of 2025, Synology as a company wants to squeeze profits out of users, and, with varying levels of firmness,
tries to force customers to buy their (white-labeled) hard drives. Western Digital and Seagate make reliable hard drives,
so we just use this `Github project <https://github.com/007revad/Synology_HDD_db>`_ to add any installed hard drives to the
local Synology compatibility database. If you install new drives/SSDs and they come up as not recognized / incompatible in the software,
you need to SSH in and re-run the script.

Note, as always, command line password interfaces do **not** show
astrisks or any other sign that you are typing a password in.

.. code-block:: console
    :class: bash-console

    $ ssh gallowaylab@smithsonian-internal.mit.edu
    $ cd Synology_HDD_db-main
    $ sudo ./syno_hdd_db.sh
    Synology_HDD_db v3.6.111
    DS1825+ x86_64 DSM 7.3.1-86003-1
    StorageManager 1.0.0-01026

    ds1825+_host_v7 version 8008

    Running from: /volume1/@userpreference/gallowaylab/Synology_HDD_db-main/syno_hdd_db.sh

    HDD/SSD models found: 1
    ST12000VN0008-2YS101,SC60,12000 GB

    M.2 drive models found: 1
    Samsung SSD 990 PRO 2TB,5B2QJXD7,2000 GB

    No M.2 PCIe cards found

    No Expansion Units found

    ST12000VN0008-2YS101 already exists in ds1825+_host_v7.db
    Samsung SSD 990 PRO 2TB already exists in ds1825+_host_v7.db

    Support disk compatibility already enabled.

    NVMe support already enabled.

    M.2 volume support already enabled.

    Drive db auto updates already enabled.

    DSM successfully checked disk compatibility.

    You may need to reboot the Synology to see the changes.

Nextcloud setup
---------------
Nextcloud is a piece of open-source software that acts like your own OneDrive
/ Google Drive / Dropbox. It provides sync clients that allows you to access
"cloud" data seamlessly and it has a web interface where you can view files.

Our version of Nextcloud is the one installed by `Nextcloud All-in-one <https://github.com/nextcloud/all-in-one>`_.

This works by running a top-level, "coordinator" Docker container that is responsible for auto-updating Nextcloud,
taking backups of the Nextcloud code, and so on.

There is a special admin account on Nextcloud that is possible to use the direct login feature with.
The username and password are in the password database. The lab computers also use a special
"service account" that is not tied to a Touchstone account.
However, most use will login using Touchstone, using your normal MIT credentials.
    
The AIO interface is accessible through https://smithsonian-internal.mit.edu:8080, but you can only directly access this interface when Nextcloud is not running.
While Nextcloud is running, you can access this by logging in as the admin user to https://smithsonian.mit.edu
and then going to https://smithsonian.mit.edu/settings/admin/overview and clicking the "Open Nextcloud AIO interface" button at the top.


In the worst case that there is large dataloss, you may have to first restore the backup
as described below, and then use the AIO interface to restore from a backup.

In a truly worst-worst case where the Nextcloud database is lost, there is still no file loss:
all of the individual data files are backed up and can be downloaded / reuploaded into a fresh Nextcloud install.


Network setup
-------------
To run all of this software correctly, we use the Synology web UI, as linked above ( https://smithsonian-internal.mit.edu:5000).

In particular, we have setup the firewall settings to block all access except Nextcloud on the "external" network,
accessible through ``smithsonian.mit.edu``. The admin interfaces are only accessible
through ``smithsonian-internal.mit.edu``.

Within the Synology UI, we have setup 1) an automatically-renewed TLS/HTTPS certificate for smithsonian.mit.edu,
and 2) a reverse proxy for this domain. The NAS itself takes care of forwarding requests to the Nextcloud docker containers.

Touchstone setup
----------------
To integrate with Touchstone, we broadly follow MIT IS&T's `instructions <https://wikis.mit.edu/confluence/display/TOUCHSTONE/Provisioning+Steps+for+Shibboleth+SP>`_.

Here, Touchstone is a SAML identity provider (IdP), and we are running a SAML Service Provider (SP).
Our service provider needs to talk to the identity provider to get information on who is logging in.

Nextcloud has a service provider built-in! You can change the configuration at https://smithsonian.mit.edu/settings/admin/saml
(when logged in as the Nextcloud admin user). Registering with Touchstone involves going back and forth
with Touchstone support, configuring our Service Provider on our end to match the settings
on the IdP. An important accessible file is the metadata XML file which SAML uses:
https://smithsonian.mit.edu/apps/user_saml/saml/metadata

Luckily, once setup, this setup should not need to be touched.

Backup setup
------------

For server backups, MIT provides a service called Spectrum Protect / TSM.
We have installed the Spectrum Protect client and packaged it as a docker container.
The Docker container build repository is at https://github.com/GallowayLabMIT/spectrum-protect-container
and the container image is available at ``ghcr.io/gallowaylabmit/spectrum-protect:latest``.

Using this Docker container, we mount two volumes: ``/volume1/NextCloudData`` (all of the actual Nextcloud files)
and ``/volume1/NextCloudBackup`` (the daily backup of the Nextcloud database and other files).
The total contents of these are uploaded to MIT's backup system.

MIT sets the schedule; these backups are run every weekday at 6pm.