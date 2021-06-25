---

layout: post-rc
title: 'New release candidate: 1.6.0rc1'
author: foosel
date: 2021-03-30 14:10:00 +0200
card: /assets/img/blog/2021-03/2021-03-30-octoprint-1.6.0rc1-card.png
featuredimage: /assets/img/blog/2021-03/2021-03-30-octoprint-1.6.0rc1-card.png
poster: /assets/img/blog/2021-03/2021-03-30-octoprint-1.6.0rc1-poster.png
images:
- url: /assets/img/blog/2021-03/2021-03-30-log-batch-download.png
  title: Bulk download of log files
- url: /assets/img/blog/2021-03/2021-03-30-timelapse-batch-download.png
  title: Bulk download of log timelapses
- url: /assets/img/blog/2021-03/2021-03-30-pmgr-ui-change.png
  title: Better UX for the Plugin Manager
- url: /assets/img/blog/2021-03/2021-03-30-swu-ui-change.png
  title: Better UX for the Software Update plugin
- url: /assets/img/blog/2021-03/2021-03-30-upload-conflict.png
  title: Upload conflict handling - cancel, rename or overwrite.
- url: /assets/img/blog/2021-03/2021-03-30-systeminfo-bundle-download.png
  title: Download SystemInfo Bundles right from the System Info panel, but also the recovery dialog and the CLI
- url: /assets/img/blog/2021-03/2021-03-30-bundleviewer.png
  title: Bundleviewer at bundleviewer.octoprint.org for viewing SystemInfo Bundles
excerpt: The first release candidate for the upcoming 1.6.0 release, containing new features, improvements and bug fixes.

release: 1.6.0rc1
channel: Maintenance RCs
feedback: 4064

headsups:
- title: "Heads-up for plugin authors: Support for the plugin control properties `__plugin_init__` and `__plugin_implementations__` (plural!) has been removed"
  content: >
    The two plugin control properties `__plugin_init__` and `__plugin_implementations__` (note the plural!)
    have been deprecated ever since OctoPrint 1.2.0 and have finally been removed.
  
    It is *highly* unlikely that your plugin has ever used them given that they were already
    marked as deprecated for the very first version of OctoPrint to ever even support plugins. 
    Still, just in the case of anyone out there making use of them regardless, here's a 
    heads-up that they will no longer be utilized in OctoPrint 1.6+.

contributors:
- costas-basdekis
- cp2004
- drifkind
- eumiro
- eyal0
- j7126
- jasonbcox
- jneilliii
- kantlivelong
- LazeMSS
- martellaj
- Master92
- MichaIng
- shadycuz
- Sophist-UK
- thinkyhead
- tirkarthi

---

Spring is here 🌼, and so is a first Release Candidate of the next OctoPrint release 1.6.0!
This one is once again packed with a ton of improvements, new features and of course
bug fixes. Let's have a look at some of the highlights from the
[changelog](https://github.com/OctoPrint/OctoPrint/releases/tag/1.6.0rc1), shall we?

  * Timelapses and log files now allow bulk downloads: Select multiple files
    and you'll be offered to download all of them in one ZIP archive.
  * [@cp2004](https://github.com/cp2004) improved the UX for the Plugin Manager and the Software Updater: All buttons and related actions
    have been moved to the top of the dialog, leaving more space for the list of plugins
    and update targets and getting rid of a double scrollbar in the process.
  * If OctoPrint's UI detects you are trying to upload a file that already exists, it'll now
    prompt you what to do: cancel, rename to a conflict free name or overwrite the existing
    file. You can disable this via the Settings if you prefer the old approach of simply
    always overwriting. Note that this conflict detection only happens if you use OctoPrint's
    user interface, the API has not been touched.
  * Remember the new System Info dialog introduced in 1.5.0? It has been enhanced and now
    also allows downloading a full SystemInfo Bundle, containing not only the system information
    visible in the dialog but also `octoprint.log`, `serial.log` and anything else that's usually
    requested from you when you report a bug or ask for support on the forums or the Discord server.
    So now you can just download a single bundle zip that contains everything in one go. The bundle
    download is also available on the recovery page (`/recovery`) and can also be requested on the
    command line (via `octoprint systeminfo .`). A [bundle viewer webapp](https://bundleviewer.octoprint.org)
    has also been created that allows viewing these bundles easily in every browser, even on mobile.
  * OctoPrint's backup plugin so far didn't allow you to restore a backup from a newer version
    than what was currently running. This was done to not run into any compatibility issues when
    you try to restore a current backup on an ancient OctoPrint install. Since this poses problems
    when you have created a backup on an only slightly newer version however (think 1.5.3 vs 1.5.2)
    this has now been slightly disarmed - OctoPrint 1.6 and later will now allow you to restore
    backups from the same major.version version, regardless of patch level. So restoring a backup from
    1.6.1 will be allowed on 1.6.0, restoring a backup from 1.7.0 on 1.6.x won't.
  * As we observed some issues in the community with misconfigured autologin settings,
    OctoPrint will now ensure the validity of IP address ranges configured for that and 
    refuse to use invalid ones.
  * The logging UI saw some work done by [@eyal0](https://github.com/eyal0) and the workflow of managing log levels during
    development or debugging has been improved by that.
  * If OctoPrint detects that it can't reach the internet, it will now display a small 
    offline indicator in the navbar. This should hopefully help people diagnose such issues
    faster.
  * A new hook `octoprint.printer.handle_connect` is now in place that allows plugin developers to hook into the process
    of connecting to a printer, prevent that from going through or triggering actions
    based on it in a synchronous fashion.
  * The bundled PiSupport Plugin has been extracted into its own project to be able to have
    it on a different release cycle than OctoPrint proper. It is still considered a bundled
    plugin by OctoPrint.
  * Several bugs have been fixed, e.g. the config CLI has been fixed so that `octoprint config set plugins.softwareupdate.credentials.github <PAT>` for setting
    the GitHub PAT for the updater's rate limiting workaround actually works, the expected
    page reload on the login dialog no longer triggers a scary "server offline" message, 
    running OctoPrint on Python 3.10 should no longer throw an endless stream of errors,
    and much much more.
