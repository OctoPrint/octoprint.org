---

layout: post-rc
title: 'New release candidate: 1.10.0rc3'
author: foosel
date: 2024-03-18 11:50:00 +0100
card: /assets/img/blog/2024-03/2024-03-18-octoprint-1.10.0rc3-card.png
featuredimage: /assets/img/blog/2024-03/2024-03-18-octoprint-1.10.0rc3-card.png
poster: /assets/img/blog/2024-03/2024-03-18-octoprint-1.10.0rc3-poster.png
excerpt: The third release candidate for the upcoming 1.10.0 release containing some fixes of observed regressions and improvements of newly added functionality, plus one security fix!

release: 1.10.0rc3
channel: Maintenance RCs
feedback: 4971

closer_look:
- Proper behaviour when using the included web interface as well as any third party clients at your disposal.
- User and group management functioning as expected.
- Plugin installation functioning as expected.
- Application key management functioning as expected. Authentication workflow with third party clients at your disposal (e.g. slicers) works as it should.
- Backup creation, download and restore functioning as expected.

contributors:
- jacopotediosi

first_time_contributors:
- jacopotediosi

---

This third release candidate for the upcoming 1.10.0 release includes one fix for a reported security issue, fixes some regressions that were reported with the first one, and also adds some improvements surrounding newly added functionality:

> **🔒 Security fixes**
> 
> - Severity Moderate (4.0): It was possible for a malicious admin to configure or to talk a victim with admin rights into configuring a webcam snapshot URL which when tested through the "Test" button included in the web interface would execute JavaScript code in the victim's browser when attempting to render the snapshot image. An attacker who successfully talked a victim with admin rights into performing a snapshot test with such a crafted URL could use this to retrieve or modify sensitive configuration settings, interrupt prints or otherwise interact with the OctoPrint instance in a malicious way.
> 
>   This has now been fixed by properly sanitizing the data received from the snapshot URL.
> 
>   See also the [GitHub Security Advisory](https://github.com/OctoPrint/OctoPrint/security/advisories/GHSA-x7mf-wrh9-r76c) and [CVE-2024-28237](https://nvd.nist.gov/vuln/detail/CVE-2024-28237).
> 
> **✨ Features & improvements**
> 
> *Core*
> 
> - [#4957](https://github.com/OctoPrint/OctoPrint/issues/4957): Bump `websocket-client` dependency to version 1.6.1, after verifying that it should still work with Python 3.7 in this version, to enable third party plugins to use bug fixes included in that version.
> - [PR#4964](https://github.com/OctoPrint/OctoPrint/pull/4964): Harden the filename sanitization in the `download_file` function against possible path traversal issue in future use cases.
> - Use `aria-label` and `role` instead of `sr-only` headings, resolving issues with the UI Customizer Plugin or other heavy CSS manipulation.
> - Use a reload popup instead of a blocking overlay modal on UI plugin and/or settings change. That should reduce the annoyance of the reload overlay popping up due to settings updates in the background. It should also help with the reload prompts sometimes observed during the newly introduced reauthentication workflow.
> 
> **🐛 Bug fixes**
> 
> *Core*
> 
> - [#4966](https://github.com/OctoPrint/OctoPrint/issues/4966) (regression): Fix handling of the reauthentication workflow for external users created & logged in from a configured header. 
> - [#4969](https://github.com/OctoPrint/OctoPrint/issues/4969) (regression): Fix the final page of the firstrun wizard interfering with the completion of arbitrary wizards from plugins, when not even shown.
> - Properly reflect that users logged in from a configured header can't log out through the logout button but rather must log out by closing the browser.
> 
> *Action Command Notification Plugin*
> 
> - [#4967](https://github.com/OctoPrint/OctoPrint/issues/4967) (regression): Fix the filter logic so that an empty filter regex won't lead to *all* notifications to be filtered out.

For heads-ups, highlights and fancy pictures, please see [the earlier post about 1.10.0rc1](/blog/2024/01/31/new-release-candidate-1.10.0rc1/).
