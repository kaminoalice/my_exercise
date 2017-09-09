#!/usr/bin/env python
#-*- coding:utf-8 -*-

import re
import os


def execCmd(cmd):
    r = os.popen(cmd)
    text = r.read()
    r.close()
    return text

# 获取计算机MAC地址和IP地址
if __name__ == '__main__':
    cmd = "ipconfig /all"
    result = execCmd(cmd)
    first_pat = r"Wireless LAN*"
    pat = re.search(first_pat,result)
    print(pat.group())
#     pat1 = "Physical Address[\. ]+: ([\w-]+)"
#     pat2 = "IPv4 Address[\. ]+: ([\.\d]+)"
#     MAC = re.findall(pat1, result)[0]    # 找到MAC
#     IP = re.findall(pat2, result)[0]    # 找到IP
#     print("MAC=%s, IP=%s" %(MAC, IP))

 
