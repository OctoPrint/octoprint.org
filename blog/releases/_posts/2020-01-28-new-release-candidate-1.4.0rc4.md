---

layout: post
title: 'New release candidate: 1.4.0rc4'
author: foosel
date: 2020-01-28 14:45:00 +0100
card: /assets/img/blog/2020-01/2020-01-28-octoprint-1.4.0rc4-card.png
featuredimage: /assets/img/blog/2020-01/2020-01-28-octoprint-1.4.0rc4-card.png
poster: /assets/img/blog/2020-01/2020-01-28-octoprint-1.4.0rc4-poster.png
excerpt: The fourth release candidate for the upcoming 1.4.0 release fixes some regressions observed with the prior ones. It's
  now also available on the Maintenance RCs channel.

---

As this is the first blog post in 2020, first of all: Happy New Year to all of you! 🥳

This fourth RC of 1.4.0 fixes some regressions and issues in the new functionality observed with the prior RCs:

>**Improvements**
>
>  * [#3400](https://github.com/foosel/OctoPrint/issues/3400): Add `ClientAuthed` event to allow plugins to react to a client logging in on the socket
>  * [#3418](https://github.com/foosel/OctoPrint/issues/3418): Add API endpoint `/api/currentuser` to retrieve permissions & groups of currently logged in user
>  * [#3425](https://github.com/foosel/OctoPrint/issues/3425): Change method of prompting for log in for guests without permissions
>  * Add documentation for `/api/access` endpoints and update existing documentation with permission information
>
>**Bug fixes**
>
>  * [#3396](https://github.com/foosel/OctoPrint/issues/3396): Fix timelapse listing not properly refreshing on rendering a new timelapse
>  * [#3398](https://github.com/foosel/OctoPrint/issues/3398): Fix checking of needs not being picky enough
>  * [#3409](https://github.com/foosel/OctoPrint/issues/3409): Fix timelapse rendering progress reporting under Python 3
>  * [#3419](https://github.com/foosel/OctoPrint/issues/3419): Fix permission modelling for `PRINT` permission
>  * [#3425](https://github.com/foosel/OctoPrint/issues/3425): Fix permissions for `/api/settings`
>  * [#3426](https://github.com/foosel/OctoPrint/issues/3426): Fix "Remember me" checkbox on forced login screen
>  * [#3428](https://github.com/foosel/OctoPrint/issues/3428): Fix plugin installation and other CLI interactions under Python 2 and 3 and Windows
>  * [#3431](https://github.com/foosel/OctoPrint/issues/3431): Fix folder writability test under Python 3
>  * Fix endless loading issue when page is cached by browser in a tab and the server is down

The heads-up regarding Plugins and Python 3 from 1.4.0rc1 still applies.

You can find the full changelog and release notes as usual [on Github](https://github.com/foosel/OctoPrint/releases/tag/1.4.0rc4).

Special thanks to everyone who contributed to this release candidate and provided full, analyzable bug reports, and also
@CapnBry and @fieldOfView for their fixes!

As the past RCs have shown me that a lot of people appear to be unaware of this: **Please do *not* install this RC if you 
expect a fully stable version**. It is not a stable release, it is a release *candidate*, and of the next big release
to boot: severe bugs may occur, and they might be bad enough that they make a manual downgrade to an earlier version 
necessary - maybe even from the command line. 

You should feel comfortable with and capable of possibly having to do this *before* installing an RC.

If you want to and can help test this release candidate, you can find information on how to switch to the 
**"Maintenance RCs"** release channel [in this guide](https://community.octoprint.org/t/how-to-use-the-release-channels-to-help-test-release-candidates/402)
if not already done (also linked below). This is the first RC of the 1.4.0 series that is also available on the
"Maintenance RCs" channel, the prior RCs were only pushed to the "Devel RCs" release channel. If you are tracking
"Devel RCs" you will also get an update notification for this, since "Devel RCs" also tracks releases on the
"Maintenance RCs" and "Stable" channels, so no need to switch.

**Please provide feedback** on this RC. For general feedback you can use 
[this ticket on the tracker](https://github.com/foosel/OctoPrint/issues/3432).
The information that everything works fine for you is also valuable feedback 😄. **For bug reports** please follow
["How to file a bug report"](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report) - 
I need logs and reproduction steps to fix issues, not just the information that something doesn't work so make sure to
**fill out all fields of the issue template**.

Thanks!

Depending on the feedback regarding this version I'll look into fixing 
any observed regressions and bugs and pushing out a follow-up version 
as soon as possible and necessary.

### Links

  * [Ticket for general feedback](https://github.com/foosel/OctoPrint/issues/3432)
  * [Changelog and Release Notes](https://github.com/foosel/OctoPrint/releases/tag/1.4.0rc4)
  * [How to use release channels to help test release candidates](https://community.octoprint.org/t/how-to-use-the-release-channels-to-help-test-release-candidates/402)
  * [How to file a bug report](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report)
  * [Contribution Guidelines (also relevant for creating bug reports!)](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md)
  * [FAQ](https://faq.octoprint.org)
  * [Documentation](http://docs.octoprint.org/)
  * [How to roll back to an earlier release (OctoPi)](https://community.octoprint.org/t/how-can-i-revert-to-an-older-version-of-the-octoprint-installation-on-my-octopi-image/205)
  * [How to roll back to an earlier release (manual install)](https://community.octoprint.org/t/how-can-i-roll-back-to-an-earlier-version-after-an-update/234)
