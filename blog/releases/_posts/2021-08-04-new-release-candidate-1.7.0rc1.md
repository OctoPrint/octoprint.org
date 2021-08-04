---

layout: post-rc
title: 'New release candidate: 1.7.0rc1'
author: foosel
date: 2021-08-04 15:15:00 +0200
card: /assets/img/blog/2021-08/2021-08-04-octoprint-1.7.0rc1-card.png
featuredimage: /assets/img/blog/2021-08/2021-08-04-octoprint-1.7.0rc1-card.png
poster: /assets/img/blog/2021-08/2021-08-04-octoprint-1.7.0rc1-poster.png
images:
- url: /assets/img/blog/2021-08/2021-08-04-screenie-eventmgr.png
  title: The new bundled Event Manager plugin, courtesy of @jneilliii, makes it easy to manage event subscriptions.
- url: /assets/img/blog/2021-08/2021-08-04-screenie-updatelog.png
  title: The update log in the Software Update plugin gives you a track log of all the updates you applied or tried to apply.
- url: /assets/img/blog/2021-08/2021-08-04-screenie-python2warning.png
  title: With Python 2.7 being EOL since January 1st 2020 now, a new warning popup will remind you to finally upgrade.
- url: /assets/img/blog/2021-08/2021-08-04-screenie-logcoloring.png
  title: On the command line, OctoPrint's output will now be colored according to the log level.
excerpt: The first release candidate for the upcoming 1.7.0 release, containing new features, improvements and bug fixes.

release: 1.7.0rc1
channel: Maintenance RCs
feedback: 4201

headsups:
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
- iawiltdotcom
- jneilliii
- jugmac00
- kantlivelong
- LazeMSS
- ldursw
- oliof
- sparxooo
- StevilKnevil
- TwoRedCells

---

I hope you are having a nice summer, even though we are still in the middle of a pandemic.
The last weeks here in OctoPrint HQ aka my office have been primarily spent on working on
what is going to be 2.0.0, however there was also a significant amount of work that went
into the next minor release, and thus I'm excited to share with you the first 1.7.0 release candidate
today!

As always, there are quite a number of improvements and fixes in this one. How about we
take a look at some of the highlights from the [changelog](https://github.com/OctoPrint/OctoPrint/releases/tag/1.7.0rc1) together?


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