---

layout: post-rc
title: 'New release candidate: 1.7.0rc2'
author: foosel
date: 2021-08-11 14:40:00 +0200
card: /assets/img/blog/2021-08/2021-08-11-octoprint-1.7.0rc2-card.png
featuredimage: /assets/img/blog/2021-08/2021-08-11-octoprint-1.7.0rc2-card.png
poster: /assets/img/blog/2021-08/2021-08-11-octoprint-1.7.0rc2-poster.png
excerpt: The second release candidate for the upcoming 1.7.0 release, fixing two observed regressions and adding an improvement for new functionality.

release: 1.7.0rc2
channel: Maintenance RCs
feedback: 4206

---

This second RC of 1.7.0 fixes two regressions observed with the first one and adds an
improvement for new functionality:

> **Improvements**
> 
>   * [#4204](https://github.com/OctoPrint/OctoPrint/issues/4204) - Make the new event manager use the new (faster) CSS only modal fade in animation.
> 
> **Bug fixes**
>  
>   * [#4202](https://github.com/OctoPrint/OctoPrint/issues/4202) (regression) - Fix `None` handling error in print time estimation during print start.
>   * [#4203](https://github.com/OctoPrint/OctoPrint/issues/4203) (regression) - Only try to set low latency mode to True, never to False. Just don't do anything if low latency mode isn't requested.
