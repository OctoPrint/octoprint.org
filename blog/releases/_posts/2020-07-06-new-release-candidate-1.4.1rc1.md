---

layout: post
title: 'New release candidate: 1.4.1rc1'
author: foosel
date: 2020-07-06 13:40:00 +0200
card: /assets/img/blog/2020-07/2020-07-06-octoprint-1.4.1rc1-card.png
featuredimage: /assets/img/blog/2020-07/2020-07-06-octoprint-1.4.1rc1-card.png
poster: /assets/img/blog/2020-07/2020-07-06-octoprint-1.4.1rc1-poster.png
images:
- url: /assets/img/blog/2020-07/2020-07-06-temperature-profiles.png
  title: Temperature profile selector for all heaters
- url: /assets/img/blog/2020-07/2020-07-06-file-move.png
  title: Move files right from the file list
- url: /assets/img/blog/2020-07/2020-07-06-pmgr-repo-browser.png
  title: The plugin manager now shows stats for the plugins on the plugin repository and allows to install single file plugins
- url: /assets/img/blog/2020-07/2020-07-06-pmgr-overview.png
  title: The plugin manager also now shows more information about the installed plugins, including their Python compatibility
excerpt: The first release candidate for the upcoming 1.4.1 release, with improvements and fixes!

---

After some insane months thanks to an pandemic induced increase in support requests, it's finally time
to push out a first release candidate for the upcoming 1.4.1 maintainence release!

The [full changelog](https://github.com/OctoPrint/OctoPrint/releases/tag/1.4.1rc1) contains a long list of improvements and bug fixes, however I want to highlight
the following:

  * The temperature tab got a new control to select preconfigured temperature profiles on all heaters with one click
  * The newly bundled "File Check" plugin will sanity check uploaded files and warn about potential issues. Currently the plugin only detects `{travel_speed}` place holders left in GCODE. Read more in [the plugin's README](https://github.com/OctoPrint/OctoPrint-FileCheck/blob/master/README.md).
  * The first run wizard now allows to restore from a plugin right away.
  * You can now move files in the file list to other folders without the need of a third party plugin.
  * The Plugin Manager now shows stats on the plugins available on the repository, such as number of known installs, date of last release etc. Installed plugins now also make it more transparent whether they are already compatible to Python 3 or not.
  * The Plugin Manager now also supports installing so called single-file plugins - mini plugins only consisting of a single python file which are a quick and easy way to work around broken communication or similar backend-only situations. This feature was developed live on air, you can learn more about it [in this episode of OctoPrint Code & Chat](https://www.youtube.com/watch?v=59xEaUwWU30). Consequently, the Software Update plugin was also extended with some new version check and updater types to support auto-updating single file plugins, read more [in the docs here](https://docs.octoprint.org/en/maintenance/bundledplugins/softwareupdate.html).
  * The Printer Safety Check has been renamed to Firmware Check & extracted into a still bundled but separately maintained plugin. It now also detects firmware with known broken communication protocol implementations (like the infamous `CBD make it` and `ZWLF make it` variants) and links to related FAQ entries on detection.
  * The broken by design comm port auto detection has been rewritten completely from scratch. That should hopefully make auto detection work more reliably in the future.
  * Original file modification timestamps will now be persisted on restoring from a backup.
  * The "read-only" group behaviour has been fixed so that it is actually possible to create a read-only account. The `User` group is no longer enforced on users, though pre checked for new users (if kept default). This makes it also possible to create group less users, so keep that in mind.
  * The permission issue that kept the Announcement icon show up on the navbar has been solved.
  * A bunch of dependencies were upgraded to the latest versions. Among these is also the templating engine Jinja2, which results in a **heads-up** for plugin authors, read below.
  * ... and many more improvements & fixes.

There are also a bunch of **heads-ups** with this release for **plugin authors** and other developers:

> **Heads-up for plugin authors: Jinja2 update has one backwards incompatibility, please read**
> 
> Current Jinja versions no longer allow modifying variables set outside of for loops inside them. [...]
> 
> See also [#1697](https://github.com/OctoPrint/OctoPrint/issues/1697) and https://jinja.palletsprojects.com/en/2.11.x/templates/#assignments
> 
> The Jinja dependency upgrade thus introduces a breaking change for plugins as well. However, it was necessary for security reasons: older versions have a bug that could allow template authors to break out of the template sandbox. Not a huge risk in the context of OctoPrint (plugins already have a lot more power than jinja would give them), but still overdue to fix.

You can find more details and example code in the [Release Notes](https://github.com/OctoPrint/OctoPrint/releases/tag/1.4.1rc1).

> **Heads-up for plugin authors: `awesome-slugify` is now bundled as `octoprint.vendor.awesome_slugify`, update your imports!**
> 
> Due to a necessary dependency update of a third party dependency pulling in a different slugify library ("python-slugify") that clashes with `awesome-slugify`, the latter has been bundled. If you use `import slugify` anywhere in your code, please be aware that that will now possibly pull in the aforementioned other library or possibly a partially overwritten `awesome-slugify`. Plugin authors are advised to update the imports of `awesome-slugify` like this:
> 
> ``` python
> ### old
> 
> # example 1
> import slugify
> 
> # example 2
> from slugify import Slugify
> 
> ### new
> 
> # example 1
> try:
>   # OctoPrint>=1.4.1
>   import octoprint.vendor.awesome_slugify as slugify 
> except ImportError:
>   # OctoPrint<=1.4.0
>   import slugify
> 
> # example 2
> try:
>   # OctoPrint>=1.4.1
>   from octoprint.vendor.awesome_slugify import Slugify
> except ImportError:
>   # OctoPrint<=1.4.0
>   from slugify import Slugify
> ```
> 
> That will also guarantee backwards compatibility if installed under OctoPrint versions prior to 1.4.1. Alternatively switch fully to the 1.4.1 version and adjust your plugin listing to a minimum OctoPrint version of 1.4.1.

> **Heads-up for developers: The included virtual printer has had its settings migrated to a different location in `config.yaml`**
> 
> The bundled Virtual Printer plugin has finally been turned fully isolated into a self contained plugin and thus its settings have been moved from `devel.virtualPrinter` to `plugins.virtual_printer` in `config.yaml`. An auto migration is in place that should take care of moving anything already configured on first start under 1.4.1+, however should you be somehow manipulating `config.yaml` through automation or something in order to change virtual printer settings, you'll have to update your workflows.

You can find the full changelog and release notes as usual [on Github](https://github.com/OctoPrint/OctoPrint/releases/tag/1.4.1rc1).

Special thanks to everyone who contributed to this release candidate and provided full, analyzable bug reports, you help
making the next release as stable as possible!

As the past RCs have shown me that a lot of people appear to be unaware of this: **Please do *not* install this RC if you 
expect a fully stable version**. It is not a stable release, it is a release *candidate*, and of the next big release
to boot: severe bugs may occur, and they might be bad enough that they make a manual downgrade to an earlier version 
necessary - maybe even from the command line. 

You should feel comfortable with and capable of possibly having to do this *before* installing an RC.

If you want to and can help test this release candidate, you can find information on how to switch to the 
**"Maintenance RCs"** release channel [in this guide](https://community.octoprint.org/t/how-to-use-the-release-channels-to-help-test-release-candidates/402)
if not already done (also linked below).

**Please provide feedback** on this RC. For general feedback you can use 
[this ticket on the tracker](https://github.com/OctoPrint/OctoPrint/issues/3626).
The information that everything works fine for you is also valuable feedback 😄. **For bug reports** please follow
["How to file a bug report"](https://github.com/OctoPrint/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report) - 
I need logs and reproduction steps to fix issues, not just the information that something doesn't work so make sure to
**fill out all fields of the issue template**.

Thanks!

Depending on the feedback regarding this version I'll look into fixing 
any observed regressions and bugs and pushing out a follow-up version 
as soon as possible and necessary.

### Links

  * [Ticket for general feedback](https://github.com/OctoPrint/OctoPrint/issues/3626)
  * [Changelog and Release Notes](https://github.com/OctoPrint/OctoPrint/releases/tag/1.4.0rc1)
  * [How to use release channels to help test release candidates](https://community.octoprint.org/t/how-to-use-the-release-channels-to-help-test-release-candidates/402)
  * [How to file a bug report](https://github.com/OctoPrint/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report)
  * [Contribution Guidelines (also relevant for creating bug reports!)](https://github.com/OctoPrint/OctoPrint/blob/master/CONTRIBUTING.md)
  * [FAQ](https://faq.octoprint.org)
  * [Documentation](http://docs.octoprint.org/)
  * [How to roll back to an earlier release (OctoPi)](https://community.octoprint.org/t/how-can-i-revert-to-an-older-version-of-the-octoprint-installation-on-my-octopi-image/205)
  * [How to roll back to an earlier release (manual install)](https://community.octoprint.org/t/how-can-i-roll-back-to-an-earlier-version-after-an-update/234)
