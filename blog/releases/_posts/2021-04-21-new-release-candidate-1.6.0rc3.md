---

layout: post-rc
title: 'New release candidate: 1.6.0rc3'
author: foosel
date: 2021-04-21 16:00:00 +0200
card: /assets/img/blog/2021-04/2021-04-21-octoprint-1.6.0rc3-card.png
featuredimage: /assets/img/blog/2021-04/2021-04-21-octoprint-1.6.0rc3-card.png
poster: /assets/img/blog/2021-04/2021-04-21-octoprint-1.6.0rc3-poster.png
excerpt: The third release candidate for the upcoming 1.6.0 release, with a one fix of a regression and one work around for a discovered firmware bug.

release: 1.6.0rc3
channel: Maintenance RCs
feedback: 4106

headsups:
- title: "Heads-up for plugin authors: Support for the plugin control properties `__plugin_init__` and `__plugin_implementations__` (plural!) has been removed"
  content: >
    The two plugin control properties `__plugin_init__` and `__plugin_implementations__` (note the plural!)
    have been deprecated ever since OctoPrint 1.2.0 and have finally been removed.
  
    It is *highly* unlikely that your plugin has ever used them given that they were already
    marked as deprecated for the very first version of OctoPrint to ever even support plugins. 
    Still, just in the case of anyone out there making use of them regardless, here's a 
    heads-up that they will no longer be utilized in OctoPrint 1.6+.
    
---

This third RC of 1.6.0 fixes one regression observed with the first two and adds one
workaround for a firmware bug discovered to fixed behaviour in OctoPrint:

> **Improvements**
> 
>   * [#4102](https://github.com/OctoPrint/OctoPrint/pull/4102) - Add option to revert back to former behaviour of always lower casing SD Card file names reported by the firmware to work around a bug in Prusa Firmware ([prusa3d/Prusa-Firmware#3115](https://github.com/prusa3d/Prusa-Firmware/issues/3115)). Auto detect Prusa Firmware and automatically enable this option if firmware autodetection is enabled. See also [#3994](https://github.com/OctoPrint/OctoPrint/issues/3994) for reference.
> 
> **Bug fixes**
>  
>   * [#4086](https://github.com/OctoPrint/OctoPrint/issues/4086) (regression) - GCode viewer: Fix visualization of models containing arcs, with "Center viewport on model" and "Zoom in on model" selected.