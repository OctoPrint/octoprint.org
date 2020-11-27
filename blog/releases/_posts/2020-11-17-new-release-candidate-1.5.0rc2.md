---

layout: post-rc
title: 'New release candidate: 1.5.0rc2'
author: foosel
date: 2020-11-17 15:45:00 +0100
card: /assets/img/blog/2020-11/2020-11-17-octoprint-1.5.0rc2-card.png
featuredimage: /assets/img/blog/2020-11/2020-11-17-octoprint-1.5.0rc2-card.png
poster: /assets/img/blog/2020-11/2020-11-17-octoprint-1.5.0rc2-poster.png
excerpt: The second release candidate for the upcoming 1.5.0 release, with some fixes of regressions from the first one and some improvements in newly added functionality.

release: 1.5.0rc2
channel: Maintenance RCs
feedback: 3823

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
    
contributors:
- cp2004

---

This second RC of 1.5.0 fixes some regressions observed with the first one and also improves some things
in newly added and changed functionality:

> **Improvements**
> 
>   * [#3804](https://github.com/OctoPrint/OctoPrint/issues/3804) - Improve handling of corrupt `users.yaml` file and refuse server start if broken and default file based UserManager is configured.
>   * [#3811](https://github.com/OctoPrint/OctoPrint/issues/3811) - Only start tracking resend ratio after a set amount of lines has been transmitted.
>   * [#3822](https://github.com/OctoPrint/OctoPrint/issues/3822) - Prevent circumvention of access control through admin subgroups/permissions
> 
> **Bug fixes**
> 
>   * [#3805](https://github.com/OctoPrint/OctoPrint/issues/3805) (regression) - Fix an internal server error on `GET /api/files/local/<filename>`
>   * [#3812](https://github.com/OctoPrint/OctoPrint/issues/3812) (regression) - Backup: Fix an `AttributeError` on CLI usage
>   * [#3813](https://github.com/OctoPrint/OctoPrint/issues/3813) (regression) - Discovery: Fix zeroconf discovery under Python 2
>   * [#3814](https://github.com/OctoPrint/OctoPrint/issues/3814) - Fix an error on language pack upload under Python 3; not a regression, but still included due to being minimally invasive (see also [#3815](https://github.com/OctoPrint/OctoPrint/issues/3815))
