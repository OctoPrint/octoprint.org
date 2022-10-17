---

layout: post-bugfix
title: 'New release: 1.8.5'
author: foosel
date: 2022-10-17 17:00:00 +0200
card: /assets/img/blog/2022-10/2022-10-17-octoprint-1.8.5-card.png
featuredimage: /assets/img/blog/2022-10/2022-10-17-octoprint-1.8.5-card.png
poster: /assets/img/blog/2022-10/2022-10-17-octoprint-1.8.5-poster.png
excerpt: "This fifth bugfix release for 1.8.0 fixes two newly reported bugs and gets rid of a runtime warning."

bugfix: 1.8.5
release:
  tag: 1.8.0
  link: /blog/2022/05/17/new-release-1.8.0/
  headsups: true
prior:
  headsups:
  - release: 1.8.3
    link: /blog/2022/09/20/new-release-1.8.3/

---

This fifth bugfix release for 1.8.0 fixes two few recently reported bugs and also gets rid of a runtime warning:

> **✨ Improvements**
> 
> Explicitly declare in-memory storage for rate limiter. Gets rid of warnings under latest `flask-limiter` versions.
> 
> **🐛 Bug fixes**
> 
> - [#4656](https://github.com/OctoPrint/OctoPrint/issues/4656) - Fix cookie suffix creation on the frontend to properly work with multi-level subpaths. The wrong suffix caused OctoPrint's core UI not to be able to extract the CSRF token when running behind a reverse proxy with a multi-level prefix path, rendering the UI non functional.
> - [#4659](https://github.com/OctoPrint/OctoPrint/issues/4659) - Fix the sanity check on the backup download API so that backups created through the CLI or third party plugins named arbitrarily will be downloadable by admins.

You can also take a look at the [changelog on GitHub](https://github.com/OctoPrint/OctoPrint/releases/tag/1.8.5) which is on the shorter side again.

Like every single release (and release candidate) of OctoPrint ever since early 2016 this release was made possible only
through your continued **[support of my work](/support-octoprint/)** 💕
