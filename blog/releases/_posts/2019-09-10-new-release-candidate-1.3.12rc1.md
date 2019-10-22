---

layout: post
title: 'New release candidate: 1.3.12rc1'
author: foosel
date: 2019-09-10 16:30:00 +0200
card: /assets/img/blog/2019-09/2019-09-10-octoprint-1.3.12rc1-card.png
featuredimage: /assets/img/blog/2019-09/2019-09-10-octoprint-1.3.12rc1-card.png
poster: /assets/img/blog/2019-09/2019-09-10-octoprint-1.3.12rc1-poster.png
excerpt: The first release candidate for the upcoming 1.3.12 stable release.

---

Summer draws to a close and it's time for a stable release. Therefore I present thee the first step towards that goal
in shape of the first release candidate of 1.3.12.

[The full changelog](https://github.com/foosel/OctoPrint/releases/tag/1.3.12rc1) is packed with 
improvements and fixes of existing functionality, most of which is once again behind the scenes. Some highlights:

  * Add command line interface for user management. Via `octoprint user [list|add|remove|activate|deactivate|password]` it is now possible to list, add, remove, activate & deactivate users or change their passwords right from the command line instead of just through the web interface. That should also make password recovery easier and as simple as `octoprint user password username`.
  * Action command prompts: Add close button to prompts triggered through action commands by the firmware, in case the firmware forgets to add action buttons.
  * Better resilience against garbage on the line on initial connect to the printer due to more handshake attempts.
  * Detect endless resend requests of the same line. If the printer keeps requesting the same line over and over again, something is either seriously wrong with the line or with the connection. In any case, log an error and disconnect.
  * Plugin Manager & Software Update: Prevent plugin installs and updates while throttled due to undervoltage or overheating. This has caused serious issues in the past for people due to system instability.
  * Tracking: Track plugins & versions once every 24h. This is a feature requested repeatedly by plugin developers and will also allow the compilation of something like a Top-10-list.
  * ... and as always a number of bug fixes and small improvements, e.g. fix of an error in the python version detection, removing action command prompts on disconnect from the printer, some unicode issues and more.

There are also two heads-ups. One concerns some third party dependencies running into issues when updating from ancient OctoPrint 
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
 
You can find the full changelog and release notes as usual [on Github](https://github.com/foosel/OctoPrint/releases/tag/1.3.12rc1).

Special thanks to everyone who contributed to this release candidate and provided full, analyzable bug reports and pull requests, especially [@aliaksei135](https://github.com/aliaksei135), [@AndyQ](https://github.com/AndyQ), [@dmweis](https://github.com/dmweis), [@esver](https://github.com/esver), [@gdombiak](https://github.com/gdombiak), [@jackwilsdon](https://github.com/jackwilsdon), [@JanneMantyharju](https://github.com/JanneMantyharju), [@kevans91](https://github.com/kevans91), [@pusewicz](https://github.com/pusewicz), [@rfinnie](https://github.com/rfinnie) and [@tduehr](https://github.com/tduehr) for their PRs.

As the past RCs have shown me that a lot of people appear to be unaware of this: **Please do *not* install this RC if you 
expect a fully stable version**. It is not a stable release, it is a release *candidate*: severe bugs may occur, and 
they might be bad enough that they make a manual downgrade to an earlier version necessary - maybe even from the command line. 

You should feel comfortable with and capable of possibly having to do this *before* installing an RC.

If you want to and can help test this release candidate, you can find information on how to switch to the 
"Maintenance RCs" release channel [in this guide](https://community.octoprint.org/t/how-to-use-the-release-channels-to-help-test-release-candidates/402)
if not already done (also linked below).

**Please provide feedback** on this RC. For general feedback you can use 
[this ticket on the tracker](https://github.com/foosel/OctoPrint/issues/3268).
The information that everything works fine for you is also valuable feedback 😄. **For bug reports** please follow
["How to file a bug report"](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report) - 
I need logs and reproduction steps to fix issues, not just the information that something doesn't work so make sure to
**fill out all fields of the issue template**.

Thanks!

Depending on how the feedback for this release candidate turns out, I'll either look into releasing 1.3.12 or fix any 
observed regressions and push out a new release candidate ASAP.

### Links

  * [Ticket for general feedback](https://github.com/foosel/OctoPrint/issues/3268)
  * [Changelog and Release Notes](https://github.com/foosel/OctoPrint/releases/tag/1.3.12rc1)
  * [How to use release channels to help test release candidates](https://community.octoprint.org/t/how-to-use-the-release-channels-to-help-test-release-candidates/402)
  * [How to file a bug report](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report)
  * [Contribution Guidelines (also relevant for creating bug reports!)](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md)
  * [FAQ](https://faq.octoprint.org)
  * [Documentation](http://docs.octoprint.org/)
  * [How to roll back to an earlier release (OctoPi)](https://community.octoprint.org/t/how-can-i-revert-to-an-older-version-of-the-octoprint-installation-on-my-octopi-image/205)
  * [How to roll back to an earlier release (manual install)](https://community.octoprint.org/t/how-can-i-roll-back-to-an-earlier-version-after-an-update/234)
