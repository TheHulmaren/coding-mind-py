#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 11 17:59:57 2022

@author: igyumin
"""

'''
1.
다음을 출력하시오.

*
**
***
****
*****



2.
다음을 출력하시오.

*****
****
***
**
*



3.
다음을 출력하시오.

    *
   ***
  *****
 *******
*********



4.
구구단을 출력하시오.

예)
1 x 1 = 1
1 x 2 = 2
...
9 x 8 = 72
9 x 9 = 81



5.
어떤 수 n 이 주어졌을때,

1 + 11 + 111 + 1111 + ... 의 합을 구하는 프로그램을 작성하시오.

예) n = 5
1 + 11 + 111 + 1111 + 11111 = 12345



6.
어떤 문자열이 주어졌을때, 그 문자열을 뒤집는 프로그램을 작성하시오.

(반복문을 이용!)

예) 'Python' -> 'nohtyP'



7.
다음과 같이 직원들의 정보가 dictionary 로 주어질때,
phone 이 010 으로 시작하고 age 가 20세 이상 30세 미만인 직원만을 추려내시오.

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


예) 
Joe Biden
Michael McNamara
Kate Mickelson




8.
다음과 같이 출력하시오.

1
21
123
4321
12345



9.
다음과 같이 출력하시오.


A
BC
DEF
GHIJ
KLMNO



10.
다음과 같이 x 자를 출력하는 코드를 작성하시오

*   *
 * *
  *
 * *
*   *


11.
다음과 같이 2차원 배열의 행, 렬의 합을 각각 구하고 총합을 구하시오

배열은 아래와 같이 주어진다.

M = [[-4,1,5,2,0],
     [7,2,-3,6,10],
     [-5,1,9,1,-7]]


예)

    +--+--+--+--+
 22 | 4| 7|10| 1|
    +--+--+--+--+
 16 | 1| 7| 3| 5|
    +--+--+--+--+
  9 | 2| 2| 4| 1|
    +--+--+--+--+
[47]  7 16 17  7

'''



temp = 0

for i in range(5):
    temp += i
    
print(temp)




for i in range(1,6):
    for j in range(1, i+1):
        print(j, end='')
    print()






