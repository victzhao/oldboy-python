#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'zhao'

import os
def fetch(domain):
    fetch_tittle = 'backend %s' %domain
    flag = False
    fetch_list = []
    with open('haproxy.conf','r') as file:
        for i in file:
            i = i.strip()
            if i == fetch_tittle:
                flag = True
                continue
            if flag and i.startswith('backend'):
                flag = False
                break
            if flag and i:
                fetch_list.append(i)

    return fetch_list
def adds(info):
    domains = info['bakend']
    tittle = 'backend %s' %domains
    fetch_list = fetch(domains)
    adds_records = 'server %s %s weight %s maxconn %s' %(info['record']['server'],info['record']['server'],info['record']['weight'],info['record']['maxconn'])
    with open('haproxy.conf','r') as read_file,open('haproxy.new','w') as write_file:
        if fetch_list:
            #如果表不为空，说明该backend已经存在，则只需要插入记录即可
            flag = False
            written = False
            if adds_records in fetch_list:
                pass
            else:
                fetch_list.append(adds_records)
            for new_lines in read_file:
                new_line = new_lines.strip()
                if new_line == tittle:
                    write_file.write(new_line+'\n')
                    flag = True
                    continue
                if flag and new_lines.startswith('backend'):
                    flag = False
                if not flag:
                    write_file.write(new_lines)
                else:
                    for i in fetch_list:
                        if not written:
                            write_file.write('%s%s\n' %(' '*8,i))
                    written = True
        else:
            #如果列表为空，则表示没有backend，则只需在末尾追加即可
            with open ('haproxy.conf','r') as read_file,open('haproxy.new','w') as write_file:
                for i in read_file:
                    write_file.write(i)
                write_file.write(tittle+'\n')
                write_file.write('%s%s'%(' '*8,adds_records))
    if os.path.exists('haproxy.conf.bak'):
        os.remove('haproxy.conf.bak')
        os.rename('haproxy.conf','haproxy.conf.bak')
    else:
        os.rename('haproxy.conf','haproxy.conf.bak')
 

    if os.path.exists('haproxy.conf'):
        os.remove('haproxy.conf')
        os.rename('haproxy.new','haproxy.conf')
    else:
        os.rename('haproxy.new','haproxy.conf')

def delete(info):
    domains = info['bakend']
    tittle = 'backend %s' %domains
    fetch_list = fetch(domains)
    adds_records = 'server %s %s weight %s maxconn %s' %(info['record']['server'],info['record']['server'],info['record']['weight'],info['record']['maxconn'])
    if fetch_list:
        #列表不空，则表示记录存在，可以删除
        with open('haproxy.conf','r') as read_file,open('haproxy.new','w') as write_file:
            flag = False
            written = False
            fetch_list.remove(adds_records)
            for i in read_file:
                lines = i.strip()
                if lines == tittle:
                    write_file.write(lines+'\n')
                    flag = True
                    continue
                if flag and i.startswith('backend'):
                    flag = False
                if not flag:
                    write_file.write(i)
                else:
                    if not written:
                        for i in fetch_list:
                            write_file.write('%s%s\n'%(' '*8,i))
                        written = True
    else:
        #列表空，说明记录不存在，无需删除
        pass
    if os.path.exists('haproxy.conf.bak'):
        os.remove('haproxy.conf.bak')
        os.rename('haproxy.conf','haproxy.conf.bak')
    else:
        os.rename('haproxy.conf','haproxy.conf.bak')


    if os.path.exists('haproxy.conf'):
        os.remove('haproxy.conf')
        os.rename('haproxy.new','haproxy.conf')
    else:
        os.rename('haproxy.new','haproxy.conf')


#domains = raw_input(u'请输入查找的域名：')
#print fetch(domains)
#infomation = {'bakend': 'www.baidu.org','record':{'server': '3.3.3.3','weight': 20,'maxconn': 3000}}
#adds(infomation)
#infomation = {'bakend': 'www.baidu.org','record':{'server': '3.3.3.3','weight': 20,'maxconn': 3000}}
#delete(infomation)

while True:
    print u'''
**********************************
    1 查找
    2 增加
    3 删除
**********************************'''
    option = str(raw_input(u'请输入您需要的功能编号:'))
    print type(option)
    if option == '1':
        domains = raw_input(u'请输入查找的域名：')
        print fetch(domains)
    elif option == '2':
        infomation = {'bakend': 'www.baidu.org','record':{'server': '3.3.3.3','weight': 20,'maxconn': 3000}}
        adds(infomation)
    elif option == '3':
        infomation = {'bakend': 'www.baidu.org','record':{'server': '3.3.3.3','weight': 20,'maxconn': 3000}}
        delete(infomation)





