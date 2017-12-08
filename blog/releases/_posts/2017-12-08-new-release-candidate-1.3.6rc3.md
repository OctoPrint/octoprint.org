---

layout: post
title: 'New release candidate: 1.3.6rc3'
author: foosel
date: 2017-12-08 16:00:00 +0100
card: /assets/img/blog/2017-12/2017-12-08-octoprint-1.3.6rc3-card.png
featuredimage: /assets/img/blog/2017-12/2017-12-08-octoprint-1.3.6rc3-card.png
poster: /assets/img/blog/2017-12/2017-12-08-octoprint-1.3.6rc3-poster.png
excerpt: This third release candidate of the 1.3.6 release fixes two small bugs found in the second one
   that were an issue with new/improved functionality and also switches plugin blacklist access to https.

---

This third release candidate of the 1.3.6 release fixes two small bugs found in 1.3.6rc2 that were regressions:

  * Fixed an issue causing redundant software update configuration settings to be written to `config.yaml`, in turn causing issues when downgrading to <1.3.5
  * Fixed an issue detecting whether the installed version is a release version or a development version.

It also switches plugin blacklist (and announcement, plugin notices and plugin repository) access to `https`.

**Please note** that the [heads-up in the 1.3.6rc1 announcement](/blog/2017/12/01/new-release-candidate-1.3.6rc1/#heads-up)
regarding the potentially breaking changes in the plugin asset bundling still applies, so give this a read if you haven't
yet. See also [this earlier dedicated post](/blog/2017/12/01/heads-up-plugin-authors/) on the matter. The plugins that so far 
are known to be affected by this are

  * [Navbar Temp](http://plugins.octoprint.org/plugins/navbartemp/) up until version 0.8 - version 0.9 is fixed!
  * [Fullscreen Webcam](http://plugins.octoprint.org/plugins/fullscreen_webcam/) up until version 0.0.3

**If you are tracking the "Maintenance RC" release channel**, you
should soon get an update notification just like you are used to from
stable releases.

**If you downgraded back to 1.3.5 from 1.3.6rc1 or 1.3.6rc2** you'll need to do a tiny fix in your `config.yaml`, 
made necessary the above mentioned (now fixed) bug, or you won't be able to switch back again to Maintenance RCs to test
this third RC or upgrade to 1.3.6 stable. You'll need to remove the ``method: pip`` line under
``plugins.softwareupdate.checks.octoprint`` and then restart. 

You can easily do this `config.yaml` change via [the YamlPatcher plugin](http://plugins.octoprint.org/plugins/yamlpatcher/) using the patch string

    [["remove", "plugins.softwareupdate.checks.octoprint.method", ""]]

or via the command line using 

    sed -i -e "s/method: pip//g" ~/.octoprint/config.yaml

**If you are not interested in helping to test release candidates**, just
ignore this post, 1.3.6 stable will hit your instance via the usual
way once it's ready :)

You can find the full changelog and release notes as usual
[on Github](https://github.com/foosel/OctoPrint/releases/tag/1.3.6rc3).

**Please provide feedback** on this RC. For general feedback you can use
[this ticket on the tracker](https://github.com/foosel/OctoPrint/issues/2276).
Note that the information that everything works fine for you is also
valuable feedback :). For bug reports please follow
["How to file a bug report"](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report).

Depending on how the feedback for this release candidate turns out, I'll
either look into releasing 1.3.6 or fix any observed regressions and push
out a fourth release candidate ASAP.

### Links

  * [Ticket for general feedback](https://github.com/foosel/OctoPrint/issues/2276)
  * [Changelog and Release Notes](https://github.com/foosel/OctoPrint/releases/tag/1.3.6rc3)
  * [Using Release Channels](https://github.com/foosel/OctoPrint/wiki/Using-Release-Channels)
  * [How to file a bug report](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report)
  * [Contribution Guidelines (also relevant for creating bug reports!)](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md)
  * [FAQ](https://github.com/foosel/OctoPrint/wiki/FAQ)
  * [Documentation](http://docs.octoprint.org/)
  * [How to roll back to an earlier release (OctoPi)](https://github.com/foosel/OctoPrint/wiki/FAQ#how-can-i-revert-to-an-older-version-of-the-octoprint-installation-on-my-octopi-image)
  * [How to roll back to an earlier release (manual install)](https://github.com/foosel/OctoPrint/wiki/FAQ#how-can-i-roll-back-to-an-earlier-version-after-an-update)
