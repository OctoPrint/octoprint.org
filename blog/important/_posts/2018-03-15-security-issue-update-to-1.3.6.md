---

layout: post
author: foosel
title: "Security vulnerability: Update to 1.3.6 ASAP!"
date: 2018-03-15 12:00:00 +0100
excerpt: If you still haven't updated to OctoPrint 1.3.6, please do so ASAP. There is a security vulnerability 
    present in versions 1.3.0rc1 through 1.3.5 that puts your instance at risk if it is accessible directly via the 
    internet or another untrusted network.

---

**If you still haven't updated to OctoPrint 1.3.6, please update ASAP.** 

There is a security vulnerability present in OctoPrint version 1.3.0rc1 through 1.3.5 that puts your instance at risk if it 
is accessible directly via the internet or another untrusted network, e.g. through a port forward in your router. 

OctoPrint version 1.3.6 fixes this vulnerability.

### Who is affected by it?

If you have your OctoPrint 1.3.0rc1 through 1.3.5 directly accessible over the internet 
through a port forward or something similar (without additional protection through a reverse proxy and/or a VPN) 
then you are affected. Update to 1.3.6 as soon as possible.

Note that other ways of accessing OctoPrint remotely are not affected, e.g. PolarCloud, OctoPrint Anywhere, Telegram etc.

### What are the details of this vulnerability? What is the attack vector?

I'm not going to go into details to protect vulnerable installations that even now still might be out there. 
What I will say is that the issue allows unprivileged admin access to your OctoPrint instance over the network, 
bypassing access control.

### Who found this vulnerability? When was it found?

I discovered it myself during maintenance work towards 1.3.6. I didn't disclose it until now to first allow 
as many people as possible to update to 1.3.6 in order to reduce the risk of active exploitation to an absolute 
minimum.

To my knowledge nobody else has discovered this vulnerability and I'm not aware of anyone exploiting it.

### How can I update?

**Use the [built-in Software Update mechanism](http://docs.octoprint.org/en/1.3.5/bundledplugins/softwareupdate.html#software-update-plugin).**
 
If that should not be available to you for some reason then you may follow these manual steps:

  * **OctoPi**: SSH into your Pi. Then run these commands:

    ```
    source ~/oprint/bin/activate
    cd ~/OctoPrint
    git pull
    pip install .
    sudo service octoprint restart
    ```
    
    Verify that it now says "OctoPrint 1.3.6" in the lower left corner of the web interface.
  * **Manual install**: Please substitute ``/path/to/OctoPrint`` with the path to your OctoPrint checkout. 
    On a command line run these commands:
    
    ```
    cd /path/to/OctoPrint
    source venv/bin/activate
    git pull
    pip install .
    ```
    
    Then restart your server. Verify that it now says "OctoPrint 1.3.6" in the lower left corner of the web interface.