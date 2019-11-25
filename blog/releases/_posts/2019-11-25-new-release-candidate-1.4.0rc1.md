---

layout: post
title: 'New release candidate: 1.4.0rc1'
author: foosel
date: 2019-11-25 17:30:00 +0100
card: /assets/img/blog/2019-11/2019-11-25-octoprint-1.4.0rc1-card.png
featuredimage: /assets/img/blog/2019-11/2019-11-25-octoprint-1.4.0rc1-card.png
images:
- url: /assets/img/blog/2019-11/2019-11-25-screenshot-access-control-users.png
  title: User management
- url: /assets/img/blog/2019-11/2019-11-25-screenshot-access-control-edit-user.png
  title: User editor
- url: /assets/img/blog/2019-11/2019-11-25-screenshot-access-control-groups.png
  title: Group management
- url: /assets/img/blog/2019-11/2019-11-25-screenshot-access-control-edit-group.png
  title: Group editor
- url: /assets/img/blog/2019-11/2019-11-25-screenshot-plugin-manager-filters-and-search.png
  title: Filters & search in Plugin Manager
poster: /assets/img/blog/2019-11/2019-11-25-octoprint-1.4.0rc1-poster.png
excerpt: The very first release candidate for the upcoming 1.4.0 release!

---

After 3 years on 1.3.x, it's time for a new big release. And this first release candidate of 1.4.0 is the very
first step towards it. 

[The full changelog](https://github.com/foosel/OctoPrint/releases/tag/1.4.0rc1) is packed with 
new features, improvements and fixes of existing functionality. Some highlights:

  * 1.4.0 introduces a **new granular permission system** that allows you to fully customize which users (and - new! - user 
    groups) are allowed to access which functionality. See the screenshots below for an idea of how all this looks
    visually. Special thanks to @Salandora for a lot of the legwork on this!
  * If you've followed me on [OctoPrint On Air](https://www.youtube.com/playlist?list=PL9j2DtsIPVkOFIMRrnnbXsnXtQmwj1IId) 
    or paid some closer attention to the output of plugin manager
    or software updater in OctoPrint, you'll have heard about the pending end of life of Python 2 in favor of the new
    version Python 3. OctoPrint so far only supported running under Python 2 - this has changed now with this RC and 1.4.x 
    in general, which should allow OctoPrint to **run problem free under both Python 2 and 3**. Please help test this! 
    And to all the plugin authors among you, please also take note of the heads-up in the changelog and also quoted below.
    Huge thanks to everyone who helped in the adjustment effort needed to make this possible, especially @ByReaL, 
    @razerraz, @smurfix & @tedder! Wouldn't have been possible without y'all!
  * Additionally to the somewhat anachronistic MPEG2 format, OctoPrint now also supports to **create timelapse recordings 
    in H264**. Special thanks to @koenkooi for this!
  * If the underlying render engine supports it there'll be a **progress bar for ongoing timelapse rendering** now thanks
    to @ZachNo!
  * A bunch of new events and plugin hooks allow for even more possibilities in regards to customization through
    plugins.
  * The Software Updater can now be configured to track Github Commits for OctoPrint right from the UI. A new version
    check `pypi_release` allows checking the Python Package Index for new releases of a package, and this is also used
    to optionally allow to keep `pip` updated right from within OctoPrint itself instead of having to go through the
    command line for that. Note that this is disabled by default since I do *not* control `pip` updates and hence cannot
    guarantee trouble free updates.
  * The Plugin Manager now has a search function and some filters to make it easier to navigate through the list
    of installed plugins. See the screenshot below. Additionally it will now offer to delete plugin data from plugins
    about to be uninstalled, and also offers a general clean-up function for left-over plugin data.
  * After a lot of begging in that regard, the Software Updater and the Plugin Manager both can now be configured to ignore
    the throttle state of the Pi by setting `ignore_throttled` in `config.yaml` for either or both. Note that this 
    setting is intentionally not exposed in the UI since too many people would use it to shoot themselves into the foot.
    Updating on a throttled system *has* caused corrupt installs in the past, same goes for new plugin installs, don't 
    say I didn't warn you.
  * There have of course also been a bunch of fixes for bugs reported in older versions, like a fix of a potential dead 
    lock when cancelling an SD print, overzealous filtering of history entries on the `/printer/{tool|bed|chamber}` 
    API endpoints, G2 and G3 arcs being misinterpreted in the GCODE viewer and more.
  * ... and more.

Due to the new Python 3 compatibility there's a heads-up for plugin authors:

> This release candidate officially adds support to run OctoPrint under Python 3 instead of 2. However, most third party plugins probably do not yet support Python 3. In order to allow Plugin Authors to test and if necessary adjust their plugins first before OctoPrint tries to load them under Python 3, a new plugin property `__plugin_pythoncompat__` has been introduced. Plugins should define the compatibly Python version via this property which OctoPrint will check on load and only proceed with loading the plugin under Python 3 if it signals compatibility. 
> 
>
> Additionally, the Plugin Repository has been expanded to include a new field `compatibility.python` which signals Python compatibility on the listing as well so that OctoPrint's Plugin Manager will only show such plugins from the repository as installable under Python 3 which are configured as such.
>
> 
> Please see [this post on the OctoPrint Community Forums](https://community.octoprint.org/t/towards-python-3-and-octoprint-1-4-0/12382?u=foosel) on how to go about compatibility testing and how to modify existing plugins to work with OctoPrint when running under Python 3.
>
> 
> By default, OctoPrint will assume compatibility to Python 2 only.

You can find the full changelog and release notes as usual [on Github](https://github.com/foosel/OctoPrint/releases/tag/1.4.0rc1).
It may look a bit shorter than the maintenance release changelogs, but that's because the points listed under "new features"
pack quite the punch with regards to involved work 😉

Special thanks to everyone who contributed to this release candidate and provided full, analyzable bug reports and pull requests, especially [balassy](https://github.com/balassy), [ByReaL](https://github.com/ByReaL), [cameroncros](https://github.com/cameroncros), [CapnBry](https://github.com/CapnBry), [cbxbiker61](https://github.com/cbxbiker61), [dforsi](https://github.com/dforsi), [eyal0](https://github.com/eyal0), [FHeilmann](https://github.com/FHeilmann), [jammi](https://github.com/jammi), [justfalter](https://github.com/justfalter), [kantlivelong](https://github.com/kantlivelong), [kevans91](https://github.com/kevans91), [koenkooi](https://github.com/koenkooi), [mkobler](https://github.com/mkobler), [noahsmartin](https://github.com/noahsmartin), [povlhp](https://github.com/povlhp), [razerraz](https://github.com/razerraz), [RyuzakiKK](https://github.com/RyuzakiKK), [Salandora](https://github.com/Salandora), [smurfix](https://github.com/smurfix), [tedder](https://github.com/tedder) & [ZachNo](https://github.com/ZachNo) for their PRs!

As the past RCs have shown me that a lot of people appear to be unaware of this: **Please do *not* install this RC if you 
expect a fully stable version**. It is not a stable release, it is a release *candidate*, and of the next big release
to boot: severe bugs may occur, and they might be bad enough that they make a manual downgrade to an earlier version 
necessary - maybe even from the command line. 

You should feel comfortable with and capable of possibly having to do this *before* installing an RC.

If you want to and can help test this release candidate, you can find information on how to switch to the 
**"Devel RCs"** release channel [in this guide](https://community.octoprint.org/t/how-to-use-the-release-channels-to-help-test-release-candidates/402)
if not already done (also linked below). Please note that **contrary to maintenance releases this RC is not available
on the "Maintenance RCs" release channel** so if you are tracking that you'll need to switch. The reason is that 
RCs of big releases might be more unstable at first than pure maintenance releases due to newly introduced features
or very heavy refactorings, so I'm splitting these between two release channels. Note that when tracking "Devel RCs" 
you'll get all releases from "Stable" and "Maintenance RCs" as well.

**Please provide feedback** on this RC. For general feedback you can use 
[this ticket on the tracker](https://github.com/foosel/OctoPrint/issues/3347).
The information that everything works fine for you is also valuable feedback 😄. **For bug reports** please follow
["How to file a bug report"](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report) - 
I need logs and reproduction steps to fix issues, not just the information that something doesn't work so make sure to
**fill out all fields of the issue template**.

Thanks!

Depending on the feedback regarding this version I'll look into fixing 
any observed regressions and bugs and pushing out a follow-up version 
as soon as possible and necessary.

### Links

  * [Ticket for general feedback](https://github.com/foosel/OctoPrint/issues/3347)
  * [Changelog and Release Notes](https://github.com/foosel/OctoPrint/releases/tag/1.4.0rc1)
  * [How to use release channels to help test release candidates](https://community.octoprint.org/t/how-to-use-the-release-channels-to-help-test-release-candidates/402)
  * [How to file a bug report](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report)
  * [Contribution Guidelines (also relevant for creating bug reports!)](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md)
  * [FAQ](https://faq.octoprint.org)
  * [Documentation](http://docs.octoprint.org/)
  * [How to roll back to an earlier release (OctoPi)](https://community.octoprint.org/t/how-can-i-revert-to-an-older-version-of-the-octoprint-installation-on-my-octopi-image/205)
  * [How to roll back to an earlier release (manual install)](https://community.octoprint.org/t/how-can-i-roll-back-to-an-earlier-version-after-an-update/234)
