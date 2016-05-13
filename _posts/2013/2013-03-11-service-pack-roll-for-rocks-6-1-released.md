---
layout: post
title: Service Pack Roll for Rocks 6.1 Released
date: 2013-03-11 16:24:08.000000000 -07:00
categories: 
- "2013"
tags: []
status: publish
type: post
published: true
meta:
  _edit_last: '1'
author:
  login: admin
  email: ppapadopoulos@ucsd.edu
  display_name: admin
  first_name: ''
  last_name: ''
---

This fixes a number bugs/errors/omissions in Rocks 6.1 (Emerald Boa).  All new
clusters should be built including the service pack roll. No further action is
required when installed on a new cluster.

The roll is also designed to be applied to existing clusters, requiring only a
reboot of the head node when complete.  The service pack is available for both
32-bit and 64-bit architectures.

Please follow the [installation instructions][1].

The Service Package fixes several problems, noted [here][2].
Direct Downloads of the service pack rolls are:

* [32-bit service pack][3] (MD5 Checksum: 944982f6da6c9cb94ff93bee24df0f9f)
* [64-bit service pack][4] (MD5 Checksum: 6ea52482d89f82a74a6a06ee48b725c7)

To maintain compatibility with installed clusters, the base OS rolls are
unchanged. The Jumbo rolls (which include all basic rolls) have been updated
to include the service pack roll.

{% assign base = 'http://central6.rocksclusters.org/roll-documentation/' %}

[1]: {{ base }}/service-pack/6.1
[2]: {{ base }}/base/6.1/x2541.html
[3]: ftp://ftp.rocksclusters.org/pub/rocks/rocks-6.1/linux/service-pack-6.1-1.i386.disk1.iso
[4]: ftp://ftp.rocksclusters.org/pub/rocks/rocks-6.1/linux/service-pack-6.1-1.x86_64.disk1.iso
