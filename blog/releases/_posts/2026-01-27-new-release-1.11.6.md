---
layout: post-bugfix
title: "New release: 1.11.6"
author: foosel
date: 2026-01-27 14:20:00 +0100
card: /assets/img/blog/2026-01/2026-01-27-octoprint-1.11.6-card.png
featuredimage: /assets/img/blog/2026-01/2026-01-27-octoprint-1.11.6-card.png
poster: /assets/img/blog/2026-01/2026-01-27-octoprint-1.11.6-poster.png

excerpt: "The sixth bugfix release for 1.11.x, fixing some bugs reported since the release of 1.11.0."

bugfix: 1.11.6
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
  - "[@yueyueL](https://github.com/yueyueL)"
---

Welcome to the first release of 2026, a bugfix release for 1.11.x, fixing a bunch of issues and one security problem:

> **🔒 Security fixes**
>
> - **Timing Side-Channel in API Key Authentication**, severity Moderate (6.0): OctoPrint versions up to and including 1.11.5 are affected by a (theoretical) timing attack vulnerability that allows API key extraction over the network.
>
>   Due to using character based comparison that short-circuits on the first mismatched character during API key validation, rather than a cryptographical method with static runtime regardless of the point of mismatch, an attacker with network based access to an affected OctoPrint could extract API keys valid on the instance by measuring the response times of the denied access responses and guess an API key character by character.
>
>   The likelihood of this attack actually working is highly dependent on the network's latency, noise and similar parameters. An actual proof of concept was not achieved so far. Still, as always administrators are advised to not expose their OctoPrint instance on hostile networks, especially not on the public internet!
>
>   See also the [GitHub Security Advisory](https://github.com/OctoPrint/OctoPrint/security/advisories/GHSA-xg4x-w2j3-57h6) and [CVE-2026-23892](https://nvd.nist.gov/vuln/detail/CVE-2026-23892)
>
> **✨ Features & improvements**
>
> _Achievements Plugin_
>
> - [#5223](https://github.com/OctoPrint/OctoPrint/issues/5223): Support resetting the yearly stats & display the status of the current year.
>
> **🐛 Bug fixes**
>
> _Core_
>
> - [#5231](https://github.com/OctoPrint/OctoPrint/issues/5231): Correctly apply preprocessors on settings get & set when handling nested values.
>
> _Achievements Plugin_
>
> - [#5223](https://github.com/OctoPrint/OctoPrint/issues/5223): Properly handle year changes during runtime in stats collection, which is also used for the [Wrapped Plugin](https://github.com/OctoPrint/OctoPrint-Wrapped/). Auto fix stats affected by the underlying issue.
>
> _Upload Manager Plugin_
>
> - [#5216](https://github.com/OctoPrint/OctoPrint/issues/5216): Fix multi select on MacOS, now uses Cmd+Click.
> - [#5217](https://github.com/OctoPrint/OctoPrint/issues/5217): Fix shift select logic to be more inline with common operating system file explorers.

You can also take a look at the [changelog on GitHub](https://github.com/OctoPrint/OctoPrint/releases/tag/1.11.3).

Like every single release (and release candidate) of OctoPrint ever since early 2016 this release was made possible only
through continued financial support by people like you! 💕

**[Click here](/support-octoprint/) if you enjoy OctoPrint and want to help with its funding!**
