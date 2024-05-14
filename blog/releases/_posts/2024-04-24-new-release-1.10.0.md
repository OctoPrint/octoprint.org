---
layout: post-release
title: 'New release: 1.10.0'
author: foosel
date: 2024-04-24 13:15:00 +0200
card: /assets/img/blog/2024-04/2024-04-24-octoprint-1.10.0-card.png
featuredimage: /assets/img/blog/2024-04/2024-04-24-octoprint-1.10.0-card.png
poster: /assets/img/blog/2024-04/2024-04-24-octoprint-1.10.0-poster.png
images:
- url: /assets/img/blog/2024-01/2024-01-31-screenshot-achievements-list.png
  title: OctoPrint's new achievements list, giving an overview of the available (and not hidden) achievements and their unlock status.
- url: /assets/img/blog/2024-01/2024-01-31-screenshot-achievement.png
  title: An achievement notification, in this case for the "Mass Production" achievement.
- url: /assets/img/blog/2024-01/2024-01-31-screenshot-instance-stats.png
  title: OctoPrint's new instance stats overview, showing information on when stats collection started and with what version, how many versions have been seen, number of server starts, print count, total print duration and longest print recorded so far.
- url: /assets/img/blog/2024-01/2024-01-31-screenshot-firmware-error-dialog.png
  title: An example of the new firmware error dialog. 
- url: /assets/img/blog/2024-01/2024-01-31-screenshot-temperature-graph.png
  title: The temperature graph with the new markers, dashed target temperature lines and the new x axis scaling.
- url: /assets/img/blog/2024-01/2024-01-31-screenshot-reauthentication.png
  title: The reauthentication dialog, in this case triggered by an attempt to install a plugin, asking to re-enter the password.

excerpt: "Ten months in development, followed by close to three months of an RC phase, it's finally time to push out 1.10.0!"

release: "1.10.0"

headsups:
- title: "Heads-up: You will now be expected to re-enter your password on critical operations"
  content: |
    This version of OctoPrint requires you to reauthenticate with your password every five minutes on various critical operations you might do on your installation, e.g. adding, changing and deleting users, adding, changing and deleting groups, installing plugins, revealing the deprecated global API key, generating, revoking, revealing and granting application keys, accessing the recovery page and downloading or restoring backups. This change matches best practices with regards to security of web applications and was done in order to protect you from various potential attack vectors. 
    
    If you do not want this reauthentication requirement, you can find information on how to disable it in the [configuration docs](https://docs.octoprint.org/en/master/configuration/config_yaml.html#access-control). Be aware though that by doing so you'll negatively impact your installation's security!

- title: "Heads-up: Slow update if your Pi is still running pip <= 20.3 (e.g. as shipped on early OctoPi 0.18 preview versions)"
  content: |
    During the release candidate phase we found that if your OctoPrint installation still is using a `pip` version below 20.3, updating to this version will take slightly longer than usual due to having to compile a third party dependency that got updated (`zeroconf`), as these ancient `pip` versions are not fetching the precompiled version from piwheels in this scenario. If you are affected, plan ahead accordingly and allow some time for the update or alternatively update pip (you can do that via the Software Update plugin's settings). Most of you however should not be affected by this at all. If you are not running a prerelease version of OctoPi 0.18.0 (the stable release of 0.18.0 is fine!), you are likely not affected by this. 

known_issues:
- issue: 4952
  content: |
    Upload of multiple files is impossible if SD support is disabled. Keep SD support enabled for now if you want to upload more than one file at once via the web UI.
- issue: 4975
  content: |
    Reserved identifiers in the temperature reports from the printer lead to a warning getting logged each time instead of just once, which can increase the log file with broken firmware implementations. Avoid firmware reporting reserved identifiers, e.g. reporting a chamber temperature while also marking a chamber as not available as observed on current Prusa XL firmware builds.
- issue: 4993
  content: |
    A bug in the GCODE analyser implementation can cause the server to get blocked if a lot of files need to get analysed at once during startup or due to a bulk upload. For now it is strongly suggested to limit the amount of freshly added files to a max of 10 at once and/or be aware of the server being very busy for a few minutes after larger numbers of added files."

contributors:
- 0r31
- bigfoxtail
- CMR-DEV
- cociweb
- cperrin88
- credomane
- crysxd
- danielkucera
- dawidpieper
- eumiro
- evanwurden
- hynek
- jacopotediosi
- jatin-47
- jneilliii 
- kaenguruhs
- mad73923
- max246
- MichaIng
- mintsoft
- neod123
- thinkyhead

first_time_contributors:
- bigfoxtail
- CMD-DEV
- cociweb
- cperrin88
- credomane
- danielkucera
- evanwurden
- hynek
- jacopotediosi
- jatin-47
- kaenguruhs
- mad73923
- mintsoft
- neod123

security:
- '[Timothy "TK" Ruppert](https://github.com/tkruppert)'
- "[Jacopo Tediosi](https://github.com/jacopotediosi)"

testers:
- b-morgan
- ChrisHeerschap
- ckuethe
- cp2004
- fredrikbaberg
- j7126
- jneilliii
- JohnOCFII
- larp-welt
- nastevens
- sarusani
- sclebo05
- tigercjn
- TLMcNulty
- tostr7191
- trunzoc
- wilmardo

stats:
  instancegraph: /assets/img/blog/2024-04/2024-04-24-rc-instances.png
  printtimegraph: /assets/img/blog/2024-04/2024-04-24-rc-prints.png
  piecharts: /assets/img/blog/2024-04/2024-04-24-rc-piecharts.png
  totalinstances: 2080
  totalprinttime: 61405
  rcs:
  - tag: 1.10.0rc3
    date: 2024-03-18
    instances: 701
    printtime: 18263
  - tag: 1.10.0rc4
    date: 2024-04-08
    instances: 617
    printtime: 10416
  rcs_incomplete:
  - tag: 1.10.0rc1
    date: 2024-01-31
    instances: 840
    printtime: 13052
  - tag: 1.10.0rc2
    date: 2024-02-12
    instances: 1480
    printtime: 26986
---

After a ten month long development phase overshadowed by a [funding crisis](/blog/2023/10/26/we-need-to-talk-about-funding/) and followed by an almost three month long RC phase with four release candidates, I'm happy to finally present to you the 1.10.0 release of OctoPrint!

Like every single release (and release candidate) of OctoPrint ever since 2016, this release was made possible only through your continued **[support of my work](/support-octoprint/)** 💕

As always with a new minor version that brings not only bug and security fixes but also improvements and whole new features, the [changelog](https://github.com/OctoPrint/OctoPrint/releases/tag/1.10.0) has grown quite large. I've done my best to make it even more readable compared to prior ones by further sub categories.

But let's still take a look at some of the highlights, shall we?

- OctoPrint now has **achievements**! The new bundled Achievements Plugin will now internally record some instance stats and monitor some events and based on that give out various achievements. This version contains 36 achievements, 22 of which are hidden and for you to be discovered. Additionally, the instance stats are also being recorded per year to make it possible in the future to give you some yearly stats overview of your OctoPrint and printing use. Be sure to check out the screenshots below!

  Unlocked achievements are also tracked via the [Anonymous Usage Tracking](https://tracking.octoprint.org). Of course, this can be disabled, and if you have not opted into tracking in the first place, nothing will be tracked, as always. Achievement stats are available on [data.octoprint.org](https://data.octoprint.org/#achievements).

  Since this question came up during the release candidate phase: The goal of these achievements is not to gamify OctoPrint, but rather to give you something fun while also making it more visible how this project is funded and how you can help, as that info is part of some of the achievements. 
  
  If you are not interested in achievements, just disable the bundled Achievements plugin via the plugin manager.

- We got some huge **performance improvements** thanks to refactoring of the internal settings data structure and making the Tornado WSGI interface run multi-threaded. What this means for you is that OctoPrint's web interface should now load significantly faster!

- A new **firmware error dialog** has been added that gets displayed when the printer reports an unrecoverable error, containing the error message, what happened due to that error (print cancellation, disconnect), if available a link to an FAQ entry, the last lines of communication and a big reminder that printer errors are printer errors and not OctoPrint's fault. For an example, [take a look here](#image-4). 
  
  The dialog will be automatically opened on connected clients, however it can also be accessed later by clicking on the new error icon added to the printer state panel. This will hopefully help all of you in the future to better understand what happened when your printer suddenly stopped printing, and where to start looking for a solution.

- The **system info bundle** now contains a new section with information supplied by your printer's response to `M115`, enabling people helping you with issues you seek help with to better understand your printer's capabilities and firmware version, allowing them to better help you. Additionally, the abridged version of the bundle can no longer be mistakenly provided instead of the full bundle zip - it has been removed from the system info bundle page unless a debugging parameter is supplied.

- The **temperature graph** has gotten some love: The x axis is now always scaled to the last 30 minutes (or whatever cut-off interval you have configured), so things should no longer jump around right after connecting, target temperatures lines are now dashed to allow them to be better distinguished from the actual temperatures by more than just color (thank you [@mintsoft](https://github.com/mintsoft)!), and two new markers have been added to the graph to indicate when the printer got connected and disconnected again. See all of that in action [in this screenshot](#image-5).

- OctoPrint now supports **Python 3.12**.

- A new **reauthentication dialog** will now pop up when you haven't entered your password in the past five minutes and are attempting to perform a potentially dangerous action (e.g. installing a plugin, adding a new user, etc) - [see here how that looks](#image-6). This also mitigates a moderate security issue responsibly disclosed by [@tkruppert](https://github.com/tkruppert) and further tracked in [CVE-2024-23637](https://nvd.nist.gov/vuln/detail/CVE-2024-23637).

- It is no longer possible to abuse the **webcam snapshot URL** for XSS attacks. The URL is now properly escaped and no longer allows for arbitrary JavaScript execution. This mitigates a moderate security issue responsibly disclosed by [@jacopotediosi](https://github.com/jacopotediosi) and further tracked in [CVE-2024-28237](https://nvd.nist.gov/vuln/detail/CVE-2024-28237).

- Several bugs have been fixed, including hardening the temperature offset code against empty temperature commands inside GCODE files, some regressions, an error when attempting to set a custom logging level under certain circumstances, folder sorting by date of last print, and more.

- ... and even more.
