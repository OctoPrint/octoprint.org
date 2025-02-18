---

layout: post-rc
title: 'New release candidate: 1.11.0rc3'
author: foosel
date: 2025-02-18 15:30:00 +0100
card: /assets/img/blog/2025-02/2025-02-18-octoprint-1.11.0rc3-card.png
featuredimage: /assets/img/blog/2025-02/2025-02-18-octoprint-1.11.0rc3-card.png
poster: /assets/img/blog/2025-02/2025-02-18-octoprint-1.11.0rc3-poster.png

excerpt: The third release candidate for the upcoming 1.11.0 release containing some fixes of observed regressions and bugs in the previous ones, plus some improvements of newly added functionality!

release: 1.11.0rc3
channel: Maintenance RCs
feedback: 5111

closer_look:
- Proper behaviour when using the included web interface as well as any third party clients at your disposal.
- The newly added Custom Control Manager plugin.
- The newly added Health Check plugin.
- The newly added Upload Manager plugin.
- The MFA-TOTP plugin using the new MFA plugin interface.
- Timelapse creation, especially with a configured rendering delay.
- Remember me functionality.

---

This third release candidate for the upcoming 1.11.0 release fixes one regression that were reported with the previous ones, as well as one bug reported for 1.10.x. It also improves on functionality of the newly added Health Check plugin:

> **✨ Features & improvements**
> 
> *Health Check Plugin*
> 
> - [#5110](https://github.com/OctoPrint/OctoPrint/issues/5110): Allow to mark reported health check issues as read.
> 
> **🐛 Bug fixes**
> 
> *Core*
> 
> - [#5105](https://github.com/OctoPrint/OctoPrint/issues/5105) (regression): Fix the "Remeber me" functionality
> - [#5109](https://github.com/OctoPrint/OctoPrint/issues/5109): Fix `octoprint.systemcommands.SystemCommandManager.has_(server_restart|system_restart|system_shutdown)_command` not returning `False` for empty commands. Not a regression, but a small enough fix to still include in 1.11.0.

For heads-ups, highlights and fancy pictures, please see [the earlier post about 1.11.0rc1](/blog/2025/01/28/new-release-candidate-1.11.0rc1/).
