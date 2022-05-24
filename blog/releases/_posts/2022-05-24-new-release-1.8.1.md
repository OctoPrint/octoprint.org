---

layout: post-bugfix
title: 'New release: 1.8.1'
author: foosel
date: 2022-05-24 12:00:00 +0200
card: /assets/img/blog/2022-05/2022-05-24-octoprint-1.8.1-card.png
featuredimage: /assets/img/blog/2022-05/2022-05-24-octoprint-1.8.1-card.png
poster: /assets/img/blog/2022-05/2022-05-24-octoprint-1.8.1-poster.png
excerpt: "This first bugfix & security release for 1.8.0 fixes a few new issues reported, including one security vulnerability."

bugfix: 1.8.1
release:
  tag: 1.8.1
  link: /blog/2022/05/17/new-release-1.8.0/
  headsups: true

---

This first bugfix & security release for 1.8.0 fixes two bugs and closes one (minor) security
vulnerability:

> **🔒 Security fixes**
> 
>   * Fixed a cross-site scripting vulnerability in the user and group managers. An attacker could talk an admin into creating a user or group with a specially crafted name containing executable  HTML/JS, and then into deleting those again, triggering the cross-site scripting issue in the deletion confirmation dialog. A stealing of credentials through this should not have been possible under 1.8.0, however in versions before 1.8.0 the stealing of the "remember me" token would have been possible through this attack vector. This could have then been used to gain access to the OctoPrint instance if somehow reachable by the attacker (e.g. if you have exposed your OctoPrint instance on the public internet or another hostile network contrary to the project's recommendations). Thanks to Akshay Ravi for reporting and disclosing this reponsibly.
> 
> **🐛 Bug fixes**
> 
>   * [#4516](https://github.com/OctoPrint/OctoPrint/issues/4516) - Fix a redirect loop on the login dialog if the Guests group was assigned the Read-Only group as a subgroup.
>   * Gracefully handle errors scanning `/dev` for serial ports. Solves an issue with Octo4a on some Android devices.

You can also take a look at the [extremely short changelog on GitHub](https://github.com/OctoPrint/OctoPrint/releases/tag/1.8.1).

Like every single release (and release candidate) of OctoPrint ever since early 2016 this release was made possible only
through your continued **[support of my work](/support-octoprint/)** 💕
