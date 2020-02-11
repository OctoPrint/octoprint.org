---

layout: post
title: 'New release candidate: 1.4.0rc5'
author: foosel
date: 2020-02-11 14:25:00 +0100
card: /assets/img/blog/2020-02/2020-02-11-octoprint-1.4.0rc5-card.png
featuredimage: /assets/img/blog/2020-02/2020-02-11-octoprint-1.4.0rc5-card.png
poster: /assets/img/blog/2020-02/2020-02-11-octoprint-1.4.0rc5-poster.png
excerpt: The fifth release candidate for the upcoming 1.4.0 release fixes some regressions observed with the prior ones.

---

This fifth RC of 1.4.0 fixes some regressions and issues in the new functionality observed with the prior RCs:


>**Improvements**
>
>  * [#3442](https://github.com/foosel/OctoPrint/issues/3442) (UX of new functionality): Plugin Manager: Add UI representation of incompatible installed plugins
>  * Removed a duplicated line of code
>
>**Bug fixes**
>
>  * [#3400](https://github.com/foosel/OctoPrint/issues/3400) (regression): Reintroduced the message backlog on unauthenticated push sockets for better backwards compatibility for third party plugins.
>  * [#3434](https://github.com/foosel/OctoPrint/issues/3434) (regression): Fixed autologin & handling of disabled access control
>  * [#3442](https://github.com/foosel/OctoPrint/issues/3442) (bug in new functionality): Fix incompatible plugins being marked as enabled
>  * (regression) Fixed handling of unset remote addresses


The heads-up regarding Plugins and Python 3 from 1.4.0rc1 still applies.

You can find the full changelog and release notes as usual [on Github](https://github.com/foosel/OctoPrint/releases/tag/1.4.0rc5).

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
[this ticket on the tracker](https://github.com/foosel/OctoPrint/issues/3450).
The information that everything works fine for you is also valuable feedback 😄. **For bug reports** please follow
["How to file a bug report"](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report) - 
I need logs and reproduction steps to fix issues, not just the information that something doesn't work so make sure to
**fill out all fields of the issue template**.

Thanks!

Depending on the feedback regarding this version I'll look into fixing 
any observed regressions and bugs and pushing out a follow-up version 
as soon as possible and necessary.

### Links

  * [Ticket for general feedback](https://github.com/foosel/OctoPrint/issues/3450)
  * [Changelog and Release Notes](https://github.com/foosel/OctoPrint/releases/tag/1.4.0rc5)
  * [How to use release channels to help test release candidates](https://community.octoprint.org/t/how-to-use-the-release-channels-to-help-test-release-candidates/402)
  * [How to file a bug report](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report)
  * [Contribution Guidelines (also relevant for creating bug reports!)](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md)
  * [FAQ](https://faq.octoprint.org)
  * [Documentation](http://docs.octoprint.org/)
  * [How to roll back to an earlier release (OctoPi)](https://community.octoprint.org/t/how-can-i-revert-to-an-older-version-of-the-octoprint-installation-on-my-octopi-image/205)
  * [How to roll back to an earlier release (manual install)](https://community.octoprint.org/t/how-can-i-roll-back-to-an-earlier-version-after-an-update/234)
