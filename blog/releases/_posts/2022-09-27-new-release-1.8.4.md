---

layout: post-bugfix
title: 'New release: 1.8.4'
author: foosel
date: 2022-09-27 17:00:00 +0200
card: /assets/img/blog/2022-09/2022-09-27-octoprint-1.8.4-card.png
featuredimage: /assets/img/blog/2022-09/2022-09-27-octoprint-1.8.4-card.png
poster: /assets/img/blog/2022-09/2022-09-27-octoprint-1.8.4-poster.png
excerpt: "This fourth bugfix release for 1.8.0 fixes a few newly reported issues and introduces a reverse proxy test page."
images:
- url: /assets/img/blog/2022-09/2022-09-27-screenie-reverse-proxy-test-yay.png
  title: OctoPrint's new reverse proxy test page. All checks are green.
- url: /assets/img/blog/2022-09/2022-09-27-screenie-reverse-proxy-test-nay.png
  title: OctoPrint's new reverse proxy test page. There's a mismatch in Protocol, Port, Path and thus Cookie Suffix between client and server that the test page marks as failed check.

bugfix: 1.8.4
release:
  tag: 1.8.0
  link: /blog/2022/05/17/new-release-1.8.0/
  headsups: true
prior:
  headsups:
  - release: 1.8.3
    link: /blog/2022/09/20/new-release-1.8.3/

---

This fourth bugfix release for 1.8.0 fixes a few recently reported bugs and introduces the new reverse proxy test page (see below for screenshots):

> **✨ Improvements**
> 
> - Added a new reverse proxy test page under `/reverse_proxy_test` (e.g. `http://octopi.local/reverse_proxy_test` or `https://example.com/octoprint/reverse_proxy_test`). This can be used to determine whether you have configured any reverse proxies that are between you and OctoPrint correctly, and if not where the error might lie. This should help in debugging issues caused by misconfigured reverse proxies and the CSRF protection introduced in 1.8.3.
> - Switched the `SameSite` setting on cookies to `Lax`. `Strict` was causing issues for users who navigate to their OctoPrint instance using a custom start page, since `SameSite=Strict` would suppress all cookies in that case, forcing you to login again. Please note that you can switch it to `Strict` yourself via the `server.cookies.samesite` configuration option, if you so desire for slightly increased security, and don't need the ability to access your OctoPrint instance from a link on another page while still staying logged in.
> 
> **🐛 Bug fixes**
> 
> - [#4648](https://github.com/OctoPrint/OctoPrint/issues/4648) - Fix passive login with global API key. The `_api` user could not be looked up for cookie signatures, this has been rectified.
> - [#4648](https://github.com/OctoPrint/OctoPrint/issues/4648) - Invalid API keys now correctly report that they are invalid instead of being treated like a guest user. 
> - [#4648](https://github.com/OctoPrint/OctoPrint/issues/4648) - Guest users on the API (no browser context, no API key) are now properly handled and no longer assumed to be a browser session, thus triggering CSRF protection.
> - [#4650](https://github.com/OctoPrint/OctoPrint/issues/4650) - Fix setting CSRF cookie on cached responses. This bug could prevent the UI from working if it was served from the browser's cache in combination with a `304 Not Modified` response from the server, instead of being freshly generated.
> - [#4653](https://github.com/OctoPrint/OctoPrint/issues/4653) - Fix handling of reauth requests on the websocket with reason `stale`, also send a `stale` reauth request in case of attempting to `auth` with an unknown user/session combo.
> - Fixed fallback to pbkdf2_sha256 if argon2 backend is missing for password hashing. The `argon2_cffi` dependency is still required and *should* be automatically installed on installation of OctoPrint 1.8.3+, but if for whatever reason that (partially) fails, OctoPrint will now gracefully fallback to a different password hashing algorithm while logging a warning about that, instead of just spewing errors.

You can also take a look at the [changelog on GitHub](https://github.com/OctoPrint/OctoPrint/releases/tag/1.8.4) which is on the shorter side again.

Like every single release (and release candidate) of OctoPrint ever since early 2016 this release was made possible only
through your continued **[support of my work](/support-octoprint/)** 💕
