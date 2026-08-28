==================
Slack bot (labbot)
==================

The lab slackbot does a lot of convenient things:

1. Uploads sequencing results automatically to the sequencing channel.
2. Handles lab job reminders.
3. Runs the label printer.

This slack bot is mostly written in Python, using the convenient slack-bolt Python library to interact with the Slack API.

Accessing the labbot server
----------------------------
The lab slack bot runs on a (free) cloud server, specifically a f1.micro Google Cloud Platform server.
This server is "owned" by Katie's Google account. The server is currently accessible at the domain name ``gallowaylabapi.meson.us``.
If the server is stopped and restarted, Google will likely change its IP address. If this happens, the subdomain
has to be pointed at the new IP address.

Currently, that domain name is a subdomain owned by Christopher Johnstone. I (CPJ) am happy to keep this subdomain going, as it doesn't
cost me any money. It's possible to point a different domain at this if needed in the future, but the Slack settings need to be updated, since
Slack servers expect to talk to the labbot at ``gallowaylabapi.meson.us``.

To have direct access to the server, you need to be added as an editor to the project by Katie, through the GCP project settings.

For Katie, the GCP console is available at https://console.cloud.google.com and permissions are editable from https://console.cloud.google.com/iam-admin/iam
This view allows for "Grant access" and "Remove access" for other people. Luckily, the labbot server only needs to be
connected to directly if you are updating Python dependencies; most other actions don't need direct access.

Updating labbot
---------------

Normal updates
***************
Through the labbot homepage within slack, if you click on **Dev Tools**, you will open a page where you can restart the labbot.
If it is misbehaving, this restart will often fix problems.

There is also a **Validate commit** button on here. This is how you normally update the labbot software. You can type in
either a specific git commit (identified by a commit hash) or a specific git branch. The labbot will validate that the
commit didn't change the depedencies, then give you an option to **Update and restart**. Upon clicking this, the labbot
will update to the latest version without having to manually log in.

Unusual updates
***************
If you update the dependencies (say, for adding a new feature or updating the slack-bolt package) or if you need
to modify a config file that lives on the server, you need to SSH into the server.

1. Have Katie grant you access to the labbot server.
2. Log into GCP (at https://console.cloud.google.com). Go specifically to the Compute Engine tab (https://console.cloud.google.com/compute/instances)
3. Click the SSH button to spawn an SSH connection into the server.

This will log you into the server running the labbot. If you want to edit the labbot files,
you need to switch to the labbot user. The server files are in a folder called ``labbot`` within the labbot user's home directory.


.. code-block:: console
    :class: bash-console

    $ sudo su labbot
    $ cd
    $ ls
    labbot
    $ cd labbot/server

Inside the server folder, you can activate the ``env`` virtual environment, updated config files, and so on.

To start, stop, and restart the labbot from the server, you need to be using your user account. If you are currently 
switched to the labbot user, exit back to your user first:

.. code-block:: console
    :class: bash-console

    $ whoami
    labbot
    $ exit
    $ whoami
    <whatever your google account is>

and then use the requisite ``systemctl`` command depending on what you want to do:

.. code-block:: console
    :class: bash-console

    $ sudo systemctl start labbot
    $ sudo systemctl stop labbot
    $ sudo systemctl restart labbot



Label printing
--------------
The label printer client connects to the label print server run by the slack bot.
This software is running on the computer that is behind the (paper) printer.
You can connect a monitor and mouse/keyboard for debugging if needed.

That computer is running the software in the ``clients/label_printer`` folder of the labbot repo.
The software runs in a loop, and connects to the labbot server to pull labels to print.

It is very simple; likely, this computer will never have to be touched. If weird stuff happens,
you can unplug the computer and plug it back in, or force shutdown and restart.
This has fixed every problem with the label printing client to date.