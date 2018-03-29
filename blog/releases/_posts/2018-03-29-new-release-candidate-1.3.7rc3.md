---

layout: post
title: 'New release candidate: 1.3.7rc3'
author: foosel
date: 2018-03-29 16:45:00 +0200
card: /assets/img/blog/2018-03/2018-03-29-octoprint-1.3.7rc3-card.png
featuredimage: /assets/img/blog/2018-03/2018-03-29-octoprint-1.3.7rc3-card.png
poster: /assets/img/blog/2018-03/2018-03-29-octoprint-1.3.7rc3-poster.png
excerpt: The third release candidate of the 1.3.7 release fixes a bugs reported with the second one
   that was an issue with new functionality.

---

This third release candidate of the 1.3.7 release fixes one bug that was found in new functionality:

  * [#2524](https://github.com/foosel/OctoPrint/issues/2524) Ignore `wait` while job is on hold.

**If you are tracking the "Maintenance RC" release channel**, you should soon get an update notification just like you 
are used to from stable releases.

If you want to help test this release candidate and **aren't yet tracking the "Maintenance RCs" release channel**, you
can find information on how to switch [in this guide](https://discourse.octoprint.org/t/how-to-use-the-release-channels-to-help-test-release-candidates/402)
(also linked below).

**If you are not interested in helping to test release candidates**, just ignore this post, 1.3.7 stable will hit 
your instance via the usual way once it's ready 😊

You can find the full changelog and release notes as usual [on Github](https://github.com/foosel/OctoPrint/releases/tag/1.3.7rc3).

**Please provide feedback** on this RC. For general feedback you can use 
[this ticket on the tracker](https://github.com/foosel/OctoPrint/issues/2529).
The information that everything works fine for you is also valuable feedback 😄 For bug reports please follow
["How to file a bug report"](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report).

Depending on how the feedback for this release candidate turns out, I'll either look into releasing 1.3.7 or fix any 
observed regressions and push out a new release candidate ASAP.

### Links

  * [Ticket for general feedback](https://github.com/foosel/OctoPrint/issues/2529)
  * [Changelog and Release Notes](https://github.com/foosel/OctoPrint/releases/tag/1.3.7rc3)
  * [How to use release channels to help test release candidates](https://discourse.octoprint.org/t/how-to-use-the-release-channels-to-help-test-release-candidates/402)
  * [How to file a bug report](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report)
  * [Contribution Guidelines (also relevant for creating bug reports!)](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md)
  * [FAQ](https://faq.octoprint.org)
  * [Documentation](http://docs.octoprint.org/)
  * [How to roll back to an earlier release (OctoPi)](https://discourse.octoprint.org/t/how-can-i-revert-to-an-older-version-of-the-octoprint-installation-on-my-octopi-image/205)
  * [How to roll back to an earlier release (manual install)](https://discourse.octoprint.org/t/how-can-i-roll-back-to-an-earlier-version-after-an-update/234)
