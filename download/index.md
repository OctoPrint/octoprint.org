---
layout: download
banner: true
title: Download & Setup OctoPrint
description: Learn how to setup OctoPrint using the preinstalled OctoPi image for Raspberry Pi, or how to install from source on Windows, Linux and Mac.
---

# OctoPi

[Guy Sheffer](https://github.com/guysoft) maintains ["OctoPi"](https://github.com/guysoft/OctoPi),
a [Raspbian (and thus Debian) based](https://www.raspbian.org/) SD card image for the Raspberry Pi
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

## Installing OctoPi

OctoPi is available through the [Raspberry Pi Imager](https://www.raspberrypi.org/software/), which you can use to download and setup OctoPi. You can install it yourself, or alternatively simply buy one of the available

<div class="text-center" style="margin-bottom: 1rem;">
    <a class="btn btn-large btn-block" href="/merch/#kits" data-event-category="download" data-event-action="kits">All-in-one OctoPrint Kits</a>
</div>

**Here's how to get started installing OctoPi**:

1. If you haven't already, **download and install [Raspberry Pi Imager](https://raspberrypi.org/software)** on your computer

2. **Find the OctoPi image** under 'Choose OS', by selecting 'Other Specific Purpose OS' followed by 'OctoPi'

3. **Open advanced options** by using the keyboard shortcut <code>ctrl</code>+<code>shift</code>+<code>x</code> to configure your Wifi connection:
  * Set your SSID, password and WiFi country using the options:
  ![Advanced Options - Wifi Setup](/assets/img/download/advanced-wifi.png)

4. **Install the image to your SD card**, then plug everything in to your Raspberry Pi and boot it up. **Do not format the SD card after installing, even if prompted to do so.** This will break the installation and you will have to start over!

5. **Log into your Pi via SSH** (it is located at ``octopi.local``
   [if your computer supports bonjour](https://learn.adafruit.com/bonjour-zeroconf-networking-for-windows-and-linux/overview)
   or the IP address assigned by your router), default username is `pi`,
   default password is `raspberry`. Run ``sudo raspi-config``. Once that is open:
    
   1. Change the password via "Change User Password"
   2. Optionally: Change the configured timezone via "Localization Options" > "Timezone".
   3. Optionally: Change the hostname via "Network Options" > "Hostname". Your OctoPi instance will then no longer be reachable under ``octopi.local`` but rather the hostname you chose postfixed with ``.local``, so keep that in mind.
    
   You can navigate in the menus using the arrow keys and <key>Enter</key>. To switch to selecting the buttons at the bottom use <key>Tab</key>.
    
   **You do not need to expand the filesystem**, current versions of OctoPi do this automatically.
   
   **You also do not need to manually enable the RaspiCam** if you have one, that is already taken care of on the image as well.

5. **Access OctoPrint** through ``http://octopi.local`` or ``http://<your pi's ip address>``. `https` is available too,
   with a self-signed certificate (which means your browser will warn you about it being invalid).

Please also refer to [OctoPi's README](https://github.com/guysoft/OctoPi), especially the ["How to use it" section](https://github.com/guysoft/OctoPi#how-to-use-it).

### Alternative Wifi Setup

If you aren't using Raspberry Pi Imager, then you can also setup the Wifi connection using the `octopi-wpa-supplicant.txt` file
on the root of the installed card when using it like a thumb drive. 
**Important: Do not use WordPad (Windows) or TextEdit (MacOS X)**  for this, those editors are known to mangle
the file, making configuration fail. Use something like Notepad++, Atom or VSCode instead or at the very 
least heed the warnings in the file.

Please also refer take a look at the [full WiFi setup guide in the FAQ](https://faq.octoprint.org/wifi-setup) that also includes troubleshooting tips.

### Video

[Thomas Sanladerer](https://www.youtube.com/channel/UCb8Rde3uRL1ohROUVg46h1A) created a great video guide on how to get OctoPi 0.18 up and running.

{% include youtube.html vid="HBd0olxI-No" %}

## Image Downloads

<!--
<div class="alert">
    There have been some reports regarding current revisions of the <strong>Raspberry Pi 4 1/2/4 GB refusing to boot</strong> with the stable
    OctoPi 0.17.0 image. If that affects you, please try the OctoPi 0.18.0 release candidate.
</div>
-->

Raspberry Pi Imager will download the latest version of OctoPi for you, but if you want to download the images 
yourself you can do so here.

### Stable OctoPi

<div class="text-center">
    <a class="btn btn-large btn-primary btn-block" href="{{ site.data.octopi.latest.url }}" data-event-category="download" data-event-action="latest">
      OctoPi&nbsp;{{ site.data.octopi.latest.octopi_version }} &amp; OctoPrint&nbsp;{{ site.data.octopi.latest.octoprint_version }}
    </a>
    <small>SHA256: <code>{{ site.data.octopi.latest.sha256 }}</code></small><br>
    <small><strong>{{ site.data.octopi.recommendation }}</strong></small><br>
    <small>Image compatible with Raspberry Pi {{ site.data.octopi.latest.pi_models }}.</small><br>
</div>

{% if site.data.octopi.next_octoprint %}
### Stable OctoPi with OctoPrint Release Candidate

The current <strong>stable OctoPi {{ site.data.octopi.latest.octopi_version }} with OctoPrint Release Candidate {{ site.data.octopi.next_octoprint.octoprint_version }}</strong> can be found here: 

<div class="text-center">
    <a class="btn btn-large btn-block" href="{{ site.data.octopi.next_octoprint.url }}" data-event-category="download" data-event-action="next">
      OctoPi&nbsp;{{ site.data.octopi.latest.octopi_version }} &amp; OctoPrint&nbsp;{{ site.data.octopi.next_octoprint.octoprint_version }}
    </a>
    <small>SHA256: <code>{{ site.data.octopi.next_octoprint.sha256 }}</code></small><br>
    <small><strong>{{ site.data.octopi.recommendation }}</strong></small><br>
    <small>Image compatible with Raspberry Pi {{ site.data.octopi.latest.pi_models }}.</small><br>
</div>
{% endif %}

{% if site.data.octopi.next_octopi %}
### OctoPi Release Candidate

The current <strong>OctoPi Release Candidate {{ site.data.octopi.next_octopi.octopi_version }}</strong> can be found here: 

<div class="text-center">
    <a class="btn btn-large btn-block" href="{{ site.data.octopi.next_octopi.url }}" data-event-category="download" data-event-action="next">
      OctoPi&nbsp;{{ site.data.octopi.next_octopi.octopi_version }} &amp; OctoPrint&nbsp;{{ site.data.octopi.next_octopi.octoprint_version }}
    </a>
    <small><strong>{{ site.data.octopi.recommendation }}</strong></small><br>
    <small>Image compatible with Raspberry Pi {{ site.data.octopi.next_octopi.pi_models }}.</small><br>
</div>
{% endif %}

### OctoPi Nightlies

You can also get the [32bit nightlies here](https://unofficialpi.org/Distros/OctoPi/nightly/) or the highly experimental [64bit nightlies here](https://unofficialpi.org/Distros/OctoPi/nightly-arm64/).


## Further resources

  * [The MagPi issue #36](https://www.raspberrypi.org/magpi/issues/36/) contains a "Getting Started" guide on 
    pages 50-51. You can find an excerpt [here](/assets/download/MagPi36_OctoPrint.pdf) 
    (MagPi License: [CC BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/3.0/)).
  * For customizing OctoPi, take a look at [CustoPiZer](https://github.com/OctoPrint/CustoPiZer).
  * Scripts to build the image yourself can be found in [OctoPi's Github repository](https://github.com/guysoft/OctoPi).

----

#  Installing manually

The generic setup instructions boil down to

1. Installing [Python 3](https://www.python.org/), including [pip](https://pip.pypa.io/en/latest/installing.html).
2. Creating a virtual environment somewhere: `python -m venv OctoPrint`
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
