---

layout: post-rc
title: 'New release candidate: 1.8.0rc1'
author: foosel
date: 2022-03-14 12:15:00 +0100
card: /assets/img/blog/2022-03/2022-03-14-octoprint-1.8.0rc1-card.png
featuredimage: /assets/img/blog/2022-03/2022-03-14-octoprint-1.8.0rc1-card.png
poster: /assets/img/blog/2022-03/2022-03-14-octoprint-1.8.0rc1-poster.png
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
excerpt: The first release candidate for the upcoming 1.8.0 release, containing new features, improvements, bug fixes and dropping Python 2 support!

release: 1.8.0rc1
channel: Maintenance RCs
feedback: 4452

headsups:
- title: "Heads-up: OctoPrint 1.8.0 drops Python 2 support!"
  content: |
    As previously announced [on the OctoBlog](https://octoprint.org/blog/2022/01/31/octoprint-1.8.0-will-require-python-3/) and in [OctoPrint On Air #43](https://www.youtube.com/watch?v=a3lnYw8_87U&t=507s), OctoPrint 1.8.0     drops Python 2 support. In order to be able to install/update to it, you *need* to be running OctoPrint under Python 3 already, e.g. as shipped on OctoPi 0.18.0. Installing on Python 2 will fail. The Software Updater     will also be redirected to a new [OctoPrint Legacy repository](https://github.com/OctoPrint/OctoPrint-Legacy) for checking for OctoPrint updates if it detects that you are still running Python 2. As outlined in the blog     post and the vlog, there are no more updates for OctoPrint 1.7/Python 2 planned. Update now or you will be left behind. 
    
    If you are unsure what version of Python your OctoPrint instance is running under, open the web interface and look into the lower left corner where it will tell you:
    
    ![image](https://user-images.githubusercontent.com/83657/156207787-5e101031-6c3c-446c-85fe-5834d6d290bb.png)
    
    [This is also covered in the FAQ](https://community.octoprint.org/t/41764).
- title: "Heads-up for plugin authors: Importing Jinja2 templates from another plugin without an explicit prefix is now deprecated!"
  content: |
    OctoPrint so far allowed (erroneously) to replace plugin templates of the same name in another plugin, depending on loading order. Fixing this required to create prefixes for templates of plugins. Relative imports (think `{% include "snippets/my_snippet.jinja2" %}`) will now attempt to resolve against the current plugin. If that isn't possible, *for now* it will also be attempted to resolve globally against all registered templates and if a match is found, a deprecation will be logged. The latter behaviour will be removed in a future version of OctoPrint and *if* your plugin includes templates from other plugins you should now change it to using plugin prefixes if running on OctoPrint 1.8.0 or higher. Plugin prefixes are `plugin_<plugin identifier>/`, so for example, to include the settings pane of the bundled software update plugin, you'd now need to use `plugin_softwareupdate/plugin_softwareupdate_settings.jinja2`.
- title: "Heads-up for plugin authors: `octoprint.util.bom_aware_open` is now deprecated and will be removed in 2.0.0"
  content: |
    If your code uses `bom_aware_open`, you should replace its use with the regular `open` with `utf-8-sig` encoding instead (or `io.open` in py2/3 compatibility mode).
- title: "Heads-up for plugin authors: `octoprint.util.commandline.clean_ansi` will no longer accept `bytes` in 2.0.0"
  content: | 
    If your code uses `clean_ansi` somewhere, make sure you supply it with `str` (formerly known as `unicode`) instead of `bytes` objects.

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

---

Given how long this has been brewing, the [changelog](https://github.com/OctoPrint/OctoPrint/releases/tag/1.8.0rc1) 
has grown quite large. Let's take a look at the highlights, shall we?

* The biggest announcement is probably that with the 1.8.0 release **OctoPrint is dropping Python 2 support**.
  I already wrote about this in a [past post here](/blog/2022/01/31/octoprint-1.8.0-will-require-python-3/), and this is now the first release candidate that 
  is Python 3 exclusive. As of the publication of this first release candidate, any OctoPrint instances
  still on Python 2 have been redirected to the legacy repository for update checks and thus will also
  no longer be able to partake in this RC phase - which they wouldn't anyway as the code base
  has already been migrated to be Python 3 exclusive, removing all the workarounds so painstakingly
  put in over the past three years.
* The temperature tab now has (optional) **event markers** for when a print gets started, paused, resumed, cancelled or finishes. Big thanks to @surdu!
* You may now **enqueue software updates** while a print is ongoing. They will then be started (after a short countdown) after successful completion of the print, or manually if you cancelled the print. You can manage the queue during the print to remove items you don't want enqueued after all, or add additional items to it as well. This was contributed by @jneilliii!
* It's now possible to **bulk enable/disable plugins**. This makes it easier for the user to locate plugins that are causing problems in the system.
* This realease adds a first version for **embedding WebRTC based webcams**. Please note that this should be considered beta and is still subject to change while further work and research is being done on the backend side of things. @johnboiles did most of the legwork on this!
* OctoPrint will now show a **heads-up notice if no serial ports are detected**, with a link to the relevant [FAQ entry](https://community.octoprint.org/t/octoprint-cant-connect-to-my-printer/223). That will hopefully make it easier to spot if the printer is not physically connected or unsupported.
* **Thumbnails for the timelapse recordings** will now be generated automatically and displayed in the UI. There's also a command line tool for generating thumbnails for the existing recordings. A fance new feature contributed by @crysxd!
* The **GCode Viewer's memory usage has been improved** by @JoveToo and @kantlivelong by switching out the underlying data structure and hunting down some bottlenecks. This means you should now be able to display larger GCode files before running into issues.
* **Performance of settings access has been greatly improved** as well, by refactoring the code to use a more efficient data structure. This was some heavy collaboration with @flaviut!
* Third party clients can now **authenticate with OctoPrint through the Application Key plugin's fancy new auth dialog** instead of having to direct the user to the more heavy weight full UI.
* An **encoding issue was solved** that was observed against the latest versions of `pip`.
* ... and even more.
