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
* [CuraEngine 15.04](https://github.com/Ultimaker/CuraEngine) for slicing directly
  on your Raspberry Pi

**Recommended hardware: Raspberry Pi 3B**. 

Please note that the **Raspberry Pi Zero W is not recommended** since severe performance 
issues were observed, caused by the WiFi interface when bandwidth is utilized (e.g. the webcam is streamed), negatively 
impacting printing results. [See also here](https://github.com/guysoft/OctoPi/issues/318#issuecomment-284762963).

You can download the latest OctoPi image via the following button. **Please note that OctoPi 0.15.1 is not yet compatible
with the recently released Raspberry Pi 3A+ and will not boot on it.** Use one of the current [OctoPi 0.16 nightlies](http://gnethomelinux.com/OctoPi/nightly/) 
if you have one of those.

<div class="text-center">
    <a class="btn btn-large btn-block" href="https://octopi.octoprint.org/latest" data-event-category="download" data-event-action="latest"><i class="fa fa-download-alt fa-lg"></i>&nbsp;&nbsp;Download&nbsp;OctoPi&nbsp;0.15.1</a>
    <small>MD5Sum of the .zip: <code>4600d24c0618376c2a10c1507b8ba990</code></small><br>
    <small>Image compatible with Raspberry Pi A, B, A+, B+, 2B, 3B, 3B+, Zero and Zero W. <strong>Not yet compatible with Raspberry Pi 3A+</strong></small><br>
    <small><strong>Raspberry Pi 3B or 3B+ strongly recommended!</strong></small>
</div>

or simply buy one of the available

<div class="text-center">
    <a class="btn btn-large btn-block" href="/support-octoprint/#kits" data-event-category="download" data-event-action="kits">All-in-one OctoPrint Kits</a>
</div>

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
   2. Optionally: Change the configured timezone via "Localization Optinos" > "Timezone".
   3. Optionally: Change the hostname via "Network Options" > "Hostname". Your OctoPi instance will then no longer be reachable under ``octopi.local`` but rather the hostname you chose postfixed with ``.local``, so keep that in mind.
    
   You can navigate in the menus using the arrow keys and Enter. To switch to selecting the buttons at the bottom use Tab.
    
   You do not need to expand the filesystem, current versions of OctoPi do this automatically.

5. Access OctoPrint through ``http://octopi.local`` or ``http://<your pi's ip address>``. https is available too,
   with a self-signed certificate.

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

#  Installing from source

The generic setup instructions boil down to

1. Installing [Python 2.7](https://www.python.org/) including [pip](https://pip.pypa.io/en/latest/installing.html) and [virtualenv](https://virtualenv.pypa.io/en/stable/installation/).
2. Obtaining the source through either of:
   1. cloning the [source repository](https://github.com/foosel/OctoPrint.git): `git clone https://github.com/foosel/OctoPrint.git`
   2. downloading an [archive of the current stable version](https://github.com/foosel/OctoPrint/archive/master.zip) from Github and unpacking it
3. Creating a (user owned) virtual environment in the source folder: `virtualenv venv`
4. Installing OctoPrint *into that virtual environment*: `./venv/bin/python setup.py install`
5. OctoPrint may then be started through `./venv/bin/octoprint` or with an absolute path `/path/to/OctoPrint/venv/bin/octoprint`

More specific setup instructions for the most common runtime environments can be found below.

##  Linux

For installing OctoPrint from source, please take a look at [the setup instructions for Raspbian on the wiki](https://github.com/foosel/OctoPrint/wiki/Setup-on-a-Raspberry-Pi-running-Raspbian).
They should be pretty much identical on other Linux distributions.

##  Windows

For installing the OctoPrint server on a Windows system, please take a look at [the setup instructions for Windows on the forum](https://discourse.octoprint.org/t/setting-up-octoprint-on-windows/383/1).

## Mac

For installing the OctoPrint server on a Mac, please take a look at [the setup instructions for MacOS on the wiki](https://github.com/foosel/OctoPrint/wiki/Setup-on-Mac).
