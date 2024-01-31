---

layout: post-rc
title: 'New release candidate: 1.10.0rc1'
author: foosel
date: 2024-01-31 18:00:00 +0100
card: /assets/img/blog/2024-01/2024-01-31-octoprint-1.10.0rc1-card.png
featuredimage: /assets/img/blog/2024-01/2024-01-31-octoprint-1.10.0rc1-card.png
poster: /assets/img/blog/2024-01/2024-01-31-octoprint-1.10.0rc1-poster.png
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
excerpt: The first release candidate for the upcoming 1.10.0 release containing new features, improvements & bug fixes!

release: 1.10.0rc1
channel: Maintenance RCs
feedback: 4938

closer_look:
- Proper behaviour when using the included web interface as well as any third party clients at your disposal.
- User and group management functioning as expected.
- Plugin installation functioning as expected.
- Application key management functioning as expected. Authentication workflow with third party clients at your disposal (e.g. slicers) works as it should.

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
- jatin-47
- kaenguruhs
- mad73923
- mintsoft
- neod123

---

Welcome to 2024! Today I'm happy to present to you the first release candidate of the upcoming 1.10.0 release. 

As always with a new minor version that brings not only bug and security fixes but also improvements and whole new features, the [changelog](https://github.com/OctoPrint/OctoPrint/releases/tag/1.10.0rc1) has grown quite large. I've done my best to make it a bit more readable by introducing some sub sections. 

But let's still take a look at some of the highlights, shall we?

* OctoPrint now has **achievements**! The new bundled Achievements Plugin will now internally record some instance stats and monitor some events and based on that give out various achievements. This version contains 36 achievements, 22 of which are hidden and for you to be discovered. Additionally, the instance stats are also being recorded per year to make it possible in the future to give you some yearly stats overview of your OctoPrint and printing use. Be sure to check out the screenshots below!
* We got some huge **performance improvements** thanks to refactoring of the internal settings data structure and making the Tornado WSGI interface run multi-threaded. What this means for you is that OctoPrint's web interface should now load significantly faster!
* A new **firmware error dialog** has been added that gets displayed when the printer reports an unrecoverable error, containing the error message, what happened due to that error (print cancellation, disconnect), if available a link to an FAQ entry, the last lines of communication and a big reminder that printer errors are printer errors and not OctoPrint's fault. For an example, [take a look here](#image-4) The dialog will be automatically opened on connected clients, however it can also be accessed later by clicking on the new error icon added to the printer state panel. This will hopefully help all of you in the future to better understand what happened when your printer suddenly stopped printing, and where to start looking for a solution.
* The **system info bundle** now contains a new section with information supplied by your printer's response to `M115`, enabling people helping you with issues you seek help with to better understand your printer's capabilities and firmware version, allowing them to better help you. Additionally, the abridged version of the bundle can no longer be mistakenly provided instead of the full bundle zip - it has been removed from the system info bundle page unless a debugging parameter is supplied.
* The **temperature graph** has gotten some love: The x axis is now always scaled to the last 30 minutes (or whatever cut-off interval you have configured), so things should no longer jump around right after connecting, target temperatures lines are now dashed to allow them to be better distinguished from the actual temperatures by more than just color (thank you [@mintsoft](https://github.com/mintsoft)!), and two new markers have been added to the graph to indicate when the printer got connected and disconnected again. See all of that in action [in this screenshot](#image-5).
* OctoPrint now supports **Python 3.12**.
* A new **reauthentication dialog** will now pop up when you haven't entered your password in the past five minutes and are attempting to perform a potentially dangerous action (e.g. installing a plugin, adding a new user, etc) - [see here how that looks](#image-6). This also mitigates a moderate security issue responsibly disclosed by [Timothy "TK" Ruppert](https://github.com/tkruppert) and further tracked in [CVE-2024-23637](https://nvd.nist.gov/vuln/detail/CVE-2024-23637).
* Several bugs have been fixed, including hardening the temperature offset code against empty temperature commands inside GCODE files, some regressions, an error when attempting to set a custom logging level under certain circumstances, folder sorting by date of last print, and more.
* ... and even more.
