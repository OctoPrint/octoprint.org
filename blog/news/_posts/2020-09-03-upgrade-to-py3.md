---
layout: post
title: "Upgrade your OctoPrint install to Python 3!"
author: cp2004
# card: /assets/img/blog/  # TODO image?
# featuredimage: /assets/img/blog/  # TODO image
# poster: /assets/img/blog/  # TODO image
date: 2020-09-03 12:00:00 +0200  # TODO change to publishing date
excerpt: Give OctoPrint a spin on Python 3! Run this simple install script.
---

Since OctoPrint version 1.4.0, the codebase has supported installation on both Python 2 and Python 3 environments, as a result of Python 2's EOL status. However, at the time of writing, less than 2% of tracked installs are running on Python 3.

The main reason for this, was the plugin repository - there was no point installing on Python 3, if you then couldn't install any plugins! These Python 3 installs tended to be manual ones, or developers who needed to test against OctoPrint running on Python 3.

First of all, there needs to be a massive shoutout to everyone who worked to make this possible, from those who contributed to core OctoPrint, to each and every plugin developer who heard the call to update their plugins to be both Python 2 & 3 compatible. As I'm writing this now, 67% of plugins are compatible with Python 3!

## OctoPrint's migration to Python 3
# TODO - Details about OctoPrint's migration?
how long it took, (3 years? that was a long time coming!), some (brief) steps involved for those who are interested, anything else you can think of...?


## I like the sound of it! How can I upgrade?
That's why I'm writing this blog post! I'm Charlie Powell ([@cp2004](https://github.com/cp2004) elsewhere), and I wrote [OctoPrint-Upgrade-To-Py3](https://github.com/cp2004/OctoPrint-Upgrade-To-Py3). It's a neat installation script that will convert your existing OctoPrint install to Python 3, hassle free. Here's how:

**This script is only compatible for users running OctoPi 0.17 and above, or if you have installed OctoPrint manually you will require Python 3.6 or higher**
1. Open a command prompt to where your OctoPrint install is. This could be via SSH, or connected via a monitor & keyboard.
2. Download & run my script with these two commands:
  ```
  curl https://get.octoprint.org/py3/upgrade.py --output upgrade.py
  python3 upgrade.py
  ```
You can then follow the prompts in the script - if you are running OctoPi then the information is automatically collected. If not (or the default install cannot be found) you will be asked for the path to your virtual environment, then the config folder, and start and stop commands.

Give it a minute to run through, installing OctoPrint takes the longest, but it will get you there in the end!

Once the script is finished, reload your web interface and you should be good to go!

## Reverting to your previous install
Just in case something goes wrong, I also built a script that can revert to your old install. You can find more details on the [repository here](https://github.com/cp2004/Octoprint-Upgrade-To-Py3#returning-to-the-old-install)

## Problems, questions or need help?
Get in touch!
* For bugs, or issues running the script, please open an issue on the [Github repository](https://github.com/cp2004/OctoPrint-Upgrade-To-Py3/issues)
* For quick, simple questions about this script **(not support)**, please comment on the post below
* For other support, please post in the [community forum](https://community.octoprint.org) - **please include as much detail about your setup as you can**


