---

layout: post
title: 'New release candidate: 1.4.1rc2'
author: foosel
date: 2020-07-08 13:15:00 +0200
card: /assets/img/blog/2020-07/2020-07-08-octoprint-1.4.1rc2-card.png
featuredimage: /assets/img/blog/2020-07/2020-07-08-octoprint-1.4.1rc2-card.png
poster: /assets/img/blog/2020-07/2020-07-08-octoprint-1.4.1rc2-poster.png
excerpt: The second release candidate for the upcoming 1.4.1 release that fixes a bunch of regressions observed in the first one

---

This second RC of 1.4.1 fixes some regressions observed with the first one:

> **Bug fixes**
> 
>   * [#3627](https://github.com/OctoPrint/OctoPrint/issues/3627) (regression) - Fix auto detection scenario with port AUTO, set baudrate and one possible port
>   * [#3628](https://github.com/OctoPrint/OctoPrint/issues/3628) (regression) - Fix unclosed tags in German translation which messed up the settings
>   * [#3629](https://github.com/OctoPrint/OctoPrint/issues/3629) (regression?) - Fix logging error caused by tracking plugin during shutdown
>   * [#3630](https://github.com/OctoPrint/OctoPrint/issues/3630) (regression) - Fix single file plugin installs under Python 2.7
>   * [#3633](https://github.com/OctoPrint/OctoPrint/issues/3633) (regression) - Fix high CPU load while connected to a printer

The heads-ups regarding Jinja2 templating, `awesome-slugify` and the virtual printer from 1.4.1rc1 still apply.

You can find the full changelog and release notes as usual [on Github](https://github.com/OctoPrint/OctoPrint/releases/tag/1.4.1rc2).

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
[this ticket on the tracker](https://github.com/OctoPrint/OctoPrint/issues/3638).
The information that everything works fine for you is also valuable feedback 😄. **For bug reports** please follow
["How to file a bug report"](https://github.com/OctoPrint/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report) - 
I need logs and reproduction steps to fix issues, not just the information that something doesn't work so make sure to
**fill out all fields of the issue template**.

Thanks!

Depending on the feedback regarding this version I'll look into fixing 
any observed regressions and bugs and pushing out a follow-up version 
as soon as possible and necessary.

### Links

  * [Ticket for general feedback](https://github.com/OctoPrint/OctoPrint/issues/3638)
  * [Changelog and Release Notes](https://github.com/OctoPrint/OctoPrint/releases/tag/1.4.1rc2)
  * [How to use release channels to help test release candidates](https://community.octoprint.org/t/how-to-use-the-release-channels-to-help-test-release-candidates/402)
  * [How to file a bug report](https://github.com/OctoPrint/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report)
  * [Contribution Guidelines (also relevant for creating bug reports!)](https://github.com/OctoPrint/OctoPrint/blob/master/CONTRIBUTING.md)
  * [FAQ](https://faq.octoprint.org)
  * [Documentation](http://docs.octoprint.org/)
  * [How to roll back to an earlier release (OctoPi)](https://community.octoprint.org/t/how-can-i-revert-to-an-older-version-of-the-octoprint-installation-on-my-octopi-image/205)
  * [How to roll back to an earlier release (manual install)](https://community.octoprint.org/t/how-can-i-roll-back-to-an-earlier-version-after-an-update/234)
