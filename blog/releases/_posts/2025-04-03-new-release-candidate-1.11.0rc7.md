---

layout: post-rc
title: 'New release candidate: 1.11.0rc7'
author: foosel
date: 2025-04-03 15:20:00 +0200
card: /assets/img/blog/2025-04/2025-04-03-octoprint-1.11.0rc7-card.png
featuredimage: /assets/img/blog/2025-04/2025-04-03-octoprint-1.11.0rc7-card.png
poster: /assets/img/blog/2025-04/2025-04-03-octoprint-1.11.0rc7-poster.png

excerpt: The seventh release candidate for the upcoming 1.11.0 release containing a for a regression in the previous one!

release: 1.11.0rc7
channel: Maintenance RCs
feedback: 5133

closer_look:
- Proper behaviour when using the included web interface as well as any third party clients at your disposal.
- The newly added Custom Control Manager plugin.
- The newly added Health Check plugin.
- The newly added Upload Manager plugin.
- The MFA-TOTP plugin using the new MFA plugin interface.
- Timelapse creation, especially with a configured rendering delay.
- Remember me functionality.

---

It looks like I unintentionally hid an April's Fools joke on myself in 1.11.0rc6, in the shape of a session related regression. So here's 1.11.0rc7 fresh off the presses for you, 
fixing that bug:

> **🐛 Bug fixes**
> 
> *Core*
>
> - [#5132](https://github.com/OctoPrint/OctoPrint/issues/5132) (regression): Fix session keepalive not getting started. Side effect of the fix of [#5125](https://github.com/OctoPrint/OctoPrint/issues/5125).

For heads-ups, highlights and fancy pictures, please see [the earlier post about 1.11.0rc1](/blog/2025/01/28/new-release-candidate-1.11.0rc1/).
