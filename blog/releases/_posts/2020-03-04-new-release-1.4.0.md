---

layout: post
title: 'New release: 1.4.0'
author: foosel
date: 2020-03-04 12:45:00 +0100
card: /assets/img/blog/2020-03/2020-03-04-octoprint-1.4.0-card.png
featuredimage: /assets/img/blog/2020-03/2020-03-04-octoprint-1.4.0-card.png
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
poster: /assets/img/blog/2020-03/2020-03-04-octoprint-1.4.0-poster.png
excerpt: A new release that brings a new granular permission system, Python 3 compatibility and
  plenty more features, improvements and bug fixes!
 
redirect_from:
- /blog/2020/03/04/new-release-candidate-1.4.0/

---

After 3 years on 1.3.x and over 3 months of release candidate testing, it's finally time to release 1.4.0!

As every single release (and release candidate) of OctoPrint ever since early 2016 this was made possible only 
through your continued **[support of my work](/support-octoprint/)** 💕

[The full changelog](https://github.com/foosel/OctoPrint/releases/tag/1.4.0) is packed with 
new features, improvements and fixes of existing functionality. Some highlights:

  * 1.4.0 introduces a **new granular permission system** that allows you to fully customize which users (and - new! - user 
    groups) are allowed to access which functionality. See the screenshots below for an idea of how all this looks
    visually. Special thanks to @Salandora for a lot of the legwork on this!
  * If you've followed me on [OctoPrint On Air](https://www.youtube.com/playlist?list=PL9j2DtsIPVkOFIMRrnnbXsnXtQmwj1IId) 
    or paid some closer attention to the output of plugin manager
    or software updater in OctoPrint, you'll have heard about the pending end of life of Python 2 in favor of the new
    version Python 3. OctoPrint so far only supported running under Python 2 - this has changed now with 1.4.0 which 
    allows OctoPrint to **run problem free under both Python 2 and 3**! 

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

> This release officially adds support to run OctoPrint under Python 3 instead of 2, which has become EOL as of January 1st 2020. However, most third party plugins probably do not yet support Python 3. In order to allow Plugin Authors to test and if necessary adjust their plugins first before OctoPrint tries to load them under Python 3, a new plugin property `__plugin_pythoncompat__` has been introduced. Plugins should define the compatibly Python version via this property which OctoPrint will check on load and only proceed with loading the plugin under Python 3 if it signals compatibility. 
>
>
> Additionally, the Plugin Repository has been expanded to include a new field `compatibility.python` which signals Python compatibility on the listing as well so that OctoPrint's Plugin Manager will only show such plugins from the repository as installable under Python 3 which are configured as such.
>
>
> Please see [this guide in the documentation](https://docs.octoprint.org/en/master/plugins/python3_migration.html) on how to go about compatibility testing and how to modify existing plugins to work with OctoPrint when running under Python 3.
>
>
> By default, OctoPrint will assume compatibility to Python 2 only.

You can find the full changelog and release notes as usual [on Github](https://github.com/foosel/OctoPrint/releases/tag/1.4.0).

Also see the **Further Information** and **Links** below for more information,
where to find help and how to roll back.

Special thanks to everyone who contributed to this release candidate and provided full, analyzable bug reports and pull requests, especially [balassy](https://github.com/balassy), [ByReaL](https://github.com/ByReaL), [cameroncros](https://github.com/cameroncros), [CapnBry](https://github.com/CapnBry), [cbxbiker61](https://github.com/cbxbiker61), [dforsi](https://github.com/dforsi), [eyal0](https://github.com/eyal0), [FHeilmann](https://github.com/FHeilmann), [fieldOfView](https://github.com/fieldOfView), [jammi](https://github.com/jammi), [justfalter](https://github.com/justfalter), [kantlivelong](https://github.com/kantlivelong), [kevans91](https://github.com/kevans91), [koenkooi](https://github.com/koenkooi), [mkobler](https://github.com/mkobler), [noahsmartin](https://github.com/noahsmartin), [povlhp](https://github.com/povlhp), [razerraz](https://github.com/razerraz), [RyuzakiKK](https://github.com/RyuzakiKK), [Salandora](https://github.com/Salandora), [smurfix](https://github.com/smurfix), [tedder](https://github.com/tedder) & [ZachNo](https://github.com/ZachNo) for their PRs!

And last but not least, another special **Thank you!** to everyone who reported back on the release candidates this time: [@1n5aN1aC](https://github.com/1n5aN1aC), [@Andy-ABTec](https://github.com/Andy-ABTec), [@BerndJM](https://github.com/BerndJM), [@bzed](https://github.com/bzed), [@CapnBry](https://github.com/CapnBry), [@ChrisHeerschap](https://github.com/ChrisHeerschap), [@ciordia9](https://github.com/ciordia9), [@CRCinAU](https://github.com/CRCinAU), [@Demigod001](https://github.com/Demigod001), [@Deneteus](https://github.com/Deneteus), [@devildant](https://github.com/devildant), [@dragonflybog](https://github.com/dragonflybog), [@elfelton](https://github.com/elfelton), [@Farami](https://github.com/Farami), [@fieldOfView](https://github.com/fieldOfView), [@FormerLurker](https://github.com/FormerLurker), [@gcurtis79](https://github.com/gcurtis79), [@gdombiak](https://github.com/gdombiak), [@gege2b](https://github.com/gege2b), [@gferon](https://github.com/gferon), [@jbjones27](https://github.com/jbjones27), [@jim-thompson](https://github.com/jim-thompson), [@jneilliii](https://github.com/jneilliii), [@JohnOFCII](https://github.com/JohnOFCII), [@kazibole](https://github.com/kazibole), [@krpepe](https://github.com/krpepe), [@Lantoit](https://github.com/Lantoit), [@loskexos](https://github.com/loskexos), [@louispires](https://github.com/louispires), [@MatejSpindler](https://github.com/MatejSpindler), [@mbelley](https://github.com/mbelley), [@MSeal](https://github.com/MSeal), [@NerdyProjects](https://github.com/NerdyProjects), [@NovaViper](https://github.com/NovaViper), [@OllisGit](https://github.com/OllisGit), [@PlasmaSoftUK](https://github.com/PlasmaSoftUK), [@reloxx13](https://github.com/reloxx13), [@rmoravcik](https://github.com/rmoravcik), [@santond](https://github.com/santond), [@schnello](https://github.com/schnello), [@schumar](https://github.com/schumar), [@sebaminguez](https://github.com/sebaminguez) & [@willhoh](https://github.com/willhoh).

If you are interested in some numbers, here's some data extracted from the anonymous usage tracking for the six RCs that
went before 1.4.0's stable release:

  * 1.4.0rc1: 123 instances, 58h or 2d accumulative printing time
  * 1.4.0rc2: 152 instances, 347h or 14d accumulative printing time
  * 1.4.0rc3: 668 instances, 22200h or 2.5y accumulative printing time
  * 1.4.0rc4: 760 instances, 16000h or 1.8y accumulative printing time
  * 1.4.0rc5: 808 instances, 19400h or 2.2y accumulative printing time
  * 1.4.0rc6: 614 instances, 6570h or 0.75y accumulative printing time

### Further Information

It may take up to 24h for your update notification to pop up, so don't 
be alarmed if it doesn't show up immediately after reading this. You
can force the update however via Settings > Software Update > 
Advanced options > Force check for update.

If you get an error about "no suitable distribution" during update, please read 
[this](https://discourse.octoprint.org/t/i-got-some-error-about-no-suitable-distribution-during-update-and-now-my-server-wont-start/235).

**If you have any problems with your OctoPrint installation, please seek 
support on the [community forum](https://community.octoprint.org).**

### Links

  * [Changelog and Release Notes](https://github.com/foosel/OctoPrint/releases/tag/1.4.0)
  * [Community forum](https://community.octoprint.org)
  * [FAQ](https://faq.octoprint.org)
  * [Documentation](http://docs.octoprint.org/)
  * [Contribution Guidelines (also relevant for creating bug reports!)](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md)
  * [How to file a bug report](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report)
  * [How to roll back to an earlier release (OctoPi)](https://discourse.octoprint.org/t/how-can-i-revert-to-an-older-version-of-the-octoprint-installation-on-my-octopi-image/205)
  * [How to roll back to an earlier release (manual install)](https://discourse.octoprint.org/t/how-can-i-roll-back-to-an-earlier-version-after-an-update/234)
