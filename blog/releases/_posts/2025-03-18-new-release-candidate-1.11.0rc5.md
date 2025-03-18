---

layout: post-rc
title: 'New release candidate: 1.11.0rc5'
author: foosel
date: 2025-03-18 15:15:00 +0100
card: /assets/img/blog/2025-03/2025-03-18-octoprint-1.11.0rc5-card.png
featuredimage: /assets/img/blog/2025-03/2025-03-18-octoprint-1.11.0rc5-card.png
poster: /assets/img/blog/2025-03/2025-03-18-octoprint-1.11.0rc5-poster.png

excerpt: The fifth release candidate for the upcoming 1.11.0 release containing a fix of an observed regression in the previous ones!

release: 1.11.0rc5
channel: Maintenance RCs
feedback: 5122

closer_look:
- Proper behaviour when using the included web interface as well as any third party clients at your disposal.
- The newly added Custom Control Manager plugin.
- The newly added Health Check plugin.
- The newly added Upload Manager plugin.
- The MFA-TOTP plugin using the new MFA plugin interface.
- Timelapse creation, especially with a configured rendering delay.
- Remember me functionality.

---

This fifth release candidate for the upcoming 1.11.0 release fixes one regression:

> **🐛 Bug fixes**
> 
> *Core*
> 
> - [#5121](https://github.com/OctoPrint/OctoPrint/issues/5121) (regression): Fix spamming of requests against `/api/files/sdcard/<path>` on selecting a file on the printer's SD card. Also added E2E tests for selecting both local and printer-side files.

For heads-ups, highlights and fancy pictures, please see [the earlier post about 1.11.0rc1](/blog/2025/01/28/new-release-candidate-1.11.0rc1/).
