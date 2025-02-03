---

layout: post-rc
title: 'New release candidate: 1.11.0rc2'
author: foosel
date: 2025-02-03 15:15:00 +0100
card: /assets/img/blog/2025-02/2025-02-03-octoprint-1.11.0rc2-card.png
featuredimage: /assets/img/blog/2025-02/2025-02-03-octoprint-1.11.0rc2-card.png
poster: /assets/img/blog/2025-02/2025-02-03-octoprint-1.11.0rc2-poster.png

excerpt: The second release candidate for the upcoming 1.11.0 release containing some fixes of observed regressions and bugs in the first one!

release: 1.11.0rc2
channel: Maintenance RCs
feedback: 5101

closer_look:
- Proper behaviour when using the included web interface as well as any third party clients at your disposal.
- The newly added Custom Control Manager plugin.
- The newly added Health Check plugin.
- The newly added Upload Manager plugin.
- The MFA-TOTP plugin using the new MFA plugin interface.
- Timelapse creation, especially with a configured rendering delay.

---

This second release candidate for the upcoming 1.11.0 release fixes two regressions that were reported with the first one, as well as two bugs reported in newly added functionality:

> **✨ Features & improvements**
> 
> *Core*
> 
> - Improved Tornado and CSRF failure logging.
> 
> **🐛 Bug fixes**
> 
> *Core*
> 
> - [#5098](https://github.com/OctoPrint/OctoPrint/issues/5098) & [#5100](https://github.com/OctoPrint/OctoPrint/issues/5100) (regression): Fixed permission fetch and `login_mechanism` setting for incoming requests with API keys. This solves the problem with all requests with an API key being responded to with an HTTP status of 403, and any API key based requests not using `GET`, `HEAD` or `OPTIONS` methods with a CSRF validation failure and thus an HTTP Status of 400, breaking communication with most third party clients.
> - [#5099](https://github.com/OctoPrint/OctoPrint/issues/5099) (regression): Fixed templating macros being broken for third party plugins not supporting autoescaping.
> 
> *Custom Control Manager*
> 
> - [#5096](https://github.com/OctoPrint/OctoPrint/issues/5096): Fixed rendering of `horizontal_grid` custom control type.
> - [#5097](https://github.com/OctoPrint/OctoPrint/issues/5097): Added missing width/offset configuration.

For heads-ups, highlights and fancy pictures, please see [the earlier post about 1.11.0rc1](/blog/2025/01/28/new-release-candidate-1.11.0rc1/).
