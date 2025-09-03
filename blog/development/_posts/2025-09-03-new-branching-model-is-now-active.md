---
layout: post
title: "Heads-up devs: New branching model is now active"
author: foosel
date: 2025-09-03 13:45:00 +0200
card: /assets/img/blog/2025-09/2025-09-03-new-branching-model-card.png
featuredimage: /assets/img/blog/2025-09/2025-09-03-new-branching-model-card.png
poster: /assets/img/blog/2025-09/2025-09-03-new-branching-model-poster.png
excerpt:
  OctoPrint's branching model has changed. If you have a local checkout of OctoPrint,
  this might affect you.
---

First of all: If you are just a regular user of OctoPrint who doesn't know what git is and
has never checked out OctoPrint's source code to look at the code and/or make changes on it,
this likely doesn't affect you and you can stop to read here 😊

For all of the power users and developers among you that want to know what changed about
OctoPrint's branching model, read on.

For the longest time now I've been unhappy with the existing branching model on OctoPrint:
The name `maintenance` for the most active development branch hasn't properly mirrored
its actual role for a long time, `devel` hasn't seen any meaningful changes in years, and
there was a whole cluster of `staging/*` and `rc/*` branches that I had to juggle on every
RC and stable release. The whole model was extremely complicated, and also made it more
difficult for contributors to send their first PR.

So, earlier this year I planned a new branching model for OctoPrint, and after a lot of
preparation just put that into effect.

To summarize the changes that happened earlier today:

- `master` has been renamed to `main`
- `maintenance` has been renamed to `dev`
- `staging/bugfix` has been renamed to `bugfix`
- `staging/maintenance` has been renamed to `next`
- `rc/maintenance`, `rc/devel` and `staging/devel` have been removed
- `devel` has been renamed to `stale/devel` and will be removed once I'm sure I have
  migrated any changes that might still be interesting from there

You can read all about the new branching model in [the updated docs](https://docs.octoprint.org/en/main/development/branches.html),
but the gist of it is that all development happens on `dev` (and that should also be the target of any
and all PRs), `bugfix` is used for preparing bugfix releases and `next` is used for preparing and tagging release candidates
of upcoming stable releases.

Web server redirects should be in place for the docs and the source view on GitHub. **If you have a local
git checkout of OctoPrint however, you need to update your branch names and upstreams!**
Read below on how to do that.

There will probably be some hiccups here and there where I forgot to rename something that's still
referring to one of the old branches, but overall I hope it should be smooth flying from here
on out.

### How to update your local checkout

First of all, make sure `main` (the former `master`) is updated correctly:

```
git fetch origin
git remote prune origin
git fetch origin
git branch -m master main
git branch -u origin/main main
git remote set-head origin -a
```

Then, to change the name and upstream on a any further branches you might have checked out, run the following commands:

```
git branch -m <oldname> <newname>
git branch -u origin/<newname> <newname>
```
