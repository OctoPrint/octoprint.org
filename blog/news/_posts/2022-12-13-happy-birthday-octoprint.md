---

layout: post
title: "Happy Birthday, OctoPrint!"
author: foosel
card: /assets/img/blog/2022-12/2022-12-13-octoprint-birthday-card.png
featuredimage: /assets/img/blog/2022-12/2022-12-13-octoprint-birthday-poster.png
poster: /assets/img/blog/2022-12/2022-12-13-octoprint-birthday-poster.png
date: 2022-12-13 14:30:00 +0100
excerpt: OctoPrint is turning 10 years old this holiday season! Time to reflect a bit on its history, and to eat cake!
---

Like every December, I'm not only looking forward to the holidays 🎄 for my yearly end-of-year vacation, some silent rest time with friends and
family, the smell of freshly baked cookies 🍪 and Die Hard on the screen 🍿, but also because it always marks another year of OctoPrint's existence.

This year, it's a special one, because OctoPrint was born on December 25th 2012, so it's turning 10 years old! 🎉

Time to do some reflection on the past decade, and I did just that in a very special OctoPrint on Air stream yesterday, where I went over 
the past 10 years, talked about the milestones, the big events, the challenges and the fun times, fielded some questions and of course also had some cake!

<div class="row-fluid" style="margin-bottom: 10px">
    <div class="span6">
        <a href="/assets/img/blog/2022-12/2022-12-13-gina-and-cupcake.jpg" data-lightbox="{{ page.id }}" data-title="Me and an OctoPrint themed cupcake"><img src="/assets/img/blog/2022-12/2022-12-13-gina-and-cupcake.jpg"></a>
    </div>
    <div class="span6">
        <a href="/assets/img/blog/2022-12/2022-12-13-gina-and-cupcake-bite.jpg" data-lightbox="{{ page.id }}" data-title="Me and the cupcake that's now missing a bite"><img src="/assets/img/blog/2022-12/2022-12-13-gina-and-cupcake-bite.jpg"></a>
    </div>
</div>

All of that you can watch in the video embed below, but I still wanted to also write down some of the things that happened exactly 10 years ago here.

## 10 years ago...

I got my first 3d printer back in November 2012. It was a first-gen Ultimaker, the one that still had an unheated acrylic build plate, 
a lasercut wooden frame, and no screen and SD card slot, unless you shelled out another 100 bucks for an add-on (which back then I did
not do). 

<div class="row-fluid" style="margin-bottom: 10px">
    <div class="span6 offset3">
        <a href="/assets/img/blog/2022-12/2022-12-13-ultimaker.jpg" data-lightbox="{{ page.id }}" data-title="Me and the cupcake that's now missing a bite"><img src="/assets/img/blog/2022-12/2022-12-13-ultimaker.jpg"></a>
    </div>
</div>

I tethered it to my PC via USB and used first Printrun and then the built-in machine control in Cura to print. But that
got annoying fast: It was loud, it was smelly and it was blocking me from using the PC to do anything else. So I started looking for
alternatives. The first RPi had just been released a few months earlier, and I figured I could add a cheap USB dongle to it and run 
some kind of server on it that would allow me to remotely monitor and control the printer.

So I got my hands on a Pi (not that easy back then either), a USB dongle and started looking for suitable software, absolutely sure
there would already be something fitting the bill. I found some stuff, but nothing that really worked for me: All of the existing options basically consisted of a very
crude web interface that allowed you to upload one file and print it, but that was it. No monitoring, no control, no nothing.

At that point in time it was already the start of December, my vacation was coming up and I had been itching for some nice pet project
for a while, so I thought "Hey, how hard it can it be!" - famous last words - and decided to just write my own solution. After some research I settled on
extending the Cura code with a web server and API and add a web interface to the mix that would allow me to utilize the existing
communication layer in Cura's machine control to talk to the printer. I figured that would be the easiest way to get something up
and running quickly, without having to fully understand the communication protocol of the printer (which I didn't at the time and
after some reading had to realize was way more than just streaming the GCode to the printer line by line over a serial interface). So I
got to work, and on December 25th I had a working prototype of "Cura WebUI" that allowed me to upload and print files, monitor the temperature in a graph 
and control the printer via a web interface. I posted about it publicly in the Google Plus 3D printing community, including a 
screenshot.

<div class="row-fluid" style="margin-bottom: 10px">
    <div class="span12">
        <a href="/assets/img/blog/2022-12/2022-12-13-first-ever-screenshot.png" data-lightbox="{{ page.id }}" data-title="The first ever screenshot of what is now OctoPrint"><img src="/assets/img/blog/2022-12/2022-12-13-first-ever-screenshot.png"></a>
    </div>
</div>

A day or two later I had restructured the layout a bit, added a file list, things like that. And I actually was printing against a real
printer for the first time!

<div class="row-fluid" style="margin-bottom: 10px">
    <div class="span12">
        <a href="/assets/img/blog/2022-12/2022-12-13-screenshot-layout.png" data-lightbox="{{ page.id }}" data-title="Layout changes and a file list"><img src="/assets/img/blog/2022-12/2022-12-13-screenshot-layout.png"></a>
    </div>
</div>

People seemed to like it, even though the dependency on the full Cura distribution was a bit annoying to some (myself included), so my next few steps were to
extract my little server/web interface from Cura and make it a standalone thing uncreatively called "Printer WebUI". 

I wanted to be able to monitor my print jobs via a webcam, and so did some experiments with OpenCV, but the poor Pi was incapable to both capture and process the images at the same time
as it was trying to keep the print job going, so that was a dead-end. But I didn't give up and instead started looking into other
options, and found mjpg-streamer, which allowed me to stream MJPG from a webcam that supported it, at only a fraction of CPU
load on the Pi. I embedded the stream into the web interface and was extremely happy to see it perform well enough to be usable.

<div class="row-fluid" style="margin-bottom: 10px">
    <div class="span12">
        <a href="/assets/img/blog/2022-12/2022-12-13-webcam.png" data-lightbox="{{ page.id }}" data-title="Renamed to Printer WebUI and now sporting a webcam tab"><img src="/assets/img/blog/2022-12/2022-12-13-webcam.png"></a>
    </div>
</div>

Shortly after that I also added a first version of the timelapse feature. By then my vacation was pretty much over (we are now in early
January of 2013), and I figured, well, that was fun, it now does everything I needed it to do, and apparently it also helps others. A nice
vacation! So I put it aside and went back to work.

## And the rest is history

<div class="row-fluid" style="margin-bottom: 10px">
    <div class="span12">
        <a href="/assets/img/blog/2022-12/2022-12-13-timeline.png" data-lightbox="{{ page.id }}" data-title="The first ever screenshot of what is now OctoPrint"><img src="/assets/img/blog/2022-12/2022-12-13-timeline.png"></a>
    </div>
</div>

I did not expect what happened next. I started getting emails from people from all across the globe thanking me, asking for features to be added,
requesting help to get it working with their printer. At that point I learned that apparently there isn't just *one* variant of that
printer communication protocol out there, and that a lot of the printers out there behaved very differently on the serial interface. That has become
a constant source of frustration for me ever since, but back then it was just a minor annoyance (probably because I did not grasp the full scope of the issue yet 😂). I was happy to help people get it
working, and I was happy to add features that people requested. I was also happy to see that people were actually using it, and that
it was helping them. Fun fact: I still am to this day 😊

Around spring of 2013 it got named OctoPrint (and how that happened is covered in the video below, so be sure to watch it 😉), Domains got registered, GitHub
repos got renamed. I reduced my work to 4 days per week in September of 2013 to have one day per week for OctoPrint which continued to grow and grow
and grow. 

By spring of 2014 it had grown so much that I felt I was not able to do it justice anymore working on it only on the side, and frankly that was also
starting to become quite unhealthy. Just at that time I got an offer by a technology company to work on it full time on their salary, and so in August 2014
I turned OctoPrint into my full-time job. By April 2016 that sadly no longer proofed financially feasible to that company, and so they had to let me go. An incredibly scary time indeed,
especially since I had sworn to never become self-employed and every fiber of my being screamed for getting a secure employment again, with it being clear that that would have
meant the end of my involvement with OctoPrint. But I also felt that I'd 
kick myself for the rest of my life if I didn't at least *try* to make my full-time focus on OctoPrint work out long-term via crowd
funding, so on April 13th 2016 I launched my [Patreon campaign](https://patreon.com/foosel) and then got overwhelmed by the community's amazing response 🥰

I've been self-employed and working [fully crowdfunded](/support-octoprint/) on OctoPrint now ever since. I consider it my life's work, and I am so incredibly grateful for the support I've
received over the years. I am also eternally grateful for the community that has grown around OctoPrint, and for the amazing people and friends I've met
along the way. Thank you all for being part of this journey with me, and for making it what it is today! 💕

On to the next decade! And of course, as always on the final blog post of the year, also Happy Holidays, Happy New Year, and - most importantly - Happy Printing! 🎄🎅🎁

***~ Gina***

---

PS: And if you want to know more about the history of OctoPrint, be sure to check out OctoPrint on Air #50:

{% include youtube.html vid="OEpnaWX-oHU" %}
