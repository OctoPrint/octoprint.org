---

layout: post
title: 'New release: 1.4.1'
author: foosel
date: 2020-08-04 11:45:00 +0200
card: /assets/img/blog/2020-08/2020-08-04-octoprint-1.4.1-card.png
featuredimage: /assets/img/blog/2020-08/2020-08-04-octoprint-1.4.1-card.png
poster: /assets/img/blog/2020-08/2020-08-04-octoprint-1.4.1-poster.png
images:
- url: /assets/img/blog/2020-07/2020-07-06-temperature-profiles.png
  title: Temperature profile selector for all heaters
- url: /assets/img/blog/2020-07/2020-07-06-file-move.png
  title: Move files right from the file list
- url: /assets/img/blog/2020-07/2020-07-06-pmgr-repo-browser.png
  title: The plugin manager now shows stats for the plugins on the plugin repository and allows to install single file plugins
- url: /assets/img/blog/2020-07/2020-07-06-pmgr-overview.png
  title: The plugin manager also now shows more information about the installed plugins, including their Python compatibility
excerpt: "Fresh off the presses, just through a month long release candidate cycle and the first one to be developed 
  during a raging pandemic, I present you the next stable release of OctoPrint: 1.4.1!"

---

Fresh off the presses, just through a month long release candidate cycle and the first one to be developed during a 
raging pandemic - which as I want to add turned out to be quite the challenge thanks to a ridiculously increased support
overhead 😱 - I present you the next stable release of OctoPrint: 1.4.1! 🥳

Like every single release (and release candidate) of OctoPrint ever since early 2016 this was made possible only 
through your continued **[support of my work](/support-octoprint/)** 💕

The [full changelog](https://github.com/OctoPrint/OctoPrint/releases/tag/1.4.1) contains a long list of improvements and bug fixes, but here are
some of the highlights:

  * The temperature tab got a new control to select preconfigured temperature profiles on all heaters with one click
  * The newly bundled "File Check" plugin will sanity check uploaded files and warn about potential issues. Currently the plugin only detects `{travel_speed}` place holders left in GCODE. Read more in [the plugin's README](https://github.com/OctoPrint/OctoPrint-FileCheck/blob/master/README.md).
  * The first run wizard now allows to restore from a backup right away.
  * You can now move files in the file list to other folders without the need of a third party plugin.
  * The Plugin Manager now shows stats on the plugins available on the repository, such as number of known installs, date of last release etc. Installed plugins now also make it more transparent whether they are already compatible to Python 3 or not.
  * The Plugin Manager now also supports installing so called single-file plugins - mini plugins only consisting of a single python file which are a quick and easy way to work around broken communication or similar backend-only situations. This feature was developed live on air, you can learn more about it [in this episode of OctoPrint Code & Chat](https://www.youtube.com/watch?v=59xEaUwWU30). Consequently, the Software Update plugin was also extended with some new version check and updater types to support auto-updating single file plugins, read more [in the docs here](https://docs.octoprint.org/en/1.4.1rc1/bundledplugins/softwareupdate.html).
  * The Printer Safety Check has been renamed to Firmware Check & extracted into a still bundled but separately maintained plugin. It now also detects firmware with known broken communication protocol implementations (like the infamous `CBD make it` and `ZWLF make it` variants) and links to related FAQ entries on detection.
  * The broken by design comm port auto detection has been rewritten completely from scratch. That should hopefully make auto detection work more reliably in the future.
  * Original file modification timestamps will now be persisted on restoring from a backup.
  * The "read-only" group behaviour has been fixed so that it is actually possible to create a read-only account. The `User` group is no longer enforced on users, though pre checked for new users (if kept default). This makes it also possible to create group less users, so keep that in mind.
  * The permission issue that kept the Announcement icon from showing up on the navbar has been solved.
  * A bunch of dependencies were upgraded to the latest versions. Among these are also the web server framework Flask, the templating engine Jinja2 and something that pulls in a conflicting slugify library, which resulted in a bunch of **heads-ups** for users and plugin authors, read below.
  * ... and many more improvements & fixes.

There are also a bunch of **heads-ups** with this release.

### Heads-ups

Please read the following carefully, it might impact you and how you use OctoPrint! Also see the **Further Information** and **Links** below for more information,
where to find help and how to roll back.
 
#### Heads-up for users of the Telegram plugin v1.5.0 or lower (and possibly other plugins that use long deprecated `flask.ext` imports)
 
The Telegram plugin up until the currently latest version 1.5.0 from August 7th 2019 is incompatible to OctoPrint 1.4.1 and later (see [this ticket](https://github.com/fabianonline/OctoPrint-Telegram/issues/269)). The reason for that is that OctoPrint had to update its third party Flask dependency for security reasons, and this plugin (and possibly others) still use an import syntax related to that dependency that has been deprecated and warned about for several years now and which finally has been removed in current versions of Flask. 

[A fix has been provided to the Telegram plugin maintainers](https://github.com/fabianonline/OctoPrint-Telegram/pull/270) and has been merged, but so far no new release has been pushed out.

If you notice the Telegram plugin or another third party plugin no longer loading under OctoPrint 1.4.1 with an error logged to `octoprint.log` that looks similar to 

```
  File "/home/pi/oprint/local/lib/python2.7/site-packages/octoprint/plugin/core.py", line 972, in _import_plugin
    module = _load_module(module_name, spec)
  File "/home/pi/oprint/local/lib/python2.7/site-packages/octoprint/plugin/core.py", line 71, in _load_module
    return imp.load_module(name, f, filename, details)
  File "/home/pi/oprint/local/lib/python2.7/site-packages/octoprint_telegram/__init__.py", line 5, in <module>
    from flask.ext.babel import gettext
ImportError: No module named ext.babel
```

then this outdated import syntax is the reason. That is something that needs to be fixed by the plugin maintainers by pushing out a new release. Please do not open issues about this on the OctoPrint repository, I cannot do anything about this.

#### Heads-up for users of the TouchUI plugin v0.3.14 or lower

The TouchUI plugin up until the currently latest version 0.3.14 from March 11 2020 is incompatible to OctoPrint as it makes assumptions about the structure of the UI that are no longer true, leading to the plugin breaking the OctoPrint UI when active.

A fix is ready but no release has been pushed out yet. Until a fixed version is released it is suggested to disable the plugin under 1.4.1.

See also the ticket [here](https://github.com/BillyBlaze/OctoPrint-TouchUI/issues/413).

#### Heads-up for plugin authors: Jinja2 update has one backwards incompatibility, please read

Current Jinja versions no longer allow modifying variables set outside of for loops inside them. See also [#1697](https://github.com/OctoPrint/OctoPrint/issues/1697) and [the Jinja docs here](https://jinja.palletsprojects.com/en/2.11.x/templates/#assignments).

The Jinja dependency upgrade thus introduces a breaking change for plugins as well. However, it was necessary for security reasons: older versions have a bug that could allow template authors to break out of the template sandbox. Not a huge risk in the context of OctoPrint (plugins already have a lot more power than jinja would give them), but still overdue to fix.

You can find more details and example code in the [Release Notes](https://github.com/OctoPrint/OctoPrint/releases/tag/1.4.1).

#### Heads-up for plugin authors: `awesome-slugify` is now bundled as `octoprint.vendor.awesome_slugify`, update your imports!

Due to a necessary dependency update of a third party dependency pulling in a different slugify library ("python-slugify") that clashes with `awesome-slugify`, the latter has been bundled. If you use `import slugify` anywhere in your code, please be aware that that will now possibly pull in the aforementioned other library or possibly a partially overwritten `awesome-slugify`. Plugin authors are advised to update the imports of `awesome-slugify` like this:

``` python
### old

# example 1
import slugify

# example 2
from slugify import Slugify

### new

# example 1
try:
  # OctoPrint>=1.4.1
  import octoprint.vendor.awesome_slugify as slugify 
except ImportError:
  # OctoPrint<=1.4.0
  import slugify

# example 2
try:
  # OctoPrint>=1.4.1
  from octoprint.vendor.awesome_slugify import Slugify
except ImportError:
  # OctoPrint<=1.4.0
  from slugify import Slugify
```

That will also guarantee backwards compatibility if installed under OctoPrint versions prior to 1.4.1. Alternatively switch fully to the 1.4.1 version and adjust your plugin listing to a minimum OctoPrint version of 1.4.1.

#### Heads-up for developers: The included virtual printer has had its settings migrated to a different location in `config.yaml`

The bundled Virtual Printer plugin has finally been turned fully isolated into a self contained plugin and thus its settings have been moved from `devel.virtualPrinter` to `plugins.virtual_printer` in `config.yaml`. An auto migration is in place that should take care of moving anything already configured on first start under 1.4.1+, however should you be somehow manipulating `config.yaml` through automation or something in order to change virtual printer settings, you'll have to update your workflows.

### Thanks

Special thanks to everyone who contributed to this release and provided full, analyzable bug reports and pull requests, especially  [@drifkind](https://github.com/drifkind), [@eyal0](https://github.com/eyal0), [@FedericoNembrini](https://github.com/FedericoNembrini), [@fieldOfView](https://github.com/fieldOfView), [@flaviut](https://github.com/flaviut), [@jneilliii](https://github.com/jneilliii), [@joshfriend](https://github.com/joshfriend), [@justfalter](https://github.com/justfalter), [@kerber](https://github.com/kerber), [@lachyc](https://github.com/lachyc), [@osubuu](https://github.com/osubuu) and [@tedder](https://github.com/tedder) for their PRs!

And last but not least, another special **Thank you!** to everyone who reported back on the release candidates this time: [@b-morgan](https://github.com/b-morgan), [@ChrisHeerschap](https://github.com/ChrisHeerschap), [@cp2004](https://github.com/cp2004), [@ctgreybeard](https://github.com/ctgreybeard), [@dcodom](https://github.com/dcodom), [@DodgeDeBoulet](https://github.com/DodgeDeBoulet), [@gege2b](https://github.com/gege2b), [@gmccauley](https://github.com/gmccauley), [@hamster65](https://github.com/hamster65), [@jbjones27](https://github.com/jbjones27), [@jneilliii](https://github.com/jneilliii), [@JohnOCFII](https://github.com/JohnOCFII), [@kantlivelong](https://github.com/kantlivelong), [@louispires](https://github.com/louispires), [@marknn3](https://github.com/marknn3), [@NotExpectedYet](https://github.com/NotExpectedYet), [@ogsv](https://github.com/ogsv), [@schnello](https://github.com/schnello), [@spling-du-futur](https://github.com/spling-du-futur) and [@zeroflow](https://github.com/zeroflow).

### Insights

If you are interested in some numbers, here's some data extracted from the **anonymous usage tracking** for the four RCs that
went before 1.4.1's stable release:

  * 1.4.1rc1 (2020-07-06): 269 instances, 1865h or 2.6 months of accumulative printing time
  * 1.4.1rc2 (2020-07-08): 480 instances, 7790h or 10.8 months of accumulative printing time
  * 1.4.1rc3 (2020-07-15): 679 instances, 15500h or 1.8 years of accumulative printing time
  * 1.4.1rc4 (2020-07-29): 454 instances, 4400h or 6 months of accumulative printing time
  
<div class="row-fluid" style="margin-bottom: 10px">
    <div class="span12">
        <a href="/assets/img/blog/2020-08/2020-08-04-rc-instances.png" data-lightbox="{{ page.id }}" data-title="1.4.1rc instances over the past month, per hour"><img src="/assets/img/blog/2020-08/2020-08-04-rc-instances.png"></a>
    </div>
</div>
<div class="row-fluid" style="margin-bottom: 10px">
    <div class="span12">
        <a href="/assets/img/blog/2020-08/2020-08-04-rc-prints.png" data-lightbox="{{ page.id }}" data-title="Accumulated 1.4.1rc print times over the past month, per hour"><img src="/assets/img/blog/2020-08/2020-08-04-rc-prints.png"></a>
    </div>
</div>
<div class="row-fluid" style="margin-bottom: 10px">
    <div class="span12">
        <a href="/assets/img/blog/2020-08/2020-08-04-rc-pies.png" data-lightbox="{{ page.id }}" data-title="1.4.1rc instances and accumulated print time over the past month, total"><img src="/assets/img/blog/2020-08/2020-08-04-rc-pies.png"></a>
    </div>
</div>
  
And if you haven't yet, maybe also [check out this recent post](/blog/2020/07/29/automating-octoprints-release-tests) 
on the new **test rig** I built for the final update tests I do for each and every OctoPrint release and release candidate.

### Further Information

It may take up to 24h for your update notification to pop up, so don't 
be alarmed if it doesn't show up immediately after reading this. You
can force the update however via Settings > Software Update > 
Advanced options > Force check for update.

If you get an error about "no suitable distribution" during update, please read 
[this](https://community.octoprint.org/t/i-got-some-error-about-no-suitable-distribution-during-update-and-now-my-server-wont-start/235).

**If you have any problems with your OctoPrint installation, please seek 
support on the [community forum](https://community.octoprint.org).**

### Links

  * [Changelog and Release Notes](https://github.com/OctoPrint/OctoPrint/releases/tag/1.4.1)
  * [Community forum](https://community.octoprint.org)
  * [Discord Server](https://discord.octoprint.org)
  * [FAQ](https://faq.octoprint.org)
  * [Documentation](http://docs.octoprint.org/)
  * [Contribution Guidelines (also relevant for creating bug reports!)](https://github.com/OctoPrint/OctoPrint/blob/master/CONTRIBUTING.md)
  * [How to file a bug report](https://github.com/OctoPrint/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report)
  * [How to roll back to an earlier release (OctoPi)](https://community.octoprint.org/t/how-can-i-revert-to-an-older-version-of-the-octoprint-installation-on-my-octopi-image/205)
  * [How to roll back to an earlier release (manual install)](https://community.octoprint.org/t/how-can-i-roll-back-to-an-earlier-version-after-an-update/234)
