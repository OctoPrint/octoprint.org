---

layout: post
title: 'New release candidate: 1.4.1rc3'
author: foosel
date: 2020-07-15 14:00:00 +0200
card: /assets/img/blog/2020-07/2020-07-15-octoprint-1.4.1rc3-card.png
featuredimage: /assets/img/blog/2020-07/2020-07-15-octoprint-1.4.1rc3-card.png
poster: /assets/img/blog/2020-07/2020-07-15-octoprint-1.4.1rc3-poster.png
excerpt: The third release candidate for the upcoming 1.4.1 release that fixes a bunch of regressions observed in the first one and improves some of the newly added functionality.

---

This third RC of 1.4.1 fixes some regressions observed with the first one and also improves some of the functionality added in 1.4.1:

> **Improvements**
> 
>   * [#3640](https://github.com/OctoPrint/OctoPrint/issue/3640): Disable JS minification for third party plugins again, it can cause issues in one plugin that are non recoverable and cause the JS of all third party plugins to no longer load. Added `devel.webassets.minify_plugins` config setting to allow to turn it back on by plugin authors to test their plugins for minification compatibility (which should be a goal).
>   * Slight changes in the HTML markup to improve E2E testability.
> 
> **Bug fixes**
> 
>   * [#3627](https://github.com/OctoPrint/OctoPrint/issue/3627) (regression): Fix another issue with auto detection failing for port `AUTO` and set baudrate.
>   * [#3642](https://github.com/OctoPrint/OctoPrint/issue/3642) (regression): Fix styling on file list titles causing an issue with plugins like PrintTimeGenius that add on to the title, making the additional information toggle no longer work.
>   * Fix a possible race condition in the login dialog causing initial login to fail.

The heads-ups regarding Jinja2 templating, `awesome-slugify` and the virtual printer from 1.4.1rc1 still apply.

You can find the full changelog and release notes as usual [on Github](https://github.com/OctoPrint/OctoPrint/releases/tag/1.4.1rc3).

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
[this ticket on the tracker](https://github.com/OctoPrint/OctoPrint/issues/3643).
The information that everything works fine for you is also valuable feedback 😄. **For bug reports** please follow
["How to file a bug report"](https://github.com/OctoPrint/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report) - 
I need logs and reproduction steps to fix issues, not just the information that something doesn't work so make sure to
**fill out all fields of the issue template**.

Thanks!

Depending on the feedback regarding this version I'll look into fixing 
any observed regressions and bugs and pushing out a follow-up version 
as soon as possible and necessary.

### Links

  * [Ticket for general feedback](https://github.com/OctoPrint/OctoPrint/issues/3643)
  * [Changelog and Release Notes](https://github.com/OctoPrint/OctoPrint/releases/tag/1.4.1rc3)
  * [How to use release channels to help test release candidates](https://community.octoprint.org/t/how-to-use-the-release-channels-to-help-test-release-candidates/402)
  * [How to file a bug report](https://github.com/OctoPrint/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report)
  * [Contribution Guidelines (also relevant for creating bug reports!)](https://github.com/OctoPrint/OctoPrint/blob/master/CONTRIBUTING.md)
  * [FAQ](https://faq.octoprint.org)
  * [Documentation](http://docs.octoprint.org/)
  * [How to roll back to an earlier release (OctoPi)](https://community.octoprint.org/t/how-can-i-revert-to-an-older-version-of-the-octoprint-installation-on-my-octopi-image/205)
  * [How to roll back to an earlier release (manual install)](https://community.octoprint.org/t/how-can-i-roll-back-to-an-earlier-version-after-an-update/234)
