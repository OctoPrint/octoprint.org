---
layout: post
title: 'New release: 1.3.8'
author: foosel
date: 2018-04-13 16:55:00 +0200
card: /assets/img/blog/2018-04/2018-04-13-octoprint-1.3.8-card.png
featuredimage: /assets/img/blog/2018-04/2018-04-13-octoprint-1.3.8-card.png
poster: /assets/img/blog/2018-04/2018-04-13-octoprint-1.3.8-poster.png
excerpt: An update of a third party dependency that OctoPrint relies on was released today that made
  a hotfix release necessary.

---

A new version of the `psutil` library was released today (5.4.4) which OctoPrint depends on. Sadly this new version is not
installable under current versions of OctoPi and hence causes significant issues on update for people
who are just updating now. 

In order to work around these issues, I decided to pin the library to the last version known to work and
push out this hotfix release with this change in place. If you have already updated to 1.3.7
you do not necessarily need to apply this update. It won't hurt if you do it, but it also won't change
anything. The observed issue for which this hotfix was put out only arises when installing OctoPrint anew
or when upgrading from a version prior to 1.3.6 (e.g. 1.3.4 as shipped with OctoPi 0.14).

This being a hotfix release means that I did not push out any
release candidates beforehand and the only change contained is a fix
for this particular issue, as visible in the
[Changelog](https://github.com/foosel/OctoPrint/releases/tag/1.3.8).

If you haven't yet,
**please also make sure to read the [release announcement for 1.3.7](/blog/2018/04/09/new-release-1.3.7/)**
as that contains more information about the things that changed
since 1.3.6. Same goes for the [Changelog for 1.3.7](https://github.com/foosel/OctoPrint/releases/tag/1.3.7).

Also see **Further Information** and **Links** below for more information,
where to find help and how to roll back.

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

  * [Changelog and Release Notes](https://github.com/foosel/OctoPrint/releases/tag/1.3.8)
  * [Community forum](https://discourse.octoprint.org)
  * [FAQ](https://faq.octoprint.org)
  * [Documentation](http://docs.octoprint.org/)
  * [Contribution Guidelines (also relevant for creating bug reports!)](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md)
  * [How to file a bug report](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report)
  * [How to roll back to an earlier release (OctoPi)](https://discourse.octoprint.org/t/how-can-i-revert-to-an-older-version-of-the-octoprint-installation-on-my-octopi-image/205)
  * [How to roll back to an earlier release (manual install)](https://discourse.octoprint.org/t/how-can-i-roll-back-to-an-earlier-version-after-an-update/234)

