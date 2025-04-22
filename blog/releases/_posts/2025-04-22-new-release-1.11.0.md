---

layout: post-release
title: 'New release: 1.11.0'
author: foosel
date: 2025-04-22 11:30:00 +0200
card: /assets/img/blog/2025-04/2025-04-22-octoprint-1.11.0-card.png
featuredimage: /assets/img/blog/2025-04/2025-04-22-octoprint-1.11.0-card.png
poster: /assets/img/blog/2025-04/2025-04-22-octoprint-1.11.0-poster.png
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

excerpt: "In development now since January 2024, and in community testing since January 2025, I'm proud to finally present you with OctoPrint 1.11.0!"

release: "1.11.0"

contributors:
- ccatlett1984
- cp2004
- dawidpieper
- endrift
- Hillshum
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
- title: "Heads-up: OctoPrint 1.11.x is the last version of OctoPrint to support Python 3.7 and 3.8"
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

security:
- "[Jacopo Tediosi](https://github.com/jacopotediosi)"

testers:
- AndKe
- b-morgan
- billygr
- ckuethe
- EddyMI3d
- fly74
- fonso2616
- jneilliii
- larp-welt
- pooh22
- XxInvictus

stats:
  instancegraph: /assets/img/blog/2025-04/2025-04-22-rc-instances.png
  printtimegraph: /assets/img/blog/2025-04/2025-04-22-rc-prints.png
  piecharts: /assets/img/blog/2025-04/2025-04-22-rc-piecharts.png
  totalinstances: 876
  totalprinttime: 24792
  rcs:
  - tag: 1.10.0rc3
    date: 2025-02-18
    instances: 450
    printtime: 9371
  - tag: 1.10.0rc4
    date: 2025-03-11
    instances: 274
    printtime: 3134
  - tag: 1.10.0rc5
    date: 2025-03-18
    instances: 342
    printtime: 5050
  - tag: 1.10.0rc6
    date: 2025-04-01
    instances: 100
    printtime: 481
  - tag: 1.10.0rc7
    date: 2025-04-03
    instances: 328
    printtime: 4183
  rcs_incomplete:
  - tag: 1.10.0rc1
    date: 2025-01-28
    instances: 42
    printtime: 284
  - tag: 1.10.0rc2
    date: 2025-02-03
    instances: 324
    printtime: 2288

---

After 12 months in development and a further 3 months of community testing during the release candidate phase, it makes me feel very happy (and to be honest also relieved) to finally release 1.11.0 for good!

Like every single release (and release candidate) of OctoPrint ever since 2016, this release was made possible only through your continued **[support of my work](/support-octoprint/)** 💕

As always with a new version this new release brings not only bug and security fixes but also improvements and a whole bunch of new features. As a consequence, the [changelog](https://github.com/OctoPrint/OctoPrint/releases/tag/1.11.0) has grown quite large, too large to include here. But don't you worry, we'll briefly take a look at some of the highlights.

Before we get to that though, let me get one big heads-up out of the way, which is also included below:

- **OctoPrint 1.11.x is the last version of OctoPrint to support Python 3.7 and 3.8**. As further detailed in the heads-up post below, both versions have now been end-of-life for a while, and due to third-party dependencies rapidly dropping support, it becomes more and more difficult to keep supporting these outdated Python versions. As a consequence, OctoPrint 1.11.x is the final OctoPrint version to support both Python 3.7 and 3.8. OctoPrint 1.12.0+ will require at least Python 3.9. A new health check has been added to OctoPrint 1.11.0 that will tell you if you are affected by this or future drops of support, and link you [the related FAQ entry](https://community.octoprint.org/t/61076). You can read more on that in [the full heads-up below](#headsups).

Now that is done, let's take a look at some of the highlights, shall we?

- OctoPrint now has a full fledged **Upload Manager** plugin bundled! It allows easy management of your uploaded files, including bulk copying, moving and removing as well as renaming, slicing, uploading to your printer etc. This new bundled plugin replaces the sadly no longer maintained File Manager plugin by Marc Hannapel with a new UI and UX and updated logic.

- Another popular but no longer mainted plugin by Marc, the Custom Control Editor, has also been revamped as the bundled **Custom Control Manager** which now provides you with a built-in UI to quickly create and manage your own custom controls that will be shown on the Control tab. A core feature since the first versions of OctoPrint over a decade ago, it was time to give this full UI configuration support in core!

- For the security conscious people out there it will be some good news to hear that there's now support for adding **Two-Factor Authentication** through plugins, and a [first plugin supporting TOTP](https://plugins.octoprint.org/plugins/mfa_totp) has already been made available on the official plugin repository!

- A new **Health Check Plugin** will will alert you of any issues with your runtime environment and OctoPrint installation. For now, it checks the following things:

  - sufficient file system storage across all configured data folders
  - OctoPrint's version not being more than two minor versions behind
  - Python version not being EOL or close to EOL

  Health checks are kept as unobstrusive as possible in the shape of a little navbar icon. Only high priority issues will cause a popup. Currently that only involves Python versions that are already EOL, and those will only be shown every 30 days (per browser, by the use of a browser cookie).

  Additional health checks can be added by plugins through the `octoprint.plugin.health_check.get_additional_checks` hook.

  A forthcoming update of the bundled [PiSupport Plugin](https://github.com/OctoPrint/OctoPrint-PiSupport) adds the results of the throttle check, model support and default password use to the set of health checks.

- As there are some hardware webcams out there that require authentication credentials, OctoPrint now supports configuring Basic, Digest or Bearer Token based **credentials for the webcam snapshot URL**.

- An **way less intrusive reload popup** has been added that replaces the modal reload overlay on plugin/settings changes and should cause less annoyance. Add

- Similar as other software out there, OctoPrint now will show you a **heads-up about the risks of Third Party Plugins** when you try to install one *for the first time*. This is not to scare you away from using Third Party Plugins in any way, but given that in theory someone *could* write a malicious one, we figured it might be a good idea to tell you about the risks and what we do to reduce them.

- In the plugin repository browser built into the Plugin Manager, OctoPrint will now also allow you to **filter out abandoned plugins** and will also show you whether a plugin is commercial (and if so whether it has a free tier) and whether it requires some kind of cloud access. We want you to be able to make an informed decision on whether to install such plugins right from within the repository browser, without having to navigate to the [official plugin repository](https://plugins.octoprint.org).

- OctoPrint now supports **Python 3.13**.

- Two **security issues** have been fixed, both reponsibly disclosed by [@jacopotediosi](https://github.com/jacopotediosi):
  - One extremely minor path traversal bug in `validate_local_redirect` that could have been abused through some manipulated link to redirect a login to a path on the same server as OctoPrint beyond those marked as safe, e.g. a malicious plugin or an external app on another path.
  - One moderate vulnerability allowing bypassing of the login redirect to access the HTML content of certain frontend pages. As data is typically loaded via API requests with additional user authentication, this had a minor practical impact, however this held the risk of potential future modifications introducing further security vulnerabilities and thus was patched. This is further tracked in [this GitHub Security Advisory](https://github.com/OctoPrint/OctoPrint/security/advisories/GHSA-qw93-h6pf-226x) and [CVE-2025-32788](https://nvd.nist.gov/vuln/detail/CVE-2025-32788).

- Several bugs have been fixed, including the offset of the chamber temperature not being properly applied, logging of exceptions on the WSGI layer, error reporting in case of upload issues, a bug that caused the reload overlay to show way more often than actually necessary, and more.

- ... and plenty other things!
