---

layout: post
title: 'New release candidate: 1.3.7rc2'
author: foosel
date: 2018-03-23 16:15:00 +0100
card: /assets/img/blog/2018-03/2018-03-23-octoprint-1.3.7rc2-card.png
featuredimage: /assets/img/blog/2018-03/2018-03-23-octoprint-1.3.7rc2-card.png
poster: /assets/img/blog/2018-03/2018-03-23-octoprint-1.3.7rc2-poster.png
excerpt: This second release candidate of the 1.3.7 release fixes a couple of bugs reported with the first one
   that were either regressions or issues with new/improved functionality.

---

This second release candidate of the 1.3.7 release fixes a few
regressions and bugs in new/improved functionality that were found and reported
in 1.3.7rc1 or just finally identified due to changes introduced in 1.3.7rc1:

  * [#1951](http://github.com/foosel/OctoPrint/issues/1951) - Fixed plugins being able to modify internal state data (e.g. progress, job), causing concurrent modification and resulting run time errors in the printer state processing.
  * [#2494](https://github.com/foosel/OctoPrint/issues/2494) - Fixed `undefined` values not saving in the settings. 
  * [#2499](https://github.com/foosel/OctoPrint/issues/2499) - Fixed communication error notification lacking the actual error message.
  * [#2501](https://github.com/foosel/OctoPrint/issues/2501) - Fixed a bug causing log downloads to fail with an HTTP 500 error.
  * [#2506](https://github.com/foosel/OctoPrint/issues/2506) - Fixed `printer.get_current_data` and `printer.get_current_job` returning `frozendict` instead of `dict` instances, causing issues with plugins relying on being able to modify the returned data (e.g. [dattas/OctoPrint-DetailedProgress#26](https://github.com/dattas/OctoPrint-DetailedProgress/issues/26)).
  * [#2508](https://github.com/foosel/OctoPrint/issues/2508) - Fixed HTTP 500 error on `/api/slicing` in case of an unconfigured slicer.
  * Have `OctoPrintJsonEncoder` fall back to regular flask JSON encoder, otherwise we might not be able to serialize some data types we need to be able to serialize.
  * Use `pkg_resources` to determine pip version during environment check instead of `import pip; pip.__version__` since the latter causes issues with pip version 9.0.2. In the same spirit make `pip.main` approach of calling `pip` in the PipCaller the last resort during auto detection, only after trying `pip` or `pip.exe` inside the same folder as the Python executable.
  * Use `octoprint.util.monotonic_time` instead of `monotonic.monotonic` in comm layer.
  * Fixed timelapse not stopping on print failure due to firmware error due to missing `PrintFailed` event.

**If you are tracking the "Maintenance RC" release channel**, you should soon get an update notification just like you 
are used to from stable releases.

If you want to help test this release candidate and **aren't yet tracking the "Maintenance RCs" release channel**, you
can find information on how to switch [in this guide](https://discourse.octoprint.org/t/how-to-use-the-release-channels-to-help-test-release-candidates/402)
(also linked below).

**If you are not interested in helping to test release candidates**, just ignore this post, 1.3.7 stable will hit 
your instance via the usual way once it's ready 😊

You can find the full changelog and release notes as usual [on Github](https://github.com/foosel/OctoPrint/releases/tag/1.3.7rc2).

**Please provide feedback** on this RC. For general feedback you can use 
[this ticket on the tracker](https://github.com/foosel/OctoPrint/issues/2510).
The information that everything works fine for you is also valuable feedback 😄 For bug reports please follow
["How to file a bug report"](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report).

Depending on how the feedback for this release candidate turns out, I'll either look into releasing 1.3.7 or fix any 
observed regressions and push out a new release candidate ASAP.

### Links

  * [Ticket for general feedback](https://github.com/foosel/OctoPrint/issues/2510)
  * [Changelog and Release Notes](https://github.com/foosel/OctoPrint/releases/tag/1.3.7rc2)
  * [How to use release channels to help test release candidates](https://discourse.octoprint.org/t/how-to-use-the-release-channels-to-help-test-release-candidates/402)
  * [How to file a bug report](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report)
  * [Contribution Guidelines (also relevant for creating bug reports!)](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md)
  * [FAQ](https://faq.octoprint.org)
  * [Documentation](http://docs.octoprint.org/)
  * [How to roll back to an earlier release (OctoPi)](https://discourse.octoprint.org/t/how-can-i-revert-to-an-older-version-of-the-octoprint-installation-on-my-octopi-image/205)
  * [How to roll back to an earlier release (manual install)](https://discourse.octoprint.org/t/how-can-i-roll-back-to-an-earlier-version-after-an-update/234)
