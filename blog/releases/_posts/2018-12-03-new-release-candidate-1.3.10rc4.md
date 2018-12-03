---

layout: post
title: 'New release candidate: 1.3.10rc4'
author: foosel
date: 2018-12-03 14:00:00 +0100
card: /assets/img/blog/2018-12/2018-12-03-octoprint-1.3.10rc4-card.png
featuredimage: /assets/img/blog/2018-12/2018-12-03-octoprint-1.3.10rc4-card.png
poster: /assets/img/blog/2018-12/2018-12-03-octoprint-1.3.10rc4-poster.png
excerpt: The fourth release candidate of the 1.3.10 release, with fixes and improvements for the newly introduced
  backup & restore plugin.

---

This fourth RC of 1.3.10 improves and fixes a couple of issues discovered in the newly introduced backup & restore plugin
and one localization issue, discovered during testing of RC3:

> ### Improvements
> 
>   * Backup: Exclude `generated`, `logs` and `watched` folders from backup
>   * Backup: Use base version for version check on restore
> 
> ### Bug fixes
> 
>   * [#2920](https://github.com/foosel/OctoPrint/issues/2920) - Backup: Fix wrong compatibility check logic in plugin install during restore
>   * Backup: Disable restore on Windows servers where it's not supported thanks to the Windows file system
>   * Backup: Fix reporting of restore failure due to version mismatch or other cases of an invalid backup
>   * Backup: Fix feedback in UI during restore, start feedback right on upload of backup
>   * Printer Safety: Fix localization of warning message

You can find the full changelog and release notes as usual [on Github](https://github.com/foosel/OctoPrint/releases/tag/1.3.10rc4).

Special thanks to everyone who contributed to this release candidate and provided full, analysable bug reports.

As the past RCs have shown me that a lot of people appear to be unaware of this: **Please do *not* install this RC if you 
expect a fully stable version**. It is not a stable release, it is a release *candidate*: severe bugs can occur, and 
they can be bad enough that they make a manual downgrade to an earlier version necessary - maybe even from the command line. 

You should be comfortable with and capable of possibly having to do this before installing an RC.

If you want to and can help test this release candidate, you can find information on how to switch to the 
"Maintenance RCs" release channel [in this guide](https://discourse.octoprint.org/t/how-to-use-the-release-channels-to-help-test-release-candidates/402)
if not already done (also linked below).

**Please provide feedback** on this RC. For general feedback you can use 
[this ticket on the tracker](https://github.com/foosel/OctoPrint/issues/2939).
The information that everything works fine for you is also valuable feedback 😄. **For bug reports** please follow
["How to file a bug report"](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report) - 
I need logs and reproduction steps to fix issues, not just the information that something doesn't work so make sure to
**fill out all fields of the issue template**.

Thanks!

Depending on how the feedback for this release candidate turns out, I'll either look into releasing 1.3.10 or fix any 
observed regressions and push out a new release candidate ASAP.

### Links

  * [Ticket for general feedback](https://github.com/foosel/OctoPrint/issues/2939)
  * [Changelog and Release Notes](https://github.com/foosel/OctoPrint/releases/tag/1.3.10rc4)
  * [How to use release channels to help test release candidates](https://discourse.octoprint.org/t/how-to-use-the-release-channels-to-help-test-release-candidates/402)
  * [How to file a bug report](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report)
  * [Contribution Guidelines (also relevant for creating bug reports!)](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md)
  * [FAQ](https://faq.octoprint.org)
  * [Documentation](http://docs.octoprint.org/)
  * [How to roll back to an earlier release (OctoPi)](https://discourse.octoprint.org/t/how-can-i-revert-to-an-older-version-of-the-octoprint-installation-on-my-octopi-image/205)
  * [How to roll back to an earlier release (manual install)](https://discourse.octoprint.org/t/how-can-i-roll-back-to-an-earlier-version-after-an-update/234)
