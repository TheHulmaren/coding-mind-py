#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 11 19:14:03 2022

@author: igyumin
"""

M = [[-4,1,5,2,0],
     [7,2,-3,6,10],
     [-5,1,9,1,-7]]

row_len = len(M[0])
cal_len = len(M)

total_sum = 0

for i in range(cal_len+1):
    print('\t' + '+--' * row_len + '+')
    if i == len(M):
        print('[{0:>2d}]'.format(total_sum), end='')
        
        for k in range(row_len):
            cal_sum = 0
            for m in range(cal_len):
                cal_sum += M[m][k]
            
            print(' {0:>2d}'.format(cal_sum), end='')
    else:
        row_sum = sum(M[i])
        total_sum += row_sum
        print(' {0:>2d} '.format(row_sum), end='')
        
        for j in M[i]:
            print('|{0:>2d}'.format(j), end='')
        print('|')
        