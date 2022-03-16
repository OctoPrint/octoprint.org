---

layout: post-rc
title: 'New release candidate: 1.8.0rc2'
author: foosel
date: 2022-03-16 11:30:00 +0100
card: /assets/img/blog/2022-03/2022-03-16-octoprint-1.8.0rc2-card.png
featuredimage: /assets/img/blog/2022-03/2022-03-16-octoprint-1.8.0rc2-card.png
poster: /assets/img/blog/2022-03/2022-03-16-octoprint-1.8.0rc2-poster.png
excerpt: The second release candidate for the upcoming 1.8.0 release, fixing observed regressions and adding some improvements of added functionality.

release: 1.8.0rc2
channel: Maintenance RCs
feedback: 4457

---

This second RC of 1.8.0 fixes regressions observed with the first one and adds improvements
of added functionality:

> **Improvements**
> 
>   * [#4460](https://github.com/OctoPrint/OctoPrint/issues/4460) - Expose new config flag `serial.ignoreEmptyPorts` to ignore empty serial ports and maintain pre 1.8.0 default behaviour regarding the handling of the situation on the UI as well (see Serial Connection > General > Connection > Advanced Options > Ignore empty ports).
>   * Application Keys: Add docs for new auth dialog work flow.
> 
> **Bug fixes**
> 
>   * [#4453](https://github.com/OctoPrint/OctoPrint/issues/4453) (regression) - Improve resilience against broken plugin template configs.
>   * [#4454](https://github.com/OctoPrint/OctoPrint/issues/4454) (regression) - Fix a fatal error in the refactored settings hierarchy upon encountering an `int` key.
>   * [#4456](https://github.com/OctoPrint/OctoPrint/issues/4456) (regression) - Fix a serial loop crash when encountering a custom temperature entry (or garbage that looks like one) that matches > the too broadly defined reserved identifier regex.
>   * [#4458](https://github.com/OctoPrint/OctoPrint/issues/4458) (regression) - Fix retrieval of full `dict` structures from the settings for which an empty default exists.
>   * [#4459](https://github.com/OctoPrint/OctoPrint/issues/4459) (regression) - GCode Viewer: Fix transmission of parsed layer data structure from the worker to the main thread.
>   * Add some missing less 4 compatibility fixes
>   * Fix version requirement of PiSupport plugin