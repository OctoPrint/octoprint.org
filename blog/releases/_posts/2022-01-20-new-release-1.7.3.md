---

layout: post-bugfix
title: 'New release: 1.7.3'
author: foosel
date: 2022-01-20 12:15:00 +0100
card: /assets/img/blog/2022-01/2022-01-20-octoprint-1.7.3-card.png
featuredimage: /assets/img/blog/2022-01/2022-01-20-octoprint-1.7.3-card.png
poster: /assets/img/blog/2022-01/2022-01-20-octoprint-1.7.3-poster.png
excerpt: "This bugfix release fixes an issue in 1.7.x and works around a new dependency incompatibility."

bugfix: 1.7.3
release:
  tag: 1.7.0
  link: /blog/2021/10/11/new-release-1.7.0/
  headsups: true

contributors:
- kantlivelong

---

The first release of 2022 is a bugfix release for 1.7.x containing one bugfix and one workaround
for a dependency incompatibility introduced last night:

>   * [#4294](https://github.com/OctoPrint/OctoPrint/issues/4294) - Fix blacklist processing. (PR [#4296](https://github.com/OctoPrint/OctoPrint/pull/4296))
>   * [#4377](https://github.com/OctoPrint/OctoPrint/issues/4377) - Pin `regex` dependency to `<2022.1.18` under Python 2, as that and later versions are Python-3-only. [**If you still haven't upgraded to Python 3, 
please do so already!**](https://faq.octoprint.org/python3-update)

You can also take a look at the [extremely short changelog on GitHub](https://github.com/OctoPrint/OctoPrint/releases/tag/1.7.3).

Like every single release (and release candidate) of OctoPrint ever since early 2016 this release was made possible only
through your continued **[support of my work](/support-octoprint/)** 💕
