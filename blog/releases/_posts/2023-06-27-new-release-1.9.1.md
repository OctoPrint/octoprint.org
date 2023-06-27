---
layout: post-bugfix
title: 'New release: 1.9.1'
author: foosel
date: 2023-06-27 10:00:00 +0200
card: /assets/img/blog/2023-06/2023-06-27-octoprint-1.9.1-card.png
featuredimage: /assets/img/blog/2023-06/2023-06-27-octoprint-1.9.1-card.png
poster: /assets/img/blog/2023-06/2023-06-27-octoprint-1.9.1-poster.png

excerpt: "A first bugfix release for 1.9.x, fixing a few issues reported since the release of 1.9.0."

bugfix: 1.9.1
release:
  tag: 1.9.0
  link: /blog/2023/05/23/new-release-1.9.0/
  headsups: true

contributors:
- cp2004
- JoveToo
---

This first bugfix release for 1.9.0 fixes a few bugs reported since the release of 1.9.0, and also improves one of the new features introduced in 1.9.0:

> **✨ Improvements**
> 
> - [#4821](https://github.com/OctoPrint/OctoPrint/issues/4821): Defer sending of `M20` until after the capability report has been received by default, instead of defaulting to sending it right away. Most firmwares out there now *should* be sending capability reports, and for those that don't, the setting can still be manually set to `false`.
> 
> **🐛 Bug fixes**
> 
> - [#4818](https://github.com/OctoPrint/OctoPrint/issues/4818): Fix broken/erroring plugin sorting if a list of `SortablePlugin`s and non sortable plugins gets processed in the same sorting context.
> - [#4829](https://github.com/OctoPrint/OctoPrint/issues/4829): Fix URL used by the GCode Viewer's worker to fetch info about the file to be rendered. It was not supporting custom prefixes on the URL yet (e.g. `http://example.com/octoprint`), now it does.
> - [#4834](https://github.com/OctoPrint/OctoPrint/pull/4834): Fix a bug in the GCode Viewer that resulted in a print not being rendered when loaded while the tab of the viewer was not focused.
> - [#4824](https://github.com/OctoPrint/OctoPrint/pull/4824): Fix potential webcam unload/load switching when scrolling on the control tab. Could not always be triggered, but apparently was seen under some circumstances.
> - Fix the reload button of the GCode Viewer
> - Fix a bug in the GCode Viewer causing layers that were empty in one file causing that layer to not be rendered in all consecutively loaded files, until a page reload.

You can also take a look at the [short changelog on GitHub](https://github.com/OctoPrint/OctoPrint/releases/tag/1.9.1).

Like every single release (and release candidate) of OctoPrint ever since early 2016 this release was made possible only
through your continued **[support of my work](/support-octoprint/)** 💕
