---
layout: post
author: foosel
title: "New OctoPi Release: 0.15.1"
date: 2018-05-29 12:15:00 +0200
excerpt: OctoPi 0.15.1 is a minor release fixing a small issue discovered in the 0.15.0 image.
card: /assets/img/blog/2018-05/2018-05-29-octopi-0.15.1-card.png
featuredimage: /assets/img/blog/2018-05/2018-05-29-octopi-0.15.1-card.png
poster: /assets/img/blog/2018-05/2018-05-29-octopi-0.15.1-poster.png
---

[Guy Sheffer](https://github.com/guysoft) has released
OctoPi 0.15.1 - big thanks to him and also to everyone who helped test the
release candidate and the nightly builds that went into this and reported back!

0.15.1 is a minor release, fixing an [issue discovered in 0.15.0](https://github.com/guysoft/OctoPi/issues/526) 
concerning OctoPrint plugin installation:

> **Changes in the image**
>
>  * Pinned pip version to version 9

The full release notes can be found at
[Github](https://github.com/guysoft/OctoPi/releases/tag/0.15.1).

Please note that OctoPrint 1.3.9 will also contain a fix for this particular issue, so if you are already running OctoPi 0.15.0 with
OctoPrint 1.3.8 and so far haven't encountered any issues, once OctoPrint 1.3.9 is released you should also be in 
the clear. 

You can download OctoPi 0.15.1 from the [usual place](https://octoprint.org/download/). If you are asking yourself how to update from
an earlier version of OctoPi, please read on.

**"How do I update?"**

There is currently no way to update from earlier *OctoPi* versions to a new version of that image. It's not strictly necessary though -
a new image basically means that if you have to setup a new instance you'll start at a newer version of everything
bundled with the image. Anything included on the image however can also be kept up to date without having to
reflash. OctoPrint will prompt you to update itself, and most of the image itself
[can be kept up to date like every other Raspbian image](https://www.raspberrypi.org/documentation/raspbian/updating.md).

So no pressing need to reflash!

If you want to however, make sure you [back everything up](https://discourse.octoprint.org/t/how-do-i-backup-my-octoprint-settings-on-octopi/1489). I might look into a way
to automate this too.

---

*Confused about the difference between OctoPi and OctoPrint? [Read this](https://discourse.octoprint.org/t/what-is-the-difference-between-octoprint-and-octopi-are-they-the-same-thing/185)!* 