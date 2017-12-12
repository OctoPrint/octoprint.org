---
layout: post
title: 'New release: 1.3.6'
author: foosel
date: 2017-12-12 12:45:00 +0100
card: /assets/img/blog/2017-12/2017-12-12-octoprint-1.3.6-card.png
featuredimage: /assets/img/blog/2017-12/2017-12-12-octoprint-1.3.6-card.png
poster: /assets/img/blog/2017-12/2017-12-12-octoprint-1.3.6-poster.png
images:
- url: /assets/img/blog/2017-12/2017-12-01-legacy-setting.png
  title: Run into a problem with a plugin still incompatible to the new asset bundling? There's a fix for that built right in.
- url: /assets/img/blog/2017-12/2017-12-01-utf8-file-names.png
  title: File and folder names now support UTF8 - including emoji.
excerpt: As an early christmas present I'm happy to present you OctoPrint 1.3.6. This a true maintenance release 
  again, consisting of various improvements and fixes.

---

As an early christmas present 🎄 I'm happy to present you OctoPrint 1.3.6. This a true maintenance release again, 
consisting of various improvements and fixes. It was made possible only through your continued 
**[support of my work](/support-octoprint/)** 💕.

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
to the plugin author. The plugins that so far are known to be affected by this are

  * [Navbar Temp](https://plugins.octoprint.org/plugins/navbartemp/) up until version 0.8 - version 0.9 is fixed!
  * [Fullscreen Webcam](https://plugins.octoprint.org/plugins/fullscreen_webcam/) up until version 0.0.3

With that out of the way, on to **some highlights from the release notes**:

  * Over the course of the past couple of months I saw a lot of support requests about failing updates that turned 
    out to be caused by corrupted git checkouts, which OctoPrint so far relied on to update itself. Starting with 
    this version I'm going to take out the middleman (unless you are running explicitly on commit based tracking) and 
    just use `pip`. That should remove a lot of potential reasons for failure from the equation in the future.
  * A new centralized plugin blacklist allows to prevent plugins/certain versions of plugins known to cause 
    crippling issues with the normal operation of OctoPrint to be disabled from loading, if the user has opted 
    to do so in the settings/wizard.
  * The aforementioned change in the JS plugin asset bundling will better isolate plugins from each other and
    greatly reduce the risk of them interfering with each other - which was the reason this was added to begin with.
  * File and folder names now support the full UTF8 character set (at least in the file list itself - on disk they'll
    still stick to ASCII to reduce the likelihood of cross platform issues). So if you want to have a folder named
    "Favorites 🌟" or a file named "Ümläutmadneß.gcode", that's now a possibility. See [below for an example](#image-2).
  * The API key fields and the Terminal tab now have shiny new copy buttons that should make it so much easier to get
    their contents quickly.
  * The GCODE viewer now also exposes a couple of more advanced options that might help with the one or other GCODE
    file, and its options are now persisted in your browser so you don't have to reset them every time you reload.
  * The new "OctoPi Support Plugin" - which will *only* load if an OctoPi instance is detected as the underlying
    OS - will now make sure to add the OctoPi version to the version string reported in the lower left corner of the
    UI. That should hopefully clear up a lot of the usual version confusion I've seen in the past. Additionally this
    and a couple of other info snippets about the detected environment (like python & pip version and underlying
    OS) will now be logged on startup to ensure this information is easier accessible in case of reported bugs or
    on support requests with accompanying `octoprint.org`. This may not look like something exciting, but it will 
    make helping each other so much easier going forward.
  * Of course I also fixed some bugs as usual. That also includes working around some issues in Firefox (drag-n-drop 
    not properly terminating under certain conditions and the API key not being copy-able due to FF interpreting the 
    `disabled` flag on input fields differently than all other browsers), solving some problems with temperature reporting
    on shared nozzle setups, handling a specific kind of communication error correctly and being more error resilient
    against unexpected firmware responses and corrupted data in general.
  * ... and much more 

The full list of changes can of course be found in the
[Changelog](https://github.com/foosel/OctoPrint/releases/tag/1.3.6) - as always.

Also see the **Further Information** and **Links** below for more information,
where to find help and how to roll back.

And last but not least a special **Thank you!** to everyone who reported back on the release candidates this time:
[andrivet](https://github.com/andrivet), [b-morgan](https://github.com/b-morgan), 
[bjarchi](https://github.com/bjarchi), [chippypilot](https://github.com/chippypilot), 
[ChrisHeerschap](https://github.com/ChrisHeerschap), [cosmith71](https://github.com/cosmith71), 
[Crowlord](https://github.com/Crowlord), [ctgreybeard](https://github.com/ctgreybeard), 
[fiveangle](https://github.com/fiveangle), [goeland86](https://github.com/goeland86), 
[jbjones27](https://github.com/jbjones27), [jneilliii](https://github.com/jneilliii), 
[JohnOCFII](https://github.com/JohnOCFII), [Kunsi](https://github.com/Kunsi), 
[Lordxv](https://github.com/Lordxv), [malnvenshorn](https://github.com/malnvenshorn), 
[mcp5500](https://github.com/mcp5500), [ntoff](https://github.com/ntoff), 
[ripp2003](https://github.com/ripp2003) and [schorsch3000](https://github.com/schorsch3000).

### Further Information

It may take up to 24h for your update notification to pop up, so don't 
be alarmed if it doesn't show up immediately after reading this. You
can force the update however via Settings > Software Update > 
Advanced options > Force check for update.

If you don't get an "Update Now" button with your update notification, 
read [this](https://github.com/foosel/OctoPrint/wiki/Plugin:-Software-Update#making-octoprint-updateable-on-existing-installations)
or - even more specifically - [this](https://github.com/foosel/OctoPrint/wiki/Plugin:-Software-Update#octoprint--125).

If you are running 1.2.7, get an "Update Now" button but the update is immediately 
reported to be successful without any changes, read 
[this](https://github.com/foosel/OctoPrint/wiki/FAQ#im-running-127-i-tried-to-update-to-a-newer-version-via-the-software-update-plugin-but-im-still-on-127-after-restart).

If you are running 1.2.16, get an "Update Now" button but the update is immediately
producing an error message, read [this](https://github.com/foosel/OctoPrint/wiki/FAQ#im-running-1216-i-tried-to-update-to-a-newer-version-via-the-software-update-plugin-but-i-get-an-error).

If you were running 1.3.6rc1 or 1.3.6rc2, downgraded back to 1.3.5 and now can't update and/or select
your release channel, please read [this](/blog/2017/12/08/new-release-candidate-1.3.6rc3/#heads-up).

If you have any problems with your OctoPrint installation, please seek 
support on the [Mailinglist](https://groups.google.com/group/octoprint).

### Links

  * [Changelog and Release Notes](https://github.com/foosel/OctoPrint/releases/tag/1.3.6)
  * [Mailinglist](https://groups.google.com/group/octoprint)
  * [FAQ](https://github.com/foosel/OctoPrint/wiki/FAQ)
  * [Documentation](http://docs.octoprint.org/)
  * [Contribution Guidelines (also relevant for creating bug reports!)](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md)
  * [How to file a bug report](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report)
  * [How to roll back to an earlier release (OctoPi)](https://github.com/foosel/OctoPrint/wiki/FAQ#how-can-i-revert-to-an-older-version-of-the-octoprint-installation-on-my-octopi-image)
  * [How to roll back to an earlier release (manual install)](https://github.com/foosel/OctoPrint/wiki/FAQ#how-can-i-roll-back-to-an-earlier-version-after-an-update)

