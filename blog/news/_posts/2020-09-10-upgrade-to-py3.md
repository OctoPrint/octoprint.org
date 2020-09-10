---
layout: post
title: "Upgrade your OctoPrint install to Python 3!"
author: cp2004
card: /assets/img/blog/2020-09/20200910-octoprint-py3-card.png
featuredimage: /assets/img/blog/2020-09/20200910-octoprint-py3-card.png
poster: /assets/img/blog/2020-09/20200910-octoprint-py3-poster.png
date: 2020-09-10 13:45:00 +0200
excerpt: Give OctoPrint a spin on Python 3! Run this simple install script.
---

Since OctoPrint version 1.4.0, the codebase has supported installation on both Python 2 and Python 3 
environments, as a result of Python 2's EOL status. However, at the time of writing, only 2.3% of all tracked installs are running on Python 3.

The main reason for this is that all current OctoPi releases up until now shipped with OctoPrint installed under Python 2. 
But there was also the issue of compatibility of the plugins in the plugin repository - 
there's no point installing on Python 3, if you then can't install any plugins! Thus so far Python 3 
installs tended to be manual ones, or developers who needed to test against OctoPrint running on Python 3.

Things have changed though! As I'm writing this now, 67% of plugins are compatible with Python 3! There needs to 
be a massive shoutout to everyone who worked to make this possible, from those who contributed to core 
OctoPrint, to each and every plugin developer who heard the call to update their plugins to be both 
Python 2 & 3 compatible. It's now time to migrate more installs to Python 3.

### Wait a second! Python 2 EOL? Python 3? What does all of this even mean?

Python is the programming language that OctoPrint is primarily written in. Up until the start of the year, there were
two versions of Python -- Python 2 and 3 -- with some big changes and incompatibilities between them. 
Python 2 has been officially declared end-of-life (EOL) by the Python maintainers 
as of January 1st of 2020, meaning it will no longer get any more updates (but obviously still continue to work as-is!). 

This meant that OctoPrint, only compatible to Python 2 up until version 1.4.0, had to become Python 3 compatible in 
order to be future-proof (and also to profit of the new possibilities and performance gains that Python 3 offers). 
However, as all OctoPi images up to and including 0.17 also shipped with a Python 2 environment for OctoPrint, 
going Python 3 *exclusive* was not an option. Thus OctoPrint was 
made compatible with both 2 **and** 3. This happened with the release of OctoPrint 1.4.0 and took well over a year and 
the combined work of Gina and four awesome contributors to get done and shipped.
 
So as of the release of OctoPrint 1.4.0, it is compatible to both major Python versions, 2 and 3. However, the 
underlying Python environments (e.g. the 64000 instances of OctoPi currently visible in the anonymous usage tracking)
are still primarily Python 2.

Since OctoPrint at some point will drop support for Python 2 as well sometime after March 2021 (the current 
compatibility to both versions means an enormous amount of maintanence overhead, plus no Python 3 exclusive 
improvements can be used), the goal is to migrate all installations out in the field -- that's you! -- to Python 3 as 
soon as possible. Future OctoPi versions starting with 0.18 will already ship with Python 3 on board, however existing
installations will not automatically update. They can be updated manually however, and even though not all
plugins are yet Python 3 compatible, this might still be worth your while as Python 3 in general has better performance
than Python 2 out of the box!

### I like the sound of it! How can I upgrade?

That's why I'm writing this blog post! I'm Charlie Powell ([@cp2004](https://github.com/cp2004) elsewhere), and I wrote [OctoPrint-Upgrade-To-Py3](https://github.com/cp2004/OctoPrint-Upgrade-To-Py3). It's a neat installation script that will convert your existing OctoPrint install to Python 3, hassle free. Here's how:

**This script is only compatible for users running OctoPi 0.17 and above, or if you have installed OctoPrint manually you will require Python 3.6 or higher**

1. Open a command prompt to where your OctoPrint install is. This could be via SSH, or connected via a monitor & keyboard.
2. Download & run my script with these two commands:
  ```
  curl -L https://get.octoprint.org/py3/upgrade.py --output upgrade.py
  python3 upgrade.py
  ```
You can then follow the prompts in the script - if you are running OctoPi then the information is automatically collected. If not (or the default install cannot be found) you will be asked for the path to your virtual environment, then the config folder, and start and stop commands.

Give it a minute to run through, installing OctoPrint takes the longest, but it will get you there in the end!

Once the script is finished, reload your web interface and you should be good to go!

## Reverting to your previous install

Just in case something goes wrong, I also built a script that can revert to your old install. You can find more details on the [repository here](https://github.com/cp2004/Octoprint-Upgrade-To-Py3#returning-to-the-old-install).

## Problems, questions or need help?

**Get in touch!**

* For bugs, or issues running the script, please open an issue on the [Github repository](https://github.com/cp2004/OctoPrint-Upgrade-To-Py3/issues)
* For quick, simple questions about this script **(not support)**, please comment on the post below
* For other support, please post in the [community forum](https://community.octoprint.org) - **please include as much detail about your setup as you can**


