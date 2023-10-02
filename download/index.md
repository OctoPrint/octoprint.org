---
layout: download
banner: true
title: Download & Setup OctoPrint
description: Learn how to setup OctoPrint using the preinstalled OctoPi image for Raspberry Pi, or how to install from source on Windows, Linux and Mac.
---

<center>
  <a href="#octopi">OctoPi (Raspberry Pi)</a> &middot; <a href="#octo4a">Octo4a (Android)</a> &middot; <a href="#octoprint-for-orange-pi">OctoPrint for Orange Pi</a> &middot; <a href="#docker">Docker install</a> &middot; <a href="#octoprint_deploy-linux">octoprint_deploy (Linux)</a> &middot; <a href="#windows-installer">Windows Installer</a> &middot; <a href="#installing-manually">Manual install (Linux, Windows, Mac)</a>
</center>

# OctoPi

[Guy Sheffer](https://github.com/guysoft) maintains ["OctoPi"](https://github.com/guysoft/OctoPi),
a [Raspbian (and thus Debian) based](https://www.raspbian.org/) SD card image for the Raspberry Pi
that already includes OctoPrint plus everything you need to run it:

* OctoPrint plus its dependencies
* [MJPG-Streamer](https://github.com/jacksonliam/mjpg-streamer)
  for live viewing of prints and timelapse video creation, compatible with various
  USB webcams and the Raspberry Pi camera

**Recommended hardware: Raspberry Pi 3B, 3B+, 4B or Zero 2. Expect print artifacts and long loading times with other 
options, especially when adding a webcam or installing third party plugins.** Setups not using
recommended hardware are not officially supported. 

Please note that the **Raspberry Pi Zero and Zero W are not recommended explicitly** since severe performance 
issues were observed, caused by the WiFi interface when bandwidth is utilized (e.g. the webcam is streamed), negatively 
impacting printing quality. [See also here](https://github.com/guysoft/OctoPi/issues/318#issuecomment-284762963). The Zero 2
however *is* recommended.

## Installing OctoPi

OctoPi is available through the [Raspberry Pi Imager](https://www.raspberrypi.org/software/), which you can use to download and setup OctoPi. You can install it yourself, or alternatively simply buy one of the available

<!--div class="text-center" style="margin-bottom: 1rem;">
    <a class="btn btn-large btn-block" href="/merch/#kits" data-analytics='"Merch Click", { "props": { "origin": "download"} }'>All-in-one OctoPrint Kits</a>
</div-->

### Installing OctoPi using the Raspberry Pi Imager

> 🤚 **Before you begin**
> 
> Read and follow these instructions **precisely**.

1. If you haven't already, **download and install [Raspberry Pi Imager](https://raspberrypi.org/software)** on your computer

2. **Find the OctoPi image** under "Choose OS", by selecting "Other Specific Purpose OS" > "3D printing" > "OctoPi" and then the "stable" version.

3. **Open advanced options** by clicking on the button with the gear, or by using the keyboard shortcut <code>ctrl</code>+<code>shift</code>+<code>x</code> and then:

   * **Configure your wifi options**: Set your SSID, password and WiFi country.
 
   * **Change the *system* password** in "Set username and password" by entering a new password to use for the system user "pi". This is *not* the password you'll use for logging into
     OctoPrint but one that you'll have to use to log into your Pi via SSH should you ever need to.
 
   * Optionally: Change the configured timezone in "Set locale settings"
 
   * Optionally: Change the hostname in "Set hostname"

   ![Advanced options, showing the "Set username and password" box ticked and a new password set, and showing the "Configure wireless LAN" box ticked and an SSID and Password set.](/assets/img/download/advanced-options.png)

4. **Install the image to your SD card**, then plug everything in to your Raspberry Pi and boot it up. **Do not format the SD card after installing, even if prompted to do so.** This will break the installation and you will have to start over!

5. **Access OctoPrint from your browser** via ``http://octopi.local`` or the hostname you 
   chose ([if your computer supports bonjour](https://learn.adafruit.com/bonjour-zeroconf-networking-for-windows-and-linux/overview)) 
   or ``http://<your pi's ip address>``. `https` is available too, with a self-signed certificate 
   (which means your browser will warn you about it being invalid - it isn't, it's just not recognized by your browser).

Please also refer to [OctoPi's README](https://github.com/guysoft/OctoPi), especially the ["How to use it" section](https://github.com/guysoft/OctoPi#how-to-use-it).

### Alternative Initial Setup

If you decide against using the Raspberry Pi Imager, here are some alternative steps to get started:

1. **Flash the image to your SD card** through whatever alternative means you've chosen.

2. With the SD card still attached to your computer, set up the Wifi connection using the `octopi-wpa-supplicant.txt` file
   on the root of the installed card when using it like a thumb drive. 
   **Important: Do not use WordPad (Windows) or TextEdit (MacOS X)**  for this, those editors are known to mangle
   the file, making configuration fail. Use something like Notepad++, Atom or VSCode instead or at the very 
   least heed the warnings in the file. If your computer doesn't see the card right away after flashing, try
   ejecting and inserting it again. **Do not format the SD card after installing, even if prompted to do so.** This will break the installation and you will have to start over!

   Please also refer take a look at the [full WiFi setup guide in the FAQ](https://faq.octoprint.org/wifi-setup) that also includes troubleshooting tips.

3. **Plug everything into your Raspberry Pi and boot it up**

4. **Log into your Pi via SSH** (it is located at ``octopi.local``
   [if your computer supports bonjour](https://learn.adafruit.com/bonjour-zeroconf-networking-for-windows-and-linux/overview)
   or the IP address assigned by your router), default username is `pi`, default password is `raspberry`.
   Run ``sudo raspi-config``. Once that is open:

   1. Change the password via "Change User Password"
   2. Optionally: Change the configured timezone via "Localization Options" > "Timezone".
   3. Optionally: Change the hostname via "Network Options" > "Hostname". Your OctoPi instance will then no longer be reachable under ``octopi.local`` but rather the hostname you chose postfixed with ``.local``, so keep that in mind.

   You can navigate in the menus using the arrow keys and <key>Enter</key>. To switch to selecting the buttons at the bottom use <key>Tab</key>.

   **You do not need to expand the filesystem**, current versions of OctoPi do this automatically.

   **You also do not need to manually enable the RaspiCam** if you have one, that is already taken care of on the image as well.

5. **Access OctoPrint** through ``http://octopi.local`` ([if your computer supports bonjour](https://learn.adafruit.com/bonjour-zeroconf-networking-for-windows-and-linux/overview)) 
   or ``http://<your pi's ip address>``. `https` is available too, with a self-signed certificate 
   (which means your browser will warn you about it being invalid - it isn't, it's just not recognized by your browser).

Please also refer to [OctoPi's README](https://github.com/guysoft/OctoPi), especially the ["How to use it" section](https://github.com/guysoft/OctoPi#how-to-use-it).

## Image Downloads

Raspberry Pi Imager will download the latest version of OctoPi for you, but if you want to download the images 
yourself you can do so here.

### Stable OctoPi

<div class="text-center">
    <a class="btn btn-large btn-primary btn-block" href="{{ site.data.octopi.latest.url }}" data-analytics='"Download Click", { "props": { "target": "latest"} }'>
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
    <a class="btn btn-large btn-block" href="{{ site.data.octopi.next_octoprint.url }}" data-analytics='"Download Click", { "props": { "target": "next_octoprint"} }'>
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
    <a class="btn btn-large btn-block" href="{{ site.data.octopi.next_octopi.url }}" data-analytics='"Download Click", { "props": { "target": "next_octopi"} }'>
      OctoPi&nbsp;{{ site.data.octopi.next_octopi.octopi_version }} &amp; OctoPrint&nbsp;{{ site.data.octopi.next_octopi.octoprint_version }}
    </a>
    <small><strong>{{ site.data.octopi.recommendation }}</strong></small><br>
    <small>Image compatible with Raspberry Pi {{ site.data.octopi.next_octopi.pi_models }}.</small><br>
</div>
{% endif %}

### OctoPi Nightlies

You can also get the [32bit nightlies here](https://unofficialpi.org/Distros/OctoPi/nightly/) or the [64bit nightlies here](https://unofficialpi.org/Distros/OctoPi/nightly-arm64/).


## Further resources

  * For customizing OctoPi, take a look at [CustoPiZer](https://github.com/OctoPrint/CustoPiZer).
  * Scripts to build the image yourself can be found in [OctoPi's Github repository](https://github.com/guysoft/OctoPi).

----

# Octo4a

[Filip Grzywok](https://github.com/feelfreelinux) maintains 
["Octo4a"](https://github.com/feelfreelinux/octo4a), an Android
app that allows you to use an Android based smart phone as an OctoPrint host. Root
is not required!

Check out the [Octo4a README](https://github.com/feelfreelinux/octo4a) for information on 
how to obtain the app, install and run it.

### Video

There's also a video guide on how to get Octo4a up and running by [Thomas Sanladerer](https://www.youtube.com/channel/UCb8Rde3uRL1ohROUVg46h1A).

{% include youtube.html vid="74xdib_-X38" %}

----

# OctoPrint for Orange Pi

The [people at Obico](https://www.obico.io/) maintains an image suitable for use with the Orange Pi Zero 2 and the Orange Pi 3. You can find it [here](https://www.obico.io/docs/user-guides/orange-pi-for-octoprint-download-setup/). Please report issues to Obico.

----

# Docker

There's also an official OctoPrint Docker image, `octoprint/octoprint`. It is maintained
by [Brian Vanderbush](https://github.com/LongLiveCHIEF) and team [on GitHub](https://github.com/OctoPrint/octoprint-docker).

Please refer to its entry [on dockerhub](https://hub.docker.com/r/octoprint/octoprint) for
more details on usage and configuration.

----

# octoprint_deploy (Linux)

[octoprint_deploy](https://github.com/paukstelis/octoprint_deploy) is a guided script for installing OctoPrint and additional tools (video streamer, haproxy) on virtually any Linux system. It guides the user through creation of one or more OctoPrint instances. Creating multiple instances with the script allows control of multiple printers on a single piece of hardware. A variety of utilities improve the multi-instance experience, including automated creation of udev rules, syncing users between instances, and sharing file uploads between instances. It is compatible with OctoPi.

Maintained by [Paul Paukstelis](https://github.com/paukstelis).

----

# Windows Installer

[OctoPrint-WindowsInstaller](https://github.com/jneilliii/OctoPrint-WindowsInstaller) is a Windows installation wizard for OctoPrint. It
is maintained by [jneilliii](https://github.com/jneilliii). Please report issues [here](https://github.com/jneilliii/OctoPrint-WindowsInstaller/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc).

----

#  Installing manually

The generic setup instructions boil down to

1. Installing [Python 3](https://www.python.org/) (version 3.10 or lower), including [pip](https://pip.pypa.io/en/latest/installing.html).
2. Creating a virtual environment somewhere: `python -m venv OctoPrint`
3. Installing OctoPrint *into that virtual environment*: `OctoPrint/bin/pip install OctoPrint`
4. OctoPrint may then be started through `./OctoPrint/bin/octoprint serve` or with an absolute path `/path/to/OctoPrint/bin/octoprint serve`

More specific setup instructions for the most common runtime environments can be found below.

##  Linux

For installing OctoPrint on Linux, please take a look at [the setup instructions for Raspbian on the forum](https://community.octoprint.org/t/setting-up-octoprint-on-a-raspberry-pi-running-raspbian/2337/).
They should be pretty much identical on other Linux distributions. See <a href="#octoprint_install--octoprint_deploy-linux">octoprint_install & octoprint_deploy (Linux)</a> above for simplified scripted options.

##  Windows

For installing the OctoPrint server on a Windows system, please take a look at [the setup instructions for Windows on the forum](https://community.octoprint.org/t/setting-up-octoprint-on-windows/383/1).

## Mac

For installing the OctoPrint server on a Mac, please take a look at [the setup instructions for MacOS on the forum](https://community.octoprint.org/t/setting-up-octoprint-on-macos/13425).
