---
layout: post
title: Rocks 6.1 (x86-64) Beta (Emerald Boa) Available
date: 2012-10-23 13:36:11.000000000 -07:00
categories:
- "2012" 
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

Rocks 6.1 is now available for Beta testing.   Please see [Downloads][4] page.

This preview is based upon [CentOS Version 6.3][3] with all updates as 21 October, 2012 applied.

Some of the new features/updates of Rocks 6.1:

1. Two-factor authentication is supported using [google authenticator][1]
1. Internal ssh authentication is now host-based
1. A frontend can be installed using a single partition
1. ZFS on Linux roll now available. Based upon the [ZFS on Linux][2] rc11.  Note ZFS
   on linux is a "source" roll.
1. Support GPT partition tables for drives > 2TB
1. Improved IPMI documentation
1. **rocks create distro** speed improved by removing redundant checksum calculation
1. Infiniband (Mellanox) configured in the HPC roll with subnet manager running
   on frontend
1. SGE roll updates to GE-2011p1
1. Condor roll updated to 7.8.5

[1]: http://code.google.com/p/google-authenticator/
[2]: http://zfsonlinux.org
[3]: http://lists.centos.org/pipermail/centos-announce/2012-July/018706.html
[4]: /downloads.html
