---
layout: post
author: foosel
title: "OctoPi Release Candidate 1.0.0rc1 needs testers!"
date: 2022-02-28 14:40:00 +0100
excerpt: Guy Sheffer has published a first release candidate for the release of OctoPi 1.0.0 and is looking for feedback!
card: /assets/img/blog/2022-02/2022-02-28-octopi-1.0.0rc1-card.png
featuredimage: /assets/img/blog/2022-02/2022-02-28-octopi-1.0.0rc1-card.png
poster: /assets/img/blog/2022-02/2022-02-28-octopi-1.0.0rc1-poster.png
---

[Guy Sheffer](https://github.com/guysoft) just published a
[release candidate](https://github.com/guysoft/OctoPi/issues/770) for the next release 
of the Octo**Pi** image, version 1.0.0.

Apart from now being built against the latest RaspberryPi OS version based on Debian Bullseye 
and of course shipping with the current stable OctoPrint version 1.7.3, 1.0.0rc1 also 
contains the following changes:

> **Changes in the image**
> 
>   * OctoPrint 1.7.3
>   * Version is 1.0.0, [it seems like it's about time](https://github.com/guysoft/OctoPi/commit/b6b7f3623aa59021513693596537543b725aff04)
>   * RaspberryPi OS uses bullseye
>   * rpi.gpio-common has been added
>   * Fix webcamd daemon loop & handling of non-usb v4l2 devices [#741](https://github.com/guysoft/OctoPi/pull/741) (@foosel)
>   * Add a network monitoring for wifi connections [#729](https://github.com/guysoft/OctoPi/pull/729) (thanks @hawkeyexp)
>   * [Delete octopi-network.txt](https://github.com/guysoft/OctoPi/commit/ca2840ced1dc6ae398e4c693927a4527514b042a)
>   * picam-bullseye-fix [#763](https://github.com/guysoft/OctoPi/pull/763) (Thanks @PowerWiesel)

If you've been waiting for a new Octo**Pi** release, this is your chance to give the candidate a test drive
and [**report any findings back in the ticket on the OctoPi repository**](https://github.com/guysoft/OctoPi/issues/770) 
so we can make sure the release is solid!

You can find the download links in the [ticket](https://github.com/guysoft/OctoPi/issues/770).

---

*Confused about the difference between OctoPi and OctoPrint? [Read this](https://faq.octoprint.org/octoprint-vs-octopi)!*
