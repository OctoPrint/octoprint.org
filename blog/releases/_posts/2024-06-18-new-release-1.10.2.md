---
layout: post-bugfix
title: 'New release: 1.10.2'
author: foosel
date: 2024-06-18 10:00:00 +0200
card: /assets/img/blog/2024-06/2024-06-18-octoprint-1.10.2-card.png
featuredimage: /assets/img/blog/2024-06/2024-06-18-octoprint-1.10.2-card.png
poster: /assets/img/blog/2024-06/2024-06-18-octoprint-1.10.2-poster.png

excerpt: "The second bugfix release for 1.10.x, fixing several bugs reported since the release of 1.10.1."

bugfix: 1.10.2
release:
  tag: 1.10.0
  link: /blog/2024/04/24/new-release-1.10.0/
  headsups: true

prior:
  headsups:
  - release: 1.10.1
    link: /blog/2024/05/14/new-release-1.10.1/


---

This second bugfix release for 1.10.x fixes several bugs:

> **🐛 Bug fixes**
>
> *Core*
>
> - [#5002](https://github.com/OctoPrint/OctoPrint/issues/5002): Fix a translation string in the german translation.
> - [#5019](https://github.com/OctoPrint/OctoPrint/issues/5019): Fix/workaround for a third party dependency change, breaking the `octoprint dev plugin:new` command.
> - [#5021](https://github.com/OctoPrint/OctoPrint/issues/5021): Fix behaviour of "Hide successful prints" filter in the file list. Folders will be shown as long as they have at least one file in them that has not been printed successfully yet, and they will also be shown if they contain the currently selected file, regardless of the amount of successful prints.
> - Fix an import to be compatible to Jinja2>=3.1.3.
> - Pin pydantic to 1.10.16 to work around an issue with Python 3.12.4.
> 
> *Achievements Plugin*
> 
> - [#5017](https://github.com/OctoPrint/OctoPrint/issues/5017): Fix a string in the german translation that caused the Achievements overview to not correctly render if german language was selected.
> - [#5027](https://github.com/OctoPrint/OctoPrint/issues/5027): Fix description of the Adventurer achievement
> - Fix event processing if the backup or plugin manager plugins are disabled.

You can also take a look at the [changelog on GitHub](https://github.com/OctoPrint/OctoPrint/releases/tag/1.10.2).

Like every single release (and release candidate) of OctoPrint ever since early 2016 this release was made possible only
through continued financial support by people like you! 💕 

**[Click here](/support-octoprint/) if you enjoy OctoPrint and want to help with its funding!**
