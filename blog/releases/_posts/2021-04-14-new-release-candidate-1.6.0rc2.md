---

layout: post-rc
title: 'New release candidate: 1.6.0rc2'
author: foosel
date: 2021-04-14 15:25:00 +0200
card: /assets/img/blog/2021-04/2021-04-14-octoprint-1.6.0rc2-card.png
featuredimage: /assets/img/blog/2021-04/2021-04-14-octoprint-1.6.0rc2-card.png
poster: /assets/img/blog/2021-04/2021-04-14-octoprint-1.6.0rc2-poster.png
excerpt: The second release candidate for the upcoming 1.6.0 release, with some fixes of regressions from the first one and some improvements in newly added functionality.

release: 1.6.0rc2
channel: Maintenance RCs
feedback: 4093

headsups:
- title: "Heads-up for plugin authors: Support for the plugin control properties `__plugin_init__` and `__plugin_implementations__` (plural!) has been removed"
  content: >
    The two plugin control properties `__plugin_init__` and `__plugin_implementations__` (note the plural!)
    have been deprecated ever since OctoPrint 1.2.0 and have finally been removed.
  
    It is *highly* unlikely that your plugin has ever used them given that they were already
    marked as deprecated for the very first version of OctoPrint to ever even support plugins. 
    Still, just in the case of anyone out there making use of them regardless, here's a 
    heads-up that they will no longer be utilized in OctoPrint 1.6+.
    
contributors:
- cp2004

---

This second RC of 1.6.0 fixes some regressions observed with the first one, improves some things
in newly added and changed functionality and also adds some additional debug options to the
GCODE viewer to help in future analyses:

> **Improvements**
> 
>   * [#4071](https://github.com/OctoPrint/OctoPrint/pull/4071) - Better change of plugin manager styling that has better compatibility with some third party plugins.
>   * GCODE viewer: Option to render a layer specific bounding box, to help with further analysis of [#4086](https://github.com/OctoPrint/OctoPrint/issues/4086).
>   * GCODE viewer: Option to render line segment starts, to help with further analysis of [#4086](https://github.com/OctoPrint/OctoPrint/issues/4086).
>   * GCODE Analysis: New command line option `--layers` will also calculate and output layer stats. Recognizes zhop. To help with further analysis of [#4086](https://github.com/OctoPrint/OctoPrint/issues/4086).
> 
> **Bug fixes**
>  
>   * [#4080](https://github.com/OctoPrint/OctoPrint/issues/4080) (regression) - Fix horizontal scrollbar size in Safari and get rid of horizontal scrolling in notifications altogether.
>   * [#4082](https://github.com/OctoPrint/OctoPrint/issues/4082) (regression) - Fix SD card printing