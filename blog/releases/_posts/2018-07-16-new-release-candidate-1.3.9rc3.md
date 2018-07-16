---

layout: post
title: 'New release candidate: 1.3.9rc3'
author: foosel
date: 2018-07-16 15:00:00 +0200
card: /assets/img/blog/2018-07/2018-07-16-octoprint-1.3.9rc3-card.png
featuredimage: /assets/img/blog/2018-07/2018-07-16-octoprint-1.3.9rc3-card.png
poster: /assets/img/blog/2018-07/2018-07-16-octoprint-1.3.9rc3-poster.png
excerpt: The third release candidate of the 1.3.9 release, with two fixes for regressions discovered in 1.3.9rc1 and rc2 and
    also a small improvement.

---

This third release candidate of the 1.3.9 release fixes two regressions and adds some resilience against specific
resend and timeout scenarios during an ongoing `job_on_hold` lock (as used e.g. by Octolapse):

  * [#2677](https://github.com/foosel/OctoPrint/issues/2677) (regression) - Fix a deadlock when `job_on_hold` is utilized (causing issues at least with Octolapse)
  * [#2719](https://github.com/foosel/OctoPrint/issues/2719) (regression) - Fix live print time estimation
  * Fix resend and timeout handling during an active `job_on_hold`.

You can find the full changelog and release notes as usual [on Github](https://github.com/foosel/OctoPrint/releases/tag/1.3.9rc3).

**If you are tracking the "Maintenance RC" release channel**, you should soon get an update notification just like you 
are used to from stable releases.

If you want to help test this release candidate and **aren't yet tracking the "Maintenance RCs" release channel**, you
can find information on how to switch [in this guide](https://discourse.octoprint.org/t/how-to-use-the-release-channels-to-help-test-release-candidates/402)
(also linked below).

**If you are not interested in helping to test release candidates**, just ignore this post, 1.3.9 stable will hit 
your instance via the usual way once reports indicate that it's ready 😊

**Please provide feedback** on this RC. For general feedback you can use 
[this ticket on the tracker](https://github.com/foosel/OctoPrint/issues/2736).
The information that everything works fine for you is also valuable feedback 😄 For bug reports please follow
["How to file a bug report"](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report).

Depending on how the feedback for this release candidate turns out, I'll either look into releasing 1.3.9 or fix any 
observed regressions and push out a new release candidate ASAP.

### Links

  * [Ticket for general feedback](https://github.com/foosel/OctoPrint/issues/2736)
  * [Changelog and Release Notes](https://github.com/foosel/OctoPrint/releases/tag/1.3.9rc3)
  * [How to use release channels to help test release candidates](https://discourse.octoprint.org/t/how-to-use-the-release-channels-to-help-test-release-candidates/402)
  * [How to file a bug report](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report)
  * [Contribution Guidelines (also relevant for creating bug reports!)](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md)
  * [FAQ](https://faq.octoprint.org)
  * [Documentation](http://docs.octoprint.org/)
  * [How to roll back to an earlier release (OctoPi)](https://discourse.octoprint.org/t/how-can-i-revert-to-an-older-version-of-the-octoprint-installation-on-my-octopi-image/205)
  * [How to roll back to an earlier release (manual install)](https://discourse.octoprint.org/t/how-can-i-roll-back-to-an-earlier-version-after-an-update/234)
