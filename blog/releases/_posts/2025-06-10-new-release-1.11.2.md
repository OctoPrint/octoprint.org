---
layout: post-bugfix
title: 'New release: 1.11.2'
author: foosel
date: 2025-06-10 13:00:00 +0200
card: /assets/img/blog/2025-06/2025-06-10-octoprint-1.11.2-card.png
featuredimage: /assets/img/blog/2025-06/2025-06-10-octoprint-1.11.2-card.png
poster: /assets/img/blog/2025-06/2025-06-10-octoprint-1.11.2-poster.png

excerpt: "The second bugfix release for 1.11.x, fixing some bugs, security issues and user experience problems reported since the release of 1.11.0."

bugfix: 1.11.2
release:
  tag: 1.11.0
  link: /blog/2025/04/22/new-release-1.11.0/
  headsups: true

headsups:
- title: "🧩 `SimpleApiPlugin`s can now opt-into enforced authentication on their endpoints, a future version of OctoPrint will require an opt-out to prevent this"
  content: |
    Starting with OctoPrint 1.11.2, OctoPrint now ships with a new method [`SimpleApiPlugin.is_api_protected`](https://docs.octoprint.org/en/master/plugins/mixins.html#octoprint.plugin.SimpleApiPlugin.    is_api_protected) on its `SimpleApiPlugin` mixin that, similar to the long existing [`BlueprintPlugin.is_blueprint_protected`](https://docs.octoprint.org/en/master/plugins/mixins.html#octoprint.plugin.BlueprintPlugin.is_blueprint_protected), tells OctoPrint whether some basic authentication enforcing should be done by OctoPrint on its endpoints or not.
    
    For now, this method by default will return `False`, effectively keeping the current behaviour of plugins having to implement their own authentication in `SimpleApiPlugin.on_api_get` and `SimpleApiPlugin.    on_api_command`. However, this behaviour will change in a future version of OctoPrint (current plan is 1.13.0) to return `True` instead, effectively enforcing some basic user authentication on all     `SimpleApiPlugin`s.
    
    Plugin authors should adjust their plugins *now* and explicitly opt-into protection by implementing `is_api_protected` liek this:
    
    ``` python
    def is_api_protected(self):
        return True
    ```
    
    If this does *not* work with their plugin, they should explicitly opt *out* by returning `False` here (and *implement their own authentication* as needed).
    
    Plugins that have not yet explicitly implemented the above method will cause a warning to be logged in `octoprint.log`.

security:
- "[Jacopo Tediosi](https://github.com/jacopotediosi)"

---

This second bugfix release for 1.11.x fixes some bugs, security issues and user experience problems reported since the release of 1.11.0:

> **🔒 Security fixes**
> 
> - **File exfiltration possible via upload endpoints**, severity Moderate (5.4): OctoPrint versions up until and including 1.11.1 contain a vulnerability that allows an attacker with the `FILE_UPLOAD` permission to exfiltrate files from the host that OctoPrint has read access to, by moving them into the upload folder where they then can be downloaded from.
> 
>   The primary risk lies in the potential exfiltration of secrets stored inside OctoPrint's config, or further system files. By removing important runtime files, this could also be used to impact the availability of the host. Given that the attacker requires a user account with file upload permissions, the actual impact of this should however hopefully be minimal in most cases.
> 
>   See also the [GitHub Security Advisory](https://github.com/OctoPrint/OctoPrint/security/advisories/GHSA-m9jh-jf9h-x3h2) and [CVE-2025-48067](https://nvd.nist.gov/vuln/detail/CVE-2025-48067)
> 
> - **Denial of Service through malformed HTTP request in OctoPrint**, severity Moderate (6.5): OctoPrint versions up until and including 1.11.1 contain a vulnerability that allows any unauthenticated attacker to send a manipulated broken `multipart/form-data` request to OctoPrint and through that make the web server component become unresponsive. This could be used to effectively run a denial of service attack on the OctoPrint server.
> 
>   See also the [GitHub Security Advisory](https://github.com/OctoPrint/OctoPrint/security/advisories/GHSA-9wj4-8h85-pgrw) and [CVE-2025-48879](https://nvd.nist.gov/vuln/detail/CVE-2025-48879)
> 
> *Minor Security fixes*
> 
> - Core: Only allow bypassing CSRF protection with a provided API key. Before, OctoPrint would also disable CSRF protection if there was absolutely no session context (e.g. a manual `curl` request). Also added some E2E tests for that.
> - Application Keys Plugin: Added a strong warning to the application keys dialog that allowing an app to create an appkey will give it the user's permissions. Also added the remote address from which the appkey request is  coming from. 
> - Application Keys Plugin: Added a rate limit on the app keys request endpoint, to reduce the likelihood of an attacker on the local network spamming the instance with requests that the user then might accidentally allow.
> 
> **✨ Features & improvements**
> 
> *Core*
> 
> - [#5158](https://github.com/OctoPrint/OctoPrint/issues/5158): Pinned the third-party Click dependency to anything but 8.2.0 as that has a bug in how it parses boolean flags, leading to issues with e.g. `octoprint user add --admin` not working when it is installed.
> - Added a new decorator [`BlueprintPlugin.limit`](https://docs.octoprint.org/en/master/plugins/mixins.html#octoprint.plugin.BlueprintPlugin.limit) to decorate endpoints with a rate limiter.
> - Added a method `SimpleApiPlugin.is_api_protected` to query whether the API endpoints should have some basic authentication added by OctoPrint, similar to `BluePrintPlugin.is_blueprint_protected`. For now this method will return `False` (and log a warning to `octoprint.log`, prompting plugin authors to implement it explicitly). In a future OctoPrint version - current plan is 1.13.0 - this will default to `True`, enforcing basic protection on all `SimpleApiPlugin` implementations. See also the corresponding heads-up.
> 
> *CI*
> 
> - Now building PEP625 compatible sdists & wheels, and no longer building deprecated universal wheels.
> 
> **🐛 Bug fixes**
> 
> *Core*
> 
> - [#5156](https://github.com/OctoPrint/OctoPrint/issues/5156): Fix 403 errors triggered by `access_validation_factory` due to missing permissions getting turned into HTTP 500.
> - [#5161](https://github.com/OctoPrint/OctoPrint/issues/5161): Fixed the Reverse Proxy Test page not working when pydantic 1.x is installed (Python 3.7).
> - Made `octoprint dev plugin:install` work with `setuptools` >= 80.x and legacy plugin packaging.
> - Fixed a typo in an internal method call causing plugin loading errors for specific packaging scenarios.
> - Fixed escaping of whitespace for native `grep` calls.
> 
> *Upload Manager Plugin*
> 
> - [#5162](https://github.com/OctoPrint/OctoPrint/issues/5162): Fixed sorting by "last printed date".

You can also take a look at the [changelog on GitHub](https://github.com/OctoPrint/OctoPrint/releases/tag/1.11.2).

Like every single release (and release candidate) of OctoPrint ever since early 2016 this release was made possible only
through continued financial support by people like you! 💕 

**[Click here](/support-octoprint/) if you enjoy OctoPrint and want to help with its funding!**
