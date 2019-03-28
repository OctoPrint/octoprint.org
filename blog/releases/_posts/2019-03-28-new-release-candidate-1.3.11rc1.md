---

layout: post
title: 'New release candidate: 1.3.11rc1'
author: foosel
date: 2019-03-28 12:15:00 +0100
card: /assets/img/blog/2019-03/2019-03-28-octoprint-1.3.11rc1-card.png
featuredimage: /assets/img/blog/2019-03/2019-03-28-octoprint-1.3.11rc1-card.png
poster: /assets/img/blog/2019-03/2019-03-28-octoprint-1.3.11rc1-poster.png
excerpt: The first release candidate for the upcoming 1.3.11 stable release.

---

It's time to get the next stable release 1.3.11 out of the door and as you all know, the first step towards that goal 
is always a first release candidate. 

[The full changelog is somewhat long again](https://github.com/foosel/OctoPrint/releases/tag/1.3.11rc1) and packed with 
improvements and fixes of existing functionality, most of which this time is behind the scenes. Some highlights:

  * Create a backup of working `config.yaml` after successful startup, detect incomplete startups and set safe mode flag 
    for next startup in such cases. The latter is a particularly helpful additional "safety belt" against situations 
    where third party plugins cause the whole server to no longer start up, which has happened several times in the past.
  * Remove `UI_API_KEY` and API disabling. With the inclusion of the ForceLogin plugin that doesn't serve a real 
    purpose anymore in most cases, and it was only ever more of a rate limiting feature than an actual security measure 
    anyhow. Plus it lead to a ton of false security alarms.
  * Two new plugin hooks:
    * `octoprint.printer.sdcardupload` to allow overriding the SD card upload functionality and
    * `octoprint.events.register_custom_events` to allow adding new events.
  * Addition of a new Error Tracking plugin (opt-in only of course!) which in the future will hopefully make it easier to get error traces
    from installations in the field for further analysis, especially during the Release Candidate phase. See also the
    heads-up below.
  * Action Command Prompt plugin: Streamlining of the involved commands and protocol in collaboration with the Marlin Firmware
    project.
  * GCODE Viewer: Bring back the total number of printed layers (I know several of you have been waiting for this)
  * Cura plugin: Unbundled and renamed to "Cura Legacy", see also the heads-up below.
  * Anonymous Usage Tracking plugin: Track firmware/communication errors, printer safety warnings and uptime of OctoPrint.
  * Updates of various third party dependencies - note that this slightly increases the duration of installing 1.3.11.
  * Various bug fixes, for example notifications in the UI taking up more vertical space than available, the API keys from
    the Application Keys plugin not properly working when access control is disabled, fixed caching headers on the UI that will hopefully mitigate
    some issues caused by browser caching, fixing some bugs in the Backup plugin and more.

There are also two heads-ups. One concerns the Cura slicing plugin which got unbundled and renamed to "Cura Legacy" as
already mentioned:

> **Heads-up: 1.3.11 unbundles the Cura plugin**
> 
> If you rely on the Cura Plugin for your workflow that so far was bundled with OctoPrint, be sure to install the [Cura Legacy plugin](https://github.com/OctoPrint/OctoPrint-CuraLegacy) that's now also [available on the plugin repository](https://plugins.octoprint.org/plugins/curalegacy/).
> 
> Once installed the Cura Legacy plugin will import the settings and profiles from the former bundled Cura plugin automatically on first start.

The other is about the newly introduced Error Tracking plugin which you should please enable on Release Candidates such
as this one 🙂

> **Heads-up: 1.3.11 bundles a new Error Tracking plugin, please enable it on Release Candidates**
> 
> The Error Tracking plugin is a completely separate plugin from the existing Anonymous Usage Tracking plugin. Its tracking is disabled by default. Its purpose is to collect error information from instances in order to allow better issue analysis especially during the Release Candidate phase, or when prompted after reporting a bug. Thus it will also ask you to enable it on start while subscribed to an RC release channel. 
> 
> The plugin uses a [sentry.io](https://sentry.io) instance, kindly provided to OctoPrint by sentry.io.
 
You can find the full changelog and release notes as usual [on Github](https://github.com/foosel/OctoPrint/releases/tag/1.3.11rc1).

Special thanks to everyone who contributed to this release candidate, especially [@agrif](https://github.com/agrif), [@akraus53](https://github.com/akraus53), [@AndyQ](https://github.com/AndyQ), [@CapnBry](https://github.com/CapnBry), [@DanielJoyce](https://github.com/DanielJoyce), [@devildant](https://github.com/devildant), [@Fabi0San](https://github.com/Fabi0San), [@fake-name](https://github.com/fake-name), [@fieldOfView](https://github.com/fieldOfView), [@gloomyandy](https://github.com/gloomyandy), [@HarlemSquirrel](https://github.com/HarlemSquirrel), [@hgross](https://github.com/hgross), [@jubaleth](https://github.com/foosel/OctoPrint/commits?author=jubaleth), [@melgish](https://github.com/melgish), [@rgriebl](https://github.com/rgriebl) and [@tedder](https://github.com/tedder) for their PRs.

As the past RCs have shown me that a lot of people appear to be unaware of this: **Please do *not* install this RC if you 
expect a fully stable version**. It is not a stable release, it is a release *candidate*: severe bugs may occur, and 
they might be bad enough that they make a manual downgrade to an earlier version necessary - maybe even from the command line. 

You should feel comfortable with and capable of possibly having to do this *before* installing an RC.

If you want to and can help test this release candidate, you can find information on how to switch to the 
"Maintenance RCs" release channel [in this guide](https://community.octoprint.org/t/how-to-use-the-release-channels-to-help-test-release-candidates/402)
if not already done (also linked below).

**Please provide feedback** on this RC. For general feedback you can use 
[this ticket on the tracker](https://github.com/foosel/OctoPrint/issues/3087).
The information that everything works fine for you is also valuable feedback 😄. **For bug reports** please follow
["How to file a bug report"](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report) - 
I need logs and reproduction steps to fix issues, not just the information that something doesn't work so make sure to
**fill out all fields of the issue template**.

Thanks!

Depending on how the feedback for this release candidate turns out, I'll either look into releasing 1.3.11 or fix any 
observed regressions and push out a new release candidate ASAP.

### Links

  * [Ticket for general feedback](https://github.com/foosel/OctoPrint/issues/3087)
  * [Changelog and Release Notes](https://github.com/foosel/OctoPrint/releases/tag/1.3.11rc1)
  * [How to use release channels to help test release candidates](https://community.octoprint.org/t/how-to-use-the-release-channels-to-help-test-release-candidates/402)
  * [How to file a bug report](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report)
  * [Contribution Guidelines (also relevant for creating bug reports!)](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md)
  * [FAQ](https://faq.octoprint.org)
  * [Documentation](http://docs.octoprint.org/)
  * [How to roll back to an earlier release (OctoPi)](https://community.octoprint.org/t/how-can-i-revert-to-an-older-version-of-the-octoprint-installation-on-my-octopi-image/205)
  * [How to roll back to an earlier release (manual install)](https://community.octoprint.org/t/how-can-i-roll-back-to-an-earlier-version-after-an-update/234)
