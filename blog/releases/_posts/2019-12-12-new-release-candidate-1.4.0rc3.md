---

layout: post
title: 'New release candidate: 1.4.0rc3'
author: foosel
date: 2019-12-12 14:45:00 +0100
card: /assets/img/blog/2019-12/2019-12-12-octoprint-1.4.0rc3-card.png
featuredimage: /assets/img/blog/2019-12/2019-12-12-octoprint-1.4.0rc3-card.png
poster: /assets/img/blog/2019-12/2019-12-12-octoprint-1.4.0rc3-poster.png
excerpt: The third release candidate for the upcoming 1.4.0 release fixes some regressions observed with the first and second one.

---

This third RC of 1.3.12 fixes some regressions and issues in the new functionality observed with the first and second one:

> **Improvements**
> 
>   * [#3367](https://github.com/foosel/OctoPrint/issues/3367) - Ensure that static CSS and JS files always get the correct MIME Type associated, to work around issues when installed under Windows 10 with invalid entries in the registry triggering strict MIME checking
>   * [#3381](https://github.com/foosel/OctoPrint/issues/3381) - Continue to support request parameters on the `/api/login` endpoint for now for backwards compatibility with API clients that still use things like `/api/login?passive=true`, e.g. older versions of Printoid
>   * Remove a left-over comment from the Python 3 migration
> 
> **Bug fixes**
> 
>   * [#3365](https://github.com/foosel/OctoPrint/issues/3365) (regression) - Fix permissions of global API key
>   * [#3366](https://github.com/foosel/OctoPrint/issues/3366) (regression) - Appkeys: Fix issue causing 500/internal server error
>   * [#3370](https://github.com/foosel/OctoPrint/issues/3370) (regression) - Fix issue causing lost session in case of a client IP change
>   * [#3371](https://github.com/foosel/OctoPrint/issues/3371) - Python 3: Fix calculation of `rolling_window` in print time estimator
>   * [#3375](https://github.com/foosel/OctoPrint/issues/3375) - Fix `abort` support for `SimpleApiPlugin` implementations
>   * [#3384](https://github.com/foosel/OctoPrint/issues/3384) - Python 3: Fix login using HTTP Basic Auth
>   * [#3385](https://github.com/foosel/OctoPrint/issues/3385) - Python 3: Fix serial port auto detection
>   * [#3388](https://github.com/foosel/OctoPrint/issues/3388) - Granular permission system: Fix extruder controls being visible without control permission
>   * Fix a unicode issue under Windows (regression)

The heads-up regarding Plugins and Python 3 from 1.4.0rc1 still applies.

You can find the full changelog and release notes as usual [on Github](https://github.com/foosel/OctoPrint/releases/tag/1.4.0rc3).

Special thanks to everyone who contributed to this release candidate and provided full, analyzable bug reports!

As the past RCs have shown me that a lot of people appear to be unaware of this: **Please do *not* install this RC if you 
expect a fully stable version**. It is not a stable release, it is a release *candidate*, and of the next big release
to boot: severe bugs may occur, and they might be bad enough that they make a manual downgrade to an earlier version 
necessary - maybe even from the command line. 

You should feel comfortable with and capable of possibly having to do this *before* installing an RC.

If you want to and can help test this release candidate, you can find information on how to switch to the 
**"Devel RCs"** release channel [in this guide](https://community.octoprint.org/t/how-to-use-the-release-channels-to-help-test-release-candidates/402)
if not already done (also linked below). Please note that **contrary to maintenance releases this RC is not available
on the "Maintenance RCs" release channel** so if you are tracking that you'll need to switch. The reason is that 
RCs of big releases might be more unstable at first than pure maintenance releases due to newly introduced features
or very heavy refactorings, so I'm splitting these between two release channels. Note that when tracking "Devel RCs" 
you'll get all releases from "Stable" and "Maintenance RCs" as well.

**Please provide feedback** on this RC. For general feedback you can use 
[this ticket on the tracker](https://github.com/foosel/OctoPrint/issues/3389).
The information that everything works fine for you is also valuable feedback 😄. **For bug reports** please follow
["How to file a bug report"](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report) - 
I need logs and reproduction steps to fix issues, not just the information that something doesn't work so make sure to
**fill out all fields of the issue template**.

Thanks!

Depending on the feedback regarding this version I'll look into fixing 
any observed regressions and bugs and pushing out a follow-up version 
as soon as possible and necessary - due to the upcoming holidays 🎄 that will 
probably take until January however.

### Links

  * [Ticket for general feedback](https://github.com/foosel/OctoPrint/issues/3389)
  * [Changelog and Release Notes](https://github.com/foosel/OctoPrint/releases/tag/1.4.0rc3)
  * [How to use release channels to help test release candidates](https://community.octoprint.org/t/how-to-use-the-release-channels-to-help-test-release-candidates/402)
  * [How to file a bug report](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report)
  * [Contribution Guidelines (also relevant for creating bug reports!)](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md)
  * [FAQ](https://faq.octoprint.org)
  * [Documentation](http://docs.octoprint.org/)
  * [How to roll back to an earlier release (OctoPi)](https://community.octoprint.org/t/how-can-i-revert-to-an-older-version-of-the-octoprint-installation-on-my-octopi-image/205)
  * [How to roll back to an earlier release (manual install)](https://community.octoprint.org/t/how-can-i-roll-back-to-an-earlier-version-after-an-update/234)
