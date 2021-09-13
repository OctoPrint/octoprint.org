---

layout: post-rc
title: 'New release candidate: 1.7.0rc3'
author: foosel
date: 2021-09-13 13:35:00 +0200
card: /assets/img/blog/2021-09/2021-09-13-octoprint-1.7.0rc3-card.png
featuredimage: /assets/img/blog/2021-09/2021-09-13-octoprint-1.7.0rc3-card.png
poster: /assets/img/blog/2021-09/2021-09-13-octoprint-1.7.0rc3-poster.png
excerpt: The third release candidate for the upcoming 1.7.0 release, fixing three observed regressions and two bugs in new functionality.

release: 1.7.0rc3
channel: Maintenance RCs
feedback: 4232

contributors:
- cp2004

---

Back from a staycation, and right into prepping releases. This third RC of 1.7.0 fixes three 
regressions observed with the first ones and also fixes two bugs in new functionality:

> **Bug fixes**
>
>   * [#4207](https://github.com/OctoPrint/OctoPrint/issues/4207) - Software Update: Fix "Update log" content being visible on the wrong settings tab
>   * [#4210](https://github.com/OctoPrint/OctoPrint/issues/4210) (regression) - Fix label placement in progress dialog, as e.g. used by the timelapse bulk delete feature.
>   * [#4216](https://github.com/OctoPrint/OctoPrint/issues/4216) (regression) - Announcements: Fix announcements dialog sizing ([PR #4217](https://github.com/OctoPrint/OctoPrint/pull/4217))
>   * [#4226](https://github.com/OctoPrint/OctoPrint/issues/4226) (regression) - Set `autocapitalize="none"` on login fields again. Longer standing regression, fixed in this RC due to minimal impact and side effect potential.
>   * [#4231](https://github.com/OctoPrint/OctoPrint/issues/4231) - Plugin Manager: Make sure plugin list export URL is prefixed with the correct base URL.
mode isn't requested.
