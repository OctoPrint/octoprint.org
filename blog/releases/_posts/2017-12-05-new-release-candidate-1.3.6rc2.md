---

layout: post
title: 'New release candidate: 1.3.6rc2'
author: foosel
date: 2017-12-05 15:45:00 +0100
card: /assets/img/blog/2017-12/2017-12-05-octoprint-1.3.6rc2-card.png
featuredimage: /assets/img/blog/2017-12/2017-12-05-octoprint-1.3.6rc2-card.png
poster: /assets/img/blog/2017-12/2017-12-05-octoprint-1.3.6rc2-poster.png
excerpt: This second release candidate of the 1.3.6 release fixes a couple of bugs reported with the first one
   that were either regressions or issues with new/improved functionality.

---

This second release candidate of the 1.3.6 release fixes a few
regressions and bugs in new/improved functionality that were found and reported
in 1.3.6rc1:

  * [#2262](https://github.com/foosel/OctoPrint/issues/2262) - Fixed a bug causing `Error:checksum mismatch, Last Line: ...` errors from the firmware to be handled incorrectly.
  * [#2267](https://github.com/foosel/OctoPrint/issues/2267) - Fixed a bug causing the GCODE viewer to not get properly initialized due to a JS error on load if "Also show next layer" was selected.
  * [#2268](https://github.com/foosel/OctoPrint/issues/2268) - Fixed a bug causing a display error with the temperature offsets. If one offset was changed, all others seemed to revert back to 0.
  * Fixed ordering of plugin assets, should be alphabetical based on the plugin identifier.

**Please note** that the [heads-up in the 1.3.6rc1 announcement](/blog/2017/12/01/new-release-candidate-1.3.6rc1/#heads-up)
regarding the potentially breaking changes in the plugin asset bundling still applies, so give this a read if you haven't
yet. See also [this earlier dedicated post](/blog/2017/12/01/heads-up-plugin-authors/) on the matter. The plugins that so far 
are known to be affected by this are

  * [Navbar Temp](http://plugins.octoprint.org/plugins/navbartemp/) up until version 0.8 - version 0.9 is fixed!
  * [Fullscreen Webcam](http://plugins.octoprint.org/plugins/fullscreen_webcam/) up until version 0.0.3

**If you are tracking the "Maintenance RC" release channel**, you
should soon get an update notification just like you are used to from
stable releases.

**If you downgraded back to 1.3.5 from 1.3.6rc1** you'll need to do a tiny fix in your `config.yaml`, made necessary
by the switch to `pip` as update method in 1.3.6rc, our you won't be able to switch back again to Maintenance RCs to test
this second RC. You'll need to remove the ``method: pip`` line under
``plugins.softwareupdate.checks.octoprint`` and then restart. 

You can easily do this `config.yaml` change via [the YamlPatcher plugin](http://plugins.octoprint.org/plugins/yamlpatcher/) using the patch string

    [["remove", "plugins.softwareupdate.checks.octoprint.method", ""]]

or via the command line using 

    sed -i -e "s/method: pip//g" ~/.octoprint/config.yaml

**If you are not interested in helping to test release candidates**, just
ignore this post, 1.3.6 stable will hit your instance via the usual
way once it's ready :)

You can find the full changelog and release notes as usual
[on Github](https://github.com/foosel/OctoPrint/releases/tag/1.3.6rc2).

**Please provide feedback** on this RC. For general feedback you can use
[this ticket on the tracker](https://github.com/foosel/OctoPrint/issues/2269).
Note that the information that everything works fine for you is also
valuable feedback :). For bug reports please follow
["How to file a bug report"](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report).

Depending on how the feedback for this release candidate turns out, I'll
either look into releasing 1.3.6 or fix any observed regressions and push
out a third release candidate ASAP.

### Links

  * [Ticket for general feedback](https://github.com/foosel/OctoPrint/issues/2269)
  * [Changelog and Release Notes](https://github.com/foosel/OctoPrint/releases/tag/1.3.6rc2)
  * [Using Release Channels](https://github.com/foosel/OctoPrint/wiki/Using-Release-Channels)
  * [How to file a bug report](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report)
  * [Contribution Guidelines (also relevant for creating bug reports!)](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md)
  * [FAQ](https://github.com/foosel/OctoPrint/wiki/FAQ)
  * [Documentation](http://docs.octoprint.org/)
  * [How to roll back to an earlier release (OctoPi)](https://github.com/foosel/OctoPrint/wiki/FAQ#how-can-i-revert-to-an-older-version-of-the-octoprint-installation-on-my-octopi-image)
  * [How to roll back to an earlier release (manual install)](https://github.com/foosel/OctoPrint/wiki/FAQ#how-can-i-roll-back-to-an-earlier-version-after-an-update)
