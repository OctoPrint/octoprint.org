---
layout: post
author: foosel
title: "New OctoPi Release: 1.1.0"
date: 2025-05-06 09:15:00 +0200
excerpt: OctoPi 1.1.0 comes with Debian Bookworm and support for the RPi5, among other things.
card: /assets/img/blog/2025-05/2025-05-06-octopi-1.1.0-card.png
featuredimage: /assets/img/blog/2025-05/2025-05-06-octopi-1.1.0-card.png
poster: /assets/img/blog/2025-05/2025-05-06-octopi-1.1.0-poster.png
---

[Guy Sheffer](https://github.com/guysoft) has just released OctoPi 1.1.0 - big thanks to him and also to everyone who helped test the release candidates and the nightly builds that went into this and reported back!

OctoPi 1.1.0 contains the following changes (see also its [changelog](https://github.com/guysoft/OctoPi/releases/tag/1.1.0)):

>* Raspberry Pi 5 support [#823](https://github.com/guysoft/OctoPi/issues/823)
>* Beta support for Le Potato AML-S905X-CC
>* Images uses Debian bookworm
>* Due to bookworkm `/boot/config.txt` has moved to `/boot/firmware/config.txt` [#220](https://github.com/guysoft/CustomPiOS/issues/220)
>* Support changing default user name on rpi-imager
>  * Move octoprint python virtualenv to `/opt/custompios/oprint` and add a symlink [e62bada2](https://github.com/guysoft/OctoPi/commit/e62bada2c4e91372ace724f7839ab61e34bfb824)
>* Dropped support for wpa supplicant due to [raspberrypi/bookworm-feedback#72](https://github.com/raspberrypi/bookworm-feedback/issues/72)
>* New NetworkManager headless support added, its pretty basic for now since it is expected most people configure the wifi via rpi-imager. There is a new `wifi.nmconnection` file in the `/boot/firmware` folder that lets you configure wifi headless. Its more limited at the moment than the wpa supplicant version
>* Remove camera ID `046d:0825`. Fixes [#759](https://github.com/guysoft/OctoPi/issues/759)
>* Fixed issue with webcam not working [#837](https://github.com/guysoft/OctoPi/issues/837#issuecomment-2536532941)
>* Fixed wifi blocking [guysoft/CustomPiOS@e553cad7](https://github.com/guysoft/CustomPiOS/commit/e553cad7e09410bf27a2083211d6e606d76efe21)
>* Network check has been fixed [#840](https://github.com/guysoft/OctoPi/issues/840) (Thanks @david-forster10)
>* Updated install-desktop [430a00eba](https://github.com/guysoft/OctoPi/commit/430a00eba263cc31c92638b9a2676509956fb366)
>* Remove network monitoring (networkcheck) which only works on wpa-supplicant [ea5d502b](https://github.com/guysoft/OctoPi/commit/ea5d502bff7936ffabbf8f1cab54ab9fd26ab929)
>* switch to modern OS dependencies for latest numpy versions [bf506863](https://github.com/guysoft/OctoPi/commit/bf506863e3b8d7c5fc7b7e1026aa25c5dd33931a)

**Please note that the mjpg-streamer included on OctoPi 1.1.0 does *not* support Raspberry Pi Camera v3/libcamera**, and sadly [camera-streamer used for the new camera stack](https://octoprint.org/blog/2023/05/24/a-new-camera-stack-for-octopi/) currently refuses to compile. We are looking into that, but it might be a while until an image with the new camera stack based on OctoPi 1.1.0 will be available. It might actually even be necessary to completely switch horses there and go with a different streaming solution altogether.

You can download OctoPi 1.1.0 from the Raspberry Pi imager and of course [the download page](http://octoprint.org/download/). If you are asking yourself how to update from an earlier version of OctoPi, please read on.

<div class="alert alert-info">
    <p>
        It has come to my attention that I forgot some important bits in the OctoPi-UpToDate workflow to accomodate the 64bit variant and Pi5 support. If you want to flash the stock OctoPi 1.1.0 image that's also available in 64bit flavor, you can find it <a href="https://github.com/guysoft/OctoPi/releases/tag/1.1.0" target="_blank">here</a> - you can download it manually there and flash it via the RPi imager.
    </p><p>
        A fresh OctoPi-UpToDate build will be made available in the RPi-Imager once the above issues are solved.
    </p>
</div>

**"How do I update?"**

There is currently no way to update from earlier *OctoPi* versions to a new version of that image. It's not strictly necessary though - a new image basically means that if you have to setup a new instance you'll start at a newer version of everything bundled with the image. Anything included on the image however can also be kept up to date without having to reflash. OctoPrint will have prompted you to update itself and will continue to do so, and most of the image itself [can be kept up to date like every other RaspberryPi OS image](https://www.raspberrypi.com/documentation/computers/os.html#updating-and-upgrading-raspberry-pi-os).

The 1.0.0 image still was based on Debian Bullseye however, which is already on [its way towards end-of-life](https://endoflife.date/debian). It therefore would note be a bad idea to create a backup, reflash and restore to run off the new image. If you want to update, [read here on how to create a backup of OctoPrint](https://community.octoprint.org/t/how-do-i-backup-my-octoprint-settings-on-octopi/1489) which you can apply after reflashing.

---

*Confused about the difference between OctoPi and OctoPrint? [Read this](https://community.octoprint.org/t/what-is-the-difference-between-octoprint-and-octopi-are-they-the-same-thing/185)!*
