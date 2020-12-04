---
layout: download
banner: true
title: Download & Setup OctoPrint
description: Learn how to setup OctoPrint using the preinstalled OctoPi image for Raspberry Pi, or how to install from source on Windows, Linux and Mac.
---

# OctoPi

[Guy Sheffer](https://github.com/guysoft) maintains ["OctoPi"](https://github.com/guysoft/OctoPi),
a [Raspbian (and thus Debian) based](http://www.raspbian.org/) SD card image for the Raspberry Pi
that already includes OctoPrint plus everything you need to run it:

* OctoPrint plus its dependencies
* [MJPG-Streamer](https://github.com/jacksonliam/mjpg-streamer)
  for live viewing of prints and timelapse video creation, compatible with various
  USB webcams and the Raspberry Pi camera

**Recommended hardware: Raspberry Pi 3B, 3B+ or 4B. Expect print artifacts and long loading times with other 
options, especially when adding a webcam or installing third party plugins.** Setups not using
recommended hardware are not officially supported. 

Please note that the **Raspberry Pi Zero W is not recommended explicitly** since severe performance 
issues were observed, caused by the WiFi interface when bandwidth is utilized (e.g. the webcam is streamed), negatively 
impacting printing quality. [See also here](https://github.com/guysoft/OctoPi/issues/318#issuecomment-284762963).

## Images

<div class="alert">
    There have been some reports regarding current revisions of the <strong>Raspberry Pi 4 1/2/4 GB refusing to boot</strong> with the stable
    OctoPi 0.17.0 image. If that affects you, please try the OctoPi 0.18.0 release candidate.
</div>

### Stable

You can download the latest OctoPi image via the following button. 

<div class="text-center">
    <a class="btn btn-large btn-primary btn-block" href="https://octopi.octoprint.org/latest" data-event-category="download" data-event-action="latest"><i class="fa fa-download-alt fa-lg"></i>&nbsp;&nbsp;Download&nbsp;OctoPi&nbsp;0.17.0</a>
    <small>MD5Sum of the .zip: <code>8a550602b8ccc5df8381924757f88ab9</code></small><br>
    <small><strong>Raspberry Pi 3B, 3B+ or 4B 1/2/4GB strongly recommended, Raspberry Pi Zero/Zero W not officially supported!</strong></small><br>
    <small>Image compatible with Raspberry Pi A, B, A+, B+, 2B, 3A+, 3B, 3B+, 4B 1/2/4GB, Zero and Zero W.</small><br>
    <small>Incompatible to Raspberry Pi 4B 8GB. Only 32bit builds available.</small>
</div>

Alternatively simply buy one of the available

<div class="text-center">
    <a class="btn btn-large btn-block" href="/merch/#kits" data-event-category="download" data-event-action="kits">All-in-one OctoPrint Kits</a>
</div>

### Release Candidate

The current <strong>release candidate for 0.18.0</strong> can be found here: 

<div class="text-center">
    <a class="btn btn-large btn-block" href="https://github.com/guysoft/OctoPi/issues/692" data-event-category="download" data-event-action="next"><i class="fa fa-download-alt fa-lg"></i>&nbsp;&nbsp;OctoPi&nbsp;0.18.0rc1 (32 & 64 bit)</a>
    <small><strong>Raspberry Pi 3B, 3B+ or 4B strongly recommended, Raspberry Pi Zero/Zero W not officially supported!</strong></small><br>
    <small>Image compatible with Raspberry Pi A, B, A+, B+, 2B, 3A+, 3B, 3B+, 4B 1/2/4/8GB, Zero and Zero W.</small><br>
    <small>32 bit recommended</small>
</div>

Use this if you cannot get 0.17.0 to boot on your Pi. **It is strongly recommended to use
the 32bit build for now** as the 64bit build of Raspbian is altogether still rather experimental.

### Nightlies

You can also get the [32bit 0.18 nightlies here](http://unofficialpi.org/Distros/OctoPi/nightly/) or the highly experimental [64bit 0.18 nightlies for the RPi4 8GB here](http://unofficialpi.org/Distros/OctoPi/nightly-arm64/).

##  Setting up OctoPi

Please follow these steps after downloading:

1. Unzip the image and install the contained ``.img`` file to an SD card
   [using Etcher](https://etcher.io/). **Do not at any point format the SD from your Operating System, even if prompted to do so** - 
   that will break it and you'll have to start over. Just use Etcher to flash the `.img` file, that is enough!

2. Configure your WiFi connection by editing ``octopi-wpa-supplicant.txt`` on the root of the
   flashed card when using it like a thumb drive. **Important: Do not use WordPad (Windows) or TextEdit (MacOS X)**
   for this, those editors are known to mangle the file, making configuration fail. Use something like 
   Notepad++, Atom or VSCode instead or at the very least heed the warnings in the file.
   
   **Note:** This changed with OctoPi 0.15.0, earlier versions had you edit ``octopi-network.txt`` which has a different
   format. This old method is *no longer supported* and the contents of this file will be ignored. Just 
   use ``octopi-wpa-supplicant.txt``.
   
   Please also refer take a look at the [full WiFi setup guide in the FAQ](https://faq.octoprint.org/wifi-setup) that also includes Troubleshooting tips.

3. Boot the Pi from the card.

4. Log into your Pi via SSH (it is located at ``octopi.local``
   [if your computer supports bonjour](https://learn.adafruit.com/bonjour-zeroconf-networking-for-windows-and-linux/overview)
   or the IP address assigned by your router), default username is "pi",
   default password is "raspberry". Run ``sudo raspi-config``. Once that is open:
    
   1. Change the password via "Change User Password"
   2. Optionally: Change the configured timezone via "Localization Options" > "Timezone".
   3. Optionally: Change the hostname via "Network Options" > "Hostname". Your OctoPi instance will then no longer be reachable under ``octopi.local`` but rather the hostname you chose postfixed with ``.local``, so keep that in mind.
    
   You can navigate in the menus using the arrow keys and <key>Enter</key>. To switch to selecting the buttons at the bottom use <key>Tab</key>.
    
   **You do not need to expand the filesystem**, current versions of OctoPi do this automatically.
   
   **You also do not need to manually enable the RaspiCam** if you have one, that is already taken care of on the image as well.

5. Access OctoPrint through ``http://octopi.local`` or ``http://<your pi's ip address>``. https is available too,
   with a self-signed certificate (which means your browser will warn you about it being invalid).

Please also refer to [OctoPi's README](https://github.com/guysoft/OctoPi), especially the ["How to use it" section](https://github.com/guysoft/OctoPi#how-to-use-it).

[Thomas Sanladerer](https://www.youtube.com/channel/UCb8Rde3uRL1ohROUVg46h1A) created a great video guide on how to get OctoPi 0.12 up an running.

{% include youtube.html vid="MwsxO3ksxm4" %}

## Further resources

  * [The MagPi issue #36](https://www.raspberrypi.org/magpi/issues/36/) contains a "Getting Started" guide on 
    pages 50-51. You can find an excerpt [here](/assets/download/MagPi36_OctoPrint.pdf) 
    (MagPi License: [CC BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/3.0/)).
  * Scripts to build (and customize) the image yourself can be found in [OctoPi's Github repository](https://github.com/guysoft/OctoPi).
  * Nightly builds can be found [here](http://gnethomelinux.com/OctoPi/nightly/).

----

#  Installing manually

The generic setup instructions boil down to

1. Installing [Python](https://www.python.org/) including [pip](https://pip.pypa.io/en/latest/installing.html) and [virtualenv](https://virtualenv.pypa.io/en/stable/installation.html).
   **Please note:** While OctoPrint itself supports running under both Python 2.7 and Python 3.6+, it is recommended that you install 
   using Python 3.6+ since Python 2 is now end-of-life. A majority of the plugins are compatible to Python 3 now, full details can be 
   found on the [plugin repository](https://plugins.octoprint.org)
2. Creating a virtual environment somewhere: `virtualenv OctoPrint`
3. Installing OctoPrint *into that virtual environment*: `OctoPrint/bin/pip install OctoPrint`
4. OctoPrint may then be started through `./OctoPrint/bin/octoprint serve` or with an absolute path `/path/to/OctoPrint/bin/octoprint serve`

More specific setup instructions for the most common runtime environments can be found below.

##  Linux

For installing OctoPrint on Linux, please take a look at [the setup instructions for Raspbian on the forum](https://community.octoprint.org/t/setting-up-octoprint-on-a-raspberry-pi-running-raspbian/2337/).
They should be pretty much identical on other Linux distributions.

##  Windows

For installing the OctoPrint server on a Windows system, please take a look at [the setup instructions for Windows on the forum](https://community.octoprint.org/t/setting-up-octoprint-on-windows/383/1).

## Mac

For installing the OctoPrint server on a Mac, please take a look at [the setup instructions for MacOS on the forum](https://community.octoprint.org/t/setting-up-octoprint-on-macos/13425).
