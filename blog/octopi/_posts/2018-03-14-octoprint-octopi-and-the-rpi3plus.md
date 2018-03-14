---
layout: post
author: foosel
title: "OctoPrint, OctoPi and the Raspberry Pi 3+"
date: 2018-03-14 11:30:00 +0100
excerpt: The RPi3+ has just been released and I exactly as much as you. Still, some speculation on the usual questions
    I get bombarded with after such releases ;)
---

You probably have heard that [the Raspberry Pi 3+ was just released](https://www.raspberrypi.org/blog/raspberry-pi-3-model-bplus-sale-now-35/)
and might be wondering what this means for OctoPrint and OctoPi.

I currently have *exactly* the same amount of information as you and I don't have one of those new Pis
on hand yet. So all I can do is take some educated guesses:

  * Yes, Octo**Print** should work just fine (at least I'd be very surprised if it didn't, since OctoPrint itself runs basically 
    everywhere Python does run).
  * No, the current stable Octo**Pi** 0.14 image probably won't work with this since it's very unlikely that it already
    ships with the necessary new drivers and kernel. 
    
    A [new Raspbian Lite image has been released however](https://www.raspberrypi.org/downloads/raspbian/) and 
    [Guy](https://github.com/guysoft/OctoPi) told me he'd switch the nightly builds over to that, so the next nightly 
    builds might already work. 
    
    The stable release of OctoPi 0.15 isn't something that can be done overnight though (neither Guy nor me knew about
    this before you did). We'll first need to verify that a current nightly can even boot up as expected, then
    at least one RC will be pushed out for people to test if everything works fine and once that looks good a stable 
    release will follow. Past experience has shown us that there are usually a couple of bumps in the road regarding 
    drivers and kernel after hardware revisions like that, so please have a bit of patience until those kinks have been 
    ironed out (or found not to be present this time) and the RC process has run through 😉
  * I don't know yet if the slight increase in processing power will be something you'll notice with OctoPrint.
  * I don't know yet if the new dual-band WiFi will perform better than what we have on the RPi3. Apart from supporting
    5GHz of course, which certainly is very interesting for people like me living in areas where the 2.4GHz band is
    pretty much saturated with all those annoying access points from the neighbours 😏

Lot's of unknowns, some patience required, let's wait and see.
