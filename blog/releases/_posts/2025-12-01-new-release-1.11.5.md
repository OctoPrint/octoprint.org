---
layout: post-bugfix
title: "New release: 1.11.5"
author: foosel
date: 2025-12-01 13:55:00 +0100
card: /assets/img/blog/2025-12/2025-12-01-octoprint-1.11.5-card.png
featuredimage: /assets/img/blog/2025-12/2025-12-01-octoprint-1.11.5-card.png
poster: /assets/img/blog/22025-12/2025-12-01-octoprint-1.11.5-poster.png

excerpt: "The fifth bugfix release for 1.11.x, fixing some bugs reported since the release of 1.11.0."

bugfix: 1.11.5
release:
  tag: 1.11.0
  link: /blog/2025/04/22/new-release-1.11.0/
  headsups: true
prior:
  headsups:
    - release: 1.11.2
      link: /blog/2025/06/10/new-release-1.11.2/
    - release: 1.11.3
      link: /blog/2025/09/09/new-release-1.11.3/
---

The year is coming to an end, and while I'm currently mostly focused on 1.12.0 (and Moonraker & Bambu Connector Plugins for the new comm layer), I still wanted to push out
this bugfix release for 1.11.x with fixes for two issues that were reported in the past few weeks, and a logic error I spotted during development:

> **🐛 Bug fixes**
>
> _Core_
>
> - [#5206](https://github.com/OctoPrint/OctoPrint/issues/5206): Workaround for a regression in Tornado 6.5.x, causing file uploads with non-latin-1 characters in the name to fail.
> - Fixed logic error in pure-python fallback of `search_through_file` helper
>
> _Backup Plugin_
>
> - Apply `--no-build-isolation` during installation of plugins with legacy packaging

You can also take a look at the [changelog on GitHub](https://github.com/OctoPrint/OctoPrint/releases/tag/1.11.3).

Like every single release (and release candidate) of OctoPrint ever since early 2016 this release was made possible only
through continued financial support by people like you! 💕

**[Click here](/support-octoprint/) if you enjoy OctoPrint and want to help with its funding!**
