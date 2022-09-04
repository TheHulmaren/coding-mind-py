#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  8 11:29:51 2022

@author: igyumin
"""

from inspect import currentframe, getframeinfo

def print_indent(param):
    edited = '\n > ' + param
    
    print(edited)
    
    
def print_section(param, align = '<'):
    lines = [x.strip() for x in param.split('\n')]
    line_count = len(lines)
    line_max_len = max([len(line) for line in lines])
    
    print()
    for v in range(line_count+2):
        if v == 0:
            print('«' * (line_max_len + 10), end='')
        elif v == line_count + 1:
            print('«' * (line_max_len + 10), end='')
        else:
            print(f'«    {lines[v-1]:{align}{line_max_len}}', end='')
        print()
        

def print_line(param):
    previous_frame = getframeinfo(currentframe().f_back)
    
    path = previous_frame.filename
    path_last = path.split('/')[-1]
    
    edited = '({0}..<{1}>): {2}'.format(previous_frame.lineno, path_last, param)
    
    print(edited)
    

