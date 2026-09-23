---

title: 'New release candidate: 1.9.0rc2'
author: foosel
date: 2023-03-07 13:45:00 +0100
release: 1.9.0rc2
channel: Maintenance RCs
feedback: 4750

tags:
- Release
summary: The second release candidate for the upcoming 1.9.0 release, fixing one
  issue immediately found in the first one!
slug: new-release-candidate-1.9.0rc2
---

Hot on the heels of the first release candidate earlier today comes the second one, after I discovered an issue with installing plugins under the first one:

> **🐛 Bug fixes**
>
> - [#4749](https://github.com/OctoPrint/OctoPrint/issues/4749): Bring back a bundled `octoprint_setuptools` package, since installing the one provided by OctoPrint-Setuptools apparently won't work on updates from OctoPrint versions where OctoPrint provides that package, breaking plugin installs in the process.

For heads-ups, highlights and fancy pictures, please see [the earlier post about 1.9.0rc1](/blog/2023/03/07/new-release-candidate-1.9.0rc1/).