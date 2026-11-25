---
title: "New release: 2.0.2"
author: foosel
date: 2026-11-25 13:00:00 +0100

contributors:
- jacopotediosi
- hyperair

tags:
- release

summary: "The second bugfix release for 2.0.x, fixing a some issues reported since the release of 2.0.0."

release: 2.0.2

stable:
  tag: 2.0.0
  link: /blog/2026/11/16/new-release-2.0.0/
  headsups: true
---

Over the weekend, I got a few more bugs reported on 2.0.x, and so I spent Monday and Tuesday fixing those
before just now packaging up OctoPrint 2.0.2. The change log shows you that it was a quite busy few days:

> **🐛 Bug fixes**
> 
> *Core*
> 
> - [#5487](https://github.com/OctoPrint/OctoPrint/issues/5487): Re-enable controls while paused.
> - [#5488](https://github.com/OctoPrint/OctoPrint/issues/5488): Fix refreshing of thumbnails after re-upload. Also make sure thumbnails files are actually deleted when deleting a file.
> - [#5489](https://github.com/OctoPrint/OctoPrint/issues/5489): Fix deleting a loaded, non printing file.
> - [#5490](https://github.com/OctoPrint/OctoPrint/issues/5490): Fix custom controls with slider inputs. Also automatically detect what kind of placeholders are used in a custom control (old style `%(foo)s` or new style `{foo}`) and use the matching formatter, instead of forcing new style on 2.0.0 clients. See also [PR#5492](https://github.com/OctoPrint/OctoPrint/pull/5492).
> - [#5504](https://github.com/OctoPrint/OctoPrint/issues/5504): Fix two wrongly handled permission checks:
>   - Use `TIMELAPSE_DOWNLOAD` on the timelapse download endpoints instead of `TIMELAPSE_LIST`
>   - Check for `FILES_DELETE` when attempting to overwrite a file. In that case, also check if the file to be overwritten is currently busy.
> - Limit payload of `ConnectionAutorefreshed` event if user doesn't have the `CONNECTION` permission.
> - Keep the id of the last used connector to ensure proper reporting of the used connector in case of `PrintFailed` events triggered when the connection got already closed.
> - Update dependency from `libpass` to `passlib` under Python 3.11 and up.
> 
> *Serial Connector Plugin*
> 
> - [#5493](https://github.com/OctoPrint/OctoPrint/issues/5493): Fix a crash when a printer's file name doesn't contain a `/` while trying to detect a printer side dummy job for an unknown file. 
> - [#5499](https://github.com/OctoPrint/OctoPrint/issues/5499): Fix a case matching issue causing printer files that the printer reports with upper case names couldn't be associated with a user created job (which due to a bug got created with the lower case version of a reported name).

You can also take a look at the [changelog on GitHub](https://github.com/OctoPrint/OctoPrint/releases/tag/2.0.1).

Like every single release (and release candidate) of OctoPrint ever since early 2016 this release was made possible only
through continued financial support by people like you! 💕

**[Click here](/support-octoprint/) if you enjoy OctoPrint and want to help with its funding!**
