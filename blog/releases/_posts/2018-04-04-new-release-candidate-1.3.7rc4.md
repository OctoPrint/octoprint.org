---

layout: post
title: 'New release candidate: 1.3.7rc4'
author: foosel
date: 2018-04-04 12:00:00 +0200
card: /assets/img/blog/2018-04/2018-04-04-octoprint-1.3.7rc4-card.png
featuredimage: /assets/img/blog/2018-04/2018-04-04-octoprint-1.3.7rc4-card.png
poster: /assets/img/blog/2018-04/2018-04-04-octoprint-1.3.7rc4-poster.png
excerpt: This fourth release candidate fixes three bugs that were discovered and reported over the easter weekend in the 1.3.7 RCs.

---

This fourth release candidate fixes three bugs (one in new functionality, the other two regressions) that were 
discovered and reported over the easter weekend in the 1.3.7 RCs:

  * [#2536](https://github.com/foosel/OctoPrint/issues/2536) - Fix a wrong state tracking when starting an SD print through the controller, causing a disconnect due to a timeout.
  * [#2544](https://github.com/foosel/OctoPrint/issues/2544) - Fix an exception when connecting to the raw websocket at `/sockjs/websocket` (instead of `/sockjs/<server_id>/<session_id>/websocket`).
  * [#2546](https://github.com/foosel/OctoPrint/issues/2546) - Fix the `PRINT_FAILED` event getting triggered twice on print failure due to disconnect
  
**If you are tracking the "Maintenance RC" release channel**, you should soon get an update notification just like you 
are used to from stable releases.

If you want to help test this release candidate and **aren't yet tracking the "Maintenance RCs" release channel**, you
can find information on how to switch [in this guide](https://faq.octoprint.org/using-release-channels)
(also linked below).

**If you are not interested in helping to test release candidates**, just ignore this post, 1.3.7 stable will hit 
your instance via the usual way once it's ready 😊

You can find the full changelog and release notes as usual [on Github](https://github.com/foosel/OctoPrint/releases/tag/1.3.7rc4).

**Please provide feedback** on this RC. For general feedback you can use 
[this ticket on the tracker](https://github.com/foosel/OctoPrint/issues/2548).
The information that everything works fine for you is also valuable feedback 😄 For bug reports please follow
["How to file a bug report"](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report).

Depending on how the feedback for this release candidate turns out, I'll either look into releasing 1.3.7 or fix any 
observed regressions and push out a new release candidate ASAP.

### Links

  * [Ticket for general feedback](https://github.com/foosel/OctoPrint/issues/2548)
  * [Changelog and Release Notes](https://github.com/foosel/OctoPrint/releases/tag/1.3.7rc4)
  * [How to use release channels to help test release candidates](https://faq.octoprint.org/using-release-channels)
  * [How to file a bug report](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md#how-to-file-a-bug-report)
  * [Contribution Guidelines (also relevant for creating bug reports!)](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md)
  * [FAQ](https://faq.octoprint.org)
  * [Documentation](http://docs.octoprint.org/)
  * [How to roll back to an earlier release (OctoPi)](https://discourse.octoprint.org/t/how-can-i-revert-to-an-older-version-of-the-octoprint-installation-on-my-octopi-image/205)
  * [How to roll back to an earlier release (manual install)](https://discourse.octoprint.org/t/how-can-i-roll-back-to-an-earlier-version-after-an-update/234)
