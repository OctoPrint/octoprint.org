---

layout: post-rc
title: 'New release candidate: 1.10.0rc4'
author: foosel
date: 2024-04-08 16:40:00 +0200
card: /assets/img/blog/2024-04/2024-04-08-octoprint-1.10.0rc4-card.png
featuredimage: /assets/img/blog/2024-04/2024-04-08-octoprint-1.10.0rc4-card.png
poster: /assets/img/blog/2024-04/2024-04-08-octoprint-1.10.0rc4-poster.png
excerpt: The third release candidate for the upcoming 1.10.0 release containing some fixes of observed regressions and improvements of newly added functionality!

release: 1.10.0rc4
channel: Maintenance RCs
feedback: 4988

closer_look:
- Proper behaviour when using the included web interface as well as any third party clients at your disposal.
- User and group management functioning as expected.
- Plugin installation functioning as expected.
- Application key management functioning as expected. Authentication workflow with third party clients at your disposal (e.g. slicers) works as it should.
- Backup creation, download and restore functioning as expected.

---

This fourth release candidate for the upcoming 1.10.0 release fixes some regressions that were reported with the first one, and adds some improvements surrounding newly added functionality:

> **✨ Features & improvements**
> 
> *Core*
> 
> - Improve JS error reporting in Firefox.
> - Fix a potential race condition that might have caused some build errors recently.
> 
> *Achievements Plugin*
> 
> - Added unlocked achievements to the [Anonymous Usage Tracking](https://tracking.octoprint.org). Of course, this can be disabled, and if you have not opted into  > tracking in the first place, nothing will be tracked, as always. Achievement stats are available on [data.octoprint.org](https://data.octoprint.org).
> 
> **🐛 Bug fixes**
> 
> *Core*
> 
> - [#4980](https://github.com/OctoPrint/OctoPrint/issues/4980): Fix missing temperature history for anything but the first extruder. This was actually not a  > regression, but the bug only could be seen now after extending the timeline of the temperature graph to the full available history.
> - [#4983](https://github.com/OctoPrint/OctoPrint/issues/4983) (regression): Fix prefix caching for custom defaults. Manifested in no longer being able to select  > release channels in the Software Update plugin.
> - [#4987](https://github.com/OctoPrint/OctoPrint/issues/4983) (regression): Fix creation of the static version file during installation of sdist under Windows.
> 
> *Achievements Plugin*
> 
> - [#4984](https://github.com/OctoPrint/OctoPrint/issues/4984): Make the "Mass Production" achievement detect modifications of the file.
> - Fix the "Heavy Chonker" achievement.
> - Fix the default groups for the achievement permission.
> 
> *GCODE Viewer*
> 
> - [#4978](https://github.com/OctoPrint/OctoPrint/issues/4978): Fix reloading of the same file. First thought to be a regression, turned out to not be one but was a low hanging fruit.

For heads-ups, highlights and fancy pictures, please see [the earlier post about 1.10.0rc1](/blog/2024/01/31/new-release-candidate-1.10.0rc1/).
