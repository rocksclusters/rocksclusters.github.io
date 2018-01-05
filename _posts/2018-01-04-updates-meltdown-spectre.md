---
layout: post
title: Updating Rocks 7.0 for Spectre/Meltdown Vulnerabilities 
date: 2018-01-04 16:00:00.000000000 -07:00
categories: 
- "new"
- "2018"
tags: []
status: publish
type: post
published: true

---

The [Spectre/Meltdown][1] security vulnerabilites affect (nearly) 
all hardware and is addressed by OS updates. 
This is not a Rocks-specific issue, but Rocks-based
systems are vulnerable. See the [Centos List Archive][2] for specific
information on the Security Update

The broad brush of how to approach this:

* Create an updates roll with `rocks create mirror` 
* add this roll to your current rocks distribution with `rocks add roll`
* enable this roll `rocks enable roll`
* rebuild the distribution in `/export/rocks/install` with `rocks create distro`
* Use `yum` to update your frontend and then reboot
* Reinstall subordinate nodes or run `yum -y update` on all subordinate nodes 

Here are specific commands with mirror close to California. Use a CentOS mirror
close to you for better performance

```
# baseurl=http://mirror.hmc.edu
# osversion=7.4.1708
# version=`date +%F`
# rocks create mirror ${baseurl}/centos/${osversion}/updates/x86_64/Packages/ rollname=Updates-CentOS-${osversion} version=${version}
# rocks add roll Updates-CentOS-${osversion}-${version}*iso
# rocks enable roll Updates-CentOS-${osversion} version=${version}
# (cd /export/rocks/install; rocks create distro)
# yum clean all; yum update
```

After you have updated your frontend, you can update your compute (or other)
subordinate nodes by reinstalling them or updating them via yum. The following
gives the "yum update" method. Please note that if you have a reasonably large
cluster, it likely is faster to reinstall your compute nodes.
 
```
# rocks run host compute "yum clean all; yum -y update"
# rocks run host compute "shutdown -r now"
```

[1]: https://www.us-cert.gov/ncas/alerts/TA18-004A 
[2]: https://lists.centos.org/pipermail/centos-announce/2018-January/date.html 
