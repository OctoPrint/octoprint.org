---
layout: post
author: foosel
title: "OctoPi Release Candidate 1.0.0rc2 needs testers!"
date: 2022-08-04 14:30:00 +0200
excerpt: Guy Sheffer has published a second release candidate for the release of OctoPi 1.0.0 and is looking for feedback!
card: /assets/img/blog/2022-08/2022-08-04-octopi-1.0.0rc2-card.png
featuredimage: /assets/img/blog/2022-08/2022-08-04-octopi-1.0.0rc2-card.png
poster: /assets/img/blog/2022-08/2022-08-04-octopi-1.0.0rc2-poster.png
---

[Guy Sheffer](https://github.com/guysoft) just published a
[release candidate](https://github.com/guysoft/OctoPi/issues/788) for the next release
of the Octo**Pi** image, version 1.0.0.

Apart from now being built against the latest RaspberryPi OS version based on Debian Bullseye
and of course shipping with the current stable OctoPrint version 1.8.1, 1.0.0rc2 also
contains the following changes:

> **Changes in the image**
>
> - OctoPrint 1.8.1
> - Version is 1.0.0, it seem like its about time
> - Raspbery PI OS uses bullseye
> - rpi.gpio-common has been added
> - Fix webcamd daemon loop & handling of non-usb v4l2 devices #741 (@foosel)
> - Add a network monitoring for wifi connections #729 (thanks @hawkeyexp)
> - Delete octopi-network.txt
> - picam-bullseye-fix #763  (Thanks @PowerWiesel)

If you've been waiting for a new Octo**Pi** release, this is your chance to give the candidate a test drive
and [**report any findings back in the ticket on the OctoPi repository**](https://github.com/guysoft/OctoPi/issues/788) 
so we can make sure the release is solid!

You can find the download links in the [ticket](https://github.com/guysoft/OctoPi/issues/788).

---

*Confused about the difference between OctoPi and OctoPrint? [Read this](https://faq.octoprint.org/octoprint-vs-octopi)!*
