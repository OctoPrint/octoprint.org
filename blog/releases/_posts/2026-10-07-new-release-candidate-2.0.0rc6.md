---
layout: post-rc
title: "New release candidate: 2.0.0rc6"
author: foosel
date: 2026-10-07 13:00:00 +0200
card: /assets/img/blog/2026-10/2026-10-07-octoprint-2.0.0rc6-card.png
featuredimage: /assets/img/blog/2026-10/2026-10-07-octoprint-2.0.0rc6-card.png
poster: /assets/img/blog/2026-10/2026-10-07-octoprint-2.0.0rc6-poster.png

excerpt: The sixth release candidate for the upcoming 2.0.0 release with some more fixes of regressions and some long standing bugs, and one backwards compatiblity fix for 3rd party plugins.

release: 2.0.0rc6
channel: Release Candidates
feedback: 5467

contributors:
  - jacopotediosi

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

Slightly delayed thanks to the first cold of the season 🤧, here's the sixth release candidate for the upcoming 2.0.0 release with some more fixes of regressions and some long standing newly discovered bugs, as well as one backwards compatiblity fix for 3rd party plugins:

> **✨ Improvements**
>
> _Gcode Viewer Plugin_
>
> - Support old `loadFile` signature on view model as apparently used by third party plugins out there (e.g. UICustomizer)
>
> **🐛 Bug fixes**
>
> _Core_
>
> - [PR#5450](https://github.com/OctoPrint/OctoPrint/pull/5450): Reject `NaN` & `Inf` when saving file metadata
> - [#5454](https://github.com/OctoPrint/OctoPrint/issues/5454) (regression): Fix wrong check inside local storage that under very limited circumstances could lead to a limited path traversal vulnerability on the download API endpoint.
> - [#5466](https://github.com/OctoPrint/OctoPrint/issues/5466) (regression): Fix metadata refresh on file upload. A cache was not being emptied correctly.
> - (regression) Handle broken analysis, statistics & history metadata on files instead of just ignoring the whole file for the file list. Try to transparently sanitize data were needed, remove completely invalid data as needed.
> - (regression) Fix a race condition causing the `PrintFailed` event to be sent with the wrong payload.
> - (regression) Properly handle progress reporting for an unset job.
> - Replace use of deprecated `inspect.getargspec` (backported from [PR#5464](https://github.com/OctoPrint/OctoPrint/pull/5464)).
> - Fix logging of invalid wizard versions (backported from [PR#5464](https://github.com/OctoPrint/OctoPrint/pull/5464)).
>
> _Core UI_
>
> - Improve resilience against various runtime data issues.
>
> _Health Check Plugin_
>
> - (regression) Make storage thresholds available again on the settings API.
>
> _Serial Connector_
>
> - (regression) Gracefully handle unknown file reported by printer as selected for printing.
> - Fix wrong `seek` signature for streaming opened file handles (backported from [PR#5464](https://github.com/OctoPrint/OctoPrint/pull/5464)).
>
> _Docs_
>
> - [PR#5449](https://github.com/OctoPrint/OctoPrint/pull/5449): Fix `FileDestinations.SDCARD` notes in migration guide
> - Fix the reason for various warnings

For heads-ups, highlights and fancy pictures, please see [the earlier post about 2.0.0rc1](/blog/2026/04/27/new-release-candidate-2.0.0rc1/).
