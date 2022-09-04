#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 15 21:17:01 2022

@author: igyumin
"""


# 1

for i in range(5):
    print('*' * (i+1))
    
    
    
    
# 2

for i in range(5):
    print('*'*(4-i))




# 3

for i in range(5):
    print(' '*(4-i) + '*'*(1+2*i))


# 4

for i in range(1,10):
    for j in range(1,10):
        print(f'{i} x {j} = {i*j:>2}')




# 5

n = 5

temp = 0

for i in range(n):
    num = int('1'*(i+1))
    temp += num
    
print(temp)




# 6

m = 'Python!'

m_reversed = []

for i in range(len(m)):
    m_reversed.append(m[len(m)-1-i])

print(''.join(m_reversed))




# 7

employee_list = {'John Brown':{'age': 31, 
                               'contact': {'phone': '010-4565-2144', 
                                           'home': '031-224-2523'}},
                 'Mark Smith':{'age': 21,
                               'contact': {'phone': '011-4585-2044',
                                           'home': '031-264-1623'}},
                 'Joe Biden':{'age': 27, 
                              'contact': {'phone': '010-7640-2364',
                                          'home': '031-211-1241'}},
                 'Donald Trump':{'age': 42, 
                                 'contact': {'phone': '010-1245-2144', 
                                             'home': '031-124-2523'}},
                 'Steven Kim':{'age': 25, 
                               'contact': {'phone': '013-4515-2144',
                                           'home': '031-924-2523'}},
                 'Michael McNamara':{'age': 29,
                                     'contact': {'phone': '010-5260-2133', 
                                                 'home': '031-888-9923'}},
                 'Kate Mickelson':{'age': 20, 
                                   'contact': {'phone': '010-9219-2144',
                                               'home': '031-274-2523'}}}

for key in employee_list.keys():
    age = employee_list[key]['age']
    phone = employee_list[key]['contact']['phone']
    
    if age >= 20 and age < 30 and phone[0:3] == '010':
        print(key)





# 8

n = 7

for i in range(1,n+1):
    if i % 2 == 0:
        for j in range(1,i+1):
            print(i+1-j, end='')
        print()
        continue
    
    for j in range(1,i+1):
        print(j, end='')
    
    print()





# 9

import string

n = 5
index = 0
alphabets = string.ascii_uppercase

for i in range(n):
    for j in range(i+1):
        print(alphabets[index], end='')
        index += 1
    print()
    
    
    
    
    

# 10


p = 4

for i in range(2*p-1):
    n = i
    m = 2*p-2-i
    
    if n < m:
        print(' '*n + '*' + ' '*(m-n-1) + '*') 
    elif n == m:
        print(' '*n + '*')
    else:
        print(' '*m + '*' + ' '*(n-m-1) + '*')




# 11

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














    