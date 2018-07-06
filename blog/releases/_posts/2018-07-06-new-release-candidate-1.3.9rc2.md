---

layout: post
title: 'New release candidate: 1.3.9rc2'
author: foosel
date: 2018-07-06 14:00:00 +0200
card: /assets/img/blog/2018-07/2018-07-06-octoprint-1.3.9rc2-card.png
featuredimage: /assets/img/blog/2018-07/2018-07-06-octoprint-1.3.9rc2-card.png
poster: /assets/img/blog/2018-07/2018-07-06-octoprint-1.3.9rc2-poster.png
excerpt: The second release candidate of the 1.3.9 release, with a fix for a regression discovered in 1.3.9rc1 and
    also a small number of improvements.

---

This second release candidate of the 1.3.9 release fixes a regression and adds some resilience against possible environmental issues discovered during testing of the first RC:

  * [#2715](https://github.com/foosel/OctoPrint/issues/2715) (regression) - Fix broken estimator initialization on SD print start and resulting crash of the state update worker.
  * Add sanity check for disabled plugin list (see also [#2687 (comment)](https://github.com/foosel/OctoPrint/issues/2687#issuecomment-399797596)).
  * Improve logging of exceptions triggered inside the state update worker (see also [#2715](https://github.com/foosel/OctoPrint/issues/2715)).
  * Workaround for a potential `pip` issue when updating components through the Software Update plugin.

You can find the full changelog and release notes as usual [on Github](https://github.com/foosel/OctoPrint/releases/tag/1.3.9rc2).

**If you are tracking the "Maintenance RC" release channel**, you should soon get an update notification just like you 
are used to from stable releases.

If you want to help test this release candidate and **aren't yet tracking the "Maintenance RCs" release channel**, you
can find information on how to switch [in this guide](https://discourse.octoprint.org/t/how-to-use-the-release-channels-to-help-test-release-candidates/402)
(also linked below).

**If you are not interested in helping to test release candidates**, just ignore this post, 1.3.9 stable will hit 
your instance via the usual way once reports indicate that it's ready 😊

**Please provide feedback** on this RC. For general feedback you can use 
[this ticket on the tracker](https://github.com/foosel/OctoPrint/issues/2718).
The information that everything works fine for you is also valuable feedback 😄 For bug reports please follow
["How to file a bug report"](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report).

Depending on how the feedback for this release candidate turns out, I'll either look into releasing 1.3.9 or fix any 
observed regressions and push out a new release candidate ASAP.

### Links

  * [Ticket for general feedback](https://github.com/foosel/OctoPrint/issues/2718)
  * [Changelog and Release Notes](https://github.com/foosel/OctoPrint/releases/tag/1.3.9rc2)
  * [How to use release channels to help test release candidates](https://discourse.octoprint.org/t/how-to-use-the-release-channels-to-help-test-release-candidates/402)
  * [How to file a bug report](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report)
  * [Contribution Guidelines (also relevant for creating bug reports!)](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md)
  * [FAQ](https://faq.octoprint.org)
  * [Documentation](http://docs.octoprint.org/)
  * [How to roll back to an earlier release (OctoPi)](https://discourse.octoprint.org/t/how-can-i-revert-to-an-older-version-of-the-octoprint-installation-on-my-octopi-image/205)
  * [How to roll back to an earlier release (manual install)](https://discourse.octoprint.org/t/how-can-i-roll-back-to-an-earlier-version-after-an-update/234)
