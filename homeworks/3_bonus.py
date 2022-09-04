#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 10 20:54:10 2022

@author: igyumin
"""

line = 'Life is short, learn Python!'

n = 5

line_len = len(line)
v_limit = len(line) - n + 1

for v in range(v_limit):
    n_start = v
    n_end = n_start + n
    
    m_start = line_len - 1 - v - (n - 1)
    m_end = m_start + n
    
    if n_start <= m_start and n_end >= m_start:
        output = line[n_start:m_end]
        print(' '*n_start + output)
    elif n_start > m_start and n_start <= m_end:
        output = line[m_start:n_end]
        print(' '*m_start + output)
    elif n_start <= m_start:
        print(' '*n_start + line[n_start:n_end] + ' '*(m_start - n_end) + line[m_start:m_end])
    elif n_start > m_start:
        print(' '*m_start + line[m_start:m_end] + ' '*(n_start - m_end) + line[n_start:n_end])
        

