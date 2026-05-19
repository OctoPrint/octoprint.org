---
layout: post-rc
title: "New release candidate: 2.0.0rc2"
author: foosel
date: 2026-05-19 16:15:00 +0200
card: /assets/img/blog/2026-05/2026-05-19-octoprint-2.0.0rc2-card.png
featuredimage: /assets/img/blog/2026-05/2026-05-19-octoprint-2.0.0rc2-card.png
poster: /assets/img/blog/2026-05/2026-05-19-octoprint-2.0.0rc2-poster.png

excerpt: The second release candidate for the upcoming 2.0.0 release with fixes of observed regressions and newly discovered long standing bugs as well as some improvements.

release: 2.0.0rc2
channel: Release Candidates
feedback: 5373

closer_look:
  - Proper behaviour when using the included web interface as well as any third party clients at your disposal.
  - Printing via serial connection.
  - Managing files on your printers storage via a serial connection.
  - Blocklisted serial ports and/or baud rates are properly migrated to the serial connector (one per line, not comma-separated).
  - If your printer's disconnected state happens to be "after error", please report back on which connector you used and what the reported error is.
  - "If you have a Klipper/Moonraker based printer available: can you use it through OctoPrint when you install the [Moonraker Connector](https://github.com/OctoPrint/OctoPrint-MoonrakerConnector) (work in progress)?"
  - "If you have a Bambu based printer available: can you use it through OctoPrint when you install the [Bambu Connector](https://github.com/OctoPrint/OctoPrint-BambuConnector) (work in progress)?"

contributors:
  - jacopotediosi
  - jneilliii
---

This second release candidate for the upcoming 2.0.0 release fixes several regressions that were reported with the first one, as well as some newly found bugs. It also improves on newly added functionality and introduces two new version check options for the Software Update Plugin:

> **✨ Improvements**
>
> _Core_
>
> - [#5385](https://github.com/OctoPrint/OctoPrint/pull/5385): Add migration for terminal filters to new filter prefixes. Also improve migration guide accordingly.
>
> _Core UI_
>
> - Add option to the sidebar file manager's menu to (recursively) refresh the current storage's & path's thumbnails (if supported).
>
> _Healthcheck Plugin_
>
> - Add health check hint for unusable `gcode_thumbnail_tool` with link to [the FAQ entry](https://community.octoprint.org/t/octoprint-tells-me-that-the-gcode-thumbnail-tool-is-unavailable/66368).
>
> _Software Update Plugin_
>
> - Add support for `forgejo_release` and `forgejo_commit` version check types, which enable version checks against [Forgejo](https://forgejo.org/) code forges such as [Codeberg](https://codeberg.org/). For Codeberg specifically, there's also `codeberg_release` and `codeberg_commit` which internally gets remapped to `forgejo_*` with the correct `forge` parameter.
>
> _Docs_
>
> - Add more examples to the migration guide and deprecation list.
> - Add docs for `octoprint.util.version`.
>
> **🐛 Bug fixes**
>
> _Core_
>
> - [#5377](https://github.com/OctoPrint/OctoPrint/issues/5377) (regression): Fix evaluation of print parameter on upload API.
> - [#5379](https://github.com/OctoPrint/OctoPrint/pull/5379) (regression): Fix deselection of current print job not working.
> - [#5380](https://github.com/OctoPrint/OctoPrint/pull/5380) (regression): Allow `None` filament weight in `/api/job` response.
> - [#5390](https://github.com/OctoPrint/OctoPrint/issues/5390) (regression): Gracefully handle unavailability of `gcode_thumbnail_tool` due to missing OS dependencies.
> - [#5393](https://github.com/OctoPrint/OctoPrint/issues/5393) (regression): Fix file/folder move from root directory.
> - (regression) Fix file commands on storage root.
> - Fix repo file links still pointing to `master` vs `main`.
>
> _Core UI_
>
> - [#5375](https://github.com/OctoPrint/OctoPrint/issues/5375) (regression): Fix broken availability logic on connection button.
> - [#5384](https://github.com/OctoPrint/OctoPrint/pull/5384) (regression): Fix "Update User" button in access settings.
> - [#5386](https://github.com/OctoPrint/OctoPrint/pull/5386) (regression): Fix some template permission checks broken during removal of deprecated code.
>
> _Plugin Manager_
>
> - [#5382](https://github.com/OctoPrint/OctoPrint/issues/5382): Fix support for pip VCS URL schemes as archive URL.
>
> _Serial Connector_
>
> - Fix error handling in serial detection. A serial error raised during detection should not cause the whole detection workflow to stop, but rather just switch to the next test option.
>
> _Software Update Plugin_
>
> - [#5400](https://github.com/OctoPrint/OctoPrint/issues/5400): Fix default tracked branch for OctoPrint commit tracking, was still pointing to `master` instead of `main`.
> - Fix default user for OctoPrint release check, was still pointing to `foosel` instead of `OctoPrint` (though was also redirected).
>
> _Tracking_
>
> - Fix tracking of `printer_connected` event if the current connector doesn't send a `FirmwareData` event (prevented tracking of BambuConnector use).
>
> _Docs_
>
> - [#5394](https://github.com/OctoPrint/OctoPrint/pull/5394): Fix an example still referring to a removed function.

For heads-ups, highlights and fancy pictures, please see [the earlier post about 2.0.0rc1](/blog/2026/04/27/new-release-candidate-2.0.0rc1/).
