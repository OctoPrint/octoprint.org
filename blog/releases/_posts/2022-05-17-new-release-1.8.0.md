---
layout: post-release
title: 'New release: 1.8.0'
author: foosel
date: 2022-05-17 13:15:00 +0200
card: /assets/img/blog/2022-05/2022-05-17-octoprint-1.8.0-card.png
featuredimage: /assets/img/blog/2022-05/2022-05-17-octoprint-1.8.0-card.png
poster: /assets/img/blog/2022-05/2022-05-17-octoprint-1.8.0-poster.png
images:
- url: /assets/img/blog/2022-03/2022-03-14-screenie-temperature-markers.png
  title: The temperature graph can now show markers for print events. This was contributed by @surdu.
- url: /assets/img/blog/2022-03/2022-03-14-screenie-update-queue.png
  title: While printing you will be able to enqueue updates to be done after the print job finishes. Thanks to @jneilliii!
- url: /assets/img/blog/2022-03/2022-03-14-screenie-bulk-plugin.png
  title: The Plugin Manager now allows to enable and disable several plugins in bulk.
- url: /assets/img/blog/2022-03/2022-03-14-screenie-no-serial.png
  title: If no serial port is detected in the system, OctoPrint will now state that and link to the FAQ entry on the matter.
- url: /assets/img/blog/2022-03/2022-03-14-screenie-timelapse-thumbnails.png
  title: Timelapse recordings now also have thumbnails, thanks to the work of @crysxd!

excerpt: "After over 5 months of development and a two month long RC phase, I'm proud to present you OctoPrint 1.8.0!"

release: "1.8.0"

headsups:
- title: "OctoPrint 1.8.0 drops Python 2 support!"
  content: >
    As previously announced [on the OctoBlog](https://octoprint.org/blog/2022/01/31/octoprint-1.8.0-will-require-python-3/) and in [OctoPrint On Air #43](https://www.youtube.com/watch?v=a3lnYw8_87U&t=507s), OctoPrint 1.8.0 drops Python 2 support. In order to be able to install/update to it, you *need* to be running OctoPrint under Python 3 already, e.g. as shipped on OctoPi 0.18.0. Installing on Python 2 will fail. The Software Updater will also be redirected to a new [OctoPrint Legacy repository](https://github.com/OctoPrint/OctoPrint-Legacy) for checking for OctoPrint updates if it detects that you are still running Python 2. As outlined in the blog post and the vlog, there are no more updates for OctoPrint 1.7/Python 2 planned. Update now or you will be left behind, including for most security fixes!


    If you are unsure what version of Python your OctoPrint instance is running under, open the web interface and look into the lower left corner where it will tell you:


    ![image](https://user-images.githubusercontent.com/83657/156207787-5e101031-6c3c-446c-85fe-5834d6d290bb.png)


    [This is also covered in the FAQ](https://community.octoprint.org/t/41764).

- title: "OctoPrint 1.8.0 fixes some reported security issues, update ASAP!"
  content: > 
    While OctoPrint 1.8.0rc5 was undergoing testing, three security vulnerabilities were disclosed to me. These issues are fixed in the stable release of 1.8.0. Since these vulnerabilities are of low concern for instances that are not publicly exposed on the internet or other hostile networks, as strongly recommended, the fixes will *not* be backported to OctoPrint 1.7.x and thus instances still under Python 2.


    Please update your OctoPrint instance to the latest stable version of OctoPrint 1.8.0 as soon as possible.

- title: "Heads-up for plugin authors"
  content: >
    There are a bunch of heads-ups for plugin authors regarding deprecated functionality and
    important clarifications of functionality. Please check them out [in the release notes](https://github.com/OctoPrint/OctoPrint/releases/tag/1.8.0).

contributors:
- adamwolf
- ademuri
- cp2004
- crysxd
- DShenkle
- flaviut
- gdombiak
- GonzoDMX
- jneilliii
- johnboiles
- JoveToo
- kantlivelong
- kohend
- LazeMSS
- MartijnBraam
- NilsRo
- OllisGit
- pR0Ps
- QuinnDamerell
- rooterkyberian
- Rotzbua
- surdu
- synman
- The-EG
- thelastWallE
- TylonHH
- vector76

testers:
- 1n5aN1aC
- AndKe
- avandeputte
- b-morgan
- ChrisHeerschap
- ckuethe
- cp2004
- Cpat39
- Crowlord
- fcchambers
- goeland86
- Guilouz
- jneilliii
- JohnOCFII
- mod38
- oliof
- pingywon

security:
- "[rajbabai8](https://huntr.dev/users/rajbabai8)"

stats:
  instancegraph: /assets/img/blog/2022-05/2022-05-17-rc-instances.png
  printtimegraph: /assets/img/blog/2022-05/2022-05-17-rc-prints.png
  piecharts: /assets/img/blog/2022-05/2022-05-17-rc-piecharts.png
  totalinstances: 2147
  totalprinttime: 117080
  rcs:
  - tag: 1.8.0rc2
    date: 2022-03-16
    instances: 1064
    printtime: 27853
  - tag: 1.8.0rc3
    date: 2022-03-29
    instances: 808
    printtime: 16195
  - tag: 1.8.0rc4
    date: 2022-04-05
    instances: 833
    printtime: 14239
  - tag: 1.8.0rc5
    date: 2022-04-12
    instances: 1489
    printtime: 56103
  rcs_incomplete:
  - tag: 1.8.0rc1
    date: 2022-03-14

---

This has been an extra stressful year so far, and thus it took me a while to get this release
finalized and shipped. Thank you for your patience, and I'm glad I can finally present you all
with OctoPrint 1.8.0! 

Like every single release (and release candidate) of OctoPrint ever since 2016, this
release was made possible only through your continued **[support of my work](/support-octoprint/)** 💕

The [full changelog](https://github.com/OctoPrint/OctoPrint/releases/tag/1.8.0) contains
a long list of new features, improvements and bug fixes. Before we come to the highlights,
let me first get some big announcements out of the way (that are also included in the
heads-ups below!):

* The biggest announcement is probably that with the 1.8.0 release **OctoPrint is dropping Python 2 support**.
  I already wrote about this in a [past post here](/blog/2022/01/31/octoprint-1.8.0-will-require-python-3/), and this is now the first release that 
  is Python 3 exclusive. As of the publication of the first release candidate 1.8.0rc1, any OctoPrint instances
  still on Python 2 have already been redirected to the legacy repository for update checks and thus will also
  no longer be able to partake in future updates - which they wouldn't anyway as the code base
  has already been migrated to be Python 3 exclusive, removing all the workarounds so painstakingly
  put in over the past three years.
* **Three security vulnerabilities were fixed** that were disclosed to me while the final release candidate was undergoing testing.
  We are looking at two cross-site scripting issues and one open redirect that could have been used to steal login credentials if successfully executed. In order
  to successfully exploit these vulnerabilities, an attacker would have had to identify the admin of a vulnerable instance found somewhere on the public internet or another hostile network
  and target them with a malicious link or social engineering to
  configure a malicious webcam stream URL. These issues are now fixed in 1.8.0 stable, and as such, once you have updated your OctoPrint instance to 1.8.0
  you should no longer be potentially exposed to these issues.

  Let me once again reiterate that **you should *never* expose your OctoPrint directly on the public internet**, thinking it would not be found
  by anyone. There are search engines that constantly scan and index the entire internet for arbitrary IP addresses coming online, and those can be used
  to find your OctoPrint instance. If you keep your OctoPrint instance restricted to your LAN, a cloud connection or a VPN, you greatly reduce the likelihood
  of this or any future vulnerabilities to even remotely affect you. [Here's a great post about *safe* remote access to OctoPrint](https://octoprint.org/blog/2018/09/03/safe-remote-access/)
  for you to read.

With that covered, let's get to the highlights:

* The temperature tab now has (optional) **event markers** for when a print gets started, paused, resumed, cancelled or finishes. Big thanks to @surdu!
* You may now **enqueue software updates** while a print is ongoing. They will then be started (after a short countdown) after successful completion of the print, or manually if you cancelled the print. You can manage the queue during the print to remove items you don't want to be enqueued after all, or add additional items to it. This was contributed by @jneilliii!
* It's now possible to **bulk enable/disable plugins**. This makes it easier for the user to locate plugins that are causing problems in the system.
* This release adds the first version of **embedding WebRTC based webcams**. Please note that this should be considered beta and is still subject to change while further work and research is being done on the backend side of things. @johnboiles did most of the legwork on this!
* OctoPrint will now show a **heads-up notice if no serial ports are detected**, with a link to the relevant [FAQ entry](https://community.octoprint.org/t/octoprint-cant-connect-to-my-printer/223). That will hopefully make it easier to spot if the printer is not physically connected or unsupported.
* **Thumbnails for the timelapse recordings** will now be generated automatically and displayed in the UI. There's also a command-line tool for generating thumbnails for the existing recordings. A fancy new feature contributed by @crysxd!
* The **GCode Viewer's memory usage has been improved** by @JoveToo and @cp2004 by switching out the underlying data structure and hunting down some bottlenecks. This means you should now be able to display larger GCode files before running into issues.
* **Performance of settings access has been greatly improved** as well, by refactoring the code to use a more efficient data structure. This was some heavy collaboration with @flaviut!
* Third-party clients can now **authenticate with OctoPrint through the Application Key plugin's fancy new auth dialog** instead of having to direct the user to the more heavyweight full UI.
* An **encoding issue was solved** that was observed against the latest versions of `pip`.
* ... and even more.
