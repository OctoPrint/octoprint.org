---
layout: post-release
title: 'New release: 1.9.0'
author: foosel
date: 2023-05-23 10:00:00 +0200
card: /assets/img/blog/2023-05/2023-05-23-octoprint-1.9.0-card.png
featuredimage: /assets/img/blog/2023-05/2023-05-23-octoprint-1.9.0-card.png
poster: /assets/img/blog/2023-05/2023-05-23-octoprint-1.9.0-poster.png
images:
- url: /assets/img/blog/2023-03/2023-03-07-gif-multicam.gif
  title: Multiple registered webcam views can be switched in the Control tab.
- url: /assets/img/blog/2023-03/2023-03-07-screenshot-chartmarked.png
  title: The markers on the temperature graph can now be extended by plugins through a new event. Here you can see how the BedCooldown plugin by @rfinnie makes use of that to add a Cooldown marker.
- url: /assets/img/blog/2023-03/2023-03-07-gif-port-autorefresh.gif
  title: The port list will now autorefresh while no connection the a printer has yet been established.
- url: /assets/img/blog/2023-03/2023-03-07-screenshot-announcements-bubble.png
  title: Announcements will no longer trigger a popup (apart from priority announcements), but rather show up as a counter in the navbar.
- url: /assets/img/blog/2023-03/2023-03-07-screenshot-announcements-viewer.png
  title: The announcement viewer has been extended by a "Unread" tab and a "Mark all read" button.

excerpt: "Almost a year in development, followed by close to 3 months of an RC phase, it's finally time to push out 1.9.0!"

release: "1.9.0"

headsups:
- title: "Heads-up: OctoPrint's web interface now requires ES9 (EcmaScript 2018) support in your browser"
  content: |
    Up until now OctoPrint still supported running its UI on browsers that only supported EcmaScript 5 as released in 2009. However, given that based on [data about used browsers from the Anonymous Usage Tracking](https://data.octoprint.org/) **98.96% of all browsers used to access OctoPrint support ES9** and being able to use these features allows things like asynchronous GCODE loading in the viewer (see [#4559](https://github.com/OctoPrint/OctoPrint/pull/4559)) and in general very much improves development experience and speed, the decision has been made to greenlight the use of these features in OctoPrint's JS code base. 

    Given that pretty much all common browsers have had the required support for several years now, this change should not affect ~99% of all of you. For those 0.15% of you accessing the OctoPrint web interface with ancient browsers that don't yet have support this means it is time to upgrade. For those 0.89% of you accessing the OctoPrint web interface with browsers for which we do not know about support, it might also be time to upgrade. 

    In any case, you can check whether your chosen browser supports all the features that OctoPrint uses in core & bundled plugins by going to the new check page at [octoprint.org/browser-check/](https://octoprint.org/browser-check/). 

- title: "Heads-up for plugin and third party application developers: Webcam integration has moved to a plugin interface"
  content: |
    OctoPrint 1.9.0 has been refactored to extract the webcam integration into a new plugin type `WebcamProvider` as well as a `_webcam` template type. You may find the documentation of these here:

    - [`WebcamProviderPlugin`](https://docs.octoprint.org/en/maintenance/plugins/mixins.html#webcamproviderplugin)
    - [`TemplatePlugin` with information on Webcam templates](https://docs.octoprint.org/en/maintenance/plugins/mixins.html#octoprint.plugin.TemplatePlugin)

    A new bundled plugin `Classic Webcam` has been created that implements the existing webcam integration (mjpg/hls/beta webrtc support as well as snapshotting).

    A consequence of this refactoring is that there's no longer a general webcam configuration in the settings but rather now there are `WebcamProviderPlugin` specific settings per plugin. A backwards compatible compatibility layer has been added so that plugin's accessing any of the formerly available global webcam settings should still be able to access and change the data, however it should be considered deprecated and warnings will be logged. Please check your plugins and adjust as necessary when running on OctoPrint 1.9.0.

- title: "Heads-up for plugin developers: `octoprint_setuptools` has been extracted"
  content: |
    In order to support plugin's that want to use `pyproject.toml`, in which case current `pip` versions will build their package in isolated mode, leading to the required `octoprint_setuptools` dependency not being available and thus the install failing, `octoprint_setuptools` was extracted into its own pypi package to allow `pyproject.toml` based plugins to depend on it by adding this to `pyproject.toml`:

    ```toml
    [build-system]
    requires = ["setuptools>=40.8.0", "wheel", "octoprint-setuptools"]
    build-backend = "setuptools.build_meta"
    ```

    This should *not* affect plugins that don't use `pyproject.toml`, however like with every OctoPrint release candidate plugin developers are strongly advised to test installing their plugin under 1.9.0.

contributors:
- 040medien
- arekm
- arrdem
- cclauss
- CoReYeDe
- cp2004
- crysxd
- dawidpieper
- FedericoNembrini
- frenck
- j7126
- jneilliii
- Josef-MrBeam
- JoveToo
- kForth
- luzpaz
- max246
- msrasheed
- rfinnie
- richardsondev
- sgsunder
- smartin015
- the-ress
- tommywienert
- vector76

first_time_contributors:
- 040medien
- arekm
- arrdem
- CoReYeDe
- dawidpieper
- Josef-MrBeam
- kForth
- luzpaz
- max246
- msrasheed
- nmattis
- Patrick-Ames
- sgsunder
- smartin015
- the-ress
- tommywienert

testers:
- b-morgan
- benlye
- Bradford1040
- ChrisHeerschap
- crysxd
- dan-and
- jneilliii
- JohnOCFII
- kj5wi
- LazeMSS
- LightningShark25
- N0YHR
- NewsGuyTor
- pwhelan
- r3Fuze
- Ruhel786
- Silverstar
- The-EG
- TheMedGeek
- Thisismydigitalself

stats:
  instancegraph: /assets/img/blog/2023-05/2023-05-23-rc-instances.png
  printtimegraph: /assets/img/blog/2023-05/2023-05-23-rc-prints.png
  piecharts: /assets/img/blog/2023-05/2023-05-23-rc-piecharts.png
  totalinstances: 1683
  totalprinttime: 103811
  rcs:
  - tag: 1.9.0rc3
    date: 2023-03-22
    instances: 893
    printtime: 27635
  - tag: 1.9.0rc4
    date: 2023-04-12
    instances: 195
    printtime: 1351
  - tag: 1.9.0rc5
    date: 2023-04-13
    instances: 1035
    printtime: 42893
  - tag: 1.9.0rc6
    date: 2022-05-08
    instances: 780
    printtime: 14869
  rcs_incomplete:
  - tag: 1.9.0rc1
    date: 2023-03-07
    instances: 18
    printtime: 150
  - tag: 1.9.0rc2
    date: 2023-03-07
    instances: 714
    printtime: 16913
---

Everyone, it makes me happy to *finally* introduce you to 1.9.0! This release was originally planned for late 2022 or early 2023, but a sudden rush of security reports and consequently fixes in late summer of 2022 meant focusing on 1.8.x for a while and thus pushing this back. The good thing about this is that a number of new features now made it into 1.9.0 after all which otherwise wouldn't have been ready to be merged yet!

Like every single release (and release candidate) of OctoPrint ever since 2016, this release was made possible only through your continued **[support of my work](/support-octoprint/)** 💕

The [full changelog](https://github.com/OctoPrint/OctoPrint/releases/tag/1.9.0) contains a long list of new features, improvements and bug fixes. But before we come to the highlights, let me first get one big announcement out of the way (that is also included in the heads-ups below!):

- **OctoPrint's web interface now requires ES9 (EcmaScript 2018) support in your browser**. As further detailed in the heads-up post
  below, 98.96% of all instances sending in data via the Anonymous Tracking Plugin support ES9. Being able to use modern language
  features allows things like the big performance improvements included in the GCODE Viewer in this release, and also makes development
  and maintenance easier overall. Given that, the decision was made to allow ES9 features in OctoPrint's core UI and bundled plugins. All but the
  most ancient browsers found on really old devices should already be supporting everything needed, but just in case you can 
  check whether your chosen browser supports all the features that OctoPrint uses in core & bundled plugins by going to the new check 
  page at [octoprint.org/browser-check/](https://octoprint.org/browser-check/).

With that out of the way, on to the highlights!

* **The Webcam integration now offers a plugin interface** and the existing webcam support has been extracted into its own (bundled) "Classic Webcam" plugin. Third party plugins will now be able to offer new [webcam providers](https://docs.octoprint.org/en/maintenance/plugins/mixins.html#webcamproviderplugin) for snapshots, and also [webcam templates](https://docs.octoprint.org/en/maintenance/plugins/mixins.html#octoprint.plugin.TemplatePlugin) for embedding streams. This also includes **native multi cam support in the core UI** - if there's more than one plugin providing webcam templates, they will be offered to switch to, see [this GIF](#image-1). You have to thank [@crysxd](https://github.com/crysxd) for this, who did the bulk of the work on this feature.
* With 1.9.0 plugins can now **customize the temperature chart markers** introduced in 1.8.0, thanks to the work by [@rfinnie](https://github.com/rfinnie), who also promptly utilized it in recent versions of his [BedCooldown plugin](https://plugins.octoprint.org/plugins/bedcooldown/) as can be seen in the [below screenshot](#image-2).
* Thanks to a ton of work by [@JoveToo](https://github.com/JoveToo), **the memory footprint of the GCODE viewer has been greatly reduced**, thanks to utilizing (optional) compression and asynchronous loading of the data. This should make the GCODE viewer much more usable on lower end devices, and also make it possible to load larger files without running into memory issues.
* While no printer connection is yet established, OctoPrint will now **automatically poll for serial ports** and if new ones are found refresh the UI accordingly. This should improve user experience, as you will no longer have to manually refresh the UI to see new ports (and potentially get rid of the "no ports detected" warning added in 1.8.0). Contrary to the PortLister plugin, this will also work on Windows servers and for any kind of virtual ports. You can see this in action below.
* You can now **enqueue plugin installs** from the plugin manager thanks to work by [@jneilliii](https://github.com/jneilliii).
* The plugin manager now also supports **installing multiple plugins from an export or simple json list** either uploaded or passed in as an URL. This should make it easier to install a bunch of plugins at once.
* In a similar vain, **you can also now upload multiple files at once**, thanks to work by [@cp2004](https://github.com/cp2004).
* **Announcements will now no longer trigger a popup** (unless from a priority 1 channel like Important) but instead cause an unread counter to be rendered on the notification icon (1-9 and infinity symbol for more). The announcement reader has been extended by a default "Unread" tab that shows all unread news items, and a Mark All Read button has been added to quickly get rid of the unread counter altogether.
* As always, there have also been a ton of **bug fixes**. Examples include fixing the permissions of anonymous API access (they were too strict), including line endings when copy-pasting from the plugin manager or software update log output, and more.
