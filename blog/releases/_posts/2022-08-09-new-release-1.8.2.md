---

layout: post-bugfix
title: 'New release: 1.8.2'
author: foosel
date: 2022-08-09 14:30:00 +0200
card: /assets/img/blog/2022-08/2022-08-09-octoprint-1.8.2-card.png
featuredimage: /assets/img/blog/2022-08/2022-08-09-octoprint-1.8.2-card.png
poster: /assets/img/blog/2022-08/2022-08-09-octoprint-1.8.2-poster.png
excerpt: "This second bugfix & security release for 1.8.0 fixes a few new issues reported, including one security vulnerability."

bugfix: 1.8.2
release:
  tag: 1.8.0
  link: /blog/2022/05/17/new-release-1.8.0/
  headsups: true

---

This second bugfix & security release for 1.8.0 fixes one (potential) bug and closes one (minor) security
vulnerability:

> **🔒 Security fixes**
>
> - Fixed an open redirect vulnerability in the login dialog. An attacker could send a login URL with a specially crafted redirect parameter pointing to an external page under their control to an instance admin that if used to login would redirect this URL, allowing the attacker to start a phishing attack. This is not directly exploitable by the attacker, but after a successful phishing attack and thus obtained credentials could be used to gain access to the OctoPrint instance if somehow reachable by the attacker (e.g. if you have exposed your OctoPrint instance on the public internet or another hostile network contrary to the project's recommendations). Thanks to "Mizu" for reporting and disclosing this responsibly.
>
> **🐛 Bug fixes**
>
> - Pinned the Flask dependency to 2.1. The latest release requires a version of werkzeug that we currently cannot upgrade to due to yet another dependency, and there seem to have been cases in the field where users managed to update Flask regardless of the werkzeug version pin in OctoPrint, which caused runtime errors. This has not been successfully reproduced in the development environment, but a version pin here is a sensible precaution.

You can also take a look at the [extremely short changelog on GitHub](https://github.com/OctoPrint/OctoPrint/releases/tag/1.8.2).

Like every single release (and release candidate) of OctoPrint ever since early 2016 this release was made possible only
through your continued **[support of my work](/support-octoprint/)** 💕
