---

layout: post
title: 'New release candidate: 1.3.11rc3'
author: foosel
date: 2019-04-11 14:25:00 +0200
card: /assets/img/blog/2019-04/2019-04-11-octoprint-1.3.11rc3-card.png
featuredimage: /assets/img/blog/2019-04/2019-04-11-octoprint-1.3.11rc3-card.png
poster: /assets/img/blog/2019-04/2019-04-11-octoprint-1.3.11rc3-poster.png
excerpt: The third release candidate for the upcoming 1.3.11 stable release.

---

This third RC of 1.3.10 fixes a couple of regressions observed with past RCs and also adds some improvements
of existing or newly added functionality that became apparent during testing of the past RCs:

> ### Improvements
> 
>   * Don't confuse users with current `pip`'s "Python 2.7 is EOL" messages
>   * Define empty `UI_API_KEY` for backwards compatibility with third party plugins
>   * Add config flag `server.ignoredIncompleteStartup` to override incomplete startup detection
>   * Hardening against errors triggered during print time estimation
>   * Introduce setting to disable exclusive claim on serial port. There might be issues with this out there in the field, so having the option to disable it is a good thing.
>   * Error Tracking: Further restriction of what gets tracked
> 
> ### Bug fixes
> 
>   * [#3105](https://github.com/foosel/OctoPrint/issues/3105) (regression) - Virtual printer: Fix an encoding issue
>   * [#3108](https://github.com/foosel/OctoPrint/issues/3108) (regression) - Fix bug in port detection
>   * [#3111](https://github.com/foosel/OctoPrint/issues/3111) (regression) - Refresh port list after disconnect to detect vanishing ports
>   * [#3115](https://github.com/foosel/OctoPrint/issues/3115) (regression) - Fix extra newlines in `serial.log` and empty lines on terminal
>   * [#3116](https://github.com/foosel/OctoPrint/issues/3116) - Fix potential division by zero
>   * Fix wrong textual representation of `STARTING` state
>   * Fix some potential encoding errors in the comm layer
>   * Fix for the file list in the UI not getting refreshed after an SD list refresh from the printer.
 
You can find the full changelog and release notes as usual [on Github](https://github.com/foosel/OctoPrint/releases/tag/1.3.11rc3).

Special thanks to everyone who contributed to this release candidate!

As the past RCs have shown me that a lot of people appear to be unaware of this: **Please do *not* install this RC if you 
expect a fully stable version**. It is not a stable release, it is a release *candidate*: severe bugs may occur, and 
they might be bad enough that they make a manual downgrade to an earlier version necessary - maybe even from the command line. 

You should feel comfortable with and capable of possibly having to do this *before* installing an RC.

If you want to and can help test this release candidate, you can find information on how to switch to the 
"Maintenance RCs" release channel [in this guide](https://community.octoprint.org/t/how-to-use-the-release-channels-to-help-test-release-candidates/402)
if not already done (also linked below).

**Please provide feedback** on this RC. For general feedback you can use 
[this ticket on the tracker](https://github.com/foosel/OctoPrint/issues/3120).
The information that everything works fine for you is also valuable feedback 😄. **For bug reports** please follow
["How to file a bug report"](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report) - 
I need logs and reproduction steps to fix issues, not just the information that something doesn't work so make sure to
**fill out all fields of the issue template**.

Thanks!

### Links

  * [Ticket for general feedback](https://github.com/foosel/OctoPrint/issues/3120)
  * [Changelog and Release Notes](https://github.com/foosel/OctoPrint/releases/tag/1.3.11rc3)
  * [How to use release channels to help test release candidates](https://community.octoprint.org/t/how-to-use-the-release-channels-to-help-test-release-candidates/402)
  * [How to file a bug report](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report)
  * [Contribution Guidelines (also relevant for creating bug reports!)](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md)
  * [FAQ](https://faq.octoprint.org)
  * [Documentation](http://docs.octoprint.org/)
  * [How to roll back to an earlier release (OctoPi)](https://community.octoprint.org/t/how-can-i-revert-to-an-older-version-of-the-octoprint-installation-on-my-octopi-image/205)
  * [How to roll back to an earlier release (manual install)](https://community.octoprint.org/t/how-can-i-roll-back-to-an-earlier-version-after-an-update/234)
