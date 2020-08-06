---

layout: post
title: 'New release: 1.4.2'
author: foosel
date: 2020-08-06 13:50:00 +0200
card: /assets/img/blog/2020-08/2020-08-06-octoprint-1.4.2-card.png
featuredimage: /assets/img/blog/2020-08/2020-08-06-octoprint-1.4.2-card.png
poster: /assets/img/blog/2020-08/2020-08-06-octoprint-1.4.2-poster.png
excerpt: "This is a hotfix release to fix three bugs in 1.4.1 that sadly only were reported after the release candidate phase for 1.4.1."

---

This is a hotfix release to fix three bugs in 1.4.1 that sadly only were reported after the release candidate phase for 1.4.1.

Due to that the [changelog](https://github.com/OctoPrint/OctoPrint/releases/tag/1.4.2) is very short and only consists 
of three bug fixes:

>  * [#3674](https://github.com/OctoPrint/OctoPrint/issues/3674) - Fix a bug that prevents plugin installation via upload for plugins over 1MB in size.
>  * [#3676](https://github.com/OctoPrint/OctoPrint/issues/3676) - Work around an issue in a third party dependency causing server startup to fail if there are files in the `watched` folder and polling of the `watched` folder is enabled. Also further hardening against similar issues interfering with server startup.
>  * [#3678](https://github.com/OctoPrint/OctoPrint/issues/3678) - Fix a bug that prevents plugin installation via URL from servers that enclose the `filename` option in the `Content-Disposition` HTTP header in double quotes. Affected some plugins not hosted on Github.

Like every single release (and release candidate) of OctoPrint ever since early 2016 this was made possible only 
through your continued **[support of my work](/support-octoprint/)** 💕

### Heads-ups

The heads-ups from 1.4.1 still apply, [please read them carefully](/blog/2020/08/04/new-release-1.4.1/), they might impact you and how you use OctoPrint!
Also see the **Further Information** and **Links** below for more information,
where to find help and how to roll back.
 
### Thanks

Special thanks to everyone who contributed to this release and provided full, analyzable bug reports and pull requests, especially to Special thanks to everyone who contributed to this release and provided full, analyzable bug reports and pull requests, especially to [@osubuu](https://github.com/osubuu) for their PR!

### Further Information

It may take up to 24h for your update notification to pop up, so don't 
be alarmed if it doesn't show up immediately after reading this. You
can force the update however via Settings > Software Update > 
Advanced options > Force check for update.

If you get an error about "no suitable distribution" during update, please read 
[this](https://community.octoprint.org/t/i-got-some-error-about-no-suitable-distribution-during-update-and-now-my-server-wont-start/235).

**If you have any problems with your OctoPrint installation, please seek 
support on the [community forum](https://community.octoprint.org).**

### Links

  * [Changelog and Release Notes](https://github.com/OctoPrint/OctoPrint/releases/tag/1.4.2)
  * [Community forum](https://community.octoprint.org)
  * [Discord Server](https://discord.octoprint.org)
  * [FAQ](https://faq.octoprint.org)
  * [Documentation](http://docs.octoprint.org/)
  * [Contribution Guidelines (also relevant for creating bug reports!)](https://github.com/OctoPrint/OctoPrint/blob/master/CONTRIBUTING.md)
  * [How to file a bug report](https://github.com/OctoPrint/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report)
  * [How to roll back to an earlier release (OctoPi)](https://community.octoprint.org/t/how-can-i-revert-to-an-older-version-of-the-octoprint-installation-on-my-octopi-image/205)
  * [How to roll back to an earlier release (manual install)](https://community.octoprint.org/t/how-can-i-roll-back-to-an-earlier-version-after-an-update/234)
