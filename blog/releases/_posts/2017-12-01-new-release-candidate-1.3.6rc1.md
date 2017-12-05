---

layout: post
title: 'New release candidate: 1.3.6rc1'
author: foosel
date: 2017-12-01 15:45:00 +0100
card: /assets/img/blog/2017-12/2017-12-01-octoprint-1.3.6rc1-card.png
featuredimage: /assets/img/blog/2017-12/2017-12-01-octoprint-1.3.6rc1-card.png
poster: /assets/img/blog/2017-12/2017-12-01-octoprint-1.3.6rc1-card.png
images:
- url: /assets/img/blog/2017-12/2017-12-01-legacy-setting.png
  title: Run into a problem with a plugin still incompatible to the new asset bundling? There's a fix for that built right in.
- url: /assets/img/blog/2017-12/2017-12-01-utf8-file-names.png
  title: File and folder names now support UTF8 - including emoji.
excerpt: The first release candidate of the 1.3.6 release, with various
   improvements and bug fixes.

---

Considering that by now a couple of bug fixes and of course also nice improvements
have accumulated on the `maintenance` branch, I figured I'd see if I can't get 
a stable release out before the holidays 🎄.

So let's start towards that with this new release candidate!

Like with 1.3.5 the [changelog](https://github.com/foosel/OctoPrint/releases/tag/1.3.6rc1)
is on the lengthy side again. This is simply the consequence of these releases
to be spread a bit further apart now. I hope that doesn't initimidate you ;)

<a id="heads-up"></a>
**The most important thing first:** This release introduces a potentially breaking change
with regards to how JS plugin assets are bundled - you can read all the gritty details
[here](/blog/2017/12/01/heads-up-plugin-authors/). Not many plugins should be affected by this, but some are and for that I also added a 
little (temporary) feature toggle that will allow you to go back to the old way of bundling (with all
its downsides) until those plugins that are affected and that you rely on are updated. You
can find that toggle under ["Settings > Features > Enable legacy plugin bundling"](#image-1). Affected plugins will
produce errors in [the JS console](https://webmasters.stackexchange.com/a/77337) and most likely stop working in the browser - so if you
encounter that for a plugin after updating to this version, try enabling that flag, saving and
restarting your server and see if that fixes things - and if so best report the incompatibility
to the plugin author.

With that out of the way, on to some highlights from the release notes:

  * OctoPrint will now use plain `pip` instead of `git` + `pip` for updating OctoPrint. Over the course of the past couple of months
    I saw a lot of support requests about failing updates that turned out to be caused by corrupted git checkouts,
    which OctoPrint so far relied on to update itself. Starting with this version I'm going to take out the middleman 
    (unless you are running explicitly on commit based tracking) and just use `pip`. That should remove a lot of
    potential reasons for failure from the equation.
  * A new centralized plugin blacklist allows to prevent plugins/certain versions of plugins known to cause 
    crippling issues with the normal operation of OctoPrint to be disabled from loading, if the user has opted 
    to do so in the settings/wizard.
  * The aforementioned change in the JS plugin asset bundling will better isolate plugins from each other and
    greatly reduce the risk of them interfering with each other - which was the reason this was added to begin with.
  * File and folder names now support the full UTF8 character set (at least in the file list itself - on disk they'll
    still stick to ASCII to reduce the likelihood of cross platform issues). See [below for an example](#image-2).
  * The API key fields and the Terminal tab now have shiny new copy buttons that should make it so much easier to get
    their contents quickly.
  * The GCODE viewer now also exposes a couple of more advanced options that might help with the one or other GCODE
    file, and its options are now persisted in your browser so you don't have to reset them every time you reload.
  * The new "OctoPi Support Plugin" - which will *only* load if an OctoPi instance is detected as the underlying
    OS - will now make sure to add the OctoPi version to the version string reported in the lower left corner of the
    UI. That should hopefully clear up a lot of the usual version confusion I've seen in the past. Additionally this
    and a couple of other info snippets about the detected environment (like python & pip version and underlying
    OS) will now be logged on startup to ensure this information is easier accessible in case of reported bugs or
    on support requests. This may not look like something exciting, but it will make helping each other so much
    easier going forward.
  * Fixed some bugs and worked around some issues in Firefox (drag-n-drop not properly terminating under certain
    conditions and the API key not being easily copy-able).
  * ... and much more 

**If you are tracking the "Maintenance RC" release channel**, you
should soon get an update notification just like you are used to from
stable releases.

**If you are not interested in helping to test release candidates**, just
ignore this post, 1.3.6 stable will hit your instance via the usual
way once it's ready :)

You can find the full changelog and release notes as usual
[on Github](https://github.com/foosel/OctoPrint/releases/tag/1.3.6rc1).

Please **provide feedback** on this RC. For general feedback you can use
[this ticket on the tracker](https://github.com/foosel/OctoPrint/issues/2256).
If everything works fine for you, that is also valuable feedback :)

Depending on how the feedback for this release candidate turns out, I'll
either look into releasing 1.3.6 or fix any observed regressions and push
out a second release candidate ASAP.

### Links

  * [Changelog and Release Notes](https://github.com/foosel/OctoPrint/releases/tag/1.3.6rc1)
  * [Using Release Channels](https://github.com/foosel/OctoPrint/wiki/Using-Release-Channels)
  * [How to file a bug report](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report)
  * [Contribution Guidelines (also relevant for creating bug reports!)](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md)
  * [FAQ](https://github.com/foosel/OctoPrint/wiki/FAQ)
  * [Documentation](http://docs.octoprint.org/)
  * [How to roll back to an earlier release (OctoPi)](https://github.com/foosel/OctoPrint/wiki/FAQ#how-can-i-revert-to-an-older-version-of-the-octoprint-installation-on-my-octopi-image)
  * [How to roll back to an earlier release (manual install)](https://github.com/foosel/OctoPrint/wiki/FAQ#how-can-i-roll-back-to-an-earlier-version-after-an-update)
