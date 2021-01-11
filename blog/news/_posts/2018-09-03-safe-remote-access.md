---

layout: post
title: "A Guide To Safe Remote Access of OctoPrint"
author: jubaleth
card: /assets/img/blog/2018-09/2018-09-03-safe-remote-access-card.png
featuredimage: /assets/img/blog/2018-09/2018-09-03-safe-remote-access-card.png
poster: /assets/img/blog/2018-09/2018-09-03-safe-remote-access-poster.png
date: 2018-09-03 18:20:00 +0200
excerpt: In this guest post, community member Jubaleth will tell you about safe ways to access your OctoPrint instance from the internet.

---

*A guest post by [Jubaleth](https://jubaleth.wtf/) on a topic that is very dear to my heart and on which I'm starting
to sound like a broken record - please head this warning and invest the time that properly securing internal services
needs. ~Gina*

So, you've got your shiny new printer, and just installed OctoPrint, great! Being able to remotely monitor your print is a fantastic ability. Being able to start a print remotely is incredibly handy. From within the realm of your local network, you have a ton of power at your finger tips. What if you want to be able to do this when you're not on your local network? You could just forward ports on your router, use a DDNS service, and you're good to go, right? ... **wrong**. 

The [ISC (Internet Storm Center)](https://isc.sans.edu/forums/diary/3D+Printers+in+The+Wild+What+Can+Go+Wrong/24044/) recently published an article about OctoPrint instances exposed to the public internet. While it is possible that a percentage of the instances found are unintentionally exposed, the vast majority is very likely users who have gone out of their way to expose OctoPrint to the public internet for the sake of convenience. There are safer ways to access your instance remotely than blind port forwarding. This is a critical issue that needs to be discussed. We as a community have to get the right information to new and/or uninformed users, to prevent a catastrophy from happening.

Putting OctoPrint onto the public internet is a *terrible* idea, and I really can't emphasize that enough. Let's think about this for a moment, or two, or even three. OctoPrint is connected to a printer, complete with motors and heaters. If some hacker somewhere wanted to do some damage, they *could*. Most printers can have their firmware flashed over USB. So as soon as the box hosting OctoPrint is comprimised, there go any failsafes built into the firmware. All one would have to do, is flash a new, malicious firmware with no safeguards, over USB, and then tell the printer to keep heating, leading to catastrophic failure. Of course there are other reasons to not have an OctoPrint instance available on the public internet, such as sensitive data theft, but catastrophic failure is by far the worst case scenario here.

So, with that said, how can we accomplish remote access to monitor or control a printer, without putting OctoPrint on the public internet for everyone to abuse?  This guide will show you how.

### Plugins (The Easy Way)

Remote access via a plugin is certainly the easiest way for you to access your instance and control/monitor your printer. Unless you really know what you're doing, this is very likely the method that you're going to want to be using. There are a few different options available that accomplish remote access, without opening up OctoPrint to the rest of the world.

### OctoEverywhere.com

[OctoEverywhere.com](https://octoeverywhere.com/?source=octoprint_blog) is a free, secure, and easy to use cloud service that allows you to access your entire OctoPrint web portal from anywhere! OctoEverywhere is a community funded effort that focuses empowering everyone to create better with full remote access to their OctoPrint setup. The service supports webcam streaming, remote printer control, full plugin support, and more! To start the 2-minute setup process go [here](https://octoeverywhere.com/getStarted?source=octoprint_blog), or checkout the official plugin listed [here](https://plugins.octoprint.org/plugins/octoeverywhere/).

#### Polar Cloud

The Polar Cloud plugin lets you connect OctoPrint to your [Polar Cloud](https://polar3d.com) account. Polar Cloud is a cloud based service that adds a whole lot of flexibility to your workflow. It's certainly more than just an app to monitor/control your printer, it's a whole community of printers, designers and makers. The process of selecting an object, slicing and sending to your printer are streamlined into a simple workflow. The plugin is available [here](https://plugins.octoprint.org/plugins/polarcloud/) and is definitely worth checking out.

#### OctoPrint Anywhere (*edit: or its successor The Spaghetti Detective*)

This plugin is a cloud service that allows you to access your OctoPrint instance through a web interface.
Setup is relatively simple, install the plugin, either from the Plugin Manager, or you can grab it [here](https://plugins.octoprint.org/plugins/anywhere/). After installing, you will be greated by a setup wizard that will guide you through the rest of the steps. In just a few moments, you'll be up and running, and able to access your OctoPrint instance, without forwaring any ports, or exposing your instance to the internet.

*edit*: Check out Kenneth's new project [The Spaghetti Detective](https://plugins.octoprint.org/plugins/thespaghettidetective/)

#### OctoPrint-DiscordRemote

If you're a discord user, the DiscordRemote plugin is another option. It will join your discord channel,
respond to commands and send you snapshots from your webcam, if you have one installed. At the time of writing, there does not appear to be a way to grant permissions to a specific user, only the channel owner may issue commands. This plugin can be found in the Plugin Manager or [here](https://plugins.octoprint.org/plugins/DiscordRemote/)

#### Telegram

The telegram plugin operates similarly to the DiscordRemote plugin, in that it creates a telegram bot with which you can interact. It has relatively fine grained ACL capabilities, which allows you to grant permissions to individual users who interact with it. It can be configured to send status updates for different events in the printing process, including configurable periodic updates on layer change or at a specific time interval. The initial setup isn't complicated, but does require following the steps in the readme. It only takes a few minutes to get setup, and the plugin is available [here](https://plugins.octoprint.org/plugins/telegram/).

#### ngrok (*edit: added 2020-06-22*)

The plugin creates a secure tunnel to access OctoPrint remotely through [ngrok](https://ngrok.com/). The tunnel is encrypted with SSL and proper certificates (even if your OctoPrint instance is not accessible via HTTPS locally), and is further protected with Basic Authentication (username and password) out of the box. It pretty much wraps the "Reverse Proxy" scenario from below into an easily installable plugin.

### Advanced Access

Plugins are a fantastic way for a beginner (or veteran) to access their printer remotely, but the more advanced user has a few more tools at their disposal. Beyond this point in this post, I will intentionally not go into too much detail. I am mentioning these methods for the sake of completeness, unless you have previous experience setting up web and/or vpn servers, I highly suggest you stick with the plugins. It's not that I'm against one learning about these things, quite the contrary... I'm against learning them with a 3D printer. There is too much that can go wrong (remember, printers can cause fires!) if you misconfigure something, accidentally skip over something, and unintentionally leave your printer open to the world. 

#### VPN

**V**irtual **P**rivate **N**etworks are a great way to gain access to your OctoPrint instance. There are many options available ([PiVPN](http://www.pivpn.io/), [OpenVPN](https://openvpn.net/)), and some home routers even have a VPN server built in. The major advantage to using a tunnel into your network, is that your OctoPrint instance is *not* available to the internet in general. Without access to your VPN, the printer can *not* be accessed from outside. 

#### Reverse Proxy

One can setup a reverse proxy using solutions like nginx, Apache, and HAProxy. There are certainly other options available, these are the 3 most common, and the 3 that popped into my head. When using a reverse proxy, I highly recommend setting up some form of authentication. The most common (and easiest to setup) is basic authentication (i.e. username/password). In this case, I also highly recommend the use of rate limiting to prevent brute-force password guessing attacks. A more secure choice would be client-certificate authentication, this of course requires setting up a PKI to handle the issuance and revocation of certificates. 

Whether you use a reverse proxy, or VPN to access OctoPrint; I recommend putting it on a separate physical box to the box connected to your printer. Running everything on a single server is just asking for trouble.

### Conclusion

All in all, there are many ways one can **safely** access an OctoPrint instance remotely, that do not involve blindly forwarding ports on your router and putting yourself at risk. Plugins are a fantastic tool that I recommend beginners take advantage of. Putting OctoPrint on the internet is nothing short of dangerous. If you must do this, take advantage of the ACL system built into OctoPrint, and even better, put another form of authentication in front. Even if it seems like extra work to setup a plugin, or a VPN/reverse proxy, it's worth it. Anything with the potential to burn down your house should be treated with the utmost care. It may seem more convenient to cut corners... but is it really worth it?

*If you need help with setting up any of the proposed solutions here, get in touch on the [OctoPrint Community Forums](https://discourse.octoprint.org), you might find some help there. Also be sure to check [this topic on the forum](https://discourse.octoprint.org/t/access-your-octoprint-remotely/3628) for some more info.*