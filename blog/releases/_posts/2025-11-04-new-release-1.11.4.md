---
layout: post-bugfix
title: "New release: 1.11.4"
author: foosel
date: 2025-11-04 13:45:00 +0100
card: /assets/img/blog/2025-11/2025-11-04-octoprint-1.11.4-card.png
featuredimage: /assets/img/blog/2025-11/2025-11-04-octoprint-1.11.4-card.png
poster: /assets/img/blog/22025-11/2025-11-04-octoprint-1.11.4-poster.png

excerpt: "The fourth bugfix release for 1.11.x, fixing some bugs, security issues and user experience problems reported since the release of 1.11.0."

bugfix: 1.11.4
release:
  tag: 1.11.0
  link: /blog/2025/04/22/new-release-1.11.0/
  headsups: true
prior:
  headsups:
    - release: 1.11.2
      link: /blog/2025/06/10/new-release-1.11.2/
    - release: 1.11.3
      link: /blog/2025/09/09/new-release-1.11.3/

contributors:
  - jacopotediosi

security:
  - "[@jacopotediosi](https://github.com/jacopotediosi)"
---

Prepared in between working heavily on 1.12.0 that will bring native support for printer connection types other than serial, e.g. Moonraker/Klipper, this fourth bugfix release for 1.11.x fixes some bugs, security issues and user experience problems reported since the release of 1.11.0:

> **🔒 Security fixes**
>
> **XSS in Action Commands Notification and Prompt**, severity Moderate (4.6): OctoPrint versions up to and including 1.11.3 are affected by a vulnerability that allows injection of arbitrary HTML and JavaScript into Action Commands notification and prompt popups.
>
> An attacker who successfully convinces a victim to print a specially crafted file could exploit this issue to disrupt ongoing prints, extract information (including sensitive configuration settings, if the targeted user has the necessary permissions for that), or perform other actions on behalf of the targeted user within the OctoPrint instance.
>
> If popups have been disabled for both Action Command notifications and prompts, this vulnerability does not have an impact.
>
> See also the [GitHub Security Advisory](https://github.com/OctoPrint/OctoPrint/security/advisories/GHSA-crvm-xjhm-9h29) and [CVE-2025-64187](https://nvd.nist.gov/vuln/detail/CVE-2025-64187)
>
> _Minor Security fixes_
>
> - Protected the execution of system commands with a reauthentication request.
>
> **✨ Features & improvements**
>
> _Gcode Viewer Plugin_
>
> - Got rid of some unused calculations in the gcode parser, greatly improving loading performance.
>
> _Plugin Manager Plugin & Software Update Plugin_
>
> - [#5204](https://github.com/OctoPrint/OctoPrint/issues/5204): The Plugin Manager and the Software Update Plugin will now detect if they are about to install an OctoPrint plugin that still uses the legacy `setup.py` that depends on `octoprint_setuptools`, and add necessary parameters to `pip` for installation to work even under pip >= 25.3 (specifically `--no-build-isolation --use-pep517`). This solves errors installing plugins when the `pip` version in OctoPrint's virtual environment has been upgraded to 25.3 or newer. See also [this FAQ item](https://community.octoprint.org/t/65241).
>
> **🐛 Bug fixes**
>
> _Core_
>
> - [#5193](https://github.com/OctoPrint/OctoPrint/issues/5193): Persist cache key used for file metadata in UI to reduce the likelihood of triggering a file data polling loop.
> - [#5199](https://github.com/OctoPrint/OctoPrint/issues/5199): Trigger the reload overlay when encountering a CSRF error during a server reconnect. That fixes the "Server Offline" error encountered when restoring from a backup.
> - Pinned the `psutil` dependency less aggressively again, after a broken release was pulled by piwheels.
> - Pinned the `click` dependency to a version below 8.3 due to breaking changes. This is a temporary solution for the 1.11.x release in particular, 1.12.0 will ship with full compatibility to current `click` releases again.
> - Pinned the `markupsafe` dependency to <=3.0.2 under Python 3.9 and armv7 due to the stock Python 3 environment found on Debian Bullseye that matches these parameters containing a buggy `toml` library that can no longer parse the packaging file of recent releases.

You can also take a look at the [changelog on GitHub](https://github.com/OctoPrint/OctoPrint/releases/tag/1.11.3).

Like every single release (and release candidate) of OctoPrint ever since early 2016 this release was made possible only
through continued financial support by people like you! 💕

**[Click here](/support-octoprint/) if you enjoy OctoPrint and want to help with its funding!**
