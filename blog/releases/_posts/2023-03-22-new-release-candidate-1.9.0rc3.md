---

layout: post-rc
title: 'New release candidate: 1.9.0rc3'
author: foosel
date: 2023-03-22 14:00:00 +0100
card: /assets/img/blog/2023-03/2023-03-22-octoprint-1.9.0rc3-card.png
featuredimage: /assets/img/blog/2023-03/2023-03-22-octoprint-1.9.0rc3-card.png
poster: /assets/img/blog/2023-03/2023-03-22-octoprint-1.9.0rc3-poster.png
excerpt: The third release candidate for the upcoming 1.9.0 release, fixing some issues reported on the last ones and improving on some newly added functionality.

release: 1.9.0rc3
channel: Maintenance RCs
feedback: 4770

contributors:
- crysxd

---

This third release candidate of 1.9.0 fixes five regressions observed and reported on the last ones and improves on some newly added functionality:

> **✨ Improvements**
>
> - [#4759](https://github.com/OctoPrint/OctoPrint/pull/4759): Make it easier for plugins to move the webcam surface of the new webcam integration around.
>
> **🐛 Bug fixes**
>
> - [#4754](https://github.com/OctoPrint/OctoPrint/issues/4754) (regression): Fix saving of the number of extruders in the printer profile
> - [#4755](https://github.com/OctoPrint/OctoPrint/issues/4755) (regression): Fix the Application Keys workflow failing due to an unset CSRF cookie
> - [#4761](https://github.com/OctoPrint/OctoPrint/issues/4761) (regression): Fix an error with the new chart markings that could render the temperature graph non functional
> - [#4762](https://github.com/OctoPrint/OctoPrint/issues/4762) (regression): Fix the system wide language defaults getting ignored 
> - [#4763](https://github.com/OctoPrint/OctoPrint/issues/4763) (regression): Fix an internal server error when the Application Keys plugin is disabled
> - Fix the new `python setup.py scan_deps` dev tool breaking when encountering a non PEP440-compliant version number

For heads-ups, highlights and fancy pictures, please see [the earlier post about 1.9.0rc1](/blog/2023/03/07/new-release-candidate-1.9.0rc1/).

