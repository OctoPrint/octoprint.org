# 📊 octoprint.org scripts

Various scripts and configs used to operate OctoPrint's page on 
[octoprint.org](https://octoprint.org).

  * `nginx` - nginx configs
  * `updaters` - updater helpers, to be run on the server via cron and to keep nginx configs up to date
  * `deploy.sh` - deploy script to run on server after updates
  * `update.sh` - update script to run all updaters on the server via a cronjob
