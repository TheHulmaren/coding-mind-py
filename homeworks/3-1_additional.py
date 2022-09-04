#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  9 00:43:58 2022

@author: igyumin
"""

import copy


a = [1,2,3,4,5]

for i in a:
    print(i)
    

a = {1:'one', 2: 'two', 3:'three'}

"""
1: one
2: two
3: three
"""

for key, value in a.items():
    print('{0}: {1}'.format(key, value))
    
    

a = [1,2,3]


if 1 in a:
    print('1이 있습니다')
elif 2 in a:
    print('2가 있습니다')
elif 3 in a:
    print('3이 있습니다')
else:
    print('없습니다')
    

b = {1:'one', 2:'two', 3:'three', 4:'four'}

"""
one
two
three
four
"""






num = [-3, -5, 123, -9, 10]

'''
num 의 음수들을 모두 양수로 바꾸시오
'''



# 1st

for i in range(len(num)):
    if num[i] < 0 :
        num[i] = -1 * num[i]
    
print(num)



# 2nd

new_num = []

for i in num:
    new_num.append(abs(i))

print(new_num)













'''
*
**
***
****
*****
'''








'''
1 x 1 = 1
1 x 2 = 2
.
.
.
9 x 8 = 72
9 x 9 = 81
'''









    
