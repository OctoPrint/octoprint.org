---

layout: post-rc
title: 'New release candidate: 1.11.0rc6'
author: foosel
date: 2025-04-01 12:15:00 +0200
card: /assets/img/blog/2025-04/2025-04-01-octoprint-1.11.0rc6-card.png
featuredimage: /assets/img/blog/2025-04/2025-04-01-octoprint-1.11.0rc6-card.png
poster: /assets/img/blog/2025-04/2025-04-01-octoprint-1.11.0rc6-poster.png

excerpt: The sixth release candidate for the upcoming 1.11.0 release containing a few fixes of observed regressions & bugs in the previous ones!

release: 1.11.0rc6
channel: Maintenance RCs
feedback: 5129

contributors:
- jacopotediosi

closer_look:
- Proper behaviour when using the included web interface as well as any third party clients at your disposal.
- The newly added Custom Control Manager plugin.
- The newly added Health Check plugin.
- The newly added Upload Manager plugin.
- The MFA-TOTP plugin using the new MFA plugin interface.
- Timelapse creation, especially with a configured rendering delay.
- Remember me functionality.

---

It may be April 1st, but this sixth RC is not a joke and comes with a few fixes of observed regressions & bugs:

> **🐛 Bug fixes**
> 
> *Core*
>
> - [#5125](https://github.com/OctoPrint/OctoPrint/issues/5125) (regression): Fix reauthentication logic to not log out on reauth. This is actually not a real regression and was present in 1.10.x as well, but changes in 1.11.0 made it almost *always* trigger vs almost never on 1.10.x (due to some race condition), so it feels like a regression and needed fixing in the RC phase.
> - Fix a redirect path traversal bug in `validate_local_redirect`. This in theory could have been abused by some manipulated link to redirect a login to a path on the same server as OctoPrint beyond those marked as safe, e.g. a malicious plugin or an external app on another path. Not a regression, but better fix this now than later. Thanks to [@jacopotediosi](https://github.com/jacopotediosi) for the discovery and the suggested fix.
> 
> *Error Tracking Plugin*
> 
> - (regression) Silence some Sentry log spam
> - (regression) Fix an issue in the ignored exception filter causing no errors to be reported

For heads-ups, highlights and fancy pictures, please see [the earlier post about 1.11.0rc1](/blog/2025/01/28/new-release-candidate-1.11.0rc1/).
