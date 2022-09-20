---

layout: post-bugfix
title: 'New release: 1.8.3'
author: foosel
date: 2022-09-20 13:30:00 +0200
card: /assets/img/blog/2022-09/2022-09-20-octoprint-1.8.3-card.png
featuredimage: /assets/img/blog/2022-09/2022-09-20-octoprint-1.8.3-card.png
poster: /assets/img/blog/2022-09/2022-09-20-octoprint-1.8.3-poster.png
excerpt: "This third bugfix & security release for 1.8.0 fixes a few new issues reported, including various security vulnerabilities."

bugfix: 1.8.3
release:
  tag: 1.8.3
  link: /blog/2022/05/17/new-release-1.8.0/
  headsups: true
headsups:
  - title: Important notice about downgrading from this version
    content: >
      With OctoPrint 1.8.3, the password hashing has been changed to use the Argon2 hashing algorithm. Any existing accounts will be migrated to the new hashing format on their first login under 1.8.3 or later, and the `accessControl.salt` value will be stripped from the config once all accounts have been migrated as it is no longer needed. This however means that downgrading to an earlier version will result in no longer being able to login, since earlier versions of OctoPrint 1.8.3 have no idea what to do about the Argon2 hashes and require `accessControl.salt` as well.

      However, OctoPrint 1.8.3 and later come prepared for this scenario and will create a backup of both your users.yaml and config.yaml files, to make sure you can manually roll those back should for whatever reason you need to downgrade to a version prior 1.8.3. [Find out more in the FAQ](https://faq.octoprint.org/rollback-1-8-3).
  - title: "Plugin authors: Check out the changes due to OctoPrint's new CSRF protection"
    content: >
      To protect OctoPrint against [CSRF attacks](https://owasp.org/www-community/attacks/csrf) against the non CORS affected upload endpoints, in case of browser session based authorization the API is protected using the [Double Submit Cookie mitigation strategy](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html#double-submit-cookie). You can read more about how this is implemented and how it might affect your frontend code [in the docs](https://docs.octoprint.org/en/master/api/general.html#csrf-protection).

      If your plugin happens to implemented the `BlueprintPlugin` mixin, please also read up on the changes on *that* that relate to CSRF protection and what steps you must take to get rid of warnings you will now see in the logs otherwise. [You can find the updated docs on the `BlueprintPlugin` mixin here](https://docs.octoprint.org/en/master/plugins/mixins.html#octoprint.plugin.BlueprintPlugin).

---

This third bugfix & security release for 1.8.0 fixes two minor bugs and closes a whole number of recently reported security
vulnerabilities, primarily of low and medium severity, but also one high severity one:

> **🔒 Security fixes**
>
> - Severity High (8.3): It was possible to use Cross-Site Request Forgery combined with phishing to trick an admin user into visiting a malicious site that then could install a malicious plugin on the OctoPrint server using the logged-in admin user's browser credentials. This attack vector has now been closed. The API will now require to be sent a CSRF cookie provided by the server on initial page load as well as a CSRF header containing the same value with every API request that is not GET, HEAD or OPTIONS. Please read more about this [in the docs](https://docs.octoprint.org/en/master/api/general.html#csrf-protection).
> - Severity Medium (6.1): The "Settings Manage" permission allowed user management. This has historic reasons as it was used as the original "Admin" permission, however its description does not include this kind of access and thus it could have caused unintentional access in the field, allowing a "Settings Admin" user to elevate their own permissions or change those of others. All kinds of user management now require the "Admin" permission. A future version of OctoPrint will also drop the confusing Settings Admin permission, see [#4641](https://github.com/OctoPrint/OctoPrint/issues/4641) for the roadmap for this.
> - Severity Medium (6): A malicious admin user could upload a specially crafted language pack containing one or more symlinks to files on the OctoPrint server, which would then be contained in created backups and could thus be extracted that way. This could be used by a malicious admin user to extract files from the OctoPrint server readable by the system user the OctoPrint server is running under, including OS files outside the scope of OctoPrint. This has been fixed.
> - Severity Medium (5.3): Improved security of the password change dialog in as that it now requires you to enter your current password before allowing you to set a new one. Admins are still able to change the passwords of users without this requirement. See also [CVE-2022-2930](https://nvd.nist.gov/vuln/detail/CVE-2022-2930).
> - Severity Medium (5.3): Fixed a buggy permission role that assigned the ability to enable/disable/uninstall plugins to users with the List Plugins permission. Note that installing plugins was *not* also included in this. This could have been used by read-only or operator users to enable, disable or uninstall *already installed* plugins, without the need for an administrator. See also [CVE-2022-3068](https://nvd.nist.gov/vuln/detail/CVE-2022-3068).
> - Severity Medium (4.4): OctoPrint's login sessions will now expire after a short time (15min), unless kept alive by keeping a tab open. The remember me cookie will expire after 90 days. Sessions and the remember me cookie will also become invalid on password change. This prevents the reuse of old session credentials or remember me cookies somehow obtained by an attacker (e.g. through a compromised browser or a forgotten on a shared system). See also [CVE-2022-2888](https://nvd.nist.gov/vuln/detail/CVE-2022-2888)
> - Severity Medium (4.2): The password hashing has been switched to Argon2. Existing password hashes will be migrated transparently to this new hashing approach on login of the individual accounts, a backup of the old file will be made (and automatically removed again in a future version). **Important**: That means that you can not downgrade easily from 1.8.3 to a version prior. If you need to downgrade, [please see this FAQ entry](https://faq.octoprint.org/rollback-1-8-3).
> - Severity Low (3.7): A rate limit on the login dialog has been introduced to thwart attempts at bruteforcing a working username/password combo. After a number of failed attempts to login (3/minute, 5/10 minutes, 10/hour), you are denied further attempts until the hit rate limit expires. It will extend on each further failed attempt. The rate limit is tracked per client IP and will reset on server restart. See also [CVE-2022-2822](https://nvd.nist.gov/vuln/detail/CVE-2022-2822).
> - Severity Low (3.7): Fixed a bug that allowed someone to upload a `.gcode` file but then rename it to `.html` or similar through OctoPrint's move file functionality. This could have been used to launch a phishing or scripting attack on an unsuspecting user of the same OctoPrint instance. This has now been fixed as in that the move file feature only supports moving/renaming to file extensions that are supported for upload as well. See also [CVE-2022-2872](https://nvd.nist.gov/vuln/detail/CVE-2022-2872).
> - Severity Low (3.5): A user with the "Files Upload" permission but without the "Files Delete" permission was able to overwrite and thus effectively delete files. OctoPrint will now require the "Files Delete" permission to perform an overwrite.
> - Severity Low (3.5): While logs where not displayed on the terminal tab without the "Monitor Terminal" permission, they were still sent on the web socket. This has been rectified.
> - Severity Informational (0.0): It was possible to download files from the backup download endpoint (accessible only by admins) that weren't backups. This could possibly have been abused by a malicious admin user that first got something there somehow that wasn't a backup and then extracting it this way. While the question as to *why* that would be a preferable approach to extract data from a server you have full admin access to remains unanswered, this no longer is possible now regardless.
> - Severity Informational (0.0): Limited folder config in UI to uploads, timelapses and watched folder. Everything else needs to be configured through `config.yaml`.
>
> **🐛 Bug fixes**
>
> - Fixed a bug that prevented user creation without any attached groups. If no group was attached, OctoPrint so far forced the default user group "Operator" to be attached to the user. This has been solved.
> - Fixed a styling issue in the appearance settings.

You can also take a look at the [changelog on GitHub](https://github.com/OctoPrint/OctoPrint/releases/tag/1.8.3) which this time is a bit on the longer side.

In case you are wondering about the large number of security fixes in this release, the OctoPrint project recently got bombarded with reports from a bounty offering platform. 
This sadly caused a *lot* of overhead, as many of the reports were inaccurate, overstated to increase bounty payout or simply spam, and
this proofed to be a real resource drain on me and the whole team. So while it was good that these things were now discovered and fixed, the way things went sadly came closer
to a DDOS attack on maintainer resources than the collaboration and positive experience it should have been. You can hear more about this in
[OctoPrint on Air #47](/blog/2022/08/22/octoprint-on-air-47/) and I will most likely once again talk about it in the forthcoming OctoPrint on Air #48 as well, which should come
out sometime next week.

Like every single release (and release candidate) of OctoPrint ever since early 2016 this release was made possible only
through your continued **[support of my work](/support-octoprint/)** 💕
