---

layout: post
title: 'New release candidate: 1.3.9rc1'
author: foosel
date: 2018-06-20 15:40:00 +0200
card: /assets/img/blog/2018-06/2018-06-20-octoprint-1.3.9rc1-card.png
featuredimage: /assets/img/blog/2018-06/2018-06-20-octoprint-1.3.9rc1-card.png
poster: /assets/img/blog/2018-06/2018-06-20-octoprint-1.3.9rc1-poster.png
excerpt: The first release candidate of the 1.3.9 release, with various
   improvements and bug fixes.

---

I'm happy to present you the first release candidate of the 1.3.9 release!

[The changelog](https://github.com/foosel/OctoPrint/releases/tag/1.3.9rc1) is once again on the lengthy side 
thanks to the maintenance releases now being spread apart a bit further. Don't let that scare you though 😉

Here are some highlights from the release notes:

  * A very annoying race condition causing OctoPrint to get stuck in "Cancelling" or "Pausing" state was identified
    and fixed. [See also this FAQ entry](https://discourse.octoprint.org/t/octoprint-1-3-7-1-3-8-is-stuck-in-pausing-or-cancelling/1625) which outlines the workarounds for this issue if you didn't yet come 
    across them.
  * An observed incompatibility with pip versions 10 and after that caused issues with plugin installation/uninstallation
    was also identified and fixed (see [here](https://discourse.octoprint.org/t/installing-a-plugin-shows-me-unknown-in-the-popup-i-cant-uninstall-plugins-through-the-plugin-manager-octoprint-up-to-1-3-8-octopi-0-15-0-or-pip-10-x/1746) for details).
  * Added support for plugins to override GCODE analysis provider and live print time estimation with their own 
    implementations through two new hooks 
    [`octoprint.filemanager.analysis.factory`](http://docs.octoprint.org/en/maintenance/plugins/hooks.html#octoprint-filemanager-analysis-factory) 
    and [`octoprint.printer.estimation.factory`](http://docs.octoprint.org/en/maintenance/plugins/hooks.html#octoprint-printer-estimation-factory).
    Feel free to go nuts with this.
  * Allowed more granular control over components to be upgraded through the software update plugin in its settings dialog.
    Instead of performing an "all-or-nothing" update, you may now apply each update individually.
  * Added detection for more unsafe firmwares to the bundled Printer Safety Plugin:
    * Anycubic Mega
    * Malyan M200
    * CR-10S
    * all Repetier firmware versions prior to 0.92
    * any firmware that reports the `THERMAL_PROTECTION` capability as disabled to thermal protection warning (see also [MarlinFirmware/Marlin#10465](https://github.com/MarlinFirmware/Marlin/pull/10465))
  * Added a new bundled plugin ["Action Command Prompt support"](http://docs.octoprint.org/en/maintenance/bundledplugins/action_command_prompt.html) 
    that allows printer firmware to trigger confirmation/decision dialogs in OctoPrint (e.g. for filament swaps).
  * The bundled web server Tornado was updated to a newer version to work around issues with client IP logging and other 
    things. This also led to the discovery a **heads-up for anyone running OctoPrint behind NGINX** - please see the 
    [release notes](https://github.com/foosel/OctoPrint/releases/tag/1.3.9rc1) for details on this.
  * As [announced with the release of OctoPrint 1.3.6](https://octoprint.org/blog/2017/12/12/new-release-1.3.6/), 
    the legacy plugin bundling flag has now been removed again. Plugin authors, please 
    [make sure to check your plugins](https://octoprint.org/blog/2017/12/01/heads-up-plugin-authors/) if you haven't 
    done that so far!
  * And of course there were also quite a number of bugs fixed reported for earlier versions, e.g. the logged in user
    switching to `_api` if the general API key was used to access the API in the same browser instance, inconsistencies
    in the port and baud rate lists between connection and settings dialog, a race condition in resend handling in case
    of missing `ok`s, plus various fixes of typos and grammar in the documentation. 

You can find the full changelog and release notes as usual [on Github](https://github.com/foosel/OctoPrint/releases/tag/1.3.9rc1).

Special thanks to everyone who contributed to this release candidate, especially [@benlye](https://github.com/benlye), 
[@dadosch](https://github.com/dadosch), [@dforsi](https://github.com/dforsi), [@ganey](https://github.com/ganey),
[@malnvenshorn](https://github.com/malnvenshorn), [@ntoff](https://github.com/ntoff), [@tedder](https://github.com/tedder) 
and [@vitormhenrique](https://github.com/vitormhenrique) for their PRs.

**If you are tracking the "Maintenance RC" release channel**, you should soon get an update notification just like you 
are used to from stable releases.

If you want to help test this release candidate and **aren't yet tracking the "Maintenance RCs" release channel**, you
can find information on how to switch [in this guide](https://discourse.octoprint.org/t/how-to-use-the-release-channels-to-help-test-release-candidates/402)
(also linked below).

**If you are not interested in helping to test release candidates**, just ignore this post, 1.3.9 stable will hit 
your instance via the usual way once reports indicate that it's ready 😊

**Please provide feedback** on this RC. For general feedback you can use 
[this ticket on the tracker](https://github.com/foosel/OctoPrint/issues/2688).
The information that everything works fine for you is also valuable feedback 😄 For bug reports please follow
["How to file a bug report"](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report).

Depending on how the feedback for this release candidate turns out, I'll either look into releasing 1.3.9 or fix any 
observed regressions and push out a new release candidate ASAP.

### Links

  * [Ticket for general feedback](https://github.com/foosel/OctoPrint/issues/2688)
  * [Changelog and Release Notes](https://github.com/foosel/OctoPrint/releases/tag/1.3.9rc1)
  * [How to use release channels to help test release candidates](https://discourse.octoprint.org/t/how-to-use-the-release-channels-to-help-test-release-candidates/402)
  * [How to file a bug report](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report)
  * [Contribution Guidelines (also relevant for creating bug reports!)](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md)
  * [FAQ](https://faq.octoprint.org)
  * [Documentation](http://docs.octoprint.org/)
  * [How to roll back to an earlier release (OctoPi)](https://discourse.octoprint.org/t/how-can-i-revert-to-an-older-version-of-the-octoprint-installation-on-my-octopi-image/205)
  * [How to roll back to an earlier release (manual install)](https://discourse.octoprint.org/t/how-can-i-roll-back-to-an-earlier-version-after-an-update/234)
