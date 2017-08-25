---

layout: post
title: 'New release candidate: 1.3.5rc3'
author: foosel
date: 2017-08-25 14:30:00 +0200
card: /assets/img/blog/2017-08/2017-08-25-octoprint-1.3.5rc3-card.png
featuredimage: /assets/img/blog/2017-08/2017-08-25-octoprint-1.3.5rc3-card.png
poster: /assets/img/blog/2017-08/2017-08-25-octoprint-1.3.5rc3-poster.png
excerpt: This third release candidate of the 1.3.5 release fixes three bugs discovered in the earlier ones
   that were either regressions or issues with new/improved functionality.

---

A bit later than usual due to a long overdue vacation, this third release candidate of the 1.3.5 release fixes a few
regressions and bugs in new/improved functionality that were found and reported in 1.3.5rc2:

  * [#2059](https://github.com/foosel/OctoPrint/issues/2059) - Fix an issue causing the new temperature controls to wrap on touch enabled devices when the temperature dropdown is opened.
  * [#2090](https://github.com/foosel/OctoPrint/issues/2090) - Fix an issue causing an aborted server startup under Windows if the timing is just right.
  * Fix an issue causing rollover of `serial.log` to fail under Windows.

**If you are tracking the "Maintenance RCs" or "Devel RCs" release channel**, you
should soon get an update notification just like you are used to from
stable releases.

**If you are not interested in helping to test release candidates**, just
ignore this post, 1.3.5 stable will hit your instance via the usual
way once it's ready :)

You can find the full changelog and release notes as usual
[on Github](https://github.com/foosel/OctoPrint/releases/tag/1.3.5rc3).

**Please provide feedback** on this RC. For general feedback you can use
[this ticket on the tracker](https://github.com/foosel/OctoPrint/issues/2095).
Note that the information that everything works fine for you is also
valuable feedback :). For bug reports please follow
["How to file a bug report"](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report).

Depending on how the feedback for this release candidate turns out, I'll
either look into releasing 1.3.5 or fix any observed regressions and push
out a new release candidate within roughly a week's time.

### Links

  * [Ticket for general feedback](https://github.com/foosel/OctoPrint/issues/2095)
  * [Changelog and Release Notes](https://github.com/foosel/OctoPrint/releases/tag/1.3.5rc3)
  * [Using Release Channels](https://github.com/foosel/OctoPrint/wiki/Using-Release-Channels)
  * [How to file a bug report](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report)
  * [Contribution Guidelines (also relevant for creating bug reports!)](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md)
  * [FAQ](https://github.com/foosel/OctoPrint/wiki/FAQ)
  * [Documentation](http://docs.octoprint.org/)
  * [How to roll back to an earlier release (OctoPi)](https://github.com/foosel/OctoPrint/wiki/FAQ#how-can-i-revert-to-an-older-version-of-the-octoprint-installation-on-my-octopi-image)
  * [How to roll back to an earlier release (manual install)](https://github.com/foosel/OctoPrint/wiki/FAQ#how-can-i-roll-back-to-an-earlier-version-after-an-update)
