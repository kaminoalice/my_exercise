#!/usr/bin/env python
#-*- coding:utf-8 -*-



import urllib.request

content = '分布式'
def getUrlList():
    req = urllib.request.Request(r'https://search.bilibili.com/all?keyword=%s'%urllib.request.quote(content))
    req.add_header('user-agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')
    html = urllib.request.urlopen(req).read()
    print(html.decode('utf-8'))
    
getUrlList()

