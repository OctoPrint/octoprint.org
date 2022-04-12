---

layout: post-rc
title: 'New release candidate: 1.8.0rc5'
author: foosel
date: 2022-04-12 16:10:00 +0200
card: /assets/img/blog/2022-04/2022-04-12-octoprint-1.8.0rc5-card.png
featuredimage: /assets/img/blog/2022-04/2022-04-12-octoprint-1.8.0rc5-card.png
poster: /assets/img/blog/2022-04/2022-04-12-octoprint-1.8.0rc5-poster.png
excerpt: The fifth release candidate for the upcoming 1.8.0 release, fixing another observed regression with the first ones.

release: 1.8.0rc5
channel: Maintenance RCs
feedback: 4487

---

I'm virtually attending [PyConDE](https://2022.pycon.de/) right now but I still managed to somehow squeeze in a bug
fix for y'all in between attending talks and giving one myself 🥳 

This fifth RC of 1.8.0 fixes another regression observed with the first ones and also hardens things a bit further against misbehaving firmware:

> **Improvements**
>
>   * Harden against wonky firmware temperature responses that might lead to hotend or bed temperature values to be overwritten with something else by only ever using the first value for a sensor key seen in the response.
>
> **Bug fixes**
> 
>   * [#4486](https://github.com/OctoPrint/OctoPrint/issues/4486) (regression) - Fix changing of folder paths via the settings.

The fix also made me realize we need another heads-up:

> **Heads-up for plugin authors: `Settings._config` is read-only!**
> 
> If your plugin code has been using `Settings._config` to modify what gets stored in `config.yaml`, this will no longer work. It never was a supported method, however it did work due to how things were implemented internally. Implementation has changed now so that any code doing this will no longer work - the nested dictionary returned by the `Settings._config` is only a copy of the internal data structure and thus any modifications will be dropped silently. A deprecation warning has been added just in case. Use the provided `set` and `remove` methods on the settings object instead please.

