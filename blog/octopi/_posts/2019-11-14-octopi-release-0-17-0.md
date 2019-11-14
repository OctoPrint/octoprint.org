---
layout: post
author: foosel
title: "New OctoPi Release: 0.17.0"
date: 2019-11-14 10:15:00 +0100
excerpt: OctoPi 0.17.0 comes with the latest OctoPrint 1.3.12 and Pi 4B support, among other things.
card: /assets/img/blog/2019-11/2019-11-14-octopi-0.17.0-card.png
featuredimage: /assets/img/blog/2019-11/2019-11-14-octopi-0.17.0-card.png
poster: /assets/img/blog/2019-11/2019-11-14-octopi-0.17.0-poster.png
---

[Guy Sheffer](https://github.com/guysoft) has released
OctoPi 0.17.0 - big thanks to him and also to everyone who helped test the
release candidates and the nightly builds that went into this and reported back!

Apart from adding support for the Pi 3A+ and of course shipping with the current stable OctoPrint version
1.3.12, 0.17.0 also contains the following changes:

> Changes in the image
> 
>   * Raspberrypi 4B support
>   * linux 4.19.75 from new base image 2019-09-26-raspbian-buster-lite
>   * OctoPrint 1.3.12
>   * Fix Chinese Endoscope 8mm ( [#602](https://github.com/guysoft/OctoPi/issues/602) )
>   * Bug fixes
> 
> Build notes
> 
>   * Uses CustomPiOS in devel (which I release once I understand how to get the multi-arch tagged correctly)
>   * Our nightly/release builds have moved to the new build server, after 6+ years of operating.

The full release notes can be found at
[github](https://github.com/guysoft/OctoPi/releases/tag/0.16.0).

You can download OctoPi 0.17.0 from the [usual place](http://octoprint.org/download/). If you are asking yourself how to update from
an earlier version of OctoPi, please read on.

**"How do I update?"**

There is currently no way to update from earlier *OctoPi* versions to a new version of that image. It's not strictly necessary though -
a new image basically means that if you have to setup a new instance you'll start at a newer version of everything
bundled with the image. Anything included on the image however can also be kept up to date without having to
reflash. OctoPrint will have prompted you to update itself and will continue to do so, and most of the image itself
[can be kept up to date like every other Raspbian image](https://www.raspberrypi.org/documentation/raspbian/updating.md).

So no pressing need to reflash!

If you want to however, [create a backup](https://community.octoprint.org/t/how-do-i-backup-my-octoprint-settings-on-octopi/1489).

---

*Confused about the difference between OctoPi and OctoPrint? [Read this](https://community.octoprint.org/t/what-is-the-difference-between-octoprint-and-octopi-are-they-the-same-thing/185)!*
