---

layout: post-rc
title: 'New release candidate: 1.9.0rc5'
author: foosel
date: 2023-04-13 16:00:00 +0100
card: /assets/img/blog/2023-04/2023-04-13-octoprint-1.9.0rc5-card.png
featuredimage: /assets/img/blog/2023-04/2023-04-13-octoprint-1.9.0rc5-card.png
poster: /assets/img/blog/2023-04/2023-04-13-octoprint-1.9.0rc5-poster.png
excerpt: The fifth release candidate for the upcoming 1.9.0 release, fixing a regression reported on the last one.

release: 1.9.0rc5
channel: Maintenance RCs
feedback: 4792

---

This fifth release candidate of 1.9.0 fixes one regression reported on the last one, tweaks some wording and has some changes on the test suite:

> **✨ Improvements**
> 
> - [#4778](https://github.com/OctoPrint/OctoPrint/issues/4778): Minor phrasing tweak.
> 
> **🐛 Bug fixes**
> 
> - [#4791](https://github.com/OctoPrint/OctoPrint/issues/4791) (regression): Fix webcam initialisation on control tab if only one webcam plugin is available.
> - Migrate a unit test from `unittest` to `pytest` in the hopes that this fixes some flakiness issues observed in CI.

For heads-ups, highlights and fancy pictures, please see [the earlier post about 1.9.0rc1](/blog/2023/03/07/new-release-candidate-1.9.0rc1/).
