---
layout: post
title: Rocks 6.1.1 (Sand Boa) is now available
date: 2014-04-15 21:20:51.000000000 -07:00
categories:
- "new" 
- "2014" 
tags: []
status: publish
type: post
published: true
meta:
  _edit_last: '1'
  _thumbnail_id: '483'
imagesrc: /assets/SandBoa.png
---

The latest update of Rocks codename  Sand Boa is now released. Sand Boa is a 64-bit only
release and is based upon CentOS 6.5. The Rocks-supplied OS rolls have all updates 
applied as of April 14, 2014. This includes updates for the OpenSSL [Heartbleed][1].

Please see the [Downloads Page][2] to get started.

* [Release Notes][3] are available
* [Support for ZFS][4] has been updated to version 0.6.2
* Condor is now [HTCondor roll][5] is at release 8.0.6
* Also included is a new roll called [fingerprint][6] that dynamically
  determines dependencies of compiled code on both Rocks and non-Rocks systems

Many thanks for all those who beta-tested this version of Rocks. 
Special thanks to John Zaitseff and Trevor Cooper for their code contributions.

{% assign base = 'http://central6.rocksclusters.org/roll-documentation/' %}
            
[1]: http://www.heartbleed.com
[2]: /downloads.html
[3]: {{ base }}/base/6.1.1/x8481.html
[4]: {{ base }}/zfs-linux/0.6
[5]: {{ base }}/condor/6.1.1
[6]: https://github.com/rocksclusters/FingerPrint
