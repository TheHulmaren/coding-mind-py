#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 24 16:02:23 2022

@author: igyumin
"""

# 1.


def print_tag(txtpath):
    with open(txtpath, 'r') as file:
        lines = file.readlines()
        
        for line in lines:
            split = line.strip().split('&')
            title = split[0]
            price = int(split[1])
            discount = int(split[2])
            off_price = int(price*((100-discount)/100))
            
            tag = f'<{title}>\n\t{discount:>2}% off\n\t${price:>5} -> ${off_price:>5}'
            print(tag)


print_tag('retail.txt')
    



# 2.

# =============================================================================
# def add_product(txtpath, title, price, offrate):
#     with open(txtpath, 'a') as file:
#         text = f'\n{title}&{price}&{offrate}'
#         file.write(text)
# 
# add_product('retail.txt', 'Dell U2720Q', 750, 20)
# print_tag('retail.txt')
# =============================================================================





# 3. 

def time_convert():
    time = input('Enter the time in 12 hour format: ').strip().replace(' ','')
    
    is_am = (True if time[-2:] == 'AM' else False)
    time_split = time[:-2].split(':')
    
    hour = int(time_split[0]) + (0 if is_am else 12)
    min = int(time_split[1])
    
    print(f'{hour:0>2}:{min:0>2}')



time_convert()



# 4.

def translate(dic, text):
    for key, val in dic.items():
        text = text.replace(key, val)
        
    return text

T = 'Python is a great, easy language.'
info = {'Python':'C++', 'great':'terrible', 'easy':'difficult'}

T = translate(info, T)
print(T)




















