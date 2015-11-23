#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'zhao'
import os
def fech(arg):
    with open('haproxy.conf') as f:
        ids = False
        #fech_domain = raw_input(u'请输入您要查找的域名:')
        li = []
        for lines in f:
            lines = lines.strip()
            #print 'backend %s'%arg
            a = 'backend %s'%arg
            if lines == a:
                ids = True
                continue
            if ids and lines.startswith('backend'):
                ids = False
                break
            if ids and lines:
                li.append(lines)
    return li



fech_domain = raw_input(u'请输入您要查找的域名：')
houlaoshi = fech(fech_domain)
print houlaoshi



