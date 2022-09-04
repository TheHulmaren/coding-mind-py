# -*- coding: utf-8 -*-
"""
Created on Wed May 18 13:47:07 2022

@author: ihjo6_000
"""

import math 
import random

for i in range(0,6):
    if i <0:
        print('##')
    elif i < 5:
        print('#' + ' '*i + '#')
    else:
        print('######')
        N =[4, 12, 78, 13, 4, 6, 102, 901, 1, 34]

i = 0
_sum = 0
while i < len(N):
    _sum += N[i]
    i += 1

print(_sum)
print(len(N))

print(_sum / len(N))


N.sort()
print(N[5])

##1번 : 'ICN'

##2번 : break

##3번: current_temp

##4번: current_temp + '->' + current_temp 