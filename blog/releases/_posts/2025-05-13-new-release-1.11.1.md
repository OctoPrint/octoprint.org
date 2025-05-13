---
layout: post-bugfix
title: 'New release: 1.11.1'
author: foosel
date: 2025-05-13 15:30:00 +0200
card: /assets/img/blog/2025-05/2025-05-13-octoprint-1.11.1-card.png
featuredimage: /assets/img/blog/2025-05/2025-05-13-octoprint-1.11.1-card.png
poster: /assets/img/blog/2025-05/2025-05-13-octoprint-1.11.1-poster.png

excerpt: "The first bugfix release for 1.11.x, fixing some bugs and user experience issues reported since the release of 1.11.0."

bugfix: 1.11.1
release:
  tag: 1.11.0
  link: /blog/2025/04/22/new-release-1.11.0/
  headsups: true

---

This first bugfix release for 1.11.x fixes some bugs and user experience issues reported since the release of 1.11.0:


> **🔒 Security fixes**
> 
> *Minor Security fixes*
> 
> - Core: Thanks to [some issues with certain third party translations](https://community.octoprint.org/t/63166) it was discovered that autoescape doesn't affect strings loaded from translations, specifically any single or double quotes contained therein. Consequently, all places in OctoPrint's template files have been manually escaped using the existing filters `edq` (for double quoted strings) and `esq` (for single quoted strings). I will check if it's possible to also add some kind of autoescaping (with manual `safe` marking) *there* in a future version, so plugin authors should follow future release notes closely (as always).
> 
> **✨ Features & improvements**
> 
> *Core*
> 
> - [#5144](https://github.com/OctoPrint/OctoPrint/issues/5144): The confirmation dialog when deleting a file can now be disabled. See Settings > Features.
> - [#5145](https://github.com/OctoPrint/OctoPrint/issues/5145): Protect against potential misconfiguration of the reauthentication timeout by making sure it's always >= 0 when checking against it.
> - [#5153](https://github.com/OctoPrint/OctoPrint/issues/5153): It has been made clearer in `octoprint.log` when the connectivity check is disabled.
> 
> **🐛 Bug fixes**
> 
> *Core*
> 
> - [#5149](https://github.com/OctoPrint/OctoPrint/issues/5149): Fixed a logic error causing connection issues with printers such as Prusa MK3(s) when "wait for start on connect" is disabled.
> - [#5151](https://github.com/OctoPrint/OctoPrint/issues/5151): Fixed a validation error in the comm layer causing a deadlock when trying to connect while there are no serial ports available. Also disabled the connect button when no serial ports are available. The autorefresh in the background that has now been built-in since OctoPrint 1.9.0 should make sure this isn't a big behaviour change. However, in case that you need to refresh the available ports manually you can always use the little reload button on the header of the connection panel.
> 
> *Achievements Plugin*
> 
> - [#5148](https://github.com/OctoPrint/OctoPrint/issues/5148): Fixed the description of the "The Tinkerer" achievement.

You can also take a look at the [changelog on GitHub](https://github.com/OctoPrint/OctoPrint/releases/tag/1.11.1).

Like every single release (and release candidate) of OctoPrint ever since early 2016 this release was made possible only
through continued financial support by people like you! 💕 

**[Click here](/support-octoprint/) if you enjoy OctoPrint and want to help with its funding!**
