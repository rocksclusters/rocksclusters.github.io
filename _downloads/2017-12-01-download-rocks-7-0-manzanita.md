---
layout: page
title: Rocks 7.0 Manzanita (CentOS 7.4)
date: 2017-12-01 10:44:38.000000000 -07:00
categories: []
tags: []
---

{% assign repodir = 'http://central-7-0-x86-64.rocksclusters.org/isos/' %}
{% assign md5sum = 'md5sums.txt' %}


{% assign kernel = 'kernel-7.0-0.x86_64.disk1.iso' %}
{% assign base = 'base-7.0-2.x86_64.disk1.iso' %}
{% assign core = 'core-7.0-2.x86_64.disk1.iso' %}
{% assign CentOS = 'CentOS-7.4.1708-0.x86_64.disk1.iso' %}
{% assign fingerprint = 'fingerprint-7.0-0.x86_64.disk1.iso' %}
{% assign ganglia = 'ganglia-7.0-2.x86_64.disk1.iso' %}
{% assign hpc = 'hpc-7.0-0.x86_64.disk1.iso' %}
{% assign htcondor = 'htcondor-8.6.8-1.x86_64.disk1.iso' %}
{% assign kvm = 'kvm-7.0-0.x86_64.disk1.iso' %}
{% assign openvswitch = 'openvswitch-2.8.0-0.x86_64.disk1.iso' %}
{% assign perl = 'perl-7.0-0.x86_64.disk1.iso' %}
{% assign python = 'python-7.0-2.x86_64.disk1.iso' %}
{% assign sge = 'sge-7.0-0.x86_64.disk1.iso' %}
{% assign Updates-CentOS = 'Updates-CentOS-7.4.1708-2017-12-01-0.x86_64.disk1.iso' %}
{% assign zfs-linux = 'zfs-linux-0.7.3-1.x86_64.disk1.iso' %}
{% assign area51 = 'area51-7.0-0.x86_64.disk1.iso' %}


[1]: {{repodir}}{{md5sum}} 
[2]: {{repodir}}

### Operating System Base
Rocks 7.0 (Manzanita) x86_64 is based upon CentOS 7.4 with all updates available as of 1 Dec 2017. 

### Building a bare-bones compute cluster

* Boot your frontend with the **kernel** roll
* Then choose the following rolls: **base**, **core**, **kernel**, **CentOS** and **Updates-CentOS**

### Building a more complex cluster

In addition to above, select the following rolls: 

<table width="85%">
<tr><td width="30%">
<ul>
    <li> area51 </li>
    <li> fingerprint </li>
    <li> ganglia </li>
    <li> kvm (used for virtualization)</li>
    <li> hpc </li>
</ul>
</td>
<td>
<ul>
    <li> htcondor (used independently or in conjunction with sge)</li>
    <li> perl </li>
    <li> python </li>
    <li> sge </li>
    <li> zfs-linux (used to build reliable storage systems)</li>
</ul>
</td>
</tr>
</table>

### Building Custom Clusters
If you wish to build a custom cluster, you must choose from our a la carte selection, but make sure 
to download the required **base**, **kernel** and both **CentOS** rolls. The CentOS rolls include 
CentOS 7.4 w/updates pre-applied.  Most users will want the full updated OS
so that other software can be added.

### MD5 Checksums
Please double check the [MD5 checksums][1] for all the rolls you download.

### Downloads
All ISOs are available for downloads from [here][2].
Individual links are listed below.
<br/>

<table class="rolls">
<tr>
<th width="12%">Name</th>
<th width="38%">Description</th>
<th width="10%">Name</th>
<th width="40%">Description</th>
</tr>

<tr>
<td class="odd"><a href="{{repodir}}{{kernel}}">kernel</a></td>
<td class="odd">Rocks Bootable Kernel Roll <strong>required</strong></td>
<td class="odd"><a href="{{repodir}}{{zfs-linux}}">zfs-linux</a></td>
<td class="odd">ZFS On Linux Roll. Build and Manage Multi Terabyte File Systems.</td>
</tr>

<tr>
<td><a href="{{repodir}}{{base}}">base</a></td>
<td>Rocks Base Roll <strong>required</strong></td>
<td><a href="{{repodir}}{{fingerprint}}">fingerprint</a></td>
<td>Fingerprint application dependencies</td>
</tr>

<tr>
<td class="odd"><a href="{{repodir}}{{core}}">core</a></td>
<td class="odd">Core Roll <strong>required</strong></td>
<td class="odd"><a href="{{repodir}}{{hpc}}">hpc</a></td>
<td class="odd">Rocks HPC Roll</td>
</tr>

<tr>
<td><a href="{{repodir}}{{CentOS}}">CentOS</a></td>
<td>CentOS Roll <strong>required</strong></td>
<td><a href="{{repodir}}{{htcondir}}">htcondor</a></td>
<td>HTCondor High Throughput Computing (version 8.2.8)</td>
</tr>

<tr>
<td class="odd"><a href="{{repodir}}{{Updates-CentOS}}">Updates-CentOS</a></td>
<td class="odd">CentOS Updates Roll <strong>required</strong></td>
<td class="odd"><a href="{{repodir}}{{sge}}">sge</a>
<td class="odd">Sun Grid Engine (Open Grid Scheduler) job queueing system</td>
</tr>

<tr>
<td><a href="{{repodir}}{{kvm}}">kvm</a></td>
<td>Support for building KVM VMs on cluster nodes</td>
<td><a href="{{repodir}}{{perl}}">perl</a></td>
<td>Support for Newer Version of Perl</td>
</tr>

<tr>
<td class="odd"><a href="{{repodir}}{{ganglia}}">ganglia</a></td>
<td class="odd">Cluster monitoring system from UCB</td>
<td class="odd"><a href="{{repodir}}{{python}}">python</a>
<td class="odd">Python 2.7 and Python 3.x</td>
</tr>

<tr>
<td><a href="{{repodir}}{{area51}}">area51</a></td>
<td>System security related services and utilities </td>
<td><a href="{{repodir}}{{openvswitch}}">openvswitch</a></td>
<td>Rocks integration of OpenVswitch</td>
</tr>

</tbody>
</table>

