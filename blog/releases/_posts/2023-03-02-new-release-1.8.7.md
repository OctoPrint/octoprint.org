---

layout: post-bugfix
title: 'New release: 1.8.7'
author: foosel
date: 2023-03-02 16:45:00 +0200
card: /assets/img/blog/2023-03/2023-03-02-octoprint-1.8.7-card.png
featuredimage: /assets/img/blog/2023-03/2023-03-02-octoprint-1.8.7-card.png
poster: /assets/img/blog/2023-03/2023-03-02-octoprint-1.8.7-poster.png
excerpt: "This seventh bugfix release for 1.8.0 work around a breaking change of a dependency and adds support for Python 3.11."

bugfix: 1.8.7
release:
  tag: 1.8.0
  link: /blog/2022/05/17/new-release-1.8.0/
  headsups: true
prior:
  headsups:
  - release: 1.8.3
    link: /blog/2022/09/20/new-release-1.8.3/

contributors:
- cp2004

---

I was hoping to make 1.9.0 the first release of this year, but instead here's a hotfix for you all, made necessary by a breaking update of a third party dependency. This seventh bugfix release for 1.8.0 also adds compatibility with Python 3.11:

> **✨ Improvements**
> 
> - [#4488](https://github.com/OctoPrint/OctoPrint/issues/4488) - Add support for Python 3.11 by bumping up the version of a dependency.
> 
> **🐛 Bug fixes**
> 
> - [#4744](https://github.com/OctoPrint/OctoPrint/issues/4744) - Do not send `None` to `Locale.parse` if no match can be made between the request's accepted languages and the installed languages. Fixes a 500 server error on the API in case of Babel being at of version of 2.12 or higher.

You can also take a look at the [changelog on GitHub](https://github.com/OctoPrint/OctoPrint/releases/tag/1.8.7), but it's really short this time.

Like every single release (and release candidate) of OctoPrint ever since early 2016 this release was made possible only
through your continued **[support of my work](/support-octoprint/)** 💕
