---

layout: post-rc
title: 'New release candidate: 1.11.0rc1'
author: foosel
date: 2025-01-28 15:15:00 +0100
card: /assets/img/blog/2025-01/2025-01-28-octoprint-1.11.0rc1-card.png
featuredimage: /assets/img/blog/2025-01/2025-01-28-octoprint-1.11.0rc1-card.png
poster: /assets/img/blog/2025-01/2025-01-28-octoprint-1.11.0rc1-poster.png
images:
- url: /assets/img/blog/2025-01/2025-01-28-screenshot-upload-manager-button.png
  title: The button to launch the new Upload Manager in the file list sidebar.
- url: /assets/img/blog/2025-01/2025-01-28-screenshot-upload-manager.png
  title: The newly added Upload Manager.
- url: /assets/img/blog/2025-01/2025-01-28-screenshot-custom-controls-manager.png
  title: The newly added Custom Control Manager.
- url: /assets/img/blog/2025-01/2025-01-28-screenshot-2fa.png
  title: Example of a two-factor authentication request on the login.
- url: /assets/img/blog/2025-01/2025-01-28-screenshot-health-check.png
  title: Health checks allow you to get notified about issues with your installation.
- url: /assets/img/blog/2025-01/2025-01-28-screenshot-webcam-credentials.png
  title: You can now enter credentials for accessing the webcam snapshot URL.
- url: /assets/img/blog/2025-01/2025-01-28-screenshot-page-reload-recommended.png
  title: The new reload popup notification that in large parts replaces the blocking reload modal.
- url: /assets/img/blog/2025-01/2025-01-28-screenshot-third-party-warning.png
  title: The new information popup about third party plugins.

excerpt: The first release candidate for the upcoming 1.11.0 release containing new features, improvements & bug fixes!

release: 1.11.0rc1
channel: Maintenance RCs
feedback: 5095

closer_look:
- Proper behaviour when using the included web interface as well as any third party clients at your disposal.
- The newly added Custom Control Manager plugin.
- The newly added Health Check plugin.
- The newly added Upload Manager plugin.
- The MFA-TOTP plugin using the new MFA plugin interface.
- Timelapse creation, especially with a configured rendering delay.

contributors:
- ccatlett1984
- cp2004
- dawidpieper
- endrift
- its-leofisher
- jacopotediosi
- jneilliii
- MaienM
- nmschulte
- ofoxus
- WildRikku
- WisdomCode
- zaventh

first_time_contributors:
- ccatlett1984
- endrift
- its-leofisher
- jacopotediosi
- MaienM
- nmschulte
- ofoxus
- WildRikku
- WisdomCode
- zaventh

headsups:
- title: "Heads-up: OctoPrint 1.11.x is the last OctoPrint to support Python 3.7 and 3.8"
  content: |
    Python 3.7 has now been EOL since June 27th **2023**, and the maintenance overhead caused by still having to support it is becoming unfeasible. Python 3.8 has now been EOL since October 31st 2024, and it is to be expected that the maintenance overhead will further rise due to that.
    
    As a consequence, OctoPrint 1.11.x is the final OctoPrint version to support both Python 3.7 and 3.8. OctoPrint 1.12.0+ will require at least Python 3.9.
    
    How do you know if you will be affected and need to update? A newly added healthcheck mechanism has been added that will now alert you if your environment is outdated and about to be left behind, an [a new FAQ entry](https://community.octoprint.org/t/61076) is in place to help you figure out how to update your runtime environment. 
    
    This will be kept updated, so that you will also receive early warnings about future deprecations this way.

- title: "Heads-up: OctoPrint will now auto-escape all internal templates, plugin authors should opt-in as well!"
  content: |
    Starting with OctoPrint 1.11.0, OctoPrint will ship with auto-escaping all injected template variables and other included expressions in its template system. For 1.11.0 and 1.12.0, this will only be done for bundled plugins and those third party plugins that have *opted into* autoescaping. Starting with OctoPrint 1.13.0 however, third party plugins will have to *opt out* in order to not have autoescaping enabled on their templates.
    
    [A new entry has been added to the FAQ](https://community.octoprint.org/t/61067) that has further details.

- title: "Heads-up: `WebcamProviderPlugin.take_webcam_snapshot` has gotten its parameters fixed"
  content: |
    If you are the maintainer of a third party plugin using the [`WebcamProviderPlugin`](https://docs.octoprint.org/en/master/plugins/mixins.html#webcamproviderplugin) mixin and have implemented its [`take_snapshot`](https://docs.octoprint.org/en/master/plugins/mixins.html#octoprint.plugin.WebcamProviderPlugin.take_webcam_snapshot) method, be advised that an implementation error in OctoPrint has been fixed and the implementation aligned with the documentation: the method will now be called with the `webcamName` parameter being a string containing the name of the requested webcam, as documented, not a full webcam configuration object as previously wrongly implemented.

---

Welcome to 2025, I hope you arrived safe and sound in this year! Today I'm happy to present to you the first release candidate of the upcoming 1.11.0 release. 

As always with a new minor version that brings not only bug and security fixes but also improvements and whole new features, the [changelog](https://github.com/OctoPrint/OctoPrint/releases/tag/1.11.0rc1) has grown quite large, so I'm not going to include it here in full.

But let's still take a look at some of the highlights, shall we?

* OctoPrint now has a full fledged **Upload Manager** plugin bundled! It allows easy management of your uploaded files, including bulk copying, moving and removing as well as renaming, slicing, uploading to your printer etc. This new bundled plugin replaces the sadly no longer maintained File Manager plugin by Marc Hannapel with a new UI and UX and updated logic.
* Another popular but no longer mainted plugin by Marc, the Custom Control Editor, has also been revamped as the bundled **Custom Control Manager** which now provides you with a built-in UI to quickly create and manage your own custom controls that will be shown on the Control tab. A core feature since the first versions of OctoPrint over a decade ago, it was time to give this full UI configuration support in core!
* For the security conscious people out there it will be some good news to hear that there's now support for adding **Two-Factor Authentication** through plugins, and a [first plugin supporting TOTP](https://plugins.octoprint.org/plugins/mfa_totp) has already been made available on the official plugin repository!
* A new **Health Check Plugin** will will alert you of any issues with your runtime environment and OctoPrint installation. For now, it checks the following things:

  - sufficient file system storage across all configured data folders
  - OctoPrint's version not being more than two minor versions behind
  - Python version not being EOL or close to EOL

  Health checks are kept as unobstrusive as possible in the shape of a little navbar icon. Only high priority issues will cause a popup. Currently that only involves Python versions that are already EOL, and those will only be shown every 30 days (per browser, by the use of a browser cookie).

  Additional health checks can be added by plugins through the `octoprint.plugin.health_check.get_additional_checks` hook.

  A forthcoming update of the bundled [PiSupport Plugin](https://github.com/OctoPrint/OctoPrint-PiSupport) adds the results of the throttle check, model support and default password use to the set of health checks.
* As there are some hardware webcams out there that require authentication credentials, OctoPrint now supports configuring Basic, Digest or Bearer Token based **credentials for the webcam snapshot URL**.
* An **way less intrusive reload popup** has been added that replaces the modal reload overlay on plugin/settings changes and should cause less annoyance. Add
* Similar as other software out there, OctoPrint now will show you a **heads-up about the risks of Third Party Plugins** when you try to install one *for the first time*. This is not to scare you away from using Third Party Plugins in any way, but given that in theory someone *could* write a malicious one, we figured it might be a good idea to tell you about the risks and what we do to reduce them.
* In the plugin repository browser built into the Plugin Manager, OctoPrint will now also allow you to **filter out abandoned plugins** and will also show you whether a plugin is commercial (and if so whether it has a free tier) and whether it requires some kind of cloud access. We want you to be able to make an informed decision on whether to install such plugins right from within the repository browser, without having to navigate to the [official plugin repository](https://plugins.octoprint.org).
* OctoPrint now supports **Python 3.13**.
* Several bugs have been fixed, including the offset of the chamber temperature not being properly applied, logging of exceptions on the WSGI layer, error reporting in case of upload issues, a bug that caused the reload overlay to show way more often than actually necessary, and more.
* ... and plenty other things!
