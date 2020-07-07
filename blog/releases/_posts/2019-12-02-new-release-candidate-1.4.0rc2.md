---

layout: post
title: 'New release candidate: 1.4.0rc2'
author: foosel
date: 2019-12-02 16:15:00 +0100
card: /assets/img/blog/2019-12/2019-12-02-octoprint-1.4.0rc2-card.png
featuredimage: /assets/img/blog/2019-12/2019-12-02-octoprint-1.4.0rc2-card.png
poster: /assets/img/blog/2019-12/2019-12-02-octoprint-1.4.0rc2-poster.png
excerpt: The second release candidate for the upcoming 1.4.0 release fixes some regressions observed with the first one.

---

This second RC of 1.4.0 fixes some regressions observed with the first one:

> **Bug fixes**
>
>  * [#3348](https://github.com/foosel/OctoPrint/issues/3348) (regression) - Fix an issue with the warning decorator trying to access non existing fields on instance methods, causing trouble with plugins still using deprecated settings methods.
>  * [#3349](https://github.com/foosel/OctoPrint/issues/3349) (regression) - Fix an issue with unset optional headers on file uploads, causing uploads to fail in case of a missing content type or file name, e.g. from Cura.
>  * [#3350](https://github.com/foosel/OctoPrint/issues/3350) (regression) - Appkeys: Fix wrong data type for newly generated keys under Python 3, causing the keys to not match and the plugin to not properly work.
>  * [#3354](https://github.com/foosel/OctoPrint/issues/3354) (regression - Fix timelapse start not triggering correctly due to using a no longer existing field in the PrintStarted payload.
>  * [#3357](https://github.com/foosel/OctoPrint/issues/3357) (regression) - Fix local autologin no longer working due to a logic change introduced by the new granular permission system.
>  * [#3361](https://github.com/foosel/OctoPrint/issues/3361) (regression) - Fix an exception raised when attempting to log out the single admin user if access control is disabled.
>  * [#3362](https://github.com/foosel/OctoPrint/issues/3362) (regression) - Fix escaping of placeholders in some error notifications.
>  * [#3363](https://github.com/foosel/OctoPrint/issues/3363) (regression) - Gracefully handle missing subfolders on file list nodes.
>  * [#3364](https://github.com/foosel/OctoPrint/issues/3364) (regression) - Make sure `data` is actually set.
>  * Appkeys: Fix a deprecation warning. (regression)

The heads-up regarding Plugins and Python 3 from 1.4.0rc1 still applies.

You can find the full changelog and release notes as usual [on Github](https://github.com/foosel/OctoPrint/releases/tag/1.4.0rc2).

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
[this ticket on the tracker](https://github.com/foosel/OctoPrint/issues/3360).
The information that everything works fine for you is also valuable feedback 😄. **For bug reports** please follow
["How to file a bug report"](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report) - 
I need logs and reproduction steps to fix issues, not just the information that something doesn't work so make sure to
**fill out all fields of the issue template**.

Thanks!

Depending on the feedback regarding this version I'll look into fixing 
any observed regressions and bugs and pushing out a follow-up version 
as soon as possible and necessary.

### Links

  * [Ticket for general feedback](https://github.com/foosel/OctoPrint/issues/3360)
  * [Changelog and Release Notes](https://github.com/foosel/OctoPrint/releases/tag/1.4.0rc2)
  * [How to use release channels to help test release candidates](https://community.octoprint.org/t/how-to-use-the-release-channels-to-help-test-release-candidates/402)
  * [How to file a bug report](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report)
  * [Contribution Guidelines (also relevant for creating bug reports!)](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md)
  * [FAQ](https://faq.octoprint.org)
  * [Documentation](http://docs.octoprint.org/)
  * [How to roll back to an earlier release (OctoPi)](https://community.octoprint.org/t/how-can-i-revert-to-an-older-version-of-the-octoprint-installation-on-my-octopi-image/205)
  * [How to roll back to an earlier release (manual install)](https://community.octoprint.org/t/how-can-i-roll-back-to-an-earlier-version-after-an-update/234)
