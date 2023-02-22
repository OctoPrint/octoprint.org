---
layout: post
author: foosel
title: "New OctoPi Release: 1.0.0"
date: 2023-02-22 11:40:00 +0100
excerpt: OctoPi 1.0.0 comes with OctoPrint 1.8.6 and Debian Bullseye, among other things.
card: /assets/img/blog/2023-02/2023-02-22-octopi-1.0.0-card.png
featuredimage: /assets/img/blog/2023-02/2023-02-22-octopi-1.0.0-card.png
poster: /assets/img/blog/2023-02/2023-02-22-octopi-1.0.0-poster.png
---

[Guy Sheffer](https://github.com/guysoft) has just released OctoPi 1.0.0 - big thanks to him and also to everyone who helped test the release candidates and the nightly builds that went into this and reported back!

OctoPi 1.0.0 contains the following changes (see also its [changelog](https://github.com/guysoft/OctoPi/releases/tag/1.0.0)):

> * Version is 1.0.0, it seem like its about time [606cdaa](https://github.com/guysoft/OctoPi/commit/b6b7f3623aa59021513693596537543b725aff04)
> * OctoPrint 1.8.6
> * Uses Debian "bullseye" RpiOS 2022-09-22
> * rpi.gpio-common has been added
> * Fix webcamd daemon loop & handling of non-usb v4l2 devices [#741](https://github.com/guysoft/OctoPi/issues/741)  (@foosel)
> * Add a network monitoring for wifi connections [#729](https://github.com/guysoft/OctoPi/issues/729) (thanks @hawkeyexp)
> * [Delete octopi-network.txt](https://github.com/guysoft/OctoPi/commit/ca2840ced1dc6ae398e4c693927a4527514b042a) (@XRyu)
> * picam-bullseye-fix [#763](https://github.com/guysoft/OctoPi/issues/763) (Thanks @PowerWiesel)
> * ships ffmpeg with HLS support at ``/opt/ffmpeg-hls/ffmpeg`` [#784](https://github.com/guysoft/OctoPi/issues/784) (@chudsaviet)
> * 64 bit build has moved to raspios ([#785](https://github.com/guysoft/OctoPi/issues/785))
> * deals with the userless images changes ([guysoft/CustomPiOS#163](https://github.com/guysoft/CustomPiOS/issues/163))
> * ships with user-fix to adapt to username changes of `pi` user [#791](https://github.com/guysoft/OctoPi/issues/791) @cp2004

Please note that OctoPi 1.0.0 does *not* yet include support for the new Raspberry Pi Camera v3. However, we are actively working on a webcam stack swap that will allow us to support `libcamera` based cameras like that one and also newer Arducams. A test image built on top of OctoPi 1.0.0 via [OctoPi-UpToDate](https://github.com/OctoPrint/OctoPi-UpToDate/) with that should hopefully be available within the next two weeks!

You can download OctoPi 1.0.0 from the Raspberry Pi imager and of course [the download page](http://octoprint.org/download/). If you are asking yourself how to update from an earlier version of OctoPi, please read on.

**"How do I update?"**

There is currently no way to update from earlier *OctoPi* versions to a new version of that image. It's not strictly necessary though - a new image basically means that if you have to setup a new instance you'll start at a newer version of everything bundled with the image. Anything included on the image however can also be kept up to date without having to reflash. OctoPrint will have prompted you to update itself and will continue to do so, and most of the image itself [can be kept up to date like every other RaspberryPi OS image](https://www.raspberrypi.com/documentation/computers/os.html#updating-and-upgrading-raspberry-pi-os).

The 0.18.0 image still was based on Debian Buster however, which is already on [its way to age out of security updates](https://endoflife.date/debian). It therefore would note be a bad idea to create a backup, reflash and restore to run off the new image. If you want to update, [read here on how to create a backup of OctoPrint](https://community.octoprint.org/t/how-do-i-backup-my-octoprint-settings-on-octopi/1489) which you can apply after reflashing.

---

*Confused about the difference between OctoPi and OctoPrint? [Read this](https://community.octoprint.org/t/what-is-the-difference-between-octoprint-and-octopi-are-they-the-same-thing/185)!*
