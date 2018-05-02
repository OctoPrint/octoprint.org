---
layout: post
author: foosel
title: "New OctoPi Release: 0.15.0"
date: 2018-05-02 11:15:00 +0200
excerpt: OctoPi 0.15 comes with the latest OctoPrint 1.3.8 and Pi 3+ support, among other things.
card: /assets/img/blog/2018-05/2018-05-02-octopi-0.15-card.png
featuredimage: /assets/img/blog/2018-05/2018-05-02-octopi-0.15-card.png
poster: /assets/img/blog/2018-05/2018-05-02-octopi-0.15-poster.png
---

[Guy Sheffer](https://github.com/guysoft) has released
OctoPi 0.15 - big thanks to him and also to everyone who helped test the
release candidate and the nightly builds that went into this and reported back!

Apart from adding support for the Pi 3+ and of course shipping with the current stable OctoPrint version
1.3.8, 0.15 also contains the following changes:

>  * Raspberrypi 3B+ support
>  * `octopi-wpa-supplicant.txt` network settings now default
>  * linux kernel 4.14 from new base image 2018-04-18-octopi-stretch-lite
>  * debian stretch from new base image
>  * Bug fixes
>
> Developer Notes:
>
> We have moved to build with [CustomPiOS](https://github.com/guysoft/CustomPiOS), which means that 
> OctoPi has joined a larger build system which supports lots of modules and cool ways to configure and maintain 
> debian-based IOT distros.

The most important change for anyone setting up a new OctoPi image now here is **that the file used to configure your
wifi has changed**. You no longer have to edit ``octopi-network.txt`` (which is now non functional) but 
**edit ``octopi-wpa-supplicant.txt``**. This change had to be introduced due to limitations of the old method with regards
to certain network setups and also due to more and more incompatibility to the direction the Raspberry Pi Foundation is taking
the underlying Raspbian base image.

The full release notes can be found at
[github](https://github.com/guysoft/OctoPi/releases/tag/0.15.0).

You can download OctoPi 0.15.0 from the [usual place](http://octoprint.org/download/). If you are asking yourself how to update from
an earlier version of OctoPi, please read on.

**"How do I update?"**

There is currently no way to update from earlier *OctoPi* versions to a new version of that image. It's not strictly necessary though -
a new image basically means that if you have to setup a new instance you'll start at a newer version of everything
bundled with the image. Anything included on the image however can also be kept up to date without having to
reflash. OctoPrint will have prompted you to update itself and will continue to do so, and most of the image itself
[can be kept up to date like every other Raspbian image](https://www.raspberrypi.org/documentation/raspbian/updating.md).

So no pressing need to reflash!

If you want to however, make sure you [back everything up](https://discourse.octoprint.org/t/how-do-i-backup-my-octoprint-settings-on-octopi/1489). I might look into a way
to automate this too.

---

*Confused about the difference between OctoPi and OctoPrint? [Read this](https://discourse.octoprint.org/t/what-is-the-difference-between-octoprint-and-octopi-are-they-the-same-thing/185)!* 