---
title: "New release candidate: 2.0.0rc4"
author: foosel
date: 2026-07-14 09:56:00 +0200
summary: The fourth release candidate for the upcoming 2.0.0 release with fixes of a bug in new functionality and a newly discovered long standing bug.
tags:
- release

card: /assets/img/blog/2026-07/2026-07-14-octoprint-2.0.0rc4-card.png
featuredimage: /assets/img/blog/2026-07/2026-07-14-octoprint-2.0.0rc4-card.png
poster: /assets/img/blog/2026-07/2026-07-14-octoprint-2.0.0rc4-poster.png

release: 2.0.0rc4
channel: Release Candidates
feedback: 5434

closer_look:
  - Proper behaviour when using the included web interface as well as any third party clients at your disposal.
  - Printing via serial connection.
  - Managing files on your printers storage via a serial connection.
  - Blocklisted serial ports and/or baud rates are properly migrated to the serial connector (one per line, not comma-separated).
  - |
    **If your printer's disconnected state happens to be "after error", please report back on which connector you used and what the reported error is.**
  - "If you have a Klipper/Moonraker based printer available: can you use it through OctoPrint when you install the [Moonraker Connector](https://github.com/OctoPrint/OctoPrint-MoonrakerConnector) (work in progress)?"
  - "If you have a Bambu based printer available: can you use it through OctoPrint when you install the [Bambu Connector](https://github.com/OctoPrint/OctoPrint-BambuConnector) (work in progress)?"
---

This fourth release candidate for the upcoming 2.0.0 release fixes one bug in new functionality and one long standing newly discovered bug:

> **🐛 Bug fixes**
>
> _Core_
>
> - [#5425](https://github.com/OctoPrint/OctoPrint/issues/5425): Add reauth requirement for setting `defaultReauthenticationTimeout` via UI/settings API.
> - [#5429](https://github.com/OctoPrint/OctoPrint/issues/5429): Limit settings paths available with `SETTINGS_READ` permission to frontend relevant settings.

For heads-ups, highlights and fancy pictures, please see [the earlier post about 2.0.0rc1](/blog/2026/04/27/new-release-candidate-2.0.0rc1/).
