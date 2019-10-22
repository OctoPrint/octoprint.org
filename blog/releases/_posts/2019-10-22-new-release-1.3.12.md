---

layout: post
title: 'New release: 1.3.12'
author: foosel
date: 2019-10-22 12:00:00 +0200
card: /assets/img/blog/2019-10/2019-10-22-octoprint-1.3.12-card.png
featuredimage: /assets/img/blog/2019-10/2019-10-22-octoprint-1.3.12-card.png
poster: /assets/img/blog/2019-10/2019-10-22-octoprint-1.3.12-poster.png
excerpt: Still in time for the spooky season of the year 🎃 and after 5 months of development and testing by the community I present you OctoPrint 1.3.12.

---

Still in time for the spooky season of the year I present you OctoPrint 1.3.12 🎃 Almost four months of development and a bit over 
one of release candidate testing went into this, and it will (hopefully) be the last one on the 1.3.x version track as
I'm also prepping things for a first RC of 1.4.0 in the background.

<!--more-->

As every single release (and release candidate) of OctoPrint ever since early 2016 this was made possible only 
through your continued **[support of my work](/support-octoprint/)** 💕.

It has become a bit of a recurring pattern by now, but once again [the changelog](https://github.com/foosel/OctoPrint/releases/tag/1.3.12) 
is on the lengthy side as this release packs a ton of improvements and bug fixes which would be too many to list here. 
Instead I'll just present you with a short excerpt:

  * Add command line interface for user management. Via `octoprint user [list|add|remove|activate|deactivate|password]` it is now possible to list, add, remove, activate & deactivate users or change their passwords right from the command line instead of just through the web interface. That should also make password recovery easier and as simple as `octoprint user password username`.
  * Action command prompts: Add close button to prompts triggered through action commands by the firmware, in case the firmware forgets to add action buttons.
  * Better resilience against garbage on the line on initial connect to the printer due to more handshake attempts.
  * Detect endless resend requests of the same line. If the printer keeps requesting the same line over and over again, something is either seriously wrong with the line or with the connection. In any case, log an error and disconnect.
  * Plugin Manager & Software Update: Prevent plugin installs and updates while throttled due to undervoltage or overheating. This has caused serious issues in the past for people due to system instability.
  * Tracking: Track plugins & versions once every 24h. This is a feature requested repeatedly by plugin developers and will also allow the compilation of something like a Top-10-list.
  * ... and as always a number of bug fixes and small improvements, e.g. fix of an error in the python version detection, removing action command prompts on disconnect from the printer, some unicode issues and more.

There are also **two heads-ups**. One concerns some third party dependencies running into issues when updating from ancient OctoPrint 
versions:

> **Heads-up if you are updating from OctoPrint < 1.3.6**
>
> Due to new versions of third party dependencies, this and future versions of OctoPrint will no longer update via the update script/`python setup.py install` that used to be OctoPrint's standard update mechanism in versions prior to 1.3.6, at least not in older Python environments as they can be found on e.g. OctoPi 0.14. 
> 
> If you haven't yet updated from such a version ([which you really should have done a long time ago](https://octoprint.org/blog/2018/03/15/security-issue-update-to-1.3.6/)) you'll need to [update manually via command line](https://community.octoprint.org/t/how-can-i-update-the-octoprint-installation-on-my-octopi-image/207?u=foosel).

The other is about this release no longer going to support updates through OctoPrint itself on OctoPi 0.14:

> **Heads-up if you are still running OctoPi 0.14**
> 
> As it is becoming increasingly complicated to make OctoPrint *and its third party dependencies* run in the by now ancient Python environment found on OctoPi 0.14, **1.3.12 will no longer allow to be updated from within OctoPrint on OctoPi 0.14** or a similarly outdated Python environment.
> 
> Either [backup](https://community.octoprint.org/t/how-do-i-backup-my-octoprint-settings-on-octopi/1489?u=foosel) and migrate to a new version of OctoPi or run future updates [manually](https://community.octoprint.org/t/how-can-i-update-the-octoprint-installation-on-my-octopi-image/207?u=foosel).
> 
> [See here for more information on the matter](https://community.octoprint.org/t/octoprint-tells-me-it-cant-run-an-update-due-to-my-python-environment-being-outdated-what-do-i-do-now/4756?u=foosel).

The full list of changes can of course be found in the
[Changelog](https://github.com/foosel/OctoPrint/releases/tag/1.3.12) - as always.

Also see the **Further Information** and **Links** below for more information,
where to find help and how to roll back.

I also want to thank everyone who contributed to this release, [@aliaksei135](https://github.com/aliaksei135), [@AndyQ](https://github.com/AndyQ), [@dmweis](https://github.com/dmweis), [@esver](https://github.com/esver), [@gdombiak](https://github.com/gdombiak), [@jackwilsdon](https://github.com/jackwilsdon), [@JanneMantyharju](https://github.com/JanneMantyharju), [@kevans91](https://github.com/kevans91), [@pusewicz](https://github.com/pusewicz), [@rfinnie](https://github.com/rfinnie) and [@tduehr](https://github.com/tduehr) for their PRs.

And last but not least, another special **Thank you!** to everyone who reported back on the release candidates this time: [@arhi](https://github.com/arhi), [@b-morgan](https://github.com/b-morgan), [@EddyMI3d](https://github.com/EddyMI3d), [@ejjenkins](https://github.com/ejjenkins), [@fieldOfView](https://github.com/fieldOfView), [@gcnix](https://github.com/gcnix), [@gege2b](https://github.com/gege2b), [@gryzlov](https://github.com/gryzlov), [@Guilouz](https://github.com/Guilouz), [@JohnOCFII](https://github.com/JohnOCFII), [@kazibole](https://github.com/kazibole), [@louispires](https://github.com/louispires), [@rknobbe](https://github.com/rknobbe) & [@schnello](https://github.com/schnello).

If you are interested in some numbers, according to the anonymous usage tracking 1.3.12rc1 saw 10680 hours of successful prints on 454 unique instances,
1.3.12rc2 saw 5310 hours of successful prints on 381 unique instances, and 1.3.12rc3 saw over 26000 hours or 3 years
of successful prints on 836 unique instances.

### Further Information

It may take up to 24h for your update notification to pop up, so don't 
be alarmed if it doesn't show up immediately after reading this. You
can force the update however via Settings > Software Update > 
Advanced options > Force check for update.

If you get an error about "no suitable distribution" during update, please read 
[this](https://discourse.octoprint.org/t/i-got-some-error-about-no-suitable-distribution-during-update-and-now-my-server-wont-start/235).

**If you have any problems with your OctoPrint installation, please seek 
support on the [community forum](https://community.octoprint.org).**

### Links

  * [Changelog and Release Notes](https://github.com/foosel/OctoPrint/releases/tag/1.3.12)
  * [Community forum](https://community.octoprint.org)
  * [FAQ](https://faq.octoprint.org)
  * [Documentation](http://docs.octoprint.org/)
  * [Contribution Guidelines (also relevant for creating bug reports!)](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md)
  * [How to file a bug report](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report)
  * [How to roll back to an earlier release (OctoPi)](https://discourse.octoprint.org/t/how-can-i-revert-to-an-older-version-of-the-octoprint-installation-on-my-octopi-image/205)
  * [How to roll back to an earlier release (manual install)](https://discourse.octoprint.org/t/how-can-i-roll-back-to-an-earlier-version-after-an-update/234)

