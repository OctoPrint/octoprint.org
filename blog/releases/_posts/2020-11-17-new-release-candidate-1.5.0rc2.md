---

layout: post
title: 'New release candidate: 1.5.0rc2'
author: foosel
date: 2020-11-17 15:45:00 +0100
card: /assets/img/blog/2020-11/2020-11-17-octoprint-1.5.0rc2-card.png
featuredimage: /assets/img/blog/2020-11/2020-11-17-octoprint-1.5.0rc2-card.png
poster: /assets/img/blog/2020-11/2020-11-17-octoprint-1.5.0rc2-poster.png
excerpt: The second release candidate for the upcoming 1.5.0 release, with some fixes of regressions from the first one and some improvements in newly added functionality.

---

This second RC of 1.5.0 fixes some regressions observed with the first one and also improves some things
in newly added and changed functionality:

> **Improvements**
> 
>   * [#3804](https://github.com/OctoPrint/OctoPrint/issues/3804) - Improve handling of corrupt `users.yaml` file and refuse server start if broken and default file based UserManager is configured.
>   * [#3811](https://github.com/OctoPrint/OctoPrint/issues/3811) - Only start tracking resend ratio after a set amount of lines has been transmitted.
>   * [#3822](https://github.com/OctoPrint/OctoPrint/issues/3822) - Prevent circumvention of access control through admin subgroups/permissions
> 
> **Bug fixes**
> 
>   * [#3805](https://github.com/OctoPrint/OctoPrint/issues/3805) (regression) - Fix an internal server error on `GET /api/files/local/<filename>`
>   * [#3812](https://github.com/OctoPrint/OctoPrint/issues/3812) (regression) - Backup: Fix an `AttributeError` on CLI usage
>   * [#3813](https://github.com/OctoPrint/OctoPrint/issues/3813) (regression) - Discovery: Fix zeroconf discovery under Python 2
>   * [#3814](https://github.com/OctoPrint/OctoPrint/issues/3814) - Fix an error on language pack upload under Python 3; not a regression, but still included due to being minimally invasive (see also [#3815](https://github.com/OctoPrint/OctoPrint/issues/3815))

The **heads-up** concerning the now mandatory Access Control from 1.5.0rc1 still applies:

> **Heads-up: Access Control is now mandatory and no longer can be disabled**
> 
> If you so far had Access Control disabled, upon upgrading to 1.5.0, OctoPrint will prompt you to create a user name and password for the (first) admin user. This step was sadly necessary as too many people still will happily expose their completely unsecured OctoPrint instance on the public internet, causing additional support overhead from both attacked users and security researchers. See [this guide](https://community.octoprint.org/t/how-to-set-up-octoprint-to-autologin-a-single-user-when-connecting-from-the-internal-network/26235) for a way to have OctoPrint log you in automatically when connecting from an internal IP.

You can find the full changelog and release notes as usual [on Github](https://github.com/OctoPrint/OctoPrint/releases/tag/1.5.0rc2).

Special thanks to everyone who contributed to this release candidate and provided full, analyzable bug reports, you help
making the next release as stable as possible! And a big Thank You to [@cp2004](https://github.com/cp2004) for his PR!

As the past RCs have shown me that a lot of people appear to be unaware of this: **Please do *not* install this RC if you 
expect a fully stable version**. It is not a stable release, it is a release *candidate*: 
severe bugs may occur, and they might be bad enough that they make a manual downgrade to an earlier version 
necessary - maybe even from the command line. 

You should feel comfortable with and capable of possibly having to do this *before* installing an RC.

If you want to and can help test this release candidate, you can find information on how to switch to the 
**"Maintenance RCs"** release channel [in this guide](https://community.octoprint.org/t/how-to-use-the-release-channels-to-help-test-release-candidates/402)
if not already done (also linked below).

**Please provide feedback** on this RC. For general feedback you can use 
[this ticket on the tracker](https://github.com/OctoPrint/OctoPrint/issues/3823).
The information that everything works fine for you is also valuable feedback 😄. **For bug reports** please follow
["How to file a bug report"](https://github.com/OctoPrint/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report) - 
I need logs and reproduction steps to fix issues, not just the information that something doesn't work so make sure to
**fill out all fields of the issue template**.

Thanks!

Depending on the feedback regarding this version I'll look into fixing 
any observed regressions and bugs and pushing out a follow-up version 
as soon as possible and necessary.

### Links

  * [Ticket for general feedback](https://github.com/OctoPrint/OctoPrint/issues/3823)
  * [Changelog and Release Notes](https://github.com/OctoPrint/OctoPrint/releases/tag/1.5.0rc2)
  * [How to use release channels to help test release candidates](https://community.octoprint.org/t/how-to-use-the-release-channels-to-help-test-release-candidates/402)
  * [How to file a bug report](https://github.com/OctoPrint/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report)
  * [Contribution Guidelines (also relevant for creating bug reports!)](https://github.com/OctoPrint/OctoPrint/blob/master/CONTRIBUTING.md)
  * [FAQ](https://faq.octoprint.org)
  * [Documentation](http://docs.octoprint.org/)
  * [How to roll back to an earlier release (OctoPi)](https://community.octoprint.org/t/how-can-i-revert-to-an-older-version-of-the-octoprint-installation-on-my-octopi-image/205)
  * [How to roll back to an earlier release (manual install)](https://community.octoprint.org/t/how-can-i-roll-back-to-an-earlier-version-after-an-update/234)
