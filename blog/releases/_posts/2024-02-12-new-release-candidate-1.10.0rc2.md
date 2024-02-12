---

layout: post-rc
title: 'New release candidate: 1.10.0rc2'
author: foosel
date: 2024-02-12 13:30:00 +0100
card: /assets/img/blog/2024-02/2024-02-12-octoprint-1.10.0rc2-card.png
featuredimage: /assets/img/blog/2024-02/2024-02-12-octoprint-1.10.0rc2-card.png
poster: /assets/img/blog/2024-02/2024-02-12-octoprint-1.10.0rc2-poster.png
excerpt: The second release candidate for the upcoming 1.10.0 release containing some fixes of observed regressions and improvements of newly added functionality!

release: 1.10.0rc2
channel: Maintenance RCs
feedback: 4948

closer_look:
- Proper behaviour when using the included web interface as well as any third party clients at your disposal.
- User and group management functioning as expected.
- Plugin installation functioning as expected.
- Application key management functioning as expected. Authentication workflow with third party clients at your disposal (e.g. slicers) works as it should.
- Backup creation, download and restore functioning as expected.

---

This second release candidate for the upcoming 1.10.0 release fixes five regressions that were reported with the first one, and also adds some improvements for newly added functionality:

> **✨ Features & improvements**
> 
> *Backup Plugin*
> 
> - Require credential recheck for download & restore.
> 
> *Testing & CI*
> 
> - [#4908](https://github.com/OctoPrint/OctoPrint/issues/4908): Also automatically publish source tarball on GitHub releases.
> 
> **🐛 Bug fixes**
> 
> *Core*
> 
> - [#4939](https://github.com/OctoPrint/OctoPrint/issues/4939) (regression): Fix drag'n'drop initialization.
> - [#4940](https://github.com/OctoPrint/OctoPrint/issues/4940) (regression): Make `octoprint._version` backward compatible enough again to work around use on OctoPi images and third party plugins out there.
> - [#4941](https://github.com/OctoPrint/OctoPrint/issues/4941) (regression): Fix some syntax under Python 3.7 & 3.8.
> - [#4942](https://github.com/OctoPrint/OctoPrint/issues/4942) (regression): Fix handling of setting an empty dict on the configuration. Also added a unit test for this.
> - [#4943](https://github.com/OctoPrint/OctoPrint/issues/4943) (regression): Fix fetching of file details for the existence check, preventing the "file already exists" dialog from making the correct checks.
> - Removed a left-over from the Access Control settings panel.

For heads-ups, highlights and fancy pictures, please see [the earlier post about 1.10.0rc1](/blog/2024/01/31/new-release-candidate-1.10.0rc1/).
