---
title: "New release candidate: 2.0.0rc7"
author: foosel
date: 2026-10-20 12:55:00 +0200
release: 2.0.0rc7
channel: Release Candidates
feedback: 5473

closer_look:
- Proper behaviour when using the included web interface as well as any third 
  party clients at your disposal.
- Printing via serial connection.
- Managing files on your printers storage via a serial connection.
- Blocklisted serial ports and/or baud rates are properly migrated to the serial
  connector (one per line, not comma-separated).
- |
  **If your printer's disconnected state happens to be "after error", please report back on which connector you used and what the reported error is.**
- "If you have a Klipper/Moonraker based printer available: can you use it through
  OctoPrint when you install the [Moonraker Connector](https://github.com/OctoPrint/OctoPrint-MoonrakerConnector)
  (work in progress)?"
- "If you have a Bambu based printer available: can you use it through OctoPrint when
  you install the [Bambu Connector](https://github.com/OctoPrint/OctoPrint-BambuConnector)
  (work in progress)?"

security:
- "[@mahn-don](https://github.com/mahn-don)"
tags:
- release
summary: The seventh release candidate for the upcoming 2.0.0 release with one 
  security fix, two improvements and one fix in new functionality.
slug: new-release-candidate-2.0.0rc7
---

This one was not planned, but then I got a bug and a security report for 2.0.0rc\*, and so here we are: the seventh release candidate for the upcoming 2.0.0 release, fixing said issues and also improving one thing in the new functionality and something in the docs:

> **🔒 Security fixes**
>
> - **Stored XSS via saved connection parameters**, severity Low (2.4): OctoPrint versions 2.0.0rc1 up until version 2.0.0rc6 are susceptible to cross-site scripting via a specially crafted default `port` or `baudrate` setting on the bundled Serial Connector plugin, supplied via the API as new defaults during a `connect` request.
>
>   See also the [GitHub Security Advisory](https://github.com/OctoPrint/OctoPrint/security/advisories/GHSA-p623-mxf7-qxjm). A CVE has been requested but not yet been assigned by GitHub.
>
> **✨ Improvements**
>
> _Serial Connector_
>
> - [#5469](https://github.com/OctoPrint/OctoPrint/issues/5469): Support printer firmware that doesn't send `File selected` after `File opened` messages (e.g. Prusa Buddy Firmware).
>
> _Docs_
>
> - Explain special handling of multipart requests.
>
> **🐛 Bug fixes**
>
> _Core_
>
> - [#5469](https://github.com/OctoPrint/OctoPrint/issues/5469): Properly handle empty print job `progress`. Can happen if for some reason the printer's job cannot be found.

For heads-ups, highlights and fancy pictures, please see [the earlier post about 2.0.0rc1](/blog/2026/04/27/new-release-candidate-2.0.0rc1/).
