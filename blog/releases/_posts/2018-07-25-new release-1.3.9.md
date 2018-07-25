---
layout: post
title: 'New release: 1.3.9'
author: foosel
date: 2018-07-25 16:00:00 +0200
card: /assets/img/blog/2018-07/2018-07-25-octoprint-1.3.9-card.png
featuredimage: /assets/img/blog/2018-07/2018-07-25-octoprint-1.3.9-card.png
poster: /assets/img/blog/2018-07/2018-07-25-octoprint-1.3.9-poster.png
excerpt: Despite the current heat wave pressing down on Germany making development harder than usual, I'm happy to present you OctoPrint 1.3.9. This is a true maintenance release again, consisting of various improvements and fixes.

---

Despite the current heat wave pressing down on Germany making development harder than usual, I'm happy to present 
you OctoPrint 1.3.9. This is a true maintenance release again, consisting of various improvements and fixes. It was 
made possible only through your continued **[support of my work](/support-octoprint/)** 💕.

<a id="heads-up"></a>
**The most important thing first:** If you are still running OctoPrint 1.3.6 when updating to this (or a later) release,
you will get a message that the update failed. This is in fact not the case and caused by an issue only in the update mechanism in 1.3.6 that has since been
fixed in 1.3.7/1.3.8. Just in case though, if you get this message, simply trigger the update again by clicking on
"Check for update now" under Settings > Software Update and clicking the "Update Now" button in the notification again. 
The [release notes](https://github.com/foosel/OctoPrint/releases/tag/1.3.9) also contain some more details on this and
there is also an [FAQ entry](https://discourse.octoprint.org/t/im-running-1-3-6-i-get-an-update-error-when-trying-to-update-to-1-3-9/2971) on 
this.

Also, if you are **running OctoPrint behind NGINX** as a reverse proxy or have **IPv6 support disabled** on the system
running OctoPrint, please make sure to read the additional heads-ups in the [release notes](https://github.com/foosel/OctoPrint/releases/tag/1.3.9).

With that out of the way now on to **some highlights from the release notes**:

  * A very annoying race condition causing OctoPrint to get stuck in "Cancelling" or "Pausing" state was identified
    and fixed. [See also this FAQ entry](https://discourse.octoprint.org/t/octoprint-1-3-7-1-3-8-is-stuck-in-pausing-or-cancelling/1625) which outlines the workarounds for this issue if you didn't yet come 
    across them.

  * An observed incompatibility with pip versions 10 and after that caused issues with plugin installation/uninstallation
    was also identified and fixed (see [here](https://discourse.octoprint.org/t/installing-a-plugin-shows-me-unknown-in-the-popup-i-cant-uninstall-plugins-through-the-plugin-manager-octoprint-up-to-1-3-8-octopi-0-15-0-or-pip-10-x/1746) for details).

  * Added support for plugins to override GCODE analysis provider and live print time estimation with their own 
    implementations through two new hooks 
    [`octoprint.filemanager.analysis.factory`](http://docs.octoprint.org/en/maintenance/plugins/hooks.html#octoprint-filemanager-analysis-factory) 
    and [`octoprint.printer.estimation.factory`](http://docs.octoprint.org/en/maintenance/plugins/hooks.html#octoprint-printer-estimation-factory).
    Feel free to go nuts with this!

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
    things. This also led to the discovery of a **heads-up for anyone running OctoPrint behind NGINX** - please see the 
    [release notes](https://github.com/foosel/OctoPrint/releases/tag/1.3.9rc1) for details on this.

  * As [announced with the release of OctoPrint 1.3.6](https://octoprint.org/blog/2017/12/12/new-release-1.3.6/), 
    the legacy plugin bundling flag has now been removed again. Plugin authors, please 
    [make sure to check and if necessary fix your plugins](https://octoprint.org/blog/2017/12/01/heads-up-plugin-authors/) if you haven't 
    done that so far!

  * Of course there were also quite a number of bugs fixed reported for earlier versions, e.g. the logged in user
    switching to `_api` if the general API key was used to access the API in the same browser instance, inconsistencies
    in the port and baud rate lists between connection and settings dialog, a race condition in resend handling in case
    of missing `ok`s, plus various fixes of typos and grammar in the documentation.

  * ... and much more 

As always this is only a small excerpt, the full list of changes can of course be found in the
[release notes](https://github.com/foosel/OctoPrint/releases/tag/1.3.9).
  
Also see **Further Information** and **Links** below for more information,
where to find help and how to roll back.

I want to also thank everyone who contributed to this release, especially [@benlye](https://github.com/benlye), [@dadosch](https://github.com/dadosch), [@dforsi](https://github.com/dforsi), [@ganey](https://github.com/ganey),[@malnvenshorn](https://github.com/malnvenshorn), [@ntoff](https://github.com/ntoff), [@tedder](https://github.com/tedder) and [@vitormhenrique](https://github.com/vitormhenrique) for their PRs.

And last but not least a huge **Thank you!** to everyone who reported back on the release candidates this time:
[arhi](https://github.com/arhi), [b-morgan](https://github.com/b-morgan), [brandstaetter](https://github.com/brandstaetter), [buchnoun](https://github.com/buchnoun), [CapnBry](https://github.com/CapnBry), [chatrat12](https://github.com/chatrat12), [ChrisHeerschap](https://github.com/ChrisHeerschap), [christianlupus](https://github.com/christianlupus), [chrisWhyTea](https://github.com/chrisWhyTea), [Crowlord](https://github.com/Crowlord), [ctgreybeard](https://github.com/ctgreybeard), [Cyberwizzard](https://github.com/Cyberwizzard), [DrJuJu](https://github.com/DrJuJu), [ejjenkins](https://github.com/ejjenkins), [fieldOfView](https://github.com/fieldOfView), [FormerLurker](https://github.com/FormerLurker), [four-of-four](https://github.com/four-of-four), [Galfinite](https://github.com/Galfinite), [gege2b](https://github.com/gege2b), [HFMan](https://github.com/HFMan), [jjlink](https://github.com/jjlink), [jneilliii](https://github.com/jneilliii), [JohnOCFII](https://github.com/JohnOCFII), [jwg3](https://github.com/jwg3), [kazibole](https://github.com/kazibole), [larp-welt](https://github.com/larp-welt), [McFly99](https://github.com/McFly99), [mod38](https://github.com/mod38), [ntoff](https://github.com/ntoff), [OutsourcedGuru](https://github.com/OutsourcedGuru), [paukstelis](https://github.com/paukstelis), [pingywon](https://github.com/pingywon), [pscrespo](https://github.com/pscrespo), [Rapsey](https://github.com/Rapsey), [tech-rat](https://github.com/tech-rat), [tedder](https://github.com/tedder), [thess](https://github.com/thess), [Thisismydigitalself](https://github.com/Thisismydigitalself), [tibmeister](https://github.com/tibmeister).

### Further Information

It may take up to 24h for your update notification to pop up, so don't 
be alarmed if it doesn't show up immediately after reading this. You
can force the update however via Settings > Software Update > 
Advanced options > Force check for update.

If you get an error about "no suitable distribution" during update, please read 
[this](https://discourse.octoprint.org/t/i-got-some-error-about-no-suitable-distribution-during-update-and-now-my-server-wont-start/235).

**If you have any problems with your OctoPrint installation, please seek 
support on the [community forum](https://discourse.octoprint.org).**

### Links

  * [Changelog and Release Notes](https://github.com/foosel/OctoPrint/releases/tag/1.3.9)
  * [Community forum](https://discourse.octoprint.org)
  * [FAQ](https://faq.octoprint.org)
  * [Documentation](http://docs.octoprint.org/)
  * [Contribution Guidelines (also relevant for creating bug reports!)](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md)
  * [How to file a bug report](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report)
  * [How to roll back to an earlier release (OctoPi)](https://discourse.octoprint.org/t/how-can-i-revert-to-an-older-version-of-the-octoprint-installation-on-my-octopi-image/205)
  * [How to roll back to an earlier release (manual install)](https://discourse.octoprint.org/t/how-can-i-roll-back-to-an-earlier-version-after-an-update/234)

