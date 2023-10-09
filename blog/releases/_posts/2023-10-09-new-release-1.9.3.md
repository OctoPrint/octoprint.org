---
layout: post-bugfix
title: 'New release: 1.9.3'
author: foosel
date: 2023-10-09 16:45:00 +0200
card: /assets/img/blog/2023-10/2023-10-09-octoprint-1.9.3-card.png
featuredimage: /assets/img/blog/2023-10/2023-10-09-octoprint-1.9.3-card.png
poster: /assets/img/blog/2023-10/2023-10-09-octoprint-1.9.3-poster.png

excerpt: "The third bugfix & security release for 1.9.x, fixing one security vulnerability, one bug and adding one workaround for an issue with a third party dependency."

bugfix: 1.9.3
release:
  tag: 1.9.0
  link: /blog/2023/05/23/new-release-1.9.0/
  headsups: true

contributors:
- srLinux

first_time_contributors:
- srLinux
---

This third bugfix release & security for 1.9.x includes a fix for one security vulnerability, one bug and one workaround for an issue with a third party dependency:

> **🔒 Security fixes**
> 
> - Severity Medium (6.4): It was possible for a malicious admin to configure a specially crafted [GCODE script](https://docs.octoprint.org/en/master/features/> gcode_scripts.html) through the Settings that would allow code execution during rendering of that script. An attacker could have used this to extract data managed by > OctoPrint, or manipulate data managed by OctoPrint, as well as execute arbitrary commands with the rights of the OctoPrint process on the server system. 
>   
>   Please note that GCODE files uploaded to be printed were not affected! This vulnerability exclusively affected GCODE Scripts to be executed on connection to the > printer, print pause, resume etc, as described [in the documentation](https://docs.octoprint.org/en/master/features/gcode_scripts.html), to be found under Settings > > GCODE Scripts and configurable only by users with the `ADMIN` permission.
> 
>   <!-- See also the [GitHub Security Advisory]() and [CVE-2023-41047](https://nvd.nist.gov/vuln/detail/CVE-2023-41047). -->
> 
> **🐛 Bug fixes**
> 
> - [#4849](https://github.com/OctoPrint/OctoPrint/issues/4849) & [PR#4860](https://github.com/OctoPrint/OctoPrint/pull/4860): Fix for not being able to extrude/retract from the control panel in the UI after editing the extrusion speed in the printer profile.
> - [#4893](https://github.com/OctoPrint/OctoPrint/issues/4893): Pin pydantic dependency to 1.10.12. This works around an issue existing in some environments with pydantic > version 1.10.13, which was released on September 26 2023. Said issue causes OctoPrint to no longer be able to start. See also [pydantic/pydantic#7689](https://github.com/pydantic/pydantic/issues/7689).

You can also take a look at the [changelog on GitHub](https://github.com/OctoPrint/OctoPrint/releases/tag/1.9.3).

Like every single release (and release candidate) of OctoPrint ever since early 2016 this release was made possible only
through continued financial support by people like you! 💕 

**[Click here](/support-octoprint/) if you enjoy OctoPrint and want to help with its funding!**

