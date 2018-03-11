---
layout: post
title: 'New release: 1.3.5'
author: foosel
date: 2017-10-16 16:00:00 +0200
card: /assets/img/blog/2017-10/2017-10-16-octoprint-1.3.5-card.png
featuredimage: /assets/img/blog/2017-10/2017-10-16-octoprint-1.3.5-card.png
poster: /assets/img/blog/2017-10/2017-10-16-octoprint-1.3.5-poster.png
images:
- url: /assets/img/blog/2017-10/2017-10-16-octoprint-1.3.5-temperature_tab.png
  title: Revamped temperature inputs and new mouse over reporting on graph
excerpt: After four release candidates I'm happy to finally present you OctoPrint
  1.3.5. This a true maintenance release again, consisting of various improvements and
  fixes.
comments: false

---

After four release candidates I'm happy to finally present you OctoPrint
1.3.5. This release took way longer to get out of the door than usual thanks to a long
overdue vacation first followed by the nastiest flu of the past years that put me out 
of commission for way too long and still hasn't completely left my system 🤧.

This a true maintenance release again, consisting of various improvements and
fixes. It was made possible only through your continued [support of my work](/support-octoprint/) 💕.

Some highlights from the release notes:

  * Revamped temperature inputs. They now sport some fancy +/- buttons to increment/decrement the
    current temperature (which also auto submit after a couple of seconds) and easier editing by
    keyboard. The temperature offset was also slightly redesigned to make room for that.
  * The temperature graph now allows to mouse over it to get the temperature at that time displayed in 
    the legend instead of the current one.
  * Added a centralized online connectivity check (with opt-in of course). None of the bundled
    plugins will attempt to fetch data from the net when the connectivity check indicates that would fail
    anyhow. This should improve server startup times and various requests when running isolated.
  * Support temperature autoreporting by the firmware instead of polling if the firmware reports to
    support it (so, `Cap:AUTOREPORT_TEMP:1` is present in the response to `M115`).
  * Refactored web interface startup process to minimise risk of race conditions and for speed improvements.
  * Anet A8 firmware now gets auto-detected and treated as Repetier firmware (which it actually appears to be, just
    renamed - thanks Anet for making this even harder)
  * The last, paused and cancel temperature are now made available to GCODE scripts, if known.
  * For printers that have problems with this, position logging on cancel/pause may now be disabled through the
    advanced serial options.
  * The GCODE analysis was moved into its own subprocess, which should improve analysis speed on multi core systems 
    (such as the Pi2 and 3).
  * Fixed a couple of bugs (e.g. one causing cancelling to take too long if you had a lot of files in your
    uploads folder) and removed some potential race conditions.
  * ... and much more

The full list of changes can of course be found in the
[Changelog](https://github.com/foosel/OctoPrint/releases/tag/1.3.5) - as always.

Also see the **Further Information** and **Links** below for more information,
where to find help and how to roll back.

And last but not least a special **Thank you!** to everyone who reported back on the release candidates this time: 
[alexxy](https://github.com/alexxy), [andrivet](https://github.com/andrivet), [b-morgan](https://github.com/b-morgan), 
[BillyBlaze](https://github.com/BillyBlaze), [CapnBry](https://github.com/CapnBry), 
[chippypilot](https://github.com/chippypilot), [ctgreybeard](https://github.com/ctgreybeard), 
[cxt666](https://github.com/cxt666), [DaSTIG](https://github.com/DaSTIG), [fhbmax](https://github.com/fhbmax), 
[fiveangle](https://github.com/fiveangle), [goeland86](https://github.com/goeland86), 
[JohnOCFII](https://github.com/JohnOCFII), [Kunsi](https://github.com/Kunsi), [mgrl](https://github.com/mgrl), 
[MoonshineSG](https://github.com/MoonshineSG), [nate-ubiquisoft](https://github.com/nate-ubiquisoft), 
[Neoolog](https://github.com/Neoolog), [ntoff](https://github.com/ntoff), [oferfrid](https://github.com/oferfrid), 
[roygilby](https://github.com/roygilby), [SAinc](https://github.com/SAinc), [sbts](https://github.com/sbts), 
[thess](https://github.com/thess), [tkurbad](https://github.com/tkurbad), [tsillini](https://github.com/tsillini) and 
[TylonHH](https://github.com/TylonHH).

### Further Information

It may take up to 24h for your update notification to pop up, so don't 
be alarmed if it doesn't show up immediately after reading this. You
can force the update however via Settings > Software Update > 
Advanced options > Force check for update.

If you don't get an "Update Now" button with your update notification, 
read [this](https://github.com/foosel/OctoPrint/wiki/Plugin:-Software-Update#making-octoprint-updateable-on-existing-installations)
or - even more specifically - [this](https://github.com/foosel/OctoPrint/wiki/Plugin:-Software-Update#octoprint--125).

If you are running 1.2.7, get an "Update Now" button but the update is immediately 
reported to be successful without any changes, read 
[this](https://github.com/foosel/OctoPrint/wiki/FAQ#im-running-127-i-tried-to-update-to-a-newer-version-via-the-software-update-plugin-but-im-still-on-127-after-restart).

If you are running 1.2.16, get an "Update Now" button but the update is immediately
producing an error message, read [this](https://github.com/foosel/OctoPrint/wiki/FAQ#im-running-1216-i-tried-to-update-to-a-newer-version-via-the-software-update-plugin-but-i-get-an-error).

If you have any problems with your OctoPrint installation, please seek 
support in the [G+ Community](https://plus.google.com/communities/102771308349328485741)
or the [Mailinglist](https://groups.google.com/group/octoprint). 

### Links

  * [Changelog and Release Notes](https://github.com/foosel/OctoPrint/releases/tag/1.3.5)
  * [FAQ](https://github.com/foosel/OctoPrint/wiki/FAQ)
  * [Documentation](http://docs.octoprint.org/)
  * [Contribution Guidelines (also relevant for creating bug reports!)](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md)
  * [How to file a bug report](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report)
  * [How to roll back to an earlier release (OctoPi)](https://github.com/foosel/OctoPrint/wiki/FAQ#how-can-i-revert-to-an-older-version-of-the-octoprint-installation-on-my-octopi-image)
  * [How to roll back to an earlier release (manual install)](https://github.com/foosel/OctoPrint/wiki/FAQ#how-can-i-roll-back-to-an-earlier-version-after-an-update)

