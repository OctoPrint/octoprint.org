---

layout: post
title: 'New release candidate: 1.3.5rc2'
author: foosel
date: 2017-07-27 14:25:00 +0200
card: /assets/img/blog/2017-07/2017-07-27-octoprint-1.3.5rc2-card.png
featuredimage: /assets/img/blog/2017-07/2017-07-27-octoprint-1.3.5rc2-card.png
poster: /assets/img/blog/2017-07/2017-07-27-octoprint-1.3.5rc2-card.png
excerpt: This second release candidate of the 1.3.5 release fixes a couple of bugs reported with the first one
   the were either regressions or issues with new/improved functionality.

---

This second release candidate of the 1.3.5 release fixes a few
regressions and bugs in new/improved functionality that were found and reported
in 1.3.5rc1:

  * [#2033](https://github.com/foosel/OctoPrint/issues/2033) - Temperature tab: Fix for legend in graph not updating with current values on mouse over.
  * [#2033](https://github.com/foosel/OctoPrint/issues/2033) - Temperature tab: Fix for new temperature inputs not fitting on one line in Firefox.
  * [#2033](https://github.com/foosel/OctoPrint/issues/2033) - Temperature tab & GCODE viewer: Fix for available tools (and offsets) not properly updating on change of printer profile.
  * [#2033](https://github.com/foosel/OctoPrint/issues/2033) - Wizard: Fix sorting of required wizards not properly handling non-ASCII unicode.
  * [#2035](https://github.com/foosel/OctoPrint/issues/2035) - Fix an issue of the server not starting up if there's a file in the analysis backlog. The reason for this is that spawning a new process while the intermediary server is active causes the server port to be blocked (this is due to how subprocessing works by default), in turn leading to an error on startup since the port cannot be bound by the actual server. Since the GCODE analysis takes now place in its own subprocess and hence triggers this problem, it had to be moved until after the actual server has already started up to avoid this problem.
  * Wizard: Fix `onWizardPreventSettingsRefreshDialog` callback invocation.
  * Corewizard plugin: Fix `firstrunonly` wizards (e.g. for printer profile configuration) being displayed again if _any_ of the sub wizards (e.g. for the online check opt-in and configuration) is active.

**If you are tracking the "Maintenance RC" release channel**, you
should soon get an update notification just like you are used to from
stable releases.

**If you are not interested in helping to test release candidates**, just
ignore this post, 1.3.5 stable will hit your instance via the usual
way once it's ready :)

You can find the full changelog and release notes as usual
[on Github](https://github.com/foosel/OctoPrint/releases/tag/1.3.5rc2).

**Please provide feedback** on this RC. For general feedback you can use
[this ticket on the tracker](https://github.com/foosel/OctoPrint/issues/2038).
Note that the information that everything works fine for you is also
valuable feedback :). For bug reports please follow
["How to file a bug report"](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report).

Depending on how the feedback for this release candidate turns out, I'll
either look into releasing 1.3.5 or fix any observed regressions and push
out a second release candidate once I get back from some much needed time off.

### Links

  * [Ticket for general feedback](https://github.com/foosel/OctoPrint/issues/2038)
  * [Changelog and Release Notes](https://github.com/foosel/OctoPrint/releases/tag/1.3.5rc2)
  * [Using Release Channels](https://github.com/foosel/OctoPrint/wiki/Using-Release-Channels)
  * [How to file a bug report](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report)
  * [Contribution Guidelines (also relevant for creating bug reports!)](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md)
  * [FAQ](https://github.com/foosel/OctoPrint/wiki/FAQ)
  * [Documentation](http://docs.octoprint.org/)
  * [How to roll back to an earlier release (OctoPi)](https://github.com/foosel/OctoPrint/wiki/FAQ#how-can-i-revert-to-an-older-version-of-the-octoprint-installation-on-my-octopi-image)
  * [How to roll back to an earlier release (manual install)](https://github.com/foosel/OctoPrint/wiki/FAQ#how-can-i-roll-back-to-an-earlier-version-after-an-update)
