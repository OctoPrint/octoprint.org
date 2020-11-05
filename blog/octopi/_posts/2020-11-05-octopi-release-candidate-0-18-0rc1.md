---
layout: post
author: foosel
title: "OctoPi Release Candidate 0.18.0rc1 needs testers!"
date: 2020-11-05 11:20:00 +0100
excerpt: Guy Sheffer published a release candidate for the release of OctoPi 0.18.0 and is looking for feedback!
card: /assets/img/blog/2020-11/2020-11-05-octopi-0.18.0rc1-card.png
featuredimage: /assets/img/blog/2020-11/2020-11-05-octopi-0.18.0rc1-card.png
poster: /assets/img/blog/2020-11/2020-11-05-octopi-0.18.0rc1-poster.png
---

[Guy Sheffer](https://github.com/guysoft) just published a
[release candidate](https://github.com/guysoft/OctoPi/issues/692) for the next release 
of the OctoPi image, version 0.18.0.

Apart from adding support for the Pi 4 8GB and the Pi 4 and of course shipping with the current stable 
OctoPrint version 1.4.2 now running under Python 3, 0.18.0rc1 also contains the following changes:

> **Changes in the image**
> 
>   * OctoPrint 1.4.2
>   * OctoPi now uses Python3
>   * ``/home/pi/scripts/safemode`` (thanks @OutsourcedGuru)
>   * Fix #619 Shutdown requires network (Thanks @da4id)
>   * Fix #623 from szopen111/fix-issue-621 (Workaround for low resolution cameras)
>   * Fix/enable haproxy logging #640 and enable compression at haproxy layer #643 (thanks @tedder)
>   * Experimental HLS support #650 #668 #688 (thanks @chudsaviet)
>   * Removed old Cura. See #654 and #444.
>   * Some usb cameras setting fixed (#657 [b64a5441](https://github.com/guysoft/OctoPi/commit/b64a5441b807f449417b8bcedb41b2703adf89e9) [0d0ea375](https://github.com/guysoft/OctoPi/commit/0d0ea3751e3866d7f893699894691025e33a7757))
>   * Fixes #676 and adds deps to install numpy from wheel for plugins taht need numpy
>   * New arm64 builds
>   * Set HAProxy Diffie-Hellman key size to 2048 #685
> 
> **Build notes**
>
>   * Uses [CustomPiOS 1.4.0](https://github.com/guysoft/CustomPiOS/releases/tag/1.4.0)

If you've been waiting for a new OctoPi release, this is your chance to give the candidate a test drive
and [**report any findings back in the ticket on the OctoPi repository**](https://github.com/guysoft/OctoPi/issues/692) 
so we can make sure the release is solid!

You can find the download links in the [ticket](https://github.com/guysoft/OctoPi/issues/692).

---

*Confused about the difference between OctoPi and OctoPrint? [Read this](https://faq.octoprint.org/octoprint-vs-octopi)!*
 
