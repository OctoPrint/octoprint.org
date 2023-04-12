---

layout: post-rc
title: 'New release candidate: 1.9.0rc4'
author: foosel
date: 2023-04-12 15:25:00 +0100
card: /assets/img/blog/2023-04/2023-04-12-octoprint-1.9.0rc4-card.png
featuredimage: /assets/img/blog/2023-04/2023-04-12-octoprint-1.9.0rc4-card.png
poster: /assets/img/blog/2023-04/2023-04-12-octoprint-1.9.0rc4-poster.png
excerpt: The fourth release candidate for the upcoming 1.9.0 release, fixing some issues reported on the last ones and improving on some newly added functionality.

release: 1.9.0rc4
channel: Maintenance RCs
feedback: 4790

contributors:
- cp2004
- JoveToo

---

This fourth release candidate of 1.9.0 fixes two regressions and a few bugs in new functionality observed and reported on the last ones, and improves on some newly added functionality:

> **✨ Improvements**
> 
> - [#4778](https://github.com/OctoPrint/OctoPrint/issues/4778): Clarify the role of the "default webcam", now called "fallback webcam", since it is only responsible of providing the compatibility layer of the webcam settings for legacy clients.
> 
> **🐛 Bug fixes**
> 
> - [#4772](https://github.com/OctoPrint/OctoPrint/issues/4772) (regression): Fixed sync of GCODE Viewer with progress when behind haproxy
> - [#4776](https://github.com/OctoPrint/OctoPrint/issues/4776): Fix a typo in the new webcam visibility API
> - [#4782](https://github.com/OctoPrint/OctoPrint/issues/4782): Fix a typo in the Classic Webcam snapshot hook, leading to the SSL validation setting not being fetched correctly
> - [#4783](https://github.com/OctoPrint/OctoPrint/issues/4783): Fix saving the changes to the default snapshot webcam.
> - [#4789](https://github.com/OctoPrint/OctoPrint/issues/4789): Fix synchronization of the timelapse configuration on snapshot webcam change.
> - GCODE Viewer: Fixed a double load of the model under certain circumstances. (regression)

For heads-ups, highlights and fancy pictures, please see [the earlier post about 1.9.0rc1](/blog/2023/03/07/new-release-candidate-1.9.0rc1/).

