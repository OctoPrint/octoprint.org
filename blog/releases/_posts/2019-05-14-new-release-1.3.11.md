---

layout: post
title: 'New release: 1.3.11'
author: foosel
date: 2019-05-14 11:00:00 +0200
card: /assets/img/blog/2019-05/2019-05-14-octoprint-1.3.11-card.png
featuredimage: /assets/img/blog/2019-05/2019-05-14-octoprint-1.3.11-card.png
poster: /assets/img/blog/2019-05/2019-05-14-octoprint-1.3.11-poster.png
excerpt: After three months of development and another two of testing by the community, I'm happy to present you OctoPrint 1.3.11. While this is a maintenance release, it not only packs a bunch of bug fixes but also a whole lot of improvements.   

---

After three months of development and another two of testing by the community, I'm happy to finally present you
OctoPrint 1.3.11. This a maintenance release again, consisting of various improvements and fixes. 

It was made possible only through your continued **[support of my work](/support-octoprint/)** 💕.

Once again [the changelog](https://github.com/foosel/OctoPrint/releases/tag/1.3.11) is on the lengthy side as this
release packs a ton of improvements and bug fixes which would be too many to list here. Instead I'll just present you 
with a short excerpt:

  * The CuraEngine plugin so far bundled with OctoPrint was unbundled and lives on as the 
    [CuraEngine Legacy plugin](https://github.com/OctoPrint/OctoPrint-CuraEngineLegacy) that's [available on the plugin repository](https://plugins.octoprint.org/plugins/curalegacy/).
    On board slicing was never a primary focus of OctoPrint and the bundled plugin relied on a very dated CuraEngine
    version, so it was about time to clean up a bit. 
    
    If you happen to be one of the very small number of people who rely on the CuraEngine plugin for your workflow,
    make sure to install the CuraEngine Legacy plugin from the repository. Once installed the CuraEngine Legacy plugin will 
    import the settings and profiles from the former bundled Cura plugin automatically on first start.
  * The GCODE viewer will again show the total number of printer layers (I know quite a number of you missed that 😉).
  * Active print events (start/stop/cancel) now get logged, incl. who caused them. This will allow to audit who did what
    on shared installations.
  * Further hardening against various misconfigurations or misbehaving third party plugins or content.
  * New plugin hooks: `octoprint.printer.sdcardupload` to allow plugins to override the default SD card upload behaviour and
    `octoprint.events.register_custom_events` to allow plugins to cleanly add custom events to the system.
  * The list of GCODE commands on which OctoPrint will pause the print and/or which to suppress is now user configurable
    via the settings.
  * Performance improvements and more aggressive metadata cleanup in the internal file manager.
  * Support for firmware reporting print chamber temperatures.
  * Notifications will no longer be able to expand past the viewport size and hence should no longer become "uncloseable".  
  * ... and various further improvements and of course bug fixes.

The full list of changes can of course be found in the
[Changelog](https://github.com/foosel/OctoPrint/releases/tag/1.3.11) - as always.

Also see the **Further Information** and **Links** below for more information,
where to find help and how to roll back.

I also want to thank everyone who contributed to this release, [@agrif](https://github.com/agrif), [@akraus53](https://github.com/akraus53), [@AndyQ](https://github.com/AndyQ), [@CapnBry](https://github.com/CapnBry), [@DanielJoyce](https://github.com/DanielJoyce), [@devildant](https://github.com/devildant), [@Fabi0San](https://github.com/Fabi0San), [@fake-name](https://github.com/fake-name), [@fieldOfView](https://github.com/fieldOfView), [@gloomyandy](https://github.com/gloomyandy), [@HarlemSquirrel](https://github.com/HarlemSquirrel), [@hgross](https://github.com/hgross), [@jubaleth](https://github.com/foosel/OctoPrint/commits?author=jubaleth), [@melgish](https://github.com/melgish), [@rgriebl](https://github.com/rgriebl) and [@tedder](https://github.com/tedder) for their PRs.

And last but not least, another special **Thank you!** to everyone who reported back on the release candidates this time: [@arhi](https://github.com/arhi), [@b-morgan](https://github.com/b-morgan), [@CRCinAU](https://github.com/CRCinAU), [@devildant](https://github.com/devildant), [@evanquinnalaska](https://github.com/evanquinnalaska), [@FormerLurker](https://github.com/FormerLurker), [@gege2b](https://github.com/gege2b), [@isbric](https://github.com/isbric), [@JohnOCFII](https://github.com/JohnOCFII), [@kazibole](https://github.com/kazibole), [@nionio6915](https://github.com/nionio6915), [@reloxx13](https://github.com/reloxx13), [@schnello](https://github.com/schnello), [@trunzoc](https://github.com/trunzoc), [@vfrdirk](https://github.com/vfrdirk) & [@zeroflow](https://github.com/zeroflow).

If you are interested in some numbers, according to the anonymous usage tracking 1.3.11rc1 saw 9540 hours of successful prints on 523 unique instances,
1.3.11rc2 saw 9311h hours of successful prints on 553 unique instances, and 1.3.11rc3 saw a whopping 39578 hours (or 4.5 years)
of successful prints on 964 unique instances.

### Further Information

It may take up to 24h for your update notification to pop up, so don't 
be alarmed if it doesn't show up immediately after reading this. You
can force the update however via Settings > Software Update > 
Advanced options > Force check for update.

If you get an error about "no suitable distribution" during update, please read 
[this](https://discourse.octoprint.org/t/i-got-some-error-about-no-suitable-distribution-during-update-and-now-my-server-wont-start/235).

**If you have any problems with your OctoPrint installation, please seek 
support on the [community forum](https://discourse.octoprint.org).**

### Links

  * [Changelog and Release Notes](https://github.com/foosel/OctoPrint/releases/tag/1.3.11)
  * [Community forum](https://discourse.octoprint.org)
  * [FAQ](https://faq.octoprint.org)
  * [Documentation](http://docs.octoprint.org/)
  * [Contribution Guidelines (also relevant for creating bug reports!)](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md)
  * [How to file a bug report](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report)
  * [How to roll back to an earlier release (OctoPi)](https://discourse.octoprint.org/t/how-can-i-revert-to-an-older-version-of-the-octoprint-installation-on-my-octopi-image/205)
  * [How to roll back to an earlier release (manual install)](https://discourse.octoprint.org/t/how-can-i-roll-back-to-an-earlier-version-after-an-update/234)

