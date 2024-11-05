---
layout: post-bugfix
title: 'New release: 1.10.3'
author: foosel
date: 2024-11-05 10:21:00 +0100
card: /assets/img/blog/2024-11/2024-11-05-octoprint-1.10.3-card.png
featuredimage: /assets/img/blog/2024-11/2024-11-05-octoprint-1.10.3-card.png
poster: /assets/img/blog/2024-11/2024-11-05-octoprint-1.10.3-poster.png

excerpt: "The third security & bugfix release for 1.10.x, fixing some security vulnerabilities and bugs reported since the release of 1.10.2."

bugfix: 1.10.3
release:
  tag: 1.10.0
  link: /blog/2024/04/24/new-release-1.10.0/
  headsups: true

prior:
  headsups:
  - release: 1.10.1
    link: /blog/2024/05/14/new-release-1.10.1/

contributors:
- jacopotediosi
- jneilliii

security:
- "[Jacopo Tediosi](https://github.com/jacopotediosi)"

---

This third security & bugfix release for 1.10.x fixes some security vulnerabilities and bugs reported since the release of 1.10.2:


> **🔒 Security fixes**
>
> - Severity Moderate (5.5): OctoPrint versions up until and including 1.10.2 are vulnerable to reflected XSS vulnerabilities through its Jinja2 template system, as this is not configured to enforce automatic escaping. This affects, among other places, the login dialog and the standalone application key confirmation dialog.
> 
>   An attacker who successfully talked a victim into clicking on or through a malicious third party app successfully redirected a victim to a specially crafted link could use this to retrieve or modify sensitive configuration settings, interrupt prints or otherwise interact with the OctoPrint instance in a malicious way.
> 
>   The above mentioned specific vulnerabilities of the login dialog and the standalone application key confirmation dialog have been fixed in 1.10.3 by individual escaping of the detected locations. A global change throughout all of OctoPrint's templating system with the upcoming 1.11.0 release will handle this further, switching to globally enforced automatic escaping and thus reducing the attack surface in general.
> 
>   The latter will also improve the security of third party plugins. During a transition period, third party plugins will be able to opt *into* the automatic escaping. With OctoPrint 1.13.0, automatic escaping will be switched over to be enforced even for third party plugins, unless they explicitly *opt-out*.
> 
>   See also the [GitHub Security Advisory](https://github.com/OctoPrint/OctoPrint/security/advisories/GHSA-xvxq-g8hw-fx4g) and [CVE-2024-49377](https://nvd.nist.gov/vuln/detail/CVE-2024-49377).
> 
> - Severity Moderate (5.3): OctoPrint versions up until and including 1.10.2 contain a vulnerability that allows an attacker that has gained temporary control over an authenticated victim's OctoPrint browser session to retrieve/recreate/delete the user's or - if the victim has admin permissions - the global API key without having to reauthenticate by re-entering the user account's password.
> 
>   An attacker could use a stolen API key to access OctoPrint through its API, or disrupt workflows depending on the API key they deleted.
> 
>   See also the [GitHub Security Advisory](https://github.com/OctoPrint/OctoPrint/security/advisories/GHSA-cc6x-8cc7-9953) and [CVE-2024-51493](https://nvd.nist.gov/vuln/detail/CVE-2024-51493).
> 
> *Minor security fixes*
> 
> - Core, [PR#5070](https://github.com/OctoPrint/OctoPrint/pull/5070): Use `secrets` lib to generate Flask secret key, API keys and user session IDs.
>
> - Discovery Plugin: Removed version number from `discovery.xml` of SSDP discovery. Combats information leakage.
> 
> - GCODE Viewer Plugin: Limited access to `skip_until` check API to available `GCODE_VIEWER` and `FILES_DOWNLOAD` permissions. Combats information leakage.
> 
> **🐛 Bug fixes**
> 
> *Core*
> 
> - [#5036](https://github.com/OctoPrint/OctoPrint/issues/5036): Fixed a typo where the config setting `server.reverseProxy.trustedUpstream` was used instead of `server.reverseProxy.trustedDownstream`. Also made the SockJS trusted proxy check align with that of Flask & Tornado.
> - [#5049](https://github.com/OctoPrint/OctoPrint/issues/5049): Fixed file list cache being created before all extension tree providing plugins have had a chance to act.
> 
> *Plugin Manager*
> 
> - [#5057](https://github.com/OctoPrint/OctoPrint/issues/5057): Fixed dequeuing of plugin installs. See also [PR#5061](https://github.com/OctoPrint/OctoPrint/pull/5061).

You can also take a look at the [changelog on GitHub](https://github.com/OctoPrint/OctoPrint/releases/tag/1.10.3).

Like every single release (and release candidate) of OctoPrint ever since early 2016 this release was made possible only
through continued financial support by people like you! 💕 

**[Click here](/support-octoprint/) if you enjoy OctoPrint and want to help with its funding!**
