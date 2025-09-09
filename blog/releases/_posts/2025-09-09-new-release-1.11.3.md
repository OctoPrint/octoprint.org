---
layout: post-bugfix
title: "New release: 1.11.3"
author: foosel
date: 2025-09-09 10:00:00 +0200
card: /assets/img/blog/2025-09/2025-09-09-octoprint-1.11.3-card.png
featuredimage: /assets/img/blog/2025-09/2025-09-09-octoprint-1.11.3-card.png
poster: /assets/img/blog/2025-09/2025-09-09-octoprint-1.11.3-poster.png

excerpt: "The third bugfix release for 1.11.x, fixing some bugs, security issues and user experience problems reported since the release of 1.11.0."

bugfix: 1.11.3
release:
  tag: 1.11.0
  link: /blog/2025/04/22/new-release-1.11.0/
  headsups: true
prior:
  headsups:
    - release: 1.11.2
      link: /blog/2025/06/10/new-release-1.11.2/

headsups:
  - title: "🔒 Explicitly configure whether to use shell mode for your system event subscriptions"
    content: |
      OctoPrint 1.11.3 introduces a new `shell` parameter on `type: system` commands that allows to specify whether the command should be run in a shell (`true`, *currently* the default) or directly (`false`, the *future* default).

      Running commands in a shell has security implications as a misconfigured command with placeholders coming from external, potential untrusted sources can lead to arbitrary command execution. However, running commands in a shell also allows for more powerful scripting and also access to the shell’s environment, making it often unnecessary to set the full paths of commands that are supposed to be run.

      OctoPrint so far has been running system commands defined in event hooks within a shell. Starting with OctoPrint 1.11.3, OctoPrint will log a message to `octoprint.log` when it encounters a system hook that hasn’t yet explicitly configured `shell`, and default to enabling shell mode. From 1.13.0 onward, **this behaviour will change**, and OctoPrint will default to not enabling shell mode in such cases, to further reduce the attack surface.

      You should make an explicit decision now. Try to make your commands work without having to enable shell mode, and thoroughly vet your commands and parameter processing if you have to enable shell mode. 

      The bundled Event Manager's UI has been adjusted to allow you to configured the `shell` parameter.
  - title: "🔥 Switch to Application Keys, the global API key will be removed in 1.13.0"
    content: |
      The global API key has been deprecated for a long time now. So far the deprecation notice said it would be removed in OctoPrint 2.0, however this now has been rescheduled to OctoPrint 1.13.0.

      OctoPrint 1.12.0 will prepare this removal further and ship with a new health check enabled that will detect if you have a global API key set. OctoPrint 1.13.0 will then remove it altogether.

      Instead of using the global key you should create individual [Application Keys](https://docs.octoprint.org/en/main/bundledplugins/appkeys.html) for your third party clients. That way they get permissions matching the user account used for key creation and you can also revoke access to one app without having to change the keys for all other apps. It's also recommended to create a user account without admin access and use that for third party clients where possible.

security:
  - "[@prabhatverma47](https://github.com/prabhatverma47)"
---

<div class="alert">
  <p>
    piwheels is currently pushing out a broken tornado package on Raspberry Pis <em>running Python 3.11</em> (e.g. OctoPi 1.1.0), which causes a semi-broken
    OctoPrint UI when updating from an earlier version to 1.11.x.
  </p>
  <p>
    This issue <a href="https://github.com/piwheels/packages/issues/582" target="_blank">has already been reported to piwheels</a>, but until it is
    fixed, if you are still on a version prior to 1.11.x, e.g. 1.10.x, please either hold off from updating to 1.11.x for now <em>and check back here periodically</em>,
    or update and follow <a href="https://community.octoprint.org/t/64761" target="_blank">the steps outlined in the FAQ about this issue</a>.
  </p>
</div>

This third bugfix release for 1.11.x fixes some bugs, security issues and user experience problems reported since the release of 1.11.0:

> **🔒 Security fixes**
>
> - **RCE in OctoPrint via Unsanitized Filename in File Upload**, severity High (7.5): OctoPrint versions up until and including 1.11.2 contain
>   a vulnerability that allows an authenticated attacker to upload a file under a specially crafted filename that will allow arbitrary command
>   execution if said filename becomes included in a command defined in a system event handler and said event gets triggered.
>
>   If no event handlers executing system commands with uploaded filenames as parameters have been configured, this vulnerability does not have an impact.
>
>   See also the [GitHub Security Advisory](https://github.com/OctoPrint/OctoPrint/security/advisories/GHSA-49mj-x8jp-qvfc) and [CVE-2025-58180](https://nvd.nist.gov/vuln/detail/CVE-2025-58180)
>
> _Minor Security fixes_
>
> - [#5169](https://github.com/OctoPrint/OctoPrint/issues/5169): Got rid of unused and unneeded cookie setter functionality in `LargeResponseHandler` as it
>   could be used to break returned responses through used input.
>
> **✨ Features & improvements**
>
> _Application Keys Plugin_
>
> - Added a new CLI command to trigger the appkey request workflow, see `octoprint plugin appkeys:request-key --help` for details.
>
> _Event Manager Plugin_
>
> - Allow configuring whether to enable shell mode on a system event hook.
> - Slight UI changes to improve UX.
>
> _Healthcheck Plugin_
>
> - New healthcheck to check for deprecated global API key being set and possibly used, disabled for now, will be enabled with 1.12.0
>
> **🐛 Bug fixes**
>
> _Core_
>
> - [#5177](https://github.com/OctoPrint/OctoPrint/issues/5177): Removed an unwanted side effect on `HierarchicalChainMap._unflatten`
>   that could make it impossible to reset the run-time value of a `dict`-based setting back to an empty dict.
> - Got rid of any uses of the `cgi` module, which has been deprecated for a while now and removed from Python 3.13+.
> - Added a note that the global API key will be removed with the release of OctoPrint 1.13.0.
> - Pinned the `psutil` dependency to version 6.0.0 to work around a problem with its builds available on piwheels.
>
> _Application Keys Plugin_
>
> - [#5170](https://github.com/OctoPrint/OctoPrint/issues/5170): Fix access request handling on newly opened page
>
> _Upload Manager Plugin_
>
> - Use proper name for `filesViewModel` instead of deprecated name `gcodeFilesViewModel`.

You can also take a look at the [changelog on GitHub](https://github.com/OctoPrint/OctoPrint/releases/tag/1.11.3).

Like every single release (and release candidate) of OctoPrint ever since early 2016 this release was made possible only
through continued financial support by people like you! 💕

**[Click here](/support-octoprint/) if you enjoy OctoPrint and want to help with its funding!**
