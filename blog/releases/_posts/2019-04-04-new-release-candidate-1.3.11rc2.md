---

layout: post
title: 'New release candidate: 1.3.11rc2'
author: foosel
date: 2019-04-04 17:00:00 +0200
card: /assets/img/blog/2019-04/2019-04-04-octoprint-1.3.11rc2-card.png
featuredimage: /assets/img/blog/2019-04/2019-04-04-octoprint-1.3.11rc2-card.png
poster: /assets/img/blog/2019-04/2019-04-04-octoprint-1.3.11rc2-poster.png
excerpt: The second release candidate for the upcoming 1.3.11 stable release.

---

This second RC of 1.3.10 fixes a couple of regressions observed with the first one and also adds some improvements
of existing or newly added functionality that became apparent during testing of RC1:

> **Improvements**
> 
>   * More resilience against broken configurations.
>   * More resilience against platform startup issues during environment detection.
>   * Error Tracking: Severely restrict what gets tracked:
>     * we are only interested in handled core exceptions or unhandled exceptions
>     * we are not interested at all in `SerialException`
> 
> **Bug fixes**
> 
>   * [#3088](https://github.com/foosel/OctoPrint/issues/3088) (regression) - Fix 500 error on index rendering in case of plugins that use unicode in plugin vars.
>   * [#3089](https://github.com/foosel/OctoPrint/issues/3089) (regression) - Fix missing `_chamberTemp` definition
>   * [#3090](https://github.com/foosel/OctoPrint/issues/3090) (regression) - Fix missing method causing an exception on `/api/printer/tool` endpoint
>   * [#3091](https://github.com/foosel/OctoPrint/issues/3091) (regression) - Printer Safety Check: Fix unicode errors in certain communication scenarios.
>   * [#3092](https://github.com/foosel/OctoPrint/issues/3092) - Fix invalid tool parameter detection on `/api/printer/tool` endpoint.
>   * [#3098](https://github.com/foosel/OctoPrint/issues/3098) - Backup: Exclude temporary timelapse files as well if timelapses are excluded from backup.
>   * Fix missing default value for `self._errorValue` in comm layer.
>   * Don't read return code on async system commands, it won't work.
 
You can find the full changelog and release notes as usual [on Github](https://github.com/foosel/OctoPrint/releases/tag/1.3.11rc2).

Special thanks to everyone who contributed to this release candidate!

As the past RCs have shown me that a lot of people appear to be unaware of this: **Please do *not* install this RC if you 
expect a fully stable version**. It is not a stable release, it is a release *candidate*: severe bugs may occur, and 
they might be bad enough that they make a manual downgrade to an earlier version necessary - maybe even from the command line. 

You should feel comfortable with and capable of possibly having to do this *before* installing an RC.

If you want to and can help test this release candidate, you can find information on how to switch to the 
"Maintenance RCs" release channel [in this guide](https://community.octoprint.org/t/how-to-use-the-release-channels-to-help-test-release-candidates/402)
if not already done (also linked below).

**Please provide feedback** on this RC. For general feedback you can use 
[this ticket on the tracker](https://github.com/foosel/OctoPrint/issues/3103).
The information that everything works fine for you is also valuable feedback 😄. **For bug reports** please follow
["How to file a bug report"](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report) - 
I need logs and reproduction steps to fix issues, not just the information that something doesn't work so make sure to
**fill out all fields of the issue template**.

Thanks!

Depending on how the feedback for this release candidate turns out, I'll either look into releasing 1.3.11 or fix any 
observed regressions and push out a new release candidate ASAP.

### Links

  * [Ticket for general feedback](https://github.com/foosel/OctoPrint/issues/3103)
  * [Changelog and Release Notes](https://github.com/foosel/OctoPrint/releases/tag/1.3.11rc2)
  * [How to use release channels to help test release candidates](https://community.octoprint.org/t/how-to-use-the-release-channels-to-help-test-release-candidates/402)
  * [How to file a bug report](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report)
  * [Contribution Guidelines (also relevant for creating bug reports!)](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md)
  * [FAQ](https://faq.octoprint.org)
  * [Documentation](http://docs.octoprint.org/)
  * [How to roll back to an earlier release (OctoPi)](https://community.octoprint.org/t/how-can-i-revert-to-an-older-version-of-the-octoprint-installation-on-my-octopi-image/205)
  * [How to roll back to an earlier release (manual install)](https://community.octoprint.org/t/how-can-i-roll-back-to-an-earlier-version-after-an-update/234)
