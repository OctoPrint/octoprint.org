---

layout: post-bugfix
title: 'New release: 1.7.1'
author: foosel
date: 2021-11-01 16:00:00 +0100
card: /assets/img/blog/2021-11/2021-11-01-octoprint-1.7.1-card.png
featuredimage: /assets/img/blog/2021-11/2021-11-01-octoprint-1.7.1-card.png
poster: /assets/img/blog/2021-11/2021-11-01-octoprint-1.7.1-poster.png
excerpt: "This is a bugfix release to fix three issues in OctoPrint 1.7.0."

bugfix: 1.7.1
release:
  tag: 1.7.0
  link: /blog/2021/10/11/new-release-1.7.0/
  headsups: true

contributors:
- QuinnDamerell

---

This first bugfix release for 1.7.x fixes two bugs discovered in 1.7.0 after its stable
release (one in the handling of gcode files containing a `#`, one in the sorting of plugins
in the Plugin Manager) and also provides a mitigation for a very rare issue where attempting
to enable low latency mode on the printer (a new feature in 1.7.x) causes connection issues:

>  * [#4267](https://github.com/OctoPrint/OctoPrint/issues/4267) - Properly escape names of uploaded files and timelapses containing a `#`. Not doing so would make such files unmanageable through the core UI.
>  * [#4273](https://github.com/OctoPrint/OctoPrint/issues/4273) (PR) - Plugin Manager: Fix a wrong sorting selected in the list of installed plugins and the list of plugins on the repository.
>  * [#4292](https://github.com/OctoPrint/OctoPrint/issues/4292) - Set requesting of low latency mode on the serial connection to disabled by default, as there's a small number of users for which this causes issues in connecting.

You can also take a look at the [short changelog on GitHub](https://github.com/OctoPrint/OctoPrint/releases/tag/1.7.1).

Like every single release (and release candidate) of OctoPrint ever since early 2016 this release was made possible only
through your continued **[support of my work](/support-octoprint/)** 💕
