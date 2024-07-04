---
layout: post
title: "OctoPrint's anonymous usage stats were manipulated"
author: foosel
excerpt: OctoPrint's anonymous usage stats were manipulated, here's what we know
date: 2024-06-28 07:20:00 +0200
card: /assets/img/blog/2024-06/2024-06-28-stats-manipulation-card.png
featuredimage: /assets/img/blog/2024-06/2024-06-28-stats-manipulation-card.png
poster: /assets/img/blog/2024-06/2024-06-28-stats-manipulation-poster.png
---

While recording the latest episode of OctoPrint on Air on June 25th, I noticed that something was up with the stats. Going through the graphs on `data.octoprint.org` and commenting on them, I saw a quite irregular amount of instances running a very old version. I figured I had an issue with my data queries and decided to investigate the next day.

On June 26th I did just that, and what I found was that my queries were in fact completely ok. The actual reason was that a small number of clients were busy sending fake tracking events, simulating thousands of unique instances (shown here and below are those from the log of June 25th): 

``` bash
$ grep /pong/ tracking.log | cut -d " " -f 1 | sort | uniq -c | sort -nr | head -n 20
   5134 IRREGULAR
   1882 IRREGULAR
   1860 IRREGULAR
   1841 IRREGULAR
   1685 IRREGULAR
   1404 IRREGULAR
   1331 IRREGULAR
   1096 IRREGULAR
    838 IRREGULAR
    627 IRREGULAR
    525 REGULAR
    510 IRREGULAR
    227 REGULAR
     89 REGULAR
     38 REGULAR
     37 REGULAR
     35 REGULAR
     32 REGULAR
     32 REGULAR
     30 REGULAR
```

The requests from those clients marked as "IRREGULAR" above were found to be clearly and without a doubt faked, so I looked deeper into those requests.

Looking at the list of reported plugins, and also the list of plugins claimed to have been freshly installed, I noticed a pattern. Almost all of these instances claimed to have a specific plugin installed, OctoEverywhere, and a random set of some other of the more popular ones:

``` bash
$ grep -E "^(IRREGULAR)" tracking.log | grep /pong/ | cut -f 9 | cut -d "&" -f 11 | cut -d"=" -f 2 | cut -d'"' -f 1 | while read; do echo -e ${REPLY//%/\\x}; done | tr "," "\n" | cut -d ":" -f 1 | sort | uniq -c | sort -nr
  17555 octoeverywhere
   5167 printtimegenius
   4825 octolapse
   3247 dashboard
   2030 firmwareupdater
   1757 beedlevelvisualizer
   1682 prettygcode
    633 displaylayerprogress
    541 ender3v2tempfix
    514 themeify
    456 navbartemp
    304 fullscreen
    236 touchui
    152 prusaslicerthumbnails
    127 preheat
```

The same pattern could be seen in the faked install events:

``` bash
$ grep -E "^(IRREGULAR)" tracking.log | grep /install_plugin/ | cut -d " " -f 5 | cut -d / -f 5 | cut -d "&" -f 1 | cut -d "=" -f 2 | sort | uniq -c | sort -nr
     44 octoeverywhere
     19 PrintTimeGenius
     18 octolapse
      9 prettygcode
      1 themeify
      1 firmwareupdater
```

I have since cleaned up the data, soft-blocked the offending bad clients and am in the process of putting further mitigation strategies and alerting in place so that future manipulations like that will be more easily detected. The faked requests continued until June 27th around 01:30am UTC, several hours after I cleaned up the data, then ceased.

The result of that manipulation was a whopping **38000 fake instances** reported on OctoPrint's anonymous usage stats:

<div class="row-fluid" style="margin-bottom: 10px">
    <div class="span12">
        <a href="/assets/img/blog/2024-06/2024-06-28-usage-number-change.png" data-lightbox="{{ page.id }}" data-title="Instance stats, showing a drop of 33k after clean-up on June 26th"><img src="/assets/img/blog/2024-06/2024-06-28-usage-number-change.png"></a>
    </div>
</div>

and had an equally strong affect on the popularity stats of the plugins:

<div class="row-fluid" style="margin-bottom: 10px">
    <div class="span12">
        <a href="/assets/img/blog/2024-06/2024-06-28-plugin-stats-change.png" data-lightbox="{{ page.id }}" data-title="Plugin stats, before the clean-up and after"><img src="/assets/img/blog/2024-06/2024-06-28-plugin-stats-change.png"></a>
    </div>
</div>

And if my long term data is to be trusted, this has probably been going on, with ever so slight increases in the number of faked requests per day, since the fall of 2022.

I can only express my strong disappointment at the perpetrator(s) of this manipulation of OctoPrint's anonymous usage stats. This is data that this project relies on - that ***I*** rely on - to make informed decisions on maintenance, on development direction, in short, the future of this fully open source and free project. I cannot describe how angry it made me seeing my work being abused like this. Shame on whoever did this! 

Based on the findings presented, I reached out to OctoEverywhere about this on June 27th, and this was their official response:

> Gina, the developer of OctoPrint, informed OctoEveywhere Thursday morning of this incident. We are very grateful to Gina for bringing this to our attention, sharing the post, and working with us on the matter.
>
> OctoEverywhere used private community channels to determine that a community member was responsible for manipulation. We want to make it clear that this kind of behavior is completely unacceptable and unfit for a community like OctoEverywhere. The maker community is a place to unite, share, build, and work together. Actions like these undermine that trust, which is unacceptable. 
>
> We greatly respect Gina, OctoPrint, and the other developers who work tirelessly on the OctoPrint project. It greatly upsets us that this happened, and we would like to sincerely apologize to them. OctoEverywhere wants to make this right, so we are working with Gina to find ways to help contribute to the OctoPrint project and ensure this never happens again.
>
> OctoEverywhere also wants to make this right in our communities. Anyone who feels wronged by this incident, please use the support system on the OctoEverywhere website to contact us directly. We will work with you to make it right.

**Update 2024-06-28 @ 10:20 CEST**: OctoEverywhere has now also put out a post about this. You can find it [here](https://blog.octoeverywhere.com/our-3d-printing-community-responsiblity/).

**Update 2024-07-04 @ 09:00 CEST**: It has come to my attention that Obico has also been manipulating the stats. You can find the details [here](/blog/2024/07/04/more-stats-manipulation/).