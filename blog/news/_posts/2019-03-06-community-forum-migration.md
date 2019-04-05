---

layout: post
title: "Community Forum Migration"
author: jubaleth
card: /assets/img/blog/2019-03/2019-03-06-forum-migration-card.png
featuredimage: /assets/img/blog/2019-03/2019-03-06-forum-migration-card.png
poster: /assets/img/blog/2019-03/2019-03-06-forum-migration-poster.png
date: 2019-03-06 12:20:00 +0200
excerpt: On February 11th 2019 we migrated the community forums to a new server. This was our experience.

---

Over the last couple of months, we've been preparing to migrate the community forums
to our own server. Our primary reason for moving to a "self-hosted" setup, is we very 
quickly outgrew our free hosting plan from [Discourse](https://www.discourse.org/).
The hosting there was amazing, and we're very grateful to Discourse. 

Some of the major advantages to hosting ourselves is much finer grain control over the infrastructure,
ability to install plugins, and even write our own plugins if need be. 


#### Infrastructure
The server infrastructure for the forums is relatively simple. We have a VPS hosted in Germany, it's got 4 vCPUs and
16GB of memory. If we ever need more resources, we can expand it essentially with the click of a button. 

All of our infrastructure has been automated with Ansible. This allows us to push config changes with ease
and audibility. In the unlikely event of complete server failure, or if we ever need to move the box, provisioning
a new one only takes a few minutes, and allows us to be up and running again, very quickly.

No good infrastructure is complete without monitoring. We're currently using netdata and UptimeRobot to monitor
the forums. Both of these send us notifications at any hour of the day, if there's any kind of problem detected. Netdata
gives us realtime server stats for a wide variety of metrics.

Backups of the forum data happens daily. We take an encrypted snapshot of the forums every morning and push that to an off-site
storage facility here in Germany. To be GDPR compliant, none of the data leaves the EU, and backups are kept for a
maximum of 90 days.

#### The Migration

The migration itself took place on February 11th 2019, and was almost problem free. The few problems we did have, were
solved very quickly. To start, we put the old forums into read-only mode, and then created a new backup. After restoring
the backup on the new instance, we switched over the DNS to point to the new forums. As we have moved to a new subdomain,
all old URLs needed to redirect with a 301 to community.octoprint.org.

We did run into a couple of minor problems after the migration. The first was some image links in posts still pointed
to the old CDN, causing images in some posts not to be displayed. This was solved by telling discourse to 'rebake' all
posts.

Another issue we ran into, were the externally generated placeholder images. Discourse's default behavior, is to make
external requests to their server, in order to download a pre-generated "letter" image in various sizes and colours. This
feature is supposed to work out of the box, but for some reason, for us, it didn't. After some research, we found a setting
to disable external image generation in favour of local image generation. While generating the images locally does use
a bit more CPU, we really don't see this as a good reason to send requests to a third party, just to generate an image.

The last problem encountered had to do with email receiving. We have a mail receiver container setup, and it's configured
to post all received mail to the web containers. After having a look in the mail log, we noticed that all received mail
was being rejected. After digging a bit deeper, it became obvious that two configuration options in Discourse were overlooked,
and simply needed to be set, to tell Discourse to allow mail from the mail container to be processed.

It has been almost a month now since we migrated the forums, and everything has been very stable. We're really happy
with our decision to host the forums on our own, it gives us significantly more flexibility, and allows us to scale the
infrastructure as needed.