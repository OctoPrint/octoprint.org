---

layout: post
title: 'New release candidate: 1.3.10rc2'
author: foosel
date: 2018-11-13 14:20:00 +0100
card: /assets/img/blog/2018-11/2018-11-13-octoprint-1.3.10rc2-card.png
featuredimage: /assets/img/blog/2018-11/2018-11-13-octoprint-1.3.10rc2-card.png
poster: /assets/img/blog/2018-11/2018-11-13-octoprint-1.3.10rc2-poster.png
excerpt: The second release candidate of the 1.3.10 release, with fixes for regressions discovered
   in 1.3.10rc1 and also a small number of improvements of the newly added functionality.

---

This second RC of 1.3.10 fixes a couple of regressions observed with the first one and also adds some improvements
of existing or newly added functionality that became apparent during testing of RC1:

  * [#2872](https://github.com/foosel/OctoPrint/issues/2872) - Fix Timeout when connecting to printer that doesn't send `start` on connect
  * [#2873](https://github.com/foosel/OctoPrint/issues/2873) - Fix GCODE viewer no longer being able to load files.
  * [#2876](https://github.com/foosel/OctoPrint/issues/2876) - Fix semi functional UI when access control is disabled
  * [#2879](https://github.com/foosel/OctoPrint/issues/2879) - Fix favicon in Firefox
  * Anonymous Usage Tracking: More error resilience for the wizard to possibly work around issues observed with the first RC (for which sadly no information was provided to reproduce and analyse).
  * Anonymous Usage Tracking: Added elapsed time & reason of print failure to tracking (to be able to distinguish cancelled from errored out prints)
  * Anonymous Usage Tracking: Added undervoltage/overheat detection on Pis to tracking (to correlate print failures to power issues, see also [#2878](https://github.com/foosel/OctoPrint/pull/2878)).
  * Printer Safety Plugin: Added Ender 3 stock firmware to detection
  * Softwareupdate: More resilience against invalid data in config
  * Added documentation for `octoprint.util.commandline` module

You can find the full changelog and release notes as usual [on Github](https://github.com/foosel/OctoPrint/releases/tag/1.3.10rc2).

Special thanks to everyone who contributed to this release candidate, especially @tedder for his PR.

As the past RC has shown me that a lot of people appear to be unaware of this: **Please do *not* install this RC if you 
expect a fully stable version**. It is not a stable release, it is a release *candidate*: severe bugs can occur, and 
they can be bad enough that they make a manual downgrade to an earlier version necessary - maybe even from the command line. 

You should be comfortable with and capable of possibly having to do this before installing an RC.

If you want to and can help test this release candidate, you can find information on how to switch to the 
"Maintenance RCs" release channel [in this guide](https://discourse.octoprint.org/t/how-to-use-the-release-channels-to-help-test-release-candidates/402)
if not already done (also linked below).

**Please provide feedback** on this RC. For general feedback you can use 
[this ticket on the tracker](https://github.com/foosel/OctoPrint/issues/2889).
The information that everything works fine for you is also valuable feedback 😄. For bug reports please follow
["How to file a bug report"](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report) - 
I need logs and reproduction steps to fix issues, not just the information that something doesn't work.

Thanks!

Depending on how the feedback for this release candidate turns out, I'll either look into releasing 1.3.10 or fix any 
observed regressions and push out a new release candidate ASAP.

### Links

  * [Ticket for general feedback](https://github.com/foosel/OctoPrint/issues/2889)
  * [Changelog and Release Notes](https://github.com/foosel/OctoPrint/releases/tag/1.3.10rc2)
  * [How to use release channels to help test release candidates](https://discourse.octoprint.org/t/how-to-use-the-release-channels-to-help-test-release-candidates/402)
  * [How to file a bug report](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report)
  * [Contribution Guidelines (also relevant for creating bug reports!)](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md)
  * [FAQ](https://faq.octoprint.org)
  * [Documentation](http://docs.octoprint.org/)
  * [How to roll back to an earlier release (OctoPi)](https://discourse.octoprint.org/t/how-can-i-revert-to-an-older-version-of-the-octoprint-installation-on-my-octopi-image/205)
  * [How to roll back to an earlier release (manual install)](https://discourse.octoprint.org/t/how-can-i-roll-back-to-an-earlier-version-after-an-update/234)
