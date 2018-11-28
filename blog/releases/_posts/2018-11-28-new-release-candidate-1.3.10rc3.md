---

layout: post
title: 'New release candidate: 1.3.10rc2'
author: foosel
date: 2018-11-28 14:40:00 +0100
card: /assets/img/blog/2018-11/2018-11-28-octoprint-1.3.10rc3-card.png
featuredimage: /assets/img/blog/2018-11/2018-11-28-octoprint-1.3.10rc3-card.png
poster: /assets/img/blog/2018-11/2018-11-28-octoprint-1.3.10rc3-poster.png
excerpt: The third release candidate of the 1.3.10 release, with fixes for regressions discovered
   in 1.3.10rc2 and also a small number of improvements of the newly added functionality.

---

This third RC of 1.3.10 fixes a couple of regressions observed with the second one and also adds some improvements
of existing or newly added functionality that became apparent during testing of RC2:

> ### Improvements
> 
>   * More resilience against third party plugins that happily block or kill important startup threads
>   * Improved backwards compatibility of the `sarge` dependency by monkey patching it to support the old `async` keyword parameter. Plugin authors are still advised to switch to the new `async_` parameter if running against `sarge>=0.1.5`, unmodified plugins should continue to work now however. For reference, OctoPrint 1.3.10 requires `sarge==0.1.5post0`.
>   * Pi Support plugin: Better wording on the "undervoltage & overheat" popover & added a link to the FAQ entry
>   * Printer Safety plugin: Micro3D printers running stock or iMe firmware are now detected as unsafe
> 
> ### Bug fixes
> 
>   * [#2897](https://github.com/foosel/OctoPrint/issues/2897) - Improved error resilience of `is_lan_address` so an error during its execution no longer nukes requests
>   * [#2898](https://github.com/foosel/OctoPrint/issues/2898) - ForceLogin plugin no longer interferes with websocket messages sent by plugins right on UI load but instead puts them into a (limited) backlog and then sends them out in received order once the user has authenticated on the socket.
>   * [#2903](https://github.com/foosel/OctoPrint/issues/2903) - Backup plugin: Support for ZIP64 extensions for large zip files
>   * [#2903](https://github.com/foosel/OctoPrint/issues/2903) - Backup plugin: Better error reporting
>   * [#2908](https://github.com/foosel/OctoPrint/issues/2908) - Tracking: Use the file's `path` instead of just the `name` for file name hashing.
>   * Logout socket on UI logout
>   * Tracking: Fixed homepage link

You can find the full changelog and release notes as usual [on Github](https://github.com/foosel/OctoPrint/releases/tag/1.3.10rc3).

Special thanks to everyone who contributed to this release candidate and provided full, analysable bug reports.

As the past RCs have shown me that a lot of people appear to be unaware of this: **Please do *not* install this RC if you 
expect a fully stable version**. It is not a stable release, it is a release *candidate*: severe bugs can occur, and 
they can be bad enough that they make a manual downgrade to an earlier version necessary - maybe even from the command line. 

You should be comfortable with and capable of possibly having to do this before installing an RC.

If you want to and can help test this release candidate, you can find information on how to switch to the 
"Maintenance RCs" release channel [in this guide](https://discourse.octoprint.org/t/how-to-use-the-release-channels-to-help-test-release-candidates/402)
if not already done (also linked below).

**Please provide feedback** on this RC. For general feedback you can use 
[this ticket on the tracker](https://github.com/foosel/OctoPrint/issues/2917).
The information that everything works fine for you is also valuable feedback 😄. **For bug reports** please follow
["How to file a bug report"](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report) - 
I need logs and reproduction steps to fix issues, not just the information that something doesn't work so make sure to
**fill out all fields of the issue template**.

Thanks!

Depending on how the feedback for this release candidate turns out, I'll either look into releasing 1.3.10 or fix any 
observed regressions and push out a new release candidate ASAP.

### Links

  * [Ticket for general feedback](https://github.com/foosel/OctoPrint/issues/2917)
  * [Changelog and Release Notes](https://github.com/foosel/OctoPrint/releases/tag/1.3.10rc3)
  * [How to use release channels to help test release candidates](https://discourse.octoprint.org/t/how-to-use-the-release-channels-to-help-test-release-candidates/402)
  * [How to file a bug report](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report)
  * [Contribution Guidelines (also relevant for creating bug reports!)](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md)
  * [FAQ](https://faq.octoprint.org)
  * [Documentation](http://docs.octoprint.org/)
  * [How to roll back to an earlier release (OctoPi)](https://discourse.octoprint.org/t/how-can-i-revert-to-an-older-version-of-the-octoprint-installation-on-my-octopi-image/205)
  * [How to roll back to an earlier release (manual install)](https://discourse.octoprint.org/t/how-can-i-roll-back-to-an-earlier-version-after-an-update/234)
