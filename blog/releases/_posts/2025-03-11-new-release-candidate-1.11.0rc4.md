---

layout: post-rc
title: 'New release candidate: 1.11.0rc4'
author: foosel
date: 2025-03-11 14:30:00 +0100
card: /assets/img/blog/2025-03/2025-03-11-octoprint-1.11.0rc4-card.png
featuredimage: /assets/img/blog/2025-03/2025-03-11-octoprint-1.11.0rc4-card.png
poster: /assets/img/blog/2025-03/2025-03-11-octoprint-1.11.0rc4-poster.png

excerpt: The fourth release candidate for the upcoming 1.11.0 release containing a fix of an observed regression in the previous ones, a fix of a bug in a new feature and a small fix for an issue in 1.10.x!

release: 1.11.0rc4
channel: Maintenance RCs
feedback: 5120

closer_look:
- Proper behaviour when using the included web interface as well as any third party clients at your disposal.
- The newly added Custom Control Manager plugin.
- The newly added Health Check plugin.
- The newly added Upload Manager plugin.
- The MFA-TOTP plugin using the new MFA plugin interface.
- Timelapse creation, especially with a configured rendering delay.
- Remember me functionality.

contributors:
- Hillshum

first_time_contributors:
- Hillshum

---

This fourth release candidate for the upcoming 1.11.0 release fixes three issues - a regression, a bug in new functionality, and a bug observed in 1.10.0:

> **🐛 Bug fixes**
> 
> *Core*
> 
> - [#5115](https://github.com/OctoPrint/OctoPrint/issues/5115): Auto discovered assets for the `AssetPlugin` mixin would be returned containing `\` under Windows, leading to 404s when attempting to load them in the browser. This auto discovery is a new feature added in 1.11.0 (used by the bundled Health Check plugin) and thus this was not a regression, but rather a bug in newly added functionality.
> - [#5116](https://github.com/OctoPrint/OctoPrint/issues/5116): Fix a bug with handling JS errors in the webasset bundler. Not a regression, but a small enough fix to still include in 1.11.0.
> - [#5117](https://github.com/OctoPrint/OctoPrint/issues/5117) (regression): Fix warnings logged to the browser console due to mistakes made when upgrading to Font Awesome 6.5.1.

For heads-ups, highlights and fancy pictures, please see [the earlier post about 1.11.0rc1](/blog/2025/01/28/new-release-candidate-1.11.0rc1/).
