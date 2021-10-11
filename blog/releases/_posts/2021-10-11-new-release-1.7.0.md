---
layout: post-release
title: 'New release: 1.7.0'
author: foosel
date: 2021-10-11 16:00:00 +0200
card: /assets/img/blog/2021-10/2021-10-11-octoprint-1.7.0-card.png
featuredimage: /assets/img/blog/2021-10/2021-10-11-octoprint-1.7.0-card.png
poster: /assets/img/blog/2021-10/2021-10-11-octoprint-1.7.0-poster.png
images:
- url: /assets/img/blog/2021-08/2021-08-04-screenie-eventmgr.png
  title: The new bundled Event Manager plugin, courtesy of @jneilliii, makes it easy to manage event subscriptions.
- url: /assets/img/blog/2021-08/2021-08-04-screenie-updatelog.png
  title: The update log in the Software Update plugin gives you a track log of all the updates you applied or tried to apply.
- url: /assets/img/blog/2021-08/2021-08-04-screenie-python2warning.png
  title: With Python 2.7 being EOL since January 1st 2020 now, a new warning popup will remind you to finally upgrade.
- url: /assets/img/blog/2021-08/2021-08-04-screenie-logcoloring.png
  title: On the command line, OctoPrint's output will now be colored according to the log level.

excerpt: "After over 5 months of development and a two month long RC phase, I'm proud to present you OctoPrint 1.7.0!"

release: "1.7.0"

headsups:
- title: "Heads-up for anyone still on OctoPi 0.15.0 or 0.15.1"
  content: >
    OctoPrint 1.7.0 is the final release that will allow updating through the 
    built in Software Update plugin. The Python environment on OctoPi 0.15.* has now 
    become so ancient that the overhead of keeping on supporting it is no longer 
    sustainable, and the likelihood of spontaneous breakage has increased significantly.


    If you are one of the ~5% of users still on OctoPi 0.15, create a backup of your 
    OctoPrint data, flash the latest OctoPrint 0.18 to ideally a fresh SD card (they age 
    too...) and restore from backup. That should get you up and running under a *current* 
    OctoPi release in no time and additionally migrate you to Python 3.

- title: "Heads-up for anyone still on Python 2"
  content: > 
    I'll do my very best to keep OctoPrint functional under Python 2 until the release of OctoPrint 2.0.0, however Python 2.7 has been EOL now for almost two years, a lot of third party libraries are releasing updates for Python 3 only at this point, and many plugin authors for OctoPrint do so as well.


    It is time to upgrade, and so OctoPrint 1.7.0 will now show you a pop-up about that fact when you open the UI. You do not have to act, but it is strongly recommended you do if you don't want to be left behind, and the pop-up will also tell you [how to update](https://faq.octoprint.org/python3-update):


    ![With Python 2.7 being EOL since January 1st 2020 now, a new warning popup will remind you to finally upgrade.](/assets/img/blog/2021-08/2021-08-04-screenie-python2warning.png)


    Please do, the less Python 2 users are out there I still have to support, the more time I have for moving towards 2.0.

- title: "Heads-up for plugin authors: `octoprint.util.get_free_bytes` has been removed"
  content: >
    The utility function `octoprint.util.get_free_bytes`, now deprecated since version 
    1.2.5 in favor of `psutil.disk_usage`, has finally been removed. If for *any* reason 
    you've been using this in your third party plugin, ignoring the deprecation warning 
    OctoPrint has been printing out to the log since 2015, now is the time to finally 
    fix things.

contributors:
- apbarratt
- cp2004
- eltonlaw
- eyal0
- ianwiltdotcom
- jneilliii
- jugmac00
- kantlivelong
- LazeMSS
- ldursw
- oliof
- sparxooo
- StevilKnevil
- TwoRedCells

testers:
- AndroidCloned
- Andy-ABTec
- b-morgan
- ChrisHeerschap
- cmock
- cp2004
- donb55
- gbickel1
- jneilliii
- JohnOCFII
- kazibole
- loskexos
- MangaValk
- mild-lemon
- mod38
- Onejk1
- Phydam
- Reperiel
- sticilface
- SwgDad99
- Taomyn
- The-EG

stats:
  instancegraph: /assets/img/blog/2021-10/2021-10-11-rc-instances.png
  printtimegraph: /assets/img/blog/2021-10/2021-10-11-rc-prints.png
  piecharts: /assets/img/blog/2021-10/2021-10-11-rc-piecharts.png
  totalinstances: 1976
  totalprinttime: 112267
  rcs:
  - tag: 1.7.0rc2
    date: 2021-08-11
    instances: 1366
    printtime: 63900
  - tag: 1.7.0rc3
    date: 2021-09-13
    instances: 1330
    printtime: 45200
  rcs_incomplete:
  - tag: 1.7.0rc1
    date: 2021-08-04

---

Thanks to a vacation and a surgery, this was one of the longest Release Candidate phases
so far, spanning from August 4th until now. Thus I'm extra happy to *finally* present you with 1.7.0 
today! 🥳

Like every single release (and release candidate) of OctoPrint ever since 2016 this
release was made possible only through your continued **[support of my work](/support-octoprint/)** 💕

The [full changelog](https://github.com/OctoPrint/OctoPrint/releases/tag/1.7.0) contains
a long list of new features, improvements and bug fixes, but here are
some of the highlights:

* Added support for the `EXTENDED_M20` firmware capability. If detected, OctoPrint will 
  now send `M20 L` instead of plain `M20` requests to firmwares, to allow immediate fetch 
  of long names. Quoted long names, as apparently sent by some firmwares even though there 
  was never a mention of that during the initial feature discussions, are also supported now.
* Thanks to [@jneilliii](https://github.com/jneilliii) there's a new bundled plugin 
  "Event Manager" for managing [event subscriptions](https://docs.octoprint.org/en/master/events/index.html#configuration) 
  via the UI.
* Made the system info bundle more visible. Many users are still copy/pasting the textual 
  system info dump and forget to share the bundle. So the request was rephrased to target 
  the bundle and the textual info dump was hidden behind a "More" area. Also, the bundle 
  viewer has been linked.
* [@cp2004](https://gitnhub.com/cp2004) did some magic and improved the animation performance 
  across all modals in the UI.
* The Software Update Plugin now sports an update log with a link to the associated release notes. 
  You will now be able to see the update events of the past 30d right from within the 
  Software Update settings in case you need to debug something. The update log will also 
  be shared into the system info bundle.
* The Software Update Plugin will also now prompt for an update of OctoPrint during first
  time setup if there's a new version available, before any other settings.
* If still running under Python 2, OctoPrint will now show a notification linking to 
  update instructions to Python 3 on page reload/connection to the backend.
* Added tracking of user agent string via new tracking event `webui_load`. This will allow
  making more informed development decisions with regards to frontend development.
* OctoPrint's console output will now be colored based on log severity.
* Various fixes like fixing a non deterministic sorting behaviour and working around an arc
  rendering bug in Chrome, fixing some inconsistencies, typos and wordings and so on.
* ... and even more.
