---

layout: post
title: 'New release candidate: 1.3.7rc1'
author: foosel
date: 2018-03-19 17:00:00 +0100
card: /assets/img/blog/2018-03/2018-03-19-octoprint-1.3.7rc1-card.png
featuredimage: /assets/img/blog/2018-03/2018-03-19-octoprint-1.3.7rc1-card.png
poster: /assets/img/blog/2018-03/2018-03-19-octoprint-1.3.7rc1-poster.png
excerpt: The first release candidate of the 1.3.7 release, with various
   improvements and bug fixes.

---

I'm happy to present you the first release candidate of the 1.3.7 release!

[The changelog](https://github.com/foosel/OctoPrint/releases/tag/1.3.7rc1) is once again on the lengthy side again thanks to the maintenance releases now being spread apart a bit further. Don't let that scare you though 😉

Here are some highlights from the release notes:

  * OctoPrint will now detect prints from SD started through your printer's built-in controller, *if* the firmware fulfills a couple of requirements:
      * it must send a "File opened: ..." message on start of the print
      * it must respond to an immediately sent `M27` with `SD printing byte <current>/<total>`
      * it must stay responsive during ongoing print to allow for regular M27 polls (or push those automatically) or M25 to pause/cancel the print through OctoPrint.
    Additionally there's now support for SD status autoreport capabilities by the firmware.
  * The serial settings were got an UI overhaul to be hopefully less overwhelming.
  * The log management has been extracted into its own bundled plugin and now allows log level management. That is especially interesting to quickly get more detailed logs of specific components in case of bug reports and seeking support but can also help tremendously during plugin development.
  * A new bundled plugin "Printer Safety Check" will try to identify printer/printer firmware with known safety issues such as missing thermal runaway protection and display warning if such a printer is detected.
  * OctoPrint now has native support for the following [@ commands](http://docs.octoprint.org/en/maintenance/features/atcommands.html) that can be used in your GCODE files, scripts and basically everywhere where you'd send a command through OctoPrint to the printer: `@pause` (pauses the print), `@resume` (resumes the print), `@cancel` or `@abort` (cancels the print). More commands can be added through the plugin hooks [`octoprint.comm.protocol.atcommand.*`](http://docs.octoprint.org/en/maintenance/plugins/hooks.html#octoprint-comm-protocol-atcommand-phase).
  * GCODE commands sent through the system now have tags attached that can be utilized by plugins to detect the origin of commands (streamed vs file vs GCODE script vs user input vs plugin), the point where it entered the system and so on. A new logger `octoprint.util.comm.command_phases` was added that when switched to `DEBUG` will log the lifecycle of the commands through the communication layer including tags to `octoprint.log`.
  * Disabled plugins now will not only stay deactivated, they won't even get imported into the system at all anymore to avoid any kind of issues caused by them. 
  * And of course there were also quite a number of bugs fixed reported for earlier versions, e.g. auto connect on startup not working if `AUTO` was set as port, wrong queuing order of cancel script & first line from a printed file on quick start-cancel-start scenarios and incorrect behaviour if a print got cancelled by an error reported from the firmware, plus various fixes of typos and grammar in the documentation. 

**If you are tracking the "Maintenance RC" release channel**, you should soon get an update notification just like you 
are used to from stable releases.

**If you are not interested in helping to test release candidates**, just ignore this post, 1.3.7 stable will hit 
your instance via the usual way once it's ready 😊

You can find the full changelog and release notes as usual [on Github](https://github.com/foosel/OctoPrint/releases/tag/1.3.7rc1).

**Please provide feedback** on this RC. For general feedback you can use 
[this ticket on the tracker](https://github.com/foosel/OctoPrint/issues/2492).
The information that everything works fine for you is also valuable feedback 😄 For bug reports please follow
["How to file a bug report"](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report).

Depending on how the feedback for this release candidate turns out, I'll either look into releasing 1.3.7 or fix any 
observed regressions and push out a new release candidate ASAP.

### Links

  * [Ticket for general feedback](https://github.com/foosel/OctoPrint/issues/2492)
  * [Changelog and Release Notes](https://github.com/foosel/OctoPrint/releases/tag/1.3.7rc1)
  * [Using Release Channels](https://github.com/foosel/OctoPrint/wiki/Using-Release-Channels)
  * [How to file a bug report](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report)
  * [Contribution Guidelines (also relevant for creating bug reports!)](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md)
  * [FAQ](https://faq.octoprint.org)
  * [Documentation](http://docs.octoprint.org/)
  * [How to roll back to an earlier release (OctoPi)](https://discourse.octoprint.org/t/how-can-i-revert-to-an-older-version-of-the-octoprint-installation-on-my-octopi-image/205)
  * [How to roll back to an earlier release (manual install)](https://discourse.octoprint.org/t/how-can-i-roll-back-to-an-earlier-version-after-an-update/234)
