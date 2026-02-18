---
layout: post-bugfix
title: "New release: 1.11.7"
author: foosel
date: 2026-02-18 14:10:00 +0100
card: /assets/img/blog/2026-02/2026-02-18-octoprint-1.11.7-card.png
featuredimage: /assets/img/blog/2026-02/2026-02-18-octoprint-1.11.7-card.png
poster: /assets/img/blog/2026-02/2026-02-18-octoprint-1.11.7-poster.png

excerpt: "The seventh bugfix release for 1.11.x, fixing some bugs reported since the release of 1.11.0."

bugfix: 1.11.7
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

contributors:
  - jacopotediosi
---

I was hoping to avoid this to be able to fully concentrate on 1.12.0, but sadly a bug with PrusaSlicer's webview crept into 1.11.6, and so here is the second release of 2026, a bugfix release for 1.11.x, fixing that and a bunch of other issues:

> **🐛 Bug fixes**
>
> _Core_
>
> - [#5235](https://github.com/OctoPrint/OctoPrint/issues/5235): Add custom parser for User Agent under Prusa Slicer's webview, fixing an UI loading error
> - [#5240](https://github.com/OctoPrint/OctoPrint/issues/5240): Use the right capability for registering active position autoreporting
> - [#5248](https://github.com/OctoPrint/OctoPrint/issues/5248): Fix checkboxes not showing for unrendered timelapses
> - [#5249](https://github.com/OctoPrint/OctoPrint/issues/5249): Fix response behaviour on missing `subgroups` on access management API
> - [#5250](https://github.com/OctoPrint/OctoPrint/issues/5250): Don't send session cookies if login mechanism is `apikey`
> - [#5252](https://github.com/OctoPrint/OctoPrint/issues/5252): Correctly convert timezone in `Last-Modified`
>
> _CLI_
>
> - [#5239](https://github.com/OctoPrint/OctoPrint/issues/5239): Fix help & generated output for `octoprint user {activate|deactivate}`
>
> _Plugin Manager_
>
> - [#5254](https://github.com/OctoPrint/OctoPrint/issues/5254): Fix cleanup tab always staying empty

You can also take a look at the [changelog on GitHub](https://github.com/OctoPrint/OctoPrint/releases/tag/1.11.7).

Like every single release (and release candidate) of OctoPrint ever since early 2016 this release was made possible only
through continued financial support by people like you! 💕

**[Click here](/support-octoprint/) if you enjoy OctoPrint and want to help with its funding!**
