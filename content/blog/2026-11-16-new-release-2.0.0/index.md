---
title: "New release: 2.0.0"
author: foosel
date: 2026-11-16 14:45:00 +0100
release: 2.0.0

contributors:
- Ajimaru
- beelsebob
- bradyjoh
- emmanuel-ferdman
- Hillshum
- jacopotediosi
- jneilliii
- kubedzero
- willschlitzer

security:
- "[colinthebomb1](https://github.com/colinthebomb1)"
- "[d3do-23](https://github.com/d3do-23)"
- "[SounLabs](https://github.com/SounLabs)"
- "[lml20000827](https://github.com/lml20000827)"
- "[xIllunight](https://github.com/xIllunight)"

first_time_contributors:
- Ajimaru
- beelsebob
- bradyjoh
- emmanuel-ferdman
- Hillshum
- kubedzero
- sanjay900
- willschlitzer

testers:
- Ajimaru
- AlexDashwood
- b-morgan
- ckuethe
- corpjester
- gfaugere
- gleonard3
- IdleNet
- jacopotediosi
- jneilliii
- lexitus
- redRock14
- rodrigorc
- St-Aris
- varukasalt

stats:
  totalinstances: 973
  totalprinttime: 17812
  rcs:
  - tag: 2.0.0rc6
    date: 2026-10-07
    instances: 264
    printtime: 2350
  - tag: 2.0.0rc7
    date: 2026-10-20
    instances: 422
    printtime: 5453
  rcs_incomplete:
  - tag: 2.0.0rc1
    date: 2026-04-27
    instances: 26
    printtime: 243
  - tag: 2.0.0rc2
    date: 2026-05-19
    instances: 55
    printtime: 303
  - tag: 2.0.0rc3
    date: 2026-06-23
    instances: 37
    printtime: 286
  - tag: 2.0.0rc4
    date: 2026-07-14
    instances: 134
    printtime: 1119
  - tag: 2.0.0rc5
    date: 2026-08-24
    instances: 438
    printtime: 8556

headsups:
- title: "Heads-up: OctoPrint 2.0.0 requires Python 3.9+"
  content: |
    This release of OctoPrint requires **Python 3.9+**. Python 3.7 & 3.8, still supported by OctoPrint 1.11.x, are no longer supported. [Please also see this FAQ entry on OctoPrint's Python version requirements](https://community.octoprint.org/t/61076).
- title: "Heads-up: A new setting is available to configure trusted authentication
    proxies"
  content: |
    So far, if you set `accessControl.trustRemoteUser` to `true` in your `config.yaml`, OctoPrint would trust any incoming `X-Remote-User` header. That could of course in theory be abused if your OctoPrint instance was reachable directly in addition through your trusted authentication proxy. In OctoPrint 2.0.0, the `accessControl.trustedRemoteUser` setting has been replaced with a list of trusted authentication proxies. This defaults to empty, but if you had `trustedRemoteUser` enabled it will get set to your list of configured trusted reverse proxies. OctoPrint will now only accept and evaluate the `X-Remote-User` header if the request it is seeing came via any of your configured trusted authentication proxies - which must also be among your trusted reverse proxies. 

    If you are currently using the `accessControl.trustedRemoteUser` feature in OctoPrint, you will want to check whether your list of trusted reverse proxies is configured correctly & contains your trusted authentication proxy prior to upgrading. And once upgraded, you'll want to limit the list of trusted authentication proxies further to only those of your reverse proxies that actually provide authentication.

- title: "Heads-up: Plugin authors need to check if they are still using any of the
    now removed deprecated features"
  content: |
    OctoPrint has been logging deprecations warnings for some of its APIs, classes and utility methods for years, some of which even for a decade now.

    Plenty of plugins have been ignoring these deprecation warnings. With the advent of OctoPrint 2.0.0, most of those long deprecated bits and pieces have however now been removed, and those plugins that have been ignoring deprecations without changes will effectively break.

    If you are a plugin author, you **NEED** to consult [this migration guide](https://docs.octoprint.org/en/main/plugins/migration_2_0_0.html) to check and update your plugin so it continues to work against OctoPrint 2.0.0. You might want to check out [this scanner tool by @jacopotediosi](https://github.com/jacopotediosi/octoscanner) that allows you to scan your plugin's source code for any deprecated usages, upcoming issues with 2.0.0 and also packaging related problems.

tags:
- release

summary: Finally, the stable release of OctoPrint 2.0.0 that brings 
  support for connection options other than serial, native thumbnail support, 
  better integration of the printer's storage, multi-storage management, and of 
  course also comes with improvements and bugfixes on top!

images:
- url: images/connection-options.png
  title: OctoPrint now supports adding new connection options through plugins.
- url: images/thumbnails-storage-filelist.png
  title: The filelist now natively supports thumbnails, and allows better 
    management of local and printer storage.
- url: images/thumbnails-upmgr.png
  title: The Upload Manager plugin natively supports thumbnails too, and of 
    course also supports selecting the active storage.
---

This release was the longest ever in progress so far in the almost 14 year history of OctoPrint. I sat down and started working on what became the core feature of this release back in late 2024, and now two years later and after an extremely stressful 2026 -- including a 7 month long release candidate phase -- I'm very happy (and admittedly also both relieved and anxious at the same time) to finally push this out as OctoPrint's next stable release! Reason enough to also finally give this website a new look 😊

Like every single release (and release candidate) of OctoPrint ever since 2016, this release was made possible only through your continued **[support of my work](/support-octoprint/)** 💕

OctoPrint 2.0.0 packs a sheer ton of changes under the surface, but for me the most important one is finally enabling support for other printer interfaces than a serial connection through plugins. This is a goal I have been trying to achieve since 2015 now, and with the latest implementation approach that I started back in November 2024, I finally succeeded! 

Anyhow... as the changes required to do this were massive, and the one or other backwards compatibility issue surely crept in, at the start of this year I decided to go all in with this release, finally increase the major version to "2" and also do a long necessary clean up of bits and pieces that had been deprecated for the better part of a the past decade now.

With that being said, let's take a look at the changes. Unsurprisingly, the [changelog](https://github.com/OctoPrint/OctoPrint/releases/tag/2.0.0) is too long to include here in full, but I still want to give some more details on some personal highlights here:

- As already mentioned, OctoPrint 2.0.0 completely revamps the printer communication layer: **Connecting to and communicating with a printer is now done through a _connector_, and connectors can be added by plugins!** What used to be old comm layer has now been migrated into the bundled _Serial Connector Plugin_ that supports connecting to printers through a serial connection. And there are already two alternative connectors in the works to open up OctoPrint to other printer ecosystems: the [Moonraker Connector Plugin](https://github.com/OctoPrint/OctoPrint-MoonrakerConnector) allows connecting to printers that get shipped with Klipper/Moonraker on board, and the [Bambu Connector Plugin](https://github.com/OctoPrint/OctoPrint-BambuConnector) supports connecting to the (local!) API of printers from Bambu Lab.

  The connection dialog will offer you to select the connector to use, and then allow you to enter (and save!) the necessary connection parameters. OctoPrint then talks to your selected connector to connect to your printer, fetch data from it, send jobs to it and in general control it.

  Through connector plugins, everyone can now add support for new (and possibly even proprietary & reverse engineered) printer interfaces and thus take back control from vendors who'd prefer to keep you locked into their own ecosystems. Take back your hardware, say no to the constant monetization and enshittification.

- Together with the changes needed to make connectors possible, **printer side storage has been turned into a full blown native storage in OctoPrint's internal file manager**, and further storages can also be added through plugins. Together with multi storage support added to the file manager panel and the bundled Upload Manager Plugin, and support for cross storage transfer of files and folders, this makes for new possibilities on how to manage your printables. And the storage support built into the printer connector concept also makes sure all of this works natively with whatever printer connector you use, as long as it has implemented the necessary access methods.

- **Native thumbnail support was also added**. A stand-alone [gcode-thumbnail-tool](https://github.com/OctoPrint/gcode-thumbnail-tool) has been developed that is now used internally to perform thumbnail extraction on the `local` storage. And the printer connector interface defines methods that if implemented also support fetching & displaying the thumbnails from files stored inside the printer's storage. The file manager panel and the bundled Upload Manager Plugin have both been adjusted to display any available thumbnails.

- To give printers (and slicers) more control over print time estimation (it's likely they know best how long something will take!), **estimations will now also be fetched from the printer connector**, if it supports them. In the case of the bundled Serial Connector Plugin, `M73` commands contained in the printed GCODE file will now be used to provide print time estimation basically right from your slicer.

- As there have been plenty of changes to support the new printer connectors, the first class printer storage, and some other things, **OctoPrint now supports API versioning on its HTTP APIs**. Clients can specify the API version they require with a custom `X-OctoPrint-Api-Version` header, specifying the OctoPrint version from which they expect the API behaviour and data model, and OctoPrint will match that accordingly. See also the [newly added documentation on API versioning](https://docs.octoprint.org/en/main/api/general.html#api-versioning).

- An (optional) configuration setting of **trusted authentication proxies** has been added. If trusted authentication proxies (address or range, like trusted reverse proxies) are configured, the chain of trusted involved reverse proxies will be checked for any of the authentication proxies. Only if an authentication proxy was involved in the request will the remote user header then be evaluated. This is an additional security measure.

- OctoPrint now supports **Python 3.14 & 3.15** (and requires at least Python 3.9).

- Several bugs have been fixed, in server, frontend and the documentation.

- ... and more!
