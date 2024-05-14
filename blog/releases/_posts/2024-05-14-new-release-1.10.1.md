---
layout: post-bugfix
title: 'New release: 1.10.1'
author: foosel
date: 2024-05-14 11:30:00 +0200
card: /assets/img/blog/2024-05/2024-05-14-octoprint-1.10.1-card.png
featuredimage: /assets/img/blog/2024-05/2024-05-14-octoprint-1.10.1-card.png
poster: /assets/img/blog/2024-05/2024-05-14-octoprint-1.10.1-poster.png

excerpt: "The first bugfix & security release for 1.10.x, fixing one security vulnerability, several bugs and also adding the one or other improvement."

bugfix: 1.10.1
release:
  tag: 1.10.0
  link: /blog/2024/04/24/new-release-1.10.0/
  headsups: true

headsups:
- title: 🔒 If you use autologin and have additional reverse proxies in front of OctoPrint, make sure they are configured correctly
  content: |
    If you have autologin enabled (which means OctoPrint will log you in automatically if you are accessing it from a local address), it is of utmost importance to properly configure any reverse proxies in front of OctoPrint so that the client IP can be determined correctly.

    If you are accessing OctoPrint through haproxy as shipped on OctoPi, or behind a reverse proxy configured following one of the [reverse proxy example configurations](https://faq.octoprint.org/reverse-proxy), there should be no issue. However, **if you yourself have added any additional reverse proxies** in front of OctoPrint, make sure those are configured correctly.

    Please read more about this [in the FAQ](https://faq.octoprint.org/reverse-proxy).

contributors:
- cp2004
- dawidpieper

security:
- "[Jacopo Tediosi](https://github.com/jacopotediosi)"

---

This first bugfix & security release for 1.10.x fixes one security vulnerability, several bugs and also adds the one or other improvement:

> **🔒 Security fixes**
> 
> - Severity High (7.1): It was possible for an unauthenticated attacker to completely bypass the authentication if the `autologinLocal` option was enabled within the Access Control configuration, even if they came from networks that were not configured as `localNetworks`, by spoofing their IP via the `X-Forwarded-For` header.
> 
>   Please note that this does not affect you unless you've enabled the `autologinLocal` feature (it ships as disabled by default and requires adjusting the `config.yaml` file to enable, or the installation of a third party plugin that does this for you). It likely also doesn't affect you if you have enabled said feature but have OctoPrint only accessible on a trusted network. 
>
>   If you have `autologinLocal` enabled and your OctoPrint instance is reachable from a hostile network like the internet, e.g. through a port forward, this *does* affect you and you need to update ASAP. Until you are able to update, it is strongly recommended to disable the autologin feature and/or make your instance inaccessible from potentially hostile networks.
>
>   See also the [GitHub Security Advisory](https://github.com/OctoPrint/OctoPrint/security/advisories/GHSA-fwfg-vprh-97ph) and [CVE-2024-32977](https://nvd.nist.gov/vuln/detail/CVE-2024-32977).
> 
> **✨ Improvements**
>
> *Core*
>
> - [#4975](https://github.com/OctoPrint/OctoPrint/issues/4975): Reserved temperature identifiers not confirmed as supported but still sent by the printer's firmware will now only cause a warning log entry in `octoprint.log` on their first occurrence during a connection, not every time a temperature report is received. This is to combat log spam in case of firmware bugs and misconfiguration.
> - [#5003](https://github.com/OctoPrint/OctoPrint/issues/5003): Make the ticks on the temperature graph's timeline automatically scale with the cutoff to keep the graph readable even with several hours of history.
> - Revert back to the `netifaces` dependency. While `netifaces2` as used in 1.10.0 works well, it is sadly causing some build issues in the field. In the interest of giving as many people as possible access to any bug and especially security fixes, we are thus reverting to the (unmaintained) netifaces for now and keeping an eye on the wheel availability and compatibility of `netifaces2` for a future rollout.
>
> *Achievements Plugin*
>
> - [#5007](https://github.com/OctoPrint/OctoPrint/issues/5007): Clarify the requirement to properly configure the timezone and allow to reset all or only the time based achievements.
> - Clarify that the Achievements Plugin is a **plugin** that can be disabled, if one doesn't want to have achievements.
> 
> **🐛 Bug fixes**
> 
> *Core*
>
> - [#4952](https://github.com/OctoPrint/OctoPrint/issues/4952): Uploading multiple files through the web interface will now also work if printer side SD support has been disabled (see also [PR#4953](https://github.com/OctoPrint/OctoPrint/issues/4953)).
> - [#4993](https://github.com/OctoPrint/OctoPrint/issues/4993): Fix resource consumption and server performance issues caused by a busy loop in the GCODE analysis.
> - [PR#4996](https://github.com/OctoPrint/OctoPrint/issues/4996): Fix screenreader role on tabs to enable keyboard navigation
> - [#5004](https://github.com/OctoPrint/OctoPrint/issues/5004): Fix drag'n'drop file uploading in Safari.
> - [#5005](https://github.com/OctoPrint/OctoPrint/issues/5005): Fix netmask & external address detection.
>
> *Achievements Plugin*
>
> - Fix the quote of the "One small step for (a) man" achievement to match NASA's official transcript.
> - Use configured timezone for internal stats as well.
>
> *Application Keys Plugin*
>
> - [#5001](https://github.com/OctoPrint/OctoPrint/issues/5001): Fix regular user's (non-admins) not being able to revoke application keys.

You can also take a look at the [changelog on GitHub](https://github.com/OctoPrint/OctoPrint/releases/tag/1.10.1).

Like every single release (and release candidate) of OctoPrint ever since early 2016 this release was made possible only
through continued financial support by people like you! 💕 

**[Click here](/support-octoprint/) if you enjoy OctoPrint and want to help with its funding!**
