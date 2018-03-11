---

layout: post
title: 'New release candidate: 1.3.5rc1'
author: foosel
date: 2017-07-26 14:00:00 +0200
card: /assets/img/blog/2017-07/2017-07-26-octoprint-1.3.5rc1-card.png
featuredimage: /assets/img/blog/2017-07/2017-07-26-octoprint-1.3.5rc1-card.png
poster: /assets/img/blog/2017-07/2017-07-26-octoprint-1.3.5rc1-card.png
excerpt: The first release candidate of the 1.3.5 release, with various
   improvements and bug fixes.
comments: false

---

Let's start with getting 1.3.5 out of the door, shall we? :) This shiny
new release candidate is the first step towards the next stable release.

The [changelog](https://github.com/foosel/OctoPrint/releases/tag/1.3.5rc1)
is on the lengthy side again. This is simply the consequence of these releases
to be spread a bit further apart now. I hope that doesn't initimidate you ;)

Some highlights from the release notes:

  * Refactored web interface startup process to minimise risk of race conditions and speed improvements.
  * Support temperature autoreporting by the firmware instead of polling if the firmware reports to
    support it. For this to work with Marlin 1.1.0 to 1.1.3 you'll need to explicitly enable
    `EXTENDED_CAPABILITIES_REPORT` and `AUTO_REPORT_TEMPERATURES` in your firmware configuration,
    otherwise your firmware won't report that it actually supports this feature.
  * Refactored temperature inputs. They now sport some fancy +/- buttons to increment/decrement the
    current temperature (which also auto submit after a couple of seconds) and easier editing by
    keyboard. The temperature offset was also slightly redesigned to make room for that.
  * Added a centralized online connectivity check (with opt-in of course). None of the bundled
    plugins will attempt to fetch data from the net when the connectivity check indicates that would fail
    anyhow. This should improve server startup times and various requests when running isolated.
  * Fixed a couple of bugs (e.g. one causing cancelling to take too long if you had a lot of files in your
    uploads folder) and removed some potential race conditions.
  * ... and much more

**If you are tracking the "Maintenance RC" release channel**, you
should soon get an update notification just like you are used to from
stable releases.

**If you are not interested in helping to test release candidates**, just
ignore this post, 1.3.5 stable will hit your instance via the usual
way once it's ready :)

You can find the full changelog and release notes as usual
[on Github](https://github.com/foosel/OctoPrint/releases/tag/1.3.5rc1).

Please **provide feedback** on this RC. For general feedback you can use
[this ticket on the tracker](https://github.com/foosel/OctoPrint/issues/2033).
If everything works fine for you, that is also valuable feedback :)

Depending on how the feedback for this release candidate turns out, I'll
either look into releasing 1.3.5 or fix any observed regressions and push
out a second release candidate once I get back from some much needed time off.

### Links

  * [Changelog and Release Notes](https://github.com/foosel/OctoPrint/releases/tag/1.3.5rc1)
  * [Using Release Channels](https://github.com/foosel/OctoPrint/wiki/Using-Release-Channels)
  * [How to file a bug report](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report)
  * [Contribution Guidelines (also relevant for creating bug reports!)](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md)
  * [FAQ](https://github.com/foosel/OctoPrint/wiki/FAQ)
  * [Documentation](http://docs.octoprint.org/)
  * [How to roll back to an earlier release (OctoPi)](https://github.com/foosel/OctoPrint/wiki/FAQ#how-can-i-revert-to-an-older-version-of-the-octoprint-installation-on-my-octopi-image)
  * [How to roll back to an earlier release (manual install)](https://github.com/foosel/OctoPrint/wiki/FAQ#how-can-i-roll-back-to-an-earlier-version-after-an-update)
