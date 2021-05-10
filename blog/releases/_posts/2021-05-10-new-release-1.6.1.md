---

layout: post-bugfix
title: 'New release: 1.6.1'
author: foosel
date: 2021-05-10 15:20:00 +0200
card: /assets/img/blog/2021-05/2021-05-10-octoprint-1.6.1-card.png
featuredimage: /assets/img/blog/2021-05/2021-05-10-octoprint-1.6.1-card.png
poster: /assets/img/blog/2021-05/2021-05-10-octoprint-1.6.1-poster.png
excerpt: "This is a bugfix release to fix two bugs in OctoPrint 1.6.0."

bugfix: 1.5.1
release:
  tag: 1.6.0
  link: /blog/2021/04/27/new-release-1.6.0/
  headsups: true

---

This first bugfix release for 1.6.x fixes two bugs discovered in 1.6.0 after its stable
release, one in the GCode viewer and one in the handling of SD file list requests during
and ongoing print:

>  * [#4115](https://github.com/OctoPrint/OctoPrint/issues/4115) - GCode viewer: Fix dragging when a printer profile with center origin is selected. As a welcome side effect, this now also means the GCode viewer will finally update the bed dimensions properly on printer profile change.
>  * [#4119](https://github.com/OctoPrint/OctoPrint/issues/4119) - Fix blocking timeout when requesting an SD file list while printing & prevent an SD list refresh while printing.

You can also take a look at the [short changelog on GitHub](https://github.com/OctoPrint/OctoPrint/releases/tag/1.5.3).

Like every single release (and release candidate) of OctoPrint ever since early 2016 this release was made possible only
through your continued **[support of my work](/support-octoprint/)** 💕
