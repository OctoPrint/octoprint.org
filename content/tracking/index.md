---
title: Anonymous Usage Tracking in OctoPrint
---

Starting with version 1.3.10, OctoPrint comes with a built-in plugin "Anonymous Usage Tracking" that performs anonymous
usage tracking. Tracking will only take place if the plugin is enabled and you've decided to opt-in during initial
setup (or enabled it manually afterwards, through the corresponding switch in the settings).

## What data gets recorded?

All tracking requests record the OctoPrint version and a unique identifier of the OctoPrint instance (randomly created on first
start and not connected in any way to personal identifiable information) to allow counting of unique instances per
version. Additionally a rough location from which the request originates will be determined based on the client IP
using the [GeoLite2 City database](https://dev.maxmind.com/geoip/geoip2/geolite2/) and
[GeoIP](https://www.elastic.co/guide/en/logstash/current/plugins-filters-geoip.html).

The plugin fires tracking requests for the following events. Version numbers indicate in which OctoPrint version after
1.3.10 an event or additional data was added, also for as of yet unreleased versions. Most of the events can be
switched off in the settings.

- **Regular ping every 15min**
  - Uptime of OctoPrint <span title="Starting with OctoPrint 1.3.11" class="pill pill--info">1.3.11+</span>
  - Current printer state <span title="Starting with OctoPrint 1.6.0" class="pill pill--info">1.6.0+</span>

- **Regular pong every 24h** <span title="Can be switched off in the plugin settings" class="pill ">switchable</span> <span title="Starting with OctoPrint 1.3.12" class="pill pill--info">1.3.12+</span>
  - Installed third party plugins & their version numbers
  - OS name (e.g. "linux", "windows") <span title="Starting with OctoPrint 1.4.1" class="pill pill--info">1.4.1+</span>
  - Whether OS is 32bits or 64bits <span title="Starting with OctoPrint 1.5.0" class="pill pill--info">1.5.0+</span>
  - Python version <span title="Starting with OctoPrint 1.4.1" class="pill pill--info">1.4.1+</span>
  - Pip version <span title="Starting with OctoPrint 1.4.1" class="pill pill--info">1.4.1+</span>
  - Number of CPU cores, CPU frequency and RAM <span title="Starting with OctoPrint 1.4.1" class="pill pill--info">1.4.1+</span>
  - Raspberry Pi model <span title="Only if running on a Raspberry Pi" class="label">RPi only</span> <span title="Starting with OctoPrint 1.4.1" class="pill pill--info">1.4.1+</span>
  - OctoPi version <span title="Only if running under OctoPi" class="label">OctoPi only</span> <span title="Starting with OctoPrint 1.4.1" class="pill pill--info">1.4.1+</span>
  - Unlocked achievements <span title="Can be switched off in the plugin settings" class="pill ">switchable</span> <span title="Starting with OctoPrint 1.10.0" class="pill pill--info">1.10.0+</span>

- **Server startup** <span title="Can be switched off in the plugin settings" class="pill ">switchable</span>
  - OS name (e.g. "linux", "windows")
  - Whether OS is 32bits or 64bits <span title="Starting with OctoPrint 1.5.0" class="pill pill--info">1.5.0+</span>
  - Python version
  - Pip version
  - Number of CPU cores, CPU frequency and RAM
  - Raspberry Pi model <span title="Only if running on a Raspberry Pi" class="label">RPi only</span>
  - OctoPi version <span title="Only if running under OctoPi" class="label">OctoPi only</span>
  - OctoPi-UpToDate build <span title="Only if running from an OctoPi-UpToDate build" class="label">OctoPi-UpToDate build only</span> <span title="Starting with OctoPrint 1.8.0" class="pill pill--info">1.8.0+</span>

- **Server shutdown** <span title="Can be switched off in the plugin settings" class="pill ">switchable</span>

  No additional recorded data.

- **Connection to a printer** <span title="Can be switched off in the plugin settings" class="pill ">switchable</span>
  - Used serial port & baudrate <span title="Up until OctoPrint 1.11.x" class="pill pill--info">up until 1.11.x</span>
  - Used printer connector & connector provided connection parameters <span title="Starting with OctoPrint 2.0.0" class="pill pill--info">2.0.0+</span>
  - Firmware name as reported by the printer (e.g. through `M115`)

- **Start/cancel/finish of a print job** <span title="Can be switched off in the plugin settings" class="pill ">switchable</span>
  - Used printer connector <span title="Starting with OctoPrint 2.0.0" class="pill pill--info">2.0.0+</span>
  - Origin of printed file (local storage vs printer's SD card)
  - One-way SHA1 hash of the file name, unique to the instance
  - Elapsed time on print end
  - If the system is currently throttled: current and past throttle state <span title="Only if running on a Raspberry Pi" class="label">RPi only</span> <span title="Starting with OctoPrint 1.3.10" class="pill pill--info">1.3.10+</span>
  - If the print failed: reason of failure (cancel vs error) <span title="Starting with OctoPrint 1.3.10" class="pill pill--info">1.3.10+</span>

- **Errors in the communication with the printer and/or reported by the firmware** <span title="Can be switched off in the plugin settings" class="pill ">switchable</span> <span title="Starting with OctoPrint 1.3.11" class="pill pill--info">1.3.11+</span>
  - Error text generated by the firmware or OctoPrint

- **Printer Safety Check warnings** <span title="Can be switched off in the plugin settings" class="pill ">switchable</span> <span title="Starting with OctoPrint 1.3.11" class="pill pill--info">1.3.11+</span>
  - Warning type (e.g. "firmware-unsafe")
  - Name of check that triggered the warning

- **Install/uninstall/enabling/disabling of a plugin** <span title="Can be switched off in the plugin settings" class="pill ">switchable</span>
  - Plugin identifier
  - Plugin version

- **Update of a component** <span title="Can be switched off in the plugin settings" class="pill ">switchable</span>
  - Whether the update was successful or not
  - Component identifier
  - From version, to version

- **System got throttled/unthrottled** <span title="Only if running on a Raspberry Pi" class="label">RPi only</span> <span title="Can be switched off in the plugin settings" class="pill ">switchable</span> <span title="Starting with OctoPrint 1.3.10" class="pill pill--info">1.3.10+</span>
  - Whether there's any current issue
  - Whether there's been any past issue
  - Whether there's a current undervoltage issue
  - Whether there's been a past undervoltage issue
  - Whether there's a current overheat issue
  - Whether there's been a past overheat issue

- **Achievement unlocked** <span title="Can be switched off in the plugin settings" class="pill ">switchable</span> <span title="Starting with OctoPrint 1.10.0" class="pill pill--info">1.10.0+</span>
  - Achievement identifier

- **Onboard slicing triggered** <span title="Can be switched off in the plugin settings" class="pill ">switchable</span> <span title="Starting with OctoPrint 1.3.12" class="pill pill--info">1.3.12+</span>
  - Slicer identifier

- **WebUI loaded** <span title="Can be switched off in the plugin settings" class="pill ">switchable</span> <span title="Starting with OctoPrint 1.7.0" class="pill pill--info">1.7.0+</span>
  - Browser name & version
  - OS name & version that the browser is running under

## How and where does this data get evaluated? Are there any third parties involved?

No, there are no third parties involved.

The raw data gets recorded and evaluated on `tracking.octoprint.org`. It doesn't leave that server and gets evaluated in
place through a local [ELK stack](https://www.elastic.co/elk-stack) and [Grafana](https://grafana.com/) install.

Some exports of queries based on the data are automatically created by an hourly cronjob and made available [here](https://data.octoprint.org/export/).

Visualizations based on these exports are provided on [data.octoprint.org](https://data.octoprint.org).

## How can I disable tracking?

Open your OctoPrint settings, click on "Anonymous Usage Tracking", uncheck the box that says "Enable Anonymous Usage Tracking" and
save.

## Where can I find the source of this plugin?

You can find the source code of the tracking plugin built into OctoPrint in `src/octoprint/plugins/tracking` of the
[OctoPrint source code](https://github.com/OctoPrint/OctoPrint).

**Please also see the [Privacy Policy](/privacy/).**
