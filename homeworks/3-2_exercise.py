#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 10 18:15:45 2022

@author: igyumin
"""

import math

# 1

temp = 0

for i in range(11):
    temp += i
    
print(temp)



































# 2

n = 5

for i in range(2*n-1):
    print(' ' * abs(n-1-i) + '*' * abs(2*n-1 - 2*abs(n-1-i)))
    
    
    
    
    

    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

# 3

nums = [6,1,20,11,45,22,34,76,51,39]

temp = 0

for num in nums:
    if num > temp:
        temp = num

print(temp)










































# 4

nums = [6,1,20,11,45,22,34,76,51,39]

temp = 10000

for num in nums:
    if num < temp:
        temp = num

print(temp)















































# 5-1

n = 29

is_prime = True

for i in range(2, math.floor(math.sqrt(n)) + 1):
    if n % i == 0:
        is_prime = False
        break
    
if is_prime:
    print('{0} is a prime number.'.format(n))
else:
    print('{0} is not a prime number.'.format(n))

# 에라토스테네스?





































# 5-2
print('에라토스테네스의 채 이용')

n = 12311

nums = list(range(2, math.floor(math.sqrt(n)) + 1))

is_prime = True

for i in nums:
    if n % i == 0:
        is_prime = False
        break
    else:
        for j in nums:
            if j == i:
                continue
            if j % i == 0:
                nums.remove(j)

if is_prime:
    print('{0} is a prime number.'.format(n))
else:
    print('{0} is not a prime number.'.format(n))









    