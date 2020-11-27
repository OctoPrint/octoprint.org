---

layout: post-rc
title: 'New release candidate: 1.5.0rc3'
author: foosel
date: 2020-11-18 16:20:00 +0100
card: /assets/img/blog/2020-11/2020-11-18-octoprint-1.5.0rc3-card.png
featuredimage: /assets/img/blog/2020-11/2020-11-18-octoprint-1.5.0rc3-card.png
poster: /assets/img/blog/2020-11/2020-11-18-octoprint-1.5.0rc3-poster.png
excerpt: The third release candidate for the upcoming 1.5.0 release, with a fix for a regression in the first two.

release: 1.5.0rc3
channel: Maintenance RCs
feedback: 3827

headsups:
- title: "Heads-up: Access Control is now mandatory and no longer can be disabled"
  content: >
    If you so far had Access Control disabled, upon upgrading to 1.5.0, OctoPrint will 
    prompt you to create a user name and password for the (first) admin user. This step 
    was sadly necessary as too many people still will happily expose their completely 
    unsecured OctoPrint instance on the public internet, causing additional support 
    overhead from both attacked users and security researchers. See 
    [this guide](https://community.octoprint.org/t/how-to-set-up-octoprint-to-autologin-a-single-user-when-connecting-from-the-internal-network/26235) 
    for a way to have OctoPrint log you in automatically when connecting from an 
    internal IP.

---

This third RC of 1.5.0 fixes a regression observed in the first two:

> **Bug fixes**
> 
>   * [#3825](https://github.com/OctoPrint/OctoPrint/issues/3825) (regression) - Plugin installation broken under Windows and Python 2.7
