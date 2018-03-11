---

layout: post
title: 'New release candidate: 1.3.5rc4'
author: foosel
date: 2017-10-04 14:45:00 +0200
card: /assets/img/blog/2017-10/2017-10-04-octoprint-1.3.5rc4-card.png
featuredimage: /assets/img/blog/2017-10/2017-10-04-octoprint-1.3.5rc4-card.png
poster: /assets/img/blog/2017-10/2017-10-04-octoprint-1.3.5rc4-poster.png
excerpt: The fourth release candidate of the 1.3.5 release fixes a few issues discovered in the earlier ones
   that were either regressions or issues with new/improved functionality.
comments: false

---

After a long downtime caused by the nastiest flu I caught myself in recent years 🤧, I'm happy to finally be able to look
into getting 1.3.5 out of the door again. Having 1.3.5rc3 available for testing for a way longer time than originally
anticipated apparently had its advantages, as it unveiled some more regressions and bugs in new/improved functionality, 
and so I've decided to push out another release candidate 1.3.5rc4 with the following changes:

  * [#2135](https://github.com/foosel/OctoPrint/issues/2135) - Fix an issue causing import errors inside the GCODE analysis tool in certain environments due to `sys.path` entries causing relative imports.
  * [#2136](https://github.com/foosel/OctoPrint/issues/2136) - Fix wrong minimum version for `sockjs-tornado` dependency.
  * [#2137](https://github.com/foosel/OctoPrint/issues/2137) - Fix issue with session cookies getting lost when running an OctoPrint instance on a subpath of another (e.g. `octopi.local/` and `octopi.local/octoprint2`).
  * [#2140](https://github.com/foosel/OctoPrint/issues/2140) - Fix issue with locale dependent sorting of sub wizards during first time setup causing issues leading to the wizard not being able to complete.

**If you are tracking the "Maintenance RCs" or "Devel RCs" release channel**, you
should soon get an update notification just like you are used to from
stable releases.

**If you are not interested in helping to test release candidates**, just
ignore this post, 1.3.5 stable will hit your instance via the usual
way once it's ready :)

You can find the full changelog and release notes as usual
[on Github](https://github.com/foosel/OctoPrint/releases/tag/1.3.5rc4).

**Please provide feedback** on this RC. For general feedback you can use
[this ticket on the tracker](https://github.com/foosel/OctoPrint/issues/2141).
Note that the information that everything works fine for you is also
valuable feedback :). For bug reports please follow
["How to file a bug report"](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report).

Depending on how the feedback for this release candidate turns out, I'll
either look into releasing 1.3.5 or fix any observed regressions and push
out a new release candidate.

### Links

  * [Ticket for general feedback](https://github.com/foosel/OctoPrint/issues/2141)
  * [Changelog and Release Notes](https://github.com/foosel/OctoPrint/releases/tag/1.3.5rc4)
  * [Using Release Channels](https://github.com/foosel/OctoPrint/wiki/Using-Release-Channels)
  * [How to file a bug report](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report)
  * [Contribution Guidelines (also relevant for creating bug reports!)](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md)
  * [FAQ](https://github.com/foosel/OctoPrint/wiki/FAQ)
  * [Documentation](http://docs.octoprint.org/)
  * [How to roll back to an earlier release (OctoPi)](https://github.com/foosel/OctoPrint/wiki/FAQ#how-can-i-revert-to-an-older-version-of-the-octoprint-installation-on-my-octopi-image)
  * [How to roll back to an earlier release (manual install)](https://github.com/foosel/OctoPrint/wiki/FAQ#how-can-i-roll-back-to-an-earlier-version-after-an-update)
