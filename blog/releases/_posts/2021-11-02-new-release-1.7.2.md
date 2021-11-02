---

layout: post-bugfix
title: 'New release: 1.7.2'
author: foosel
date: 2021-11-02 18:30:00 +0100
card: /assets/img/blog/2021-11/2021-11-02-octoprint-1.7.2-card.png
featuredimage: /assets/img/blog/2021-11/2021-11-02-octoprint-1.7.2-card.png
poster: /assets/img/blog/2021-11/2021-11-02-octoprint-1.7.2-poster.png
excerpt: "This bugfix release fixes an issue just discovered in OctoPrint 1.7.1."

bugfix: 1.7.2
release:
  tag: 1.7.0
  link: /blog/2021/10/11/new-release-1.7.0/
  headsups: true

---

Hot on the heels of the first bugfix release yesterday comes a new one today, as there
was a bug in 1.7.1 that caused issues for third party clients (e.g. the Cura Connection Plugin):

>  * [#4293](https://github.com/OctoPrint/OctoPrint/issues/4293) - Fix double quoting of the `resource` ref on the files API. This was causing issues with the Cura plugin and other third party API clients.

You can also take a look at the [extremely short changelog on GitHub](https://github.com/OctoPrint/OctoPrint/releases/tag/1.7.2).

Like every single release (and release candidate) of OctoPrint ever since early 2016 this release was made possible only
through your continued **[support of my work](/support-octoprint/)** 💕
