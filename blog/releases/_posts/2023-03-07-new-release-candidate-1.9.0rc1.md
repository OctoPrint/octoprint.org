---

layout: post-rc
title: 'New release candidate: 1.9.0rc1'
author: foosel
date: 2023-03-07 11:50:00 +0100
card: /assets/img/blog/2023-03/2023-03-07-octoprint-1.9.0rc1-card.png
featuredimage: /assets/img/blog/2023-03/2023-03-07-octoprint-1.9.0rc1-card.png
poster: /assets/img/blog/2023-03/2023-03-07-octoprint-1.9.0rc1-poster.png
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
excerpt: The first release candidate for the upcoming 1.9.0 release containing new features, improvements & bug fixes!

release: 1.9.0rc1
channel: Maintenance RCs
feedback: 4748
changelog: https://gist.github.com/foosel/f67a7a5b697d68f94ecbf4d49647c572

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

---

<div class="alert">
  No matter how much you test, sometimes something slips through. 1.9.0rc2 is incoming due to the <code>octoprint_setuptools</code> refactoring breaking most plugin installs on 1.9.0rc1 after all. Sorry for the inconvenience, new RC asap!
</div>

Originally planned for late 2022, I'm happy to finally present you the first release candidate of the upcoming 1.9.0 release. Given how long this has been brewing, the [changelog](https://gist.github.com/foosel/f67a7a5b697d68f94ecbf4d49647c572) has grown quite large (Gist since 1.9.0rc1 had to be pulled). Let's take a look at some of the highlights, shall we?

* **The Webcam integration now offers a plugin interface** and the existing webcam support has been extracted into its own (bundled) "Classic Webcam" plugin. Third party plugins will now be able to offer new [webcam providers](https://docs.octoprint.org/en/maintenance/plugins/mixins.html#webcamproviderplugin) for snapshots, and also [webcam templates](https://docs.octoprint.org/en/maintenance/plugins/mixins.html#octoprint.plugin.TemplatePlugin) for embedding streams. This also includes native multi cam support in the core UI - if there's more than one plugin providing webcam templates, they will be offered to switch to, see [this GIF](#image-1).
* With 1.9.0 plugins can now **customize the temperature chart markers** introduced in 1.8.0, thanks to the work by @rfinnie, who also promptly utilized it in recent versions of his BedCooldown plugin as can be seen in the [below screenshot](#image-2).
* Thanks to a ton of work by @JoveToo, **the memory footprint of the GCODE viewer has been greatly reduced**, thanks to utilizing (optional) compression and asynchronous loading of the data. This should make the GCODE viewer much more usable on lower end devices, and also make it possible to load larger files without running into memory issues.
* While no printer connection is yet established, OctoPrint will now **automatically poll for serial ports** and if new ones are found refresh the UI accordingly. This should improve user experience, as you will no longer have to manually refresh the UI to see new ports (and potentially get rid of the "no ports detected" warning added in 1.8.0). Contrary to the PortLister plugin, this will also work on Windows servers and for any kind of virtual ports. You can see this in action below.
* You can now **enqueue plugin installs** from the plugin manager thanks to work by @jneilliii.
* The plugin manager now also supports **installing mulitple plugins from an export or simple json list** either uploaded or passed in as an URL. This should make it easier to install a bunch of plugins at once.
* In a similar vain, **you can also now upload multiple files at once**, thanks to work by @cp2004.
* **Announcements will now no longer trigger a popup** (unless from a priority 1 channel like Important) but instead cause an unread counter to be rendered on the notification icon (1-9 and infinity symbol for more). The announcement reader has been extended by a default "Unread" tab that shows all unread news items, and a Mark All Read button has been added to quickly get rid of the unread counter altogether.
* As always, there have also been a ton of **bug fixes**. Examples include fixing the permissions of anonymous API access (they were too strict), including line endings when copy-pasting from the plugin manager or software update log output, and even more.
* ... and even more.
