#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 13:14:21 2022

@author: igyumin
"""

def is_odd(num):
    return True if num%2 == 1 else False


print(is_odd(7))
print(is_odd(10))



def replace_txt(filepath, target, new):
    # 파일 내용 읽기
    rf = open(filepath, 'r')
    content = rf.read()
    
    wf = open(filepath, 'w')
    
    # 내용 수정 후 쓰기
    edited = content.replace(target, new)
    wf.write(edited)
    
    wf.close()


replace_txt('test.txt', 'short', '짧음')
