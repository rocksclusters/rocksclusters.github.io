---
layout: post
title: Rocks 6.2 is Released
date: 2015-05-11 11:47:49.000000000 -07:00
categories: []
tags: []
status: publish
type: post
published: true

---

The latest update of Rocks codename Sidewinder is now released. Sidewinder is
a 64-bit only release and is based upon CentOS 6.6   The Rocks-supplied OS
rolls have all updates applied as of May 10, 2015.

Please see the  <a href="/downloads.html">Downloads Page</a> to get started.

* [Release notes][1] are available
* [Support for ZFS][2] has been updated to version 0.6.4.1.
* [HTCondor roll][3] (former Condor) is at release 8.2.8
* Also included is support for perfSONAR, where cluster builders can decide to
  install the full GUI (recommended for a standalone perfSONAR host) or just the
  command tools. [Customizing what is installed for perfSONAR][4] gives four
  attributes that control which elements of perfSONAR are installed on hosts.
* New to 6.2 is the ability to reconfigure the fully qualified domain name of
  your cluster (FQDN). There are some [caveats][5] to the process.
* When building a frontend on networks with jumbo frames, the cluster builder
  can specify the mtu on the "build" command line.

You can visit Rocks source code [github][6]

{% assign base = 'http://central6.rocksclusters.org/roll-documentation/' %}

[1]: {{ base }}/base/6.2/x8552.html
[2]: {{ base }}/zfs-linux/0.6.4.1
[3]: {{ base }}/condor/8.2.8
[4]: {{ base }}/perfSONAR/3.4.1/customizing-perfsonar.html#AEN39
[5]: {{ base }}/base/6.2/reconfigure.html
[6]: {{ site.github_url }}
