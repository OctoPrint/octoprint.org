---
layout: post
author: foosel
title: "OctoPi Release Candidate 0.15.1rc1 needs testers!"
date: 2018-05-10 10:30:00 +0200
excerpt: Guy Sheffer just published a release candidate for a hotfix release of OctoPi 0.15 and is looking for feedback!
card: /assets/img/blog/2018-05/2018-05-10-octopi-0.15.1rc1-card.png
featuredimage: /assets/img/blog/2018-05/2018-05-10-octopi-0.15.1rc1-card.png
poster: /assets/img/blog/2018-05/2018-05-10-octopi-0.15.1rc1-poster.png
---

[Guy Sheffer](https://github.com/guysoft) just published a
[release candidate](https://github.com/guysoft/OctoPi/issues/530) for a hotfix release of the OctoPi image, version 0.15.1.

Compared to the just recently released 0.15.0 image this RC only contains a fix for an incompatibility between the 
bundled OctoPrint 1.3.8 and the bundled `pip` 10:

>  This is a hotfix pinning pip to version 9 because version 10 does not play nice with OctoPrint plugins.

If you've got a spare SD card to help test this, your help would be greatly appreciated. Please 
[report any findings back here](https://github.com/guysoft/OctoPi/issues/530) - even a "works fine for me" is valuable 
information!

If you already updated to 0.15.0 and are wondering how this incompatibility manifests and how to work around it, 
[take a look at this FAQ entry](https://discourse.octoprint.org/t/1746). The issue will be fixed in OctoPrint 1.3.9 as well.

You can find the download links in the [ticket](https://github.com/guysoft/OctoPi/issues/530).

---

*Confused about the difference between OctoPi and OctoPrint? [Read this](https://discourse.octoprint.org/t/what-is-the-difference-between-octoprint-and-octopi-are-they-the-same-thing/185)!* 