---
layout: page
title: Rocks 6.2 Sidewinder (CentOS 6.6)
date: 2015-05-11 10:01:38.000000000 -07:00
categories: []
tags: []
---

{% assign repodir = 'https://drive.google.com/open?id=' %}
{% assign md5sum = '0By0W9PhyYsOpMV9WSWk1eU5Xc2s' %}
{% assign dvd1 = '0B2VTJMbHpU8yS1hzRW1CNTVfYkU' %}
{% assign dvd2 = '0B2VTJMbHpU8yNzZ5MlE1emV1M00' %}
{% assign kernel = '0B2VTJMbHpU8yY1lURWsweS15V0k' %}
{% assign base = '0B2VTJMbHpU8yMHJJSlJCVzk5akE' %}
{% assign os1 = '0B2VTJMbHpU8yMkdVRk1nUk5rajA' %}
{% assign os2 = '0B2VTJMbHpU8yLUJuZTdTcXNoQ00' %}
{% assign os3 = '0B2VTJMbHpU8yZzBRSWJqNG1STnc' %}
{% assign os4 = '0B2VTJMbHpU8ybVU4ZjVvYlhDaEk' %}
{% assign os5 = '0B2VTJMbHpU8yckRPbGNDaklvR3M' %}
{% assign os6 = '0B2VTJMbHpU8yd2FxSEF2V0pJWXM' %}
{% assign os7 = '0B2VTJMbHpU8ycF9rV211cWdUaVk' %}
{% assign os8 = '0B2VTJMbHpU8yZklXQy1YTHY3Nmc' %}
{% assign os9 = '0B2VTJMbHpU8yLUU4UHMxTUE4Mlk' %}
{% assign os10 = '0B2VTJMbHpU8yUjhXYzhBVEhvVDQ' %}
{% assign area51 = '0B2VTJMbHpU8yazZxQnhicmVzTDQ' %}
{% assign bio = '0B2VTJMbHpU8yNW1POE9LX1NTdTQ' %}
{% assign fingerprint = '0B2VTJMbHpU8ydE0tT0xRUEg0ZTA' %}
{% assign ganglia = '0B2VTJMbHpU8yblR0Q3prQmt3T3c' %}
{% assign hpc = '0B2VTJMbHpU8ySVJ2S25TYkhEcmc' %}
{% assign htcondor = '0B2VTJMbHpU8yb25wS3A3c3J5czQ' %}
{% assign idpl-config = '0B2VTJMbHpU8ycjkwczhmV3VzMzA' %}
{% assign java = '0B2VTJMbHpU8yMDk5eHUyN2FFdG8' %}
{% assign kvm = '0B2VTJMbHpU8yNGNnTVN4cE5RVFE' %}
{% assign perfSONAR = '0B2VTJMbHpU8yOF9UcHFwaE9qcGs' %}
{% assign perl = '0B2VTJMbHpU8yNzlPbFBFQ2RBYU0' %}
{% assign python = '0B2VTJMbHpU8yNHc3OEhNRmVaWlE' %}
{% assign serf = '0B2VTJMbHpU8yM0NORU5ZcWNMNWs' %}
{% assign sge = '0B2VTJMbHpU8yMVpCZ2YxS1ZvYlE' %}
{% assign web-server = '0B2VTJMbHpU8yYUU2Qm5tQWk4MDg' %}
{% assign zfs-linux = '0B2VTJMbHpU8ySHltU3h3bmc5RFk' %}
{% assign jumbo1 = 'Area51, Base, Bio, Fingerprint, Ganglia, Hpc, Htcondor, Idpl-config, Java,<br/>Kernel, KVM,OS, perfSONAR, Perl, Python, SGE, Web-server, ZFS' %}
{% assign jumbo2 = 'Above rolls without idpl-config' %}
{% assign googledrive = "https://drive.google.com/folderview?id=0B2VTJMbHpU8yYXpwZ1MwVlJIQmM#list" %}

[1]: {{repodir}}{{md5sum}} 
[2]: {{googledrive}}

### Operating System Base
Rocks 6.2 (Sidewinder) x86_64 is based upon CentOS 6.6 with all updates available as of 10 May 2015. 

### Building a bare-bones compute cluster

* Boot your frontend with the **Kernel/Boot Roll**
* Then supply the 
  * **Base roll**
  * **OS roll Disk 1**
  * **OS roll Disk 2**
  * **OS roll Disk 3** 

### Building a more complex cluster

In addition to above select the following rolls: 

* Area51 
* HPC 
* Ganglia 
* web-server 
* perl 
* python 
* SGE or Torque (not both)
* Condor can be used independently or in conjunction with SGE/Torque. 
* ZFS version 0.6.4.1 can be used to build reliable storage systems. 
* New for 6.2 is support for perfSONAR (version 3.4.2).

### Building Custom Clusters
If you wish to build a custom cluster, you must choose from our a la carte selection, but make sure 
to download the required Base, Kernel/Boot and all of the OS rolls. The OS rolls include 
CentOS 6.6 w/updates pre-applied (you may also use your own Red Hat Enterprise
Linux 6.6 media). The first 3 disks are the only ones required to build a
cluster with the rolls on this site. Most users will want the full updated OS
so that other software can be added. You may add the os disks 4 - 10 after you
have installed your frontend.

### MD5 Checksums
Please double check the [MD5 checksums][1] for all the rolls you download.

### Downloads
All ISOs are available for downloads from [here][2].
Individual links are listed below.

**Jumbo DVDs (x86_64)**

<table class="rolls">
  <tr>
    <th width="30%">DVD</th>
    <th width="70%">Description</th>
  </tr>
  <tr>
    <td class="odd"><a href="{{repodir}}{{dvd1}}">jumbo dvd option 1</a></td>
    <td class="odd">Jumbo DVD: {{jumbo1}} </td>
  </tr>
  <tr>
    <td><a href="{{repodir}}{{dvd2}}">jumbo dvd option 2</a></td>
    <td>Jumbo DVD: {{jumbo2}}</td>
  </tr>
</table>
<br/>

**Individual rolls (x86_64)**

<table class="rolls">
<tr>
  <th width="10%">Name</th>
  <th width="40%">Description</th>
  <th width="10%">Name</th>
  <th width="40%">Description</th>
</tr>
<tr>
  <td class="odd"><a href="{{repodir}}{{kernel}}">kernel</a></td>
  <td class="odd">Rocks Bootable Kernel Roll <strong>required</strong></td>
  <td class="odd"><a href="{{repodir}}{{bio}}">bio</a></td>
  <td class="odd">Bioinformatics utilities</td>
</tr>
<tr>
  <td><a href="{{repodir}}{{base}}">base</a></td>
  <td>Rocks Base Roll <strong>required</strong></td>
  <td><a href="{{repodir}}{{fingerprint}}">fingerprint</a></td>
  <td>Fingerprint application dependencies</td>
</tr>
<tr>
  <td class="odd"><a href="{{repodir}}{{os1}}">os disk 1</a></td>
  <td class="odd">OS Roll <strong>required</strong></td>
  <td class="odd"><a href="{{repodir}}{{htcondir}}">HTCondor</a></td>
  <td class="odd">HTCondor High Throughput Computing (version 8.2.8)</td>
</tr>
<tr>
  <td><a href="{{repodir}}{{os2}}">os disk 2</a></td>
  <td>OS Roll <strong>required</strong></td>
  <td><a href="{{repodir}}{{ganglia}}">ganglia</a></td>
  <td>Cluster monitoring system from UCB</td>
</tr>
<tr>
  <td class="odd"><a href="{{repodir}}{{os3}}">os disk 3</a></td>
  <td class="odd">OS Roll <strong>required</strong></td>
  <td class="odd"><a href="{{repodir}}{{hpc}}">hpc</a></td>
  <td class="odd">Rocks HPC Roll</td>
</tr>
<tr>
  <td><a href="{{repodir}}{{os4}}">os disk 4</a></td>
  <td>OS Roll (optional)</td>
  <td><a href="{{repodir}}{{kvm}}">kvm</a></td>
  <td>Support for building KVM VMs on cluster nodes</td>
</tr>
<tr>
  <td class="odd"><a href="{{repodir}}{{os5}}">os disk 5</a></td>
  <td class="odd">OS Roll (optional)</td>
  <td class="odd"><a href="{{repodir}}{{perfsonar}}">perfSONAR</a></td>
  <td class="odd">The perfSONAR Roll (Version 3.4.2)</td>
</tr>
<tr>
  <td><a href="{{repodir}}{{os6}}">os disk 6</a></td>
  <td>OS Roll (optional)</td>
  <td><a href="{{repodir}}{{perl}}">perl</a></td>
  <td>Support for Newer Version of Perl</td>
</tr>
<tr>
  <td class="odd"><a href="{{repodir}}{{os7}}">os disk 7</a></td>
  <td class="odd">OS Roll (optional)</td>
  <td class="odd"><a href="{{repodir}}{{python}}">python</a>
  <td class="odd">Python 2.7 and Python 3.x</td>
</tr>
<tr>
  <td><a href="{{repodir}}{{os8}}">os disk 8</a></td>
  <td>OS Roll (optional)</td>
  <td><a href="{{repodir}}{{sge}}">sge</a>
  <td>Sun Grid Engine (Open Grid Scheduler)  job queueing system (Version GE2011)</td>
</tr>
<tr>
  <td class="odd"><a href="{{repodir}}{{os9}}">os disk 9</a></td>
  <td class="odd">OS Roll (optional)</td>
  <td class="odd"><a href="ftp://ftp.uit.no/pub/linux/rocks/torque-roll/6.1.0">torque</a></td>
  <td class="odd">Torque+Maui job queueing system (packaged by HPC Group at University of Tromso, Norway)</td>
</tr>
<tr>
  <td><a href="{{repodir}}{{os10}}">os disk 10</a></td>
  <td>OS Roll (optional)</td>
  <td><a href="{{repodir}}{{web-server}}">web-server</a></td>
  <td>Rocks Web Server Roll</td>
</tr>
<tr>
  <td class="odd"><a href="{{repodir}}{{area51}}">area51</a></td>
  <td class="odd">System security related services and utilities </td>
  <td class="odd"><a href="{{repodir}}{{zfs-linux}}">zfs-linux</a></td>
  <td class="odd">ZFS On Linux Roll. Build and Manage Multi Terabyte File Systems.</td>
</tr>
</table>

