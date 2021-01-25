---
layout: post
author: foosel
title: "New OctoPi Release: 0.18.0"
date: 2021-01-25 11:00:00 +0100
excerpt: OctoPi 0.18.0 comes with OctoPrint 1.5.2 and Python 3, among other things.
card: /assets/img/blog/2021-01/2021-01-25-octopi-0.18.0-card.png
featuredimage: /assets/img/blog/2021-01/2021-01-25-octopi-0.18.0-card.png
poster: /assets/img/blog/2021-01/2021-01-25-octopi-0.18.0-poster.png
---

[Guy Sheffer](https://github.com/guysoft) has just released
OctoPi 0.18.0 - big thanks to him and also to everyone who helped test the
release candidates and the nightly builds that went into this and reported back!

OctoPi 0.18.0 contains the following changes (see also its [changelog](https://github.com/guysoft/OctoPi/releases/tag/0.18.0)):

>   * OctoPrint 1.5.2
>   * OctoPi now uses Python3
>   * RpiOS image ``2020-12-02``
>   * ``/home/pi/scripts/safemode`` (thanks @OutsourcedGuru)
>   *  Fix [#619](https://github.com/guysoft/OctoPi/issues/619) Shutdown requires network (Thanks @da4id)
>   * [#623](https://github.com/guysoft/OctoPi/pull/623) from szopen111/fix-issue-621 (Workaround for low resolution cameras)
>   * Fix/enable haproxy logging [#640](https://github.com/guysoft/OctoPi/issues/640) and enable compression at haproxy layer [#643](https://github.com/guysoft/OctoPi/pull/643) (thanks @tedder)
>   * Experimental HLS support [#650](https://github.com/guysoft/OctoPi/pull/650) [#668](https://github.com/guysoft/OctoPi/pull/668) [#688](https://github.com/guysoft/OctoPi/pull/688) (thanks @chudsaviet)
>   * Removed old Cura. See [#654](https://github.com/guysoft/OctoPi/issues/654) and [#444](https://github.com/guysoft/OctoPi/issues/444).
>   * Some usb cameras setting fixed ([#657](https://github.com/guysoft/OctoPi/issues/657) [b64a544](https://github.com/guysoft/OctoPi/commit/b64a5441b807f449417b8bcedb41b2703adf89e9) [0d0ea37](https://github.com/guysoft/OctoPi/commit/0d0ea3751e3866d7f893699894691025e33a7757))
>   * Fixes [#676](https://github.com/guysoft/OctoPi/issues/676) and adds deps to install numpy from wheel for plugins taht need numpy
>   * New arm64 builds (Not released yet)
>   * Set HAProxy Diffie-Hellman key size to 2048 [#685](https://github.com/guysoft/OctoPi/pull/685)
> 
> ### Build notes
>
>   * Uses RC2 was built from commit [guysoft/CustomPiOS@7ea63e9](https://github.com/guysoft/CustomPiOS/commit/7ea63e92b1907da8f1a1a50770f390b1d36d72f5). However should also work with  [CustomPiOS 1.4.0](https://github.com/guysoft/CustomPiOS/releases/tag/1.4.0) 

You'll note that OctoPrint is still at 1.5.2, not the latest 1.5.3 released last week - 
the RC for OctoPi was already underway and we didn't want to delay the image even further
for another RC round including the latest bugfix release. However, you can just immediately
upgrade OctoPrint, it should prompt you.

You can download OctoPi 0.18.0 from the [usual place](http://octoprint.org/download/). If you are asking yourself how to update from
an earlier version of OctoPi, please read on.

**"How do I update?"**

There is currently no way to update from earlier *OctoPi* versions to a new version of that image. It's not strictly necessary though -
a new image basically means that if you have to setup a new instance you'll start at a newer version of everything
bundled with the image. Anything included on the image however can also be kept up to date without having to
reflash. OctoPrint will have prompted you to update itself and will continue to do so, and most of the image itself
[can be kept up to date like every other Raspbian image](https://www.raspberrypi.org/documentation/raspbian/updating.md).

Normally there'd be no pressing need to reflash, however since this image finally ditches
Python 2 in favour of Python 3, which apart from continued support also adds some nice
performance improvements, you might want to switch sooner rather than later.

If so, [read here on how to create a backup of OctoPrint](https://community.octoprint.org/t/how-do-i-backup-my-octoprint-settings-on-octopi/1489)
which you can apply after reflashing and updating to the latest version.

---

*Confused about the difference between OctoPi and OctoPrint? [Read this](https://community.octoprint.org/t/what-is-the-difference-between-octoprint-and-octopi-are-they-the-same-thing/185)!*
