---
layout: post
title: "More manipulation of OctoPrint's anonymous usage stats"
author: foosel
excerpt: It has barely been a week since I discovered that someone had been manipulating OctoPrint's anonymous usage stats in OctoEverywhere's favor, and now it has come to my attention that Obico has also been doing the same
date: 2024-07-04 09:25:00 +0200
card: /assets/img/blog/2024-07/2024-07-04-stats-manipulation-card.png
featuredimage: /assets/img/blog/2024-07/2024-07-04-stats-manipulation-card.png
poster: /assets/img/blog/2024-07/2024-07-04-stats-manipulation-poster.png
---

It has barely been a week since [I discovered that someone had been manipulating OctoPrint's anonymous usage stats in OctoEverywhere's favor](/blog/2024/06/28/stats-manipulation/), and now I had to discover that Obico has also been doing the same. 😡

### The discovery

Since I found out about the manipulation last week I've been busy with further investigation and deploying mitigation strategies, and over the course of that I stumbled over a few more irregularities in the data. I spotted a single client that was sending a suspiciously high number of tracking events. However, the traffic looked organic, and on first glance like it was coming from real OctoPrint instances, although with a strong bias for having Obico installed: two third of all of these instances were reporting to have Obico installed, and the rest was a mix of 309 other plugins from the repo, with a clear focus on plugins that are known to be popular.

Some details of the observed requests didn't add up (version discrepancies), but on first look this could have been some automated testing or similar development related activity with some weird enviornment, just as well as anything sinister. In any case, I blocked the IP address of the client in question and promptly moved on to clean-up all of the **15000** instances it had created the past 30 days.

<div class="row-fluid" style="margin-bottom: 10px">
    <div class="span12">
        <a href="/assets/img/blog/2024-07/2024-07-04-usage-number-change.png" data-lightbox="{{ page.id }}" data-title="A graph of OctoPrint's long term usage numbers, dropping first from ~145k to ~107k and then a few days later further down to ~91k"><img src="/assets/img/blog/2024-07/2024-07-04-usage-number-change.png"></a>
    </div>
</div>

I reached out to Obico and asked if they had any CI matching the public IP I was seeing, and they confirmed that it was one of their VMs. They promised to investigate whether some CI runs were causing this. Meanwhile I dug deeper on my end with the help of some analysis scripts I built. It turns out that the overwhelming majority of these instances were alive for less than 30min, but their lifetime ranged from less than that to up to 12h. There was no clear pattern in start hour distribution or start date distribution. The reported versions were all over the place, but the majority was focused on versions 1.8.6, 1.9.0 and 1.7.2. The Python version distribution had clear peaks at 3.7.3, the version found on OctoPi 0.18, and 3.9.2, the version found on OctoPi 1.0, however none of these instances reported running OctoPi. What really stood out though was that some of these instances reported running Python 2.7 and OctoPrint versions of 1.8.0 and up - which is impossible since OctoPrint dropped Python 2 support with that version.

I compiled all of these findings into a report and sent it to Obico, and that was when they came clean. To quote [Kenneth's own blog post on the matter](https://www.obico.io/blog/2024/07/03/my-apologies-for-the-mistake/):

> I created a script to manipulate the OctoPrint stats to boost the ranking of Obico for OctoPrint plugin, probably back in 2022, after having some suspicion that [OctoEverywhere] was doing that.
> 
> I have left the script on auto-pilot for a long time now since Obico pivoted to working on the nozzle camera AI early 2023. When Gina told me about what she found out about OE, I should have had the gut and ownership to make this confession at that time. I guess I was feeling opportunistic since I was quite sure the script had been long dead.
>
> [...]
>
> I have now made sure the script is truly stopped. And I'll be happy to work with you to make it right for the community.

To be honest, that left me speechless. Instead of approaching me with their suspicions back then and saving myself and the community a lot of work and headache now, 
Obico decided to play the same game and manipulate the stats themselves, and even kept doing that after I had already discovered the manipulation in favor of OctoEverywhere. I'm glad that they finally came clean, but I can't put into words the disappointment, betrayal and also anger I feel.

### Consequences

Even though it costs me, **I've dropped Obico as a Sponsor** over this. I cannot in good conscience prominently advertise for a company that has been manipulating the stats of my project for their own personal gain and through that caused damage to the project and the community. 

I'm also going to **invoice both Obico and OctoEverywhere** for the time I had to spend on cleaning up the mess that only their plugins profited off - analysis and clean-up. I don't think it would be fair to ask the community who's [been supporting me so generously](/support-octoprint/) to foot the bill for this. It's bad enough that it has already cost me a lot of time and nerves and continues to do so.

Further, after discussing this whole situation with the team, we've decided to **change some things about how commercial plugins are handled** on the [official plugin repository](https://plugins.octoprint.org) and with regards to tracking. I've already switched the Top 10 and Weekly lists over to a randomized list of the 20 most popular plugins, so **the plugin charts are a thing of the past** now. We have also decided that we are going to **no longer track stats for commercial plugins** publicly at all, and I'll adjust the related data exports later today. I'm sorry for the inconvenience this might cause the legitimate commercial plugin developers, but I hope you understand that this is a necessary step to prevent further manipulation of the usage stats this project heavily relies on.

**As for myself, at this point I'm just tired, disappointed and outright exhausted**. I'm tired of having to deal with this kind of stuff, and I'm disappointed that some people in this community apparently think it's okay to manipulate the stats of a project that's fully open source and free to use for their own personal gain. I still have a lot of work ahead of me as a result of this, and I also have a business trip to EuroPython coming up next week that I need to prepare for. But after that, I'll have to take a break. I need some time to process all of this and to recharge my batteries. I hope you understand.
