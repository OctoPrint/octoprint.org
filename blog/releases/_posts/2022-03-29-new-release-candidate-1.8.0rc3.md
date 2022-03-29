---

layout: post-rc
title: 'New release candidate: 1.8.0rc3'
author: foosel
date: 2022-03-29 13:30:00 +0200
card: /assets/img/blog/2022-03/2022-03-29-octoprint-1.8.0rc3-card.png
featuredimage: /assets/img/blog/2022-03/2022-03-29-octoprint-1.8.0rc3-card.png
poster: /assets/img/blog/2022-03/2022-03-29-octoprint-1.8.0rc3-poster.png
excerpt: The third release candidate for the upcoming 1.8.0 release, fixing observed regressions and adding a workaround for recent third party dependency issues.

release: 1.8.0rc3
channel: Maintenance RCs
feedback: 4475

---

This third RC of 1.8.0 fixes regressions observed with the two first ones and adds a 
workaround for a recently raised third party issue:

> **Improvements**
> 
>   * Update version requirement for PiSupport plugin to latest release
> 
> **Bug fixes**
> 
>   * [#4463](https://github.com/OctoPrint/OctoPrint/issues/4463) (regression) - GCode Viewer: Fix viewer not showing the last layer.
>   * Fixed a potential race condition that could cause an Internal Server Error on initial page load (self-fixing on the next reload though). Likely a regression caused by the changes to the > webassets cache handling.
>   * Work around a compatibility issue between latest werkzeug and flask-login releases by pinning werkzeug to 2.0.x.
