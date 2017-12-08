---
layout: post
title: Rocks 7.0 ZFS Roll Updated 
date: 2017-12-08 12:00:00.000000000 -07:00
categories: 
- "new"
- "2017"
tags: []
status: publish
type: post
published: true

---

The ZFS roll for Rocks 7.0 has been updated. It addresses an issue at node installation
when a new kernel is in rocks distribution (via `rocks create distro`), but there is no
corresponding kmod-spl/kmod-zfs rpm to match the new kernel.

New installations from the current Rocks central server will automatically use the
updated roll. 

Existing installations should 
* download the [updated zfs roll][1] roll iso. (you should validate its [md5sum][2]) 
* add this roll to your current rocks distribution with `rocks add roll zfs-linux*iso`
* rebuild the distribution in `/export/rocks/install` with `rocks create distro`

No further action is needed after you have updated the roll.

{% assign base = 'http://central-7-0-x86-64.rocksclusters.org/isos/' %}

[1]: {{ base }}/zfs-linux-0.7.3-2.x86_64.disk1.iso
[2]: {{ base }}/md5sums.txt
