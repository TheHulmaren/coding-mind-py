#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  4 13:11:28 2022

@author: igyumin
"""



path = "Users/kyumin/documents/coding.app/codingmind.zip/1-1.py/muhyun/blah.swift/python.py"


# 2-1

selection = "muhyun"

path_split = path.split('/') # 슬래시 기준으로 쪼개기

sel_depth = path_split.index(selection) # muhyun 찾기

print(sel_depth)
print()


# 2-2

first = "kyumin"
second = "blah.swift"

path_split = path.split('/')

first_index = path_split.index(first)
second_index = path_split.index(second)

interval = abs(first_index - second_index) - 1

print(interval)
print()



# 2-3

target = "coding.app"

path_split = path.split('/')

path_split.remove(target)

path_new = '/'.join(path_split) # 사이에 /를 넣고 붙이기

print(path_new)
print()



# 2-4

path_split = path.split('/')

output = '\n> '.join(path_split)

print(output)
print()
















