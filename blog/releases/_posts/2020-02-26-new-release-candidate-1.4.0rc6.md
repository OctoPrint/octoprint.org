---

layout: post
title: 'New release candidate: 1.4.0rc6'
author: foosel
date: 2020-02-26 15:10:00 +0100
card: /assets/img/blog/2020-02/2020-02-26-octoprint-1.4.0rc6-card.png
featuredimage: /assets/img/blog/2020-02/2020-02-26-octoprint-1.4.0rc6-card.png
poster: /assets/img/blog/2020-02/2020-02-26-octoprint-1.4.0rc6-poster.png
excerpt: The sixth release candidate for the upcoming 1.4.0 release fixes some regressions observed with the prior ones.

---

This sixth RC of 1.4.0 fixes some regressions and issues in the new functionality observed with the prior RCs:

> **Improvements**
> 
>   * [#3454](https://github.com/foosel/OctoPrint/issues/3454): Explicitly document changed `LineProcessorStream` behaviour under Python 3
>   * Implement login dialog through a UiPlugin to work around various issues with regards to caching and general workflow with the current approach.
>   * Docs for new access control situation.
>   * Remove some left-overs of old login UI and fix some code comments.
> 
> **Bug fixes**
> 
>   * [#3455](https://github.com/foosel/OctoPrint/issues/3455) (regression): Fix a Python 3 bug with the `self._printer` wrapper injected into plugins.
>   * [#3456](https://github.com/foosel/OctoPrint/issues/3456): Fix firmware info not being reported to plugins if firmware autodetection is disabled. Not a regression, but severe enough to merit inclusion ASAP.
>   * [#3459](https://github.com/foosel/OctoPrint/issues/3459) (regression): Fix login sessions not being persistent even with "Remember me" selected due to forced logout when becoming stale after 24h.
>   * (regression) Fix buggy implementation of `octoprint.server.api.(before|after)_request` hooks.
>   * (regression) Fix missing protection for blueprint plugins
>   * (regression) Fix yet another Python 3 list vs iterator issue

The heads-up regarding Plugins and Python 3 from 1.4.0rc1 still applies.

You can find the full changelog and release notes as usual [on Github](https://github.com/foosel/OctoPrint/releases/tag/1.4.0rc6).

Special thanks to everyone who contributed to this release candidate and provided full, analyzable bug reports, you help
making the next release as stable as possible!

As the past RCs have shown me that a lot of people appear to be unaware of this: **Please do *not* install this RC if you 
expect a fully stable version**. It is not a stable release, it is a release *candidate*, and of the next big release
to boot: severe bugs may occur, and they might be bad enough that they make a manual downgrade to an earlier version 
necessary - maybe even from the command line. 

You should feel comfortable with and capable of possibly having to do this *before* installing an RC.

If you want to and can help test this release candidate, you can find information on how to switch to the 
**"Maintenance RCs"** release channel [in this guide](https://community.octoprint.org/t/how-to-use-the-release-channels-to-help-test-release-candidates/402)
if not already done (also linked below).

**Please provide feedback** on this RC. For general feedback you can use 
[this ticket on the tracker](https://github.com/foosel/OctoPrint/issues/3463).
The information that everything works fine for you is also valuable feedback 😄. **For bug reports** please follow
["How to file a bug report"](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report) - 
I need logs and reproduction steps to fix issues, not just the information that something doesn't work so make sure to
**fill out all fields of the issue template**.

Thanks!

Depending on the feedback regarding this version I'll look into fixing 
any observed regressions and bugs and pushing out a follow-up version 
as soon as possible and necessary.

### Links

  * [Ticket for general feedback](https://github.com/foosel/OctoPrint/issues/3463)
  * [Changelog and Release Notes](https://github.com/foosel/OctoPrint/releases/tag/1.4.0rc6)
  * [How to use release channels to help test release candidates](https://community.octoprint.org/t/how-to-use-the-release-channels-to-help-test-release-candidates/402)
  * [How to file a bug report](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report)
  * [Contribution Guidelines (also relevant for creating bug reports!)](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md)
  * [FAQ](https://faq.octoprint.org)
  * [Documentation](http://docs.octoprint.org/)
  * [How to roll back to an earlier release (OctoPi)](https://community.octoprint.org/t/how-can-i-revert-to-an-older-version-of-the-octoprint-installation-on-my-octopi-image/205)
  * [How to roll back to an earlier release (manual install)](https://community.octoprint.org/t/how-can-i-roll-back-to-an-earlier-version-after-an-update/234)
