---

layout: post-bugfix
title: 'New release: 1.5.1'
author: foosel
date: 2020-12-04 11:50:00 +0100
card: /assets/img/blog/2020-12/2020-12-04-octoprint-1.5.1-card.png
featuredimage: /assets/img/blog/2020-12/2020-12-04-octoprint-1.5.1-card.png
poster: /assets/img/blog/2020-12/2020-12-04-octoprint-1.5.1-poster.png
excerpt: "This is a hotfix release to fix two bugs in 1.5 that sadly only were reported after the release candidate phase."

bugfix: 1.5.1
release:
  tag: 1.5.0
  link: /blog/2020/11/30/new-release-1.5.0/
  headsups: true

---

This is a hotfix release to fix two bugs in 1.5 that sadly only were reported after the release candidate phase.

Due to that the [changelog](https://github.com/OctoPrint/OctoPrint/releases/tag/1.5.1) is very short and only consists
of these entries:

>  * [#3844](https://github.com/OctoPrint/OctoPrint/issues/3844) - Fix `api/files/<origin>/<path>` not returning `children` for folders
>  * [#3852](https://github.com/OctoPrint/OctoPrint/issues/3852) - Fix service discovery messing with hostname resolution. Still unclear on *how* that even happens and unable to reproduce, but at least simply completely ignoring loopback devices seems to do the trick.

Like every single release (and release candidate) of OctoPrint ever since early 2016 this release was made possible only
through your continued **[support of my work](/support-octoprint/)** 💕
