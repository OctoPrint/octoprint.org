---
title: "An Open Letter to OctoPrint's Plugin Authors"
author: foosel
date: 2026-09-01 15:00:00 +0200
summary: OctoPrint 2.0.0 is now on the fifth release candidate and getting close to the stable release. It's really time to look into your plugin's compatibility, if not done yet!

tags:
- development

card: /assets/img/blog/2026-09/2026-09-01-open-letter-card.png
featuredimage: /assets/img/blog/2026-09/2026-09-01-open-letter-card.png
poster: /assets/img/blog/2026-09/2026-09-01-open-letter-poster.png
---

OctoPrint 2.0.0 is now on the fifth release candidate and after four months of a release candidate phase we are getting close to the stable release.

[Back in April I wrote](https://octoprint.org/blog/2026/04/20/octoprint-2.0.0-is-coming-soon/) that plugin authors should **go through [the Migration Guide](https://docs.octoprint.org/en/dev/plugins/migration_2_0_0.html)** and check whether their plugin is affected by any of the points listed therein. The [`octoscanner` tool](https://github.com/jacopotediosi/octoscanner) provided by Jacopo Tediosi was also made available around that time, to further help in identifying any kind of issues. Furthermore, several PRs have been sent to the more popular plugins to help with getting them migrated.

Plenty of you have responded to these efforts, migrated their plugins and released new, compatible, versions. Thank you for that! 🚀

However, there are some hold-outs, and I'd like to once more implore you: If you are the author of an OctoPrint plugin, haven't yet checked whether your plugin needs migration, maybe even have been ignoring some migration PRs sent your way, _please take care of this now_. If you no longer want to maintain your plugin, that's fine too, but in that case, please give it up for adoption so we can find a solution for your users. If you keep ignoring this call to action, at some point we might have to force-adopt your plugin for the sake of OctoPrint's users, which we'd rather not.

Thank you! 💚
