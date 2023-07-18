---
layout: post-bugfix
title: 'New release: 1.9.2'
author: foosel
date: 2023-07-18 13:15:00 +0200
card: /assets/img/blog/2023-07/2023-07-18-octoprint-1.9.2-card.png
featuredimage: /assets/img/blog/2023-07/2023-07-18-octoprint-1.9.2-card.png
poster: /assets/img/blog/2023-07/2023-07-18-octoprint-1.9.2-poster.png

excerpt: "The second bugfix release for 1.9.x, mostly to work around a new bug in a third party dependency."

bugfix: 1.9.2
release:
  tag: 1.9.0
  link: /blog/2023/05/23/new-release-1.9.0/
  headsups: true

contributors:
- cperrin88

first_time_contributors:
- cperrin88
---

This second bugfix release for 1.9.x includes a work around for an issue with a third party dependency that arose since yesterday, July 17th, and also backports two fixes from the upcoming 1.10.0 release:

> **🐛 Bug fixes**
> 
> - [#4779](https://github.com/OctoPrint/OctoPrint/issues/4779) & [PR#4780](https://github.com/OctoPrint/OctoPrint/pull/4780): Work around `argon2` password hashing algorithm not working reliably on Rock64/aarch64 - no error is produced, but the hash verification just fails.  Fall back to `pbkdf2_sha256` if this happens. Backported from 1.10.0.dev.
> - [#4806](https://github.com/OctoPrint/OctoPrint/issues/4806): Fix the `httpheader` software update check type. Backported from 1.10.0.dev.
> - [#4854](https://github.com/OctoPrint/OctoPrint/issues/4854): Upgrade PyYaml dependency to 6.0.1+. This works around an issue existing in PyYaml versions 5.4.0 to 6.0.0 with its dependency Cython in version 3.0, which was released on July 17th 2023. Said issue renders OctoPrint uninstallable due to PyYaml's install failing.

You can also take a look at the [short changelog on GitHub](https://github.com/OctoPrint/OctoPrint/releases/tag/1.9.2).

Like every single release (and release candidate) of OctoPrint ever since early 2016 this release was made possible only
through your continued **[support of my work](/support-octoprint/)** 💕
