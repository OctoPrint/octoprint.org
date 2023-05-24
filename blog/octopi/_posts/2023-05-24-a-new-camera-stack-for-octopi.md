---
layout: post
author: foosel
title: "A new camera stack for OctoPi"
date: 2023-05-24 14:00:00 +0200
excerpt: For the past few months, I've not only worked on OctoPrint 1.9.0 and its RCs, but I've also been working on a new camera stack for OctoPi. Today I want to tell you a bit more about it.
card: /assets/img/blog/2023-05/2023-05-24-new-camera-stack-card.png
featuredimage: /assets/img/blog/2023-05/2023-05-24-new-camera-stack-card.png
poster: /assets/img/blog/2023-05/2023-05-24-new-camera-stack-poster.png
---

For the past few months, I've not only worked on OctoPrint 1.9.0 and its RCs, but I've also been working on a new camera stack for OctoPi.

The current camera stack in OctoPi is using [mjpg-streamer](https://github.com/jacksonliam/mjpg-streamer), and while that has been working great for a decade now (and also was pretty much the only thing that worked reliably on the available hardware back when I originally created OctoPrint in late 2012), with the release of the Raspberry Pi Camera v3 which requires the use of something called [`libcamera`](https://libcamera.org/) that sadly no longer was the case. Add to that the fact that mjpg streams are notoriously bandwidth heavy and more modern alternatives exist these days, and it was clear that it was time for a change.

So over the course of an action week[^1] back in February of this year[^2], I started development on a new camera stack for OctoPi based on [@ayufan's](https://github.com/ayufan/) quite awesome [camera-streamer](https://github.com/ayufan/camera-streamer) project, and created an [OctoPi-UpToDate](https://github.com/OctoPrint/OctoPi-UpToDate/tree/camera-streamer) image based on it. This image has been available for testing on the repository for a while now and gone through several iterations. 

But what has this new camera stack that the original one doesn't have? I'm glad you asked!

## What's new?

As already hinted at, first of all this new camera stack supports the **Raspberry Pi Camera v3** and all other currently available Raspberry Pi Camera modules. In fact it supports any camera that is supported by `libcamera`, including - after some additional steps - various [**Arducam**](https://www.arducam.com/) cameras. Additionally, the new stack of course also supports **USB cameras**.

So that alone might already be a reason why you might want to give it a try, but there's more! Thanks to some `systemd` magic, I was able to make it quite easy to **add more than one camera** to your setup. You can combine one `libcamera` based camera with one or more USB based webcams, or just run one ore more USB cams on their own, and there's also some special commands to help you add a new camera to your setup. All of this has been documented already [in the FAQ](https://community.octoprint.org/t/49950), so best check that out. 

What the heavy use of `systemd` units and paths here also does is give us some nice **hotplug support for USB webcams**, without having to poll available devices - a *big* step up from the old `webcamd` shell script that's grown organically over the years to the point it has become quite unmaintainable. Camera settings are done through **individual `conf` files** - one per camera - available directly on the `/boot` partition (so also when using a flashed SD like a thumb drive). This not only makes things way cleaner, it also makes it easy to **share configs** in the community, and during the testing phase it made me very happy to already see that happening.

Apart from this, `camera-streamer` at the core of this stack also supports a lot of additional features that the old stack didn't have, like streaming **H264** via MP4, MKV or HLS, streaming via **WebRTC**, defining **different resolutions for snapshots and video streams**, and more. I've documented all of this in the [camera-streamer FAQ](https://community.octoprint.org/t/49950). It's also very actively maintained by [@ayufan](https://github.com/ayufan/), and we've already been in contact as well.

## Where to get it?

As of yesterday, an up-to-date OctoPi image with the new camera stack is **available on the [Raspberry Pi Imager](https://www.raspberrypi.com/software/)**:

![A screenshot of the Raspberry Pi Imager showing the two available download options for OctoPi, "stable" and "new camera stack"](/assets/img/blog/2023-05/2023-05-24-rpi-imager.png)

The goal is to make the new camera stack the default in the future, but for now some more widespread testing feels like a good idea. Therefore I'm currently offering both an up-to-date OctoPi ("stable"), and an up-to-date OctoPi with the camera stack replaced by the new one ("new camera stack"). 

If you want to help with testing, just play around with it or if you have been waiting for something that supports the RPiCamV3 out of the box, please grab the new image, either via the RPi Imager or by picking the latest "branch camera-streamer" build from [the OctoPi-UpToDate release page](https://github.com/OctoPrint/OctoPi-UpToDate/releases), and give it a spin! 

At this point it can be considered fairly stable based on the initial testing by some awesome members of the community 💕, but if you encounter any issues with *camera functionality* specifically, **please report them on the [OctoPi-UpToDate repository](https://github.com/OctoPrint/OctoPi-UpToDate)** (*not* the OctoPi repository please - this new stack is not (yet?) part of stock OctoPi and I don't want to confuse people and especially the OctoPi maintainer by having issues with it reported there).

## What's next?

As already mentioned, the next step is going to be to offer this new camera stack as the default in OctoPi. Along with that, it would also be time to think to switch the default OctoPrint configuration shipped on the image to no longer be set to utilize the mjpg stream but rather a less bandwidth hungry option offered by camera-streamer. For that however, some more testing will be needed to make the right call here between the available options with regards to delay and resource consumption. 

With OctoPrint 1.9.0 now out of the door, and with it a new fangled webcam plugin interface, things should be a lot easier to tackle here than they were ever before!

---

[^1]: An action week is a week where I focus on topics from the backlog that require a lot of uninterrupted time to tackle. Contrast that to reaction weeks, where I jump back and forth between issues, PRs, community management and other things that require a lot of context switching. I've been switching between those two modes every week since the start of this year now, on my constant quest to find a good balance between getting things done and not burning out, and so far it looks like a good approach.
[^2]: Big shoutout to [@PowerWiesel](https://github.com/PowerWiesel), who paired with me on this via an extended audio call one day and helped getting this off the ground!
