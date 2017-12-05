---
layout: page
title: Users Guides
date: 2017-12--1 
categories: []
tags: []
weight: 1
---


### Users Guide

The [Rocks Users Guide][1] contains procedures and methods to install and manage your cluster.

### Roll Guides

An archive of User guides for different versions of Rocks is available [here][19].

Previous Rocks 6.2 userguides are [here][3].

Guides available for the latest Rocks version (unless noted otherwise) are linked below:

* [area 51][2]
* [base][1]
* [htcondor][4]
* [fingerprint][7]
* [ganglia][5]
* [hpc][6]
* [kvm][10]
* [openvswitch][12]
* [perl][8]
* [python][9]
* [sge][11]
* [zfs-linux][13]

###  Community documentation

These documents are written in Spanish by Jorge Zuluaga from the Universidad de
Antioquia, Medellin Colombia (c. 2006).

* [Linux Clustering con Rocks, una Gu&iacute;a Pr&aacute;ctica][14] A Practical Guide to Rocks.
* [Ap&eacute;ndice A Instalaci&oacute;n de un Cluster Rocks][15]
* [Ap&eacute;ndice A Instalaci&oacute;n de Gaussian en un Cluster Rocks][16]
* [Montaje B&aacute;sico de Linux Clusters Una Guia Pr&aacute;ctica][17]

{% assign base = 'http://central-7-0-x86-64.rocksclusters.org/roll-documentation' %}
{% assign archbase = '/assets/usersguides/roll-documentation' %}
{% assign version = '7.0' %}
{% assign condorversion = '8.6.8' %}
{% assign zfsversion = '0.7.3' %}
{% assign fprintversion = '1.0' %}
{% assign ovsversion = '2.7.2' %}

[3]:  /docs/guides-6-2
[1]: {{ base }}/base/{{ version }} 
[2]: {{ base }}/area51/{{ version }} 

[4]: {{ base }}/condor/{{ condorversion }} 
[5]: {{ base }}/ganglia/{{ version }} 
[6]: {{ base }}/hpc/{{ version }} 
[7]: {{ base }}/fingerprint/{{ fprintversion }} 
[8]: {{ base }}/perl/{{ version }} 
[9]: {{ base }}/python/{{ version }} 
[10]: {{ base }}/kvm/{{ version }} 
[11]: {{ base }}/sge/{{ version }} 
[12]: {{ base }}/openvswitch/{{ ovsversion }} 
[13]: {{ base }}/zfs-linux/{{ zfsversion }}
[19]: {{ archbase }}/

