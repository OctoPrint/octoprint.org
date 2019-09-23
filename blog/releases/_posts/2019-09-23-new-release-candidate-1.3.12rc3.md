---

layout: post
title: 'New release candidate: 1.3.12rc3'
author: foosel
date: 2019-09-23 15:00:00 +0200
card: /assets/img/blog/2019-09/2019-09-23-octoprint-1.3.12rc3-card.png
featuredimage: /assets/img/blog/2019-09/2019-09-23-octoprint-1.3.12rc3-card.png
poster: /assets/img/blog/2019-09/2019-09-23-octoprint-1.3.12rc3-poster.png
excerpt: The third release candidate for the upcoming 1.3.12 stable release.

---

This third RC of 1.3.12 fixes two regression observed with the first and second one:

> **Bug fixes**
> 
>   * [#3277](https://github.com/foosel/OctoPrint/issues/3277) (regression) - GCODE viewer: Fix huge memory consumption due to misplaced deep clone.
>   * [#3282](https://github.com/foosel/OctoPrint/issues/3282) (regression) - Don't trigger `M112` routine for firmware errors on a connection error when no connection has even been established yet.

The heads-up from last time regarding a wrong version check included in 1.3.12rc1 still applies if you are coming from
that version on OctoPi 0.15.1:

> **Heads-up for RC testers on OctoPi OctoPi 0.15.1 with 1.3.12rc1**
> 
> Those of you who are running OctoPi 0.15.1 and already updated to 1.3.12rc1 will either have to manually update their pip version to something >=10.0.1 or manually update to this second release candidate. I sadly made a mistake in the version limitations introduced to exclude OctoPi 0.14 and lower and thus OctoPrint 1.3.12rc1 won't allow to update itself on OctoPi 0.15.1 with stock pip version.
> 
> To manually update pip (via SSH):
> 
>     source ~/oprint/bin/activate
>     pip install -U pip
>     sudo service octoprint restart
> 
> You might have to "Force Check for Update" in the Software Update plugin after this.
>
> To manually update OctoPrint (via SSH):
> 
>     source ~/oprint/bin/activate
>     pip install https://github.com/foosel/OctoPrint/archive/1.3.12rc3.zip
>     sudo service octoprint restart

You can find the full changelog and release notes as usual [on Github](https://github.com/foosel/OctoPrint/releases/tag/1.3.12rc3).

Special thanks to everyone who contributed to this release candidate and provided full, analyzable bug reports!

As the past RCs have shown me that a lot of people appear to be unaware of this: **Please do *not* install this RC if you 
expect a fully stable version**. It is not a stable release, it is a release *candidate*: severe bugs may occur, and 
they might be bad enough that they make a manual downgrade to an earlier version necessary - maybe even from the command line. 

You should feel comfortable with and capable of possibly having to do this *before* installing an RC.

If you want to and can help test this release candidate, you can find information on how to switch to the 
"Maintenance RCs" release channel [in this guide](https://community.octoprint.org/t/how-to-use-the-release-channels-to-help-test-release-candidates/402)
if not already done (also linked below).

**Please provide feedback** on this RC. For general feedback you can use 
[this ticket on the tracker](https://github.com/foosel/OctoPrint/issues/3283).
The information that everything works fine for you is also valuable feedback 😄. **For bug reports** please follow
["How to file a bug report"](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report) - 
I need logs and reproduction steps to fix issues, not just the information that something doesn't work so make sure to
**fill out all fields of the issue template**.

Thanks!

Depending on how the feedback for this release candidate turns out, I'll either look into releasing 1.3.12 or fix any 
observed regressions and push out a new release candidate ASAP.

### Links

  * [Ticket for general feedback](https://github.com/foosel/OctoPrint/issues/3283)
  * [Changelog and Release Notes](https://github.com/foosel/OctoPrint/releases/tag/1.3.12rc3)
  * [How to use release channels to help test release candidates](https://community.octoprint.org/t/how-to-use-the-release-channels-to-help-test-release-candidates/402)
  * [How to file a bug report](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report)
  * [Contribution Guidelines (also relevant for creating bug reports!)](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md)
  * [FAQ](https://faq.octoprint.org)
  * [Documentation](http://docs.octoprint.org/)
  * [How to roll back to an earlier release (OctoPi)](https://community.octoprint.org/t/how-can-i-revert-to-an-older-version-of-the-octoprint-installation-on-my-octopi-image/205)
  * [How to roll back to an earlier release (manual install)](https://community.octoprint.org/t/how-can-i-roll-back-to-an-earlier-version-after-an-update/234)
