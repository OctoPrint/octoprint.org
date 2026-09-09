---
layout: post-rc
title: "New release candidate: 2.0.0rc5"
date: 2026-08-24 13:15:00 +0200
modified: 2026-09-09 13:15:00 +0200
summary: The fifth release candidate for the upcoming 2.0.0 release with some more fixes of regressions and some long standing bugs.
tags:
- release

card: card.png
featuredimage: card.png
poster: poster.png

author: foosel

release: 2.0.0rc5
channel: Release Candidates
feedback: 5448

contributors:
  - jacopotediosi
  - sanjay900

first_time_contributors:
  - sanjay900

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

The fifth release candidate for the upcoming 2.0.0 release with some more fixes of regressions and some long standing newly discovered bugs:

> **🐛 Bug fixes**
>
> _Core_
>
> - Fix standard options on `octoprint config` not working as they should. E.g. the `--basedir` option was ignored unless it came before the `config` subcommand.
> - Fix the config schema to include default chamber values of 0. That also fixed the issue that the frontend would always send all temperature profiles on every settings save, even if there were no changes to them, due to an internal conversion due to the missing schema entry.
>
> _Core UI_
>
> - [#5438](https://github.com/OctoPrint/OctoPrint/issues/5438): Get rid of the deprecated `babel-polyfill` dependency that was causing performance issues on the UI.
>
> _Discovery Plugin_
>
> - [PR#5445](https://github.com/OctoPrint/OctoPrint/pull/5445) (regression): Re-expose public discovery data on the settings API (for logged-in users), as with Home Assistant at least one third party client depends on the UUID being available there.
>
> _Gcode Viewer Plugin_
>
> - [PR#5446](https://github.com/OctoPrint/OctoPrint/pull/5446): Stop decompressing the model twice. This is a performance improvement.
>
> _Serial Connector Plugin_
>
> - [PR#5447](https://github.com/OctoPrint/OctoPrint/pull/5447) (regression): Don't send `Error` events twice

For heads-ups, highlights and fancy pictures, please see [the earlier post about 2.0.0rc1](/blog/2026/04/27/new-release-candidate-2.0.0rc1/).
