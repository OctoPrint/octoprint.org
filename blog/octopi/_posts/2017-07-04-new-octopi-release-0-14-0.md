---
layout: post
author: foosel
title: "New OctoPi Release: 0.14.0"
date: 2017-07-05 13:10:00 +0200
excerpt: OctoPi 0.14 comes with the latest OctoPrint 1.3.4 and Pi Zero W support, among other things.
featuredimage: /assets/img/blog/2017-07/2017-07-05-octopi-release.png
card: /assets/img/blog/2017-07/2017-07-05-octopi-release.png
poster: /assets/img/blog/2017-07/2017-07-05-octopi-release-poster.png

---

[Guy Sheffer](https://github.com/guysoft) just released
OctoPi 0.14 - big thanks to him and also to everyone who helped test the
three Release Candidates that went into this and reported back!

Apart from adding support for the Pi Zero W and of course shipping with the current stable OctoPrint version
1.3.4, 0.14 also contains the following changes:

> **Changes in the image**
>
>   * Added note to `/root/bin/webcamd` to use `octopi.txt` for configuration
>   * Added note to `octopi-network.txt` for Mac OS X users to not use Textedit/properly configure Textedit
>   * Added note with further instructions on usage to boot and login screen
>   * Allow configuration of multiple wifi networks via `octopi-wpa-supplicant.txt`
>   * Better "service not running" error pages
>   * Enabled SSH by default (we usually run headless, disabling it is not an option)
>   * Updated stock `config.yaml` and init script for OctoPrint to 1.3.0+
>   * Updated `install-desktop` script to only pull in needed packages
>   * Fixes:
>     * Prevent NTP updates from failing on RPi3 wifi ([#327](https://github.com/guysoft/OctoPi/issues/327))
>     * Prevent weird SSH issues on RPi3 ([#294](https://github.com/guysoft/OctoPi/issues/294))
>     * Prevent duplicate X-Scheme headers in haproxy ([#239](https://github.com/guysoft/OctoPi/issues/239))
>     * Workaround for an issue with recent `pip` versions and pyasn1 ([#276](https://github.com/guysoft/OctoPi/issues/276))
>
> **Changes in the build scripts**
>
>   * Support for building against Armbian
>   * Support for custom number for root partition
>   * Fixed pybonjour download link (google code is dead)
>   * Switched vagrant box to one including guest additions

The full release notes can be found at
[github](https://github.com/guysoft/OctoPi/releases/tag/0.14.0).

You can download OctoPi 0.14.0 from the [usual](http://octoprint.org/download/)
[places](https://octopi.octoprint.org). If you are asking yourself how to update from
an earlier version of OctoPi, please read on.

**"How do I update?"**

There is currently no way to update from earlier *OctoPi* versions to a new version of that image. It's not necessary though -
a new image basically means that if you have to setup a new instance you'll start at a newer version of everything
bundled with the image. Anything included on the image however can also be kept up to date without having to
reflash. OctoPrint will have prompted you to update itself and will continue to do so, and most of the image itself
[can be kept up to date like every other Raspbian image](https://www.raspberrypi.org/documentation/raspbian/updating.md).

So no need to reflash!

If you want to however, make sure you backup anything under `~pi/.octoprint` on your current instance and also
make a list of your installed plugins so that you can restore your data on your new one. I might look into a way
to automate this too.
