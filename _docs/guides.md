---
layout: page
title: Users Guides
date: 2016-05-16 
categories: []
tags: []
weight: 2
---


### Users Guide

* The [Rocks Users Guide][1] contains procedures and methods to install and manage your cluster.
* The [Roll Developers Guide][18] contains information for Roll developers. It covers the internals 
  of a Roll structure, how to build a Roll and advice on how to debug and test a Roll.

### Roll Guides

An archive of User guides for different versions of Rocks is available [here][19].

Guides available for the latest Rocks version (unless noted otherwise) are linked below:

* [Area 51][2]
* [Bio][3]
* [Condor][4]
* [Ganglia][5]
* [HPC][6]
* [Java][7]
* [Perl][8]
* [Python][9]
* [Service Pack][10] (for Rocks 6.1)
* [Sun Grid Engine (SGE)][11]
* [Xen][12] (for Rocks 5.5)
* [ZFS on Linux][13]

###  Community documentation

These documents are written in Spanish by Jorge Zuluaga from the Universidad de
Antioquia, Medellin Colombia (c. 2006).

* [Linux Clustering con Rocks, una Gu&iacute;a Pr&aacute;ctica][14] A Practical Guide to Rocks.
* [Ap&eacute;ndice A Instalaci&oacute;n de un Cluster Rocks][15]
* [Ap&eacute;ndice A Instalaci&oacute;n de Gaussian en un Cluster Rocks][16]
* [Montaje B&aacute;sico de Linux Clusters Una Guia Pr&aacute;ctica][17]

{% assign base = '/assets/usersguides/roll-documentation' %}
{% assign version = '6.2' %}
{% assign condorversion = '8.2.8' %}

[1]: {{ base }}/base/{{ version }} 
[2]: {{ base }}/area51/{{ version }} 
[3]: {{ base }}/bio/{{ version }} 
[4]: {{ base }}/condor/{{ condorversion }} 
[5]: {{ base }}/ganglia/{{ version }} 
[6]: {{ base }}/hpc/{{ version }} 
[7]: {{ base }}/java/{{ version }} 
[8]: {{ base }}/perl/{{ version }} 
[9]: {{ base }}/python/{{ version }} 
[10]: {{ base }}/service-pack/6.1
[11]: {{ base }}/sge/{{ version }} 
[12]: {{ base }}/xen/5.5
[13]: {{ base }}/zfs-linux/0.6.4.1
[18]: {{ base }}/developers-guide/6.0
[19]: {{ base }}/

{% assign spanish = '/assets/usersguides/spanish' %}

[14]: {{ spanish }}/rocks-practical-guide-manager_user-rel1.pdf
[15]: {{ spanish }}/rocks-practical-guide-appendix-A-rel1.pdf
[16]: {{ spanish }}/rocks-practical-guide-appendix-B-rel1.pdf
[17]: {{ spanish }}/cluster-practical-guide-rel1.pdf

