---
title: "New release: 2.0.1"
author: foosel
date: 2026-11-18 15:00:00 +0100

security:
- "[@rlawltnrj](https://github.com/rlawltnrj)"

tags:
- release

summary: "The first bugfix release for 2.0.x, fixing a blocking issue, one security issue and one
  other issue reported since the release of 2.0.0."

release: 2.0.1

stable:
  tag: 2.0.0
  link: /blog/2026/11/16/new-release-2.0.0/
  headsups: true
---

Tonight I got [a report about a crash inside the serial connector's communication loop](https://github.com/OctoPrint/OctoPrint/issues/5486).
While this seems to be a quite rare problem, given that we are currently already looking at over 2200 instances updated
to 2.0.0 with a collective print time of over 6500h just 48 hours after 2.0.0's release, I still decided to
consider this a high priority issue given it's blocking nature. So, here you have 2.0.1, with a fix for this and two 
fixes for slightly less pressing issues I had already been preparing:

> **🔒 Security fixes**
> 
> - **Classic Webcam snapshot credentials are returned by /api/settings to users without the SETTINGS permission**, severity Low (2.1): OctoPrint versions from 1.11.0 up until version 2.0.0 contain an invalid permission restriction on the bundled Classic Webcam Plugin's snapshot credentials, allowing users with permission `SETTINGS_READ` to read those, even though they should be restricted to the `SETTINGS` permission.
>   
>   See also the [GitHub Security Advisory](https://github.com/OctoPrint/OctoPrint/security/advisories/GHSA-rhc2-22vx-4qpg). A CVE has been requested from GitHub but not yet been provided.
> 
> **🐛 Bug fixes**
> 
> *Core*
> 
> - Redact connection parameters on `/api/connection` when the requesting account does not have the `CONNECTION` permission. This is to prevent possible credentials leaking as part of the parameters needed for connectors, e.g. API keys, serial numbers, host names etc.
> 
> *Serial Connector Plugin*
> 
> - [#5486](https://github.com/OctoPrint/OctoPrint/issues/5486): Fix an error leading to a crash in the communication loop when the firmware did not report a `FIRMWARE_NAME` (or `NAME`) as response to `M115`.

You can also take a look at the [changelog on GitHub](https://github.com/OctoPrint/OctoPrint/releases/tag/2.0.1).

Like every single release (and release candidate) of OctoPrint ever since early 2016 this release was made possible only
through continued financial support by people like you! 💕

**[Click here](/support-octoprint/) if you enjoy OctoPrint and want to help with its funding!**
