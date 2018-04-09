---
layout: post
title: 'New release: 1.3.7'
author: foosel
date: 2018-04-09 16:50:00 +0200
card: /assets/img/blog/2018-04/2018-04-09-octoprint-1.3.7-card.png
featuredimage: /assets/img/blog/2018-04/2018-04-09-octoprint-1.3.7-card.png
poster: /assets/img/blog/2018-04/2018-04-09-octoprint-1.3.7-poster.png
excerpt: After several months of work I'm happy to present you OctoPrint 1.3.7. This a true maintenance release again, consisting of various improvements and fixes.
images:
- url: /assets/img/blog/2018-04/2018-04-09-serial_settings_ui_overhaul.gif
  title: The serial settings got an UI overhaul to be hopefully less cluttered and overwhelming
- url: /assets/img/blog/2018-04/2018-04-09-safetycheck.png
  title: A new bundled plugin "Printer Safety Check" will warn you if your printer's firmware is known to have safety issues.

---

After several months of work I'm happy to present you OctoPrint 1.3.7. This a true maintenance release again, 
consisting of various improvements and fixes. It was made possible only through your continued 
**[support of my work](/support-octoprint/)** 💕.

**Some highlights from the release notes**:

  * OctoPrint will now detect prints from SD started through your printer's built-in controller, *if* the firmware fulfills a couple of requirements:
      * it must send a "File opened: ..." message on start of the print
      * it must respond to an immediately sent `M27` with `SD printing byte <current>/<total>`
      * it must stay responsive during ongoing print to allow for regular M27 polls (or push those automatically) or M25 to pause/cancel the print through OctoPrint.
      * when the print is done or gets cancelled it must must send `Done printing file` or respond to `M27` with `Not SD printing`.
    Additionally there's now support for SD status autoreport capabilities by the firmware.

  * The serial settings got an UI overhaul to be hopefully less cluttered and overwhelming. Serial related settings that so far were located in the "Features" section of the settings were moved to "Serial Connection" were they make more sense. 

  * The log management has been extracted into its own bundled plugin and now allows log level management. That is especially interesting to quickly get more detailed logs of specific components in case of bug reports and seeking support but can also help tremendously during plugin development.

  * A new bundled plugin "Printer Safety Check" will try to identify printer/printer firmware with known safety issues such as missing thermal runaway protection on connection and display warning if such a printer is detected. [Read more about it here](https://discourse.octoprint.org/t/octoprint-tells-me-that-my-printers-firmware-lacks-mandatory-safety-features-what-does-this-mean/350/1).

  * OctoPrint now has native support for the following [@ commands](http://docs.octoprint.org/en/master/features/atcommands.html) that can be used in your GCODE files, scripts and basically everywhere where you'd send a command through OctoPrint to the printer: `@pause` (pauses the print), `@resume` (resumes the print), `@cancel` or `@abort` (cancels the print). More commands can be added through the plugin hooks [`octoprint.comm.protocol.atcommand.*`](http://docs.octoprint.org/en/master/plugins/hooks.html#octoprint-comm-protocol-atcommand-phase).

  * GCODE commands sent through the system now have tags attached that can be utilized by plugins to detect the origin of commands (streamed vs file vs GCODE script vs user input vs plugin), the point where it entered the system and so on. A new logger `octoprint.util.comm.command_phases` was added that when switched to `DEBUG` will log the lifecycle of the commands through the communication layer including tags to `octoprint.log`.

  * Disabled plugins now will not only stay deactivated, they won't even get imported into the system at all anymore to avoid any kind of issues caused by them. 

  * Of course there were also quite a number of bugs fixed reported for earlier versions, e.g. auto connect on startup not working if `AUTO` was set as port, wrong queuing order of cancel script & first line from a printed file on quick start-cancel-start scenarios and incorrect behaviour if a print got cancelled by an error reported from the firmware, plus various fixes of typos and grammar in the documentation. 

  * ... and much more 

As always this is only a small excerpt, the full list of changes can of course be found in the
[Changelog](https://github.com/foosel/OctoPrint/releases/tag/1.3.7).

Also see **Further Information** and **Links** below for more information,
where to find help and how to roll back.

And last but not least a special **Thank you!** to everyone who reported back on the release candidates this time:
[aaronkeck](https://github.com/aaronkeck), [akurz42](https://github.com/akurz42), [andrivet](https://github.com/andrivet), [anthonyst91](https://github.com/anthonyst91), [arhi](https://github.com/arhi), [b-morgan](https://github.com/b-morgan), [BryanSmithDev](https://github.com/BryanSmithDev), [chippypilot](https://github.com/chippypilot), [ChrisHeerschap](https://github.com/ChrisHeerschap), [Crowlord](https://github.com/Crowlord), [dforsi](https://github.com/dforsi), [drdelaney](https://github.com/drdelaney), [FormerLurker](https://github.com/FormerLurker), [goeland86](https://github.com/goeland86), [inspiredbylife](https://github.com/inspiredbylife), [jbjones27](https://github.com/jbjones27), [jesasi](https://github.com/jesasi), [jneilliii](https://github.com/jneilliii), [JohnOCFII](https://github.com/JohnOCFII), [kantlivelong](https://github.com/kantlivelong), [lnx13](https://github.com/lnx13), [makaper](https://github.com/makaper), [markwal](https://github.com/markwal), [MiquelAdell](https://discourse.octoprint.org/u/MiquelAdell), [ml0w](https://github.com/ml0w), [mmotley999](https://github.com/mmotley999), [mrhanman](https://github.com/mrhanman), [SCiunczyk](https://github.com/SCiunczyk), [tdub415](https://github.com/tdub415), [tedder42](https://discourse.octoprint.org/u/tedder42), [thatjoshguy](https://github.com/thatjoshguy), [wescrockett](https://github.com/wescrockett).

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

  * [Changelog and Release Notes](https://github.com/foosel/OctoPrint/releases/tag/1.3.7)
  * [Community forum](https://discourse.octoprint.org)
  * [FAQ](https://faq.octoprint.org)
  * [Documentation](http://docs.octoprint.org/)
  * [Contribution Guidelines (also relevant for creating bug reports!)](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md)
  * [How to file a bug report](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report)
  * [How to roll back to an earlier release (OctoPi)](https://discourse.octoprint.org/t/how-can-i-revert-to-an-older-version-of-the-octoprint-installation-on-my-octopi-image/205)
  * [How to roll back to an earlier release (manual install)](https://discourse.octoprint.org/t/how-can-i-roll-back-to-an-earlier-version-after-an-update/234)

