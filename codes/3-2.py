#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  9 17:25:15 2022

@author: igyumin
"""

import random


'''
[반복문]

python 의 반복문에는 두가지 종류가 있다:
    for, while

둘은 특정한 작업을 반복한다는 점이 비슷하지만, 용도와 특징에 있어서 조금 다르다.

for 문은 "정해진 횟수만큼" 반복 할때 유용하다.
'''

a = [1,2,3,4,5]

for i in a:
    print(i)


'''
위와 같이 배열을 순회하거나 혹은
'''

for i in range(10):
    print(i)
    

'''
즉석에서 range 객체를 생성해 정해진 횟수(위에선 10회) 만큼 반복할 수 있다.




반면, while 문은 "반복할 횟수가 정해지지 않았을때" 유용하다
'''
print()


while(True):
    random_num = random.randrange(0,20)
    
    print(random_num)
    
    if random_num == 10:
        print('10 입니다! while 문 탈출!')
        break
    

'''
위의 코드에서는 계속해서 랜덤하게 숫자를 뽑다가, 10이 뽑히면 반복을 중단한다.


이 경우에는 언제 10이 뽑힐지 모르기 때문에 (=반복 횟수가 미리 정해져 있지 않기 때문에)
for 를 통해 반복을 수행하기 보다 while 이 적절하다.




if 문과 while 문 모두에서 쓸수 있는 명령어로, 

continue 와 break 이 있다.



continue 는 해당 명령어가 쓰인 이후의 과정을 건너뛰고, 다음으로 간다.

break 은 루프를 중단하고, 탈출한다.
'''

print()

for i in range(20):
    if i < 5:
        print('continue:', i)
        continue # i 가 5 미만인 경우 아래의 과정을 건너뛰고 다음으로 넘어간다
    
    print(i)
    
    if i == 10:
        break # i 가 10 인 경우 루프를 중단한다.


'''
만약 반복문이 중첩되어 있다면, continue 와 break 은 가장 가까운 상위의 반복문에만 작용한다.

'''

for i in range(3):
    for j in range(10):
        if j == 3:
            break
        for k in range(10):
            print(i,j,k)
            

'''
무한 루프를 조심하자!

아래의 while 문을 실행해보자.

while(True):
    print('infinity')

'''

'''
python 의 조건문에는 한가지가 있다:
    if
    

(많은 경우, 다른 언어에는 switch 라는 조건문이 별도로 존재하나, 파이썬에는 switch 문이 존재하지 않는다.)


조건문에서 조건을 판별할 때 쓸 수 있는 "비교 연산자"로는:
    
    == 같음
    != 다름
    >=, <= 이상 이하
    >, < 미만 초과

가 있고,


그 밖에 또다른 연산자로:
    
    and ~이고
    or ~이거나
    not ~이 아닌
    
이 있다.

또한:
    
    in ~에 포함된
    not in ~에 포함되지 않은

도 있다.


'''


'''
1-100 범위에서 뽑고, (랜덤)

그게 20-25 사이면 탈출

'''







members_dict = {'조한영': 15, 
                '이규민': 43, 
                '임유빈': 21, 
                '기도율': 17, 
                '김철수': 34, 
                '최영희': 27, 
                '문재인': 1}

print()

# 1st

for key, value in members_dict.items():
    if value >= 10 and value < 20:
        print('{0}님은 10대 입니다'.format(key))
    
    if value >= 20 and value < 30:
        print('{0}님은 20대 입니다'.format(key))
    
    if value >= 30 and value < 40:
        print('{0}님은 30대 입니다'.format(key))
    
    if value >= 40:
        print('{0}님은 40대 이상 입니다'.format(key))
    
    if value < 10:
        print('{0}님은 10살 미만 입니다.'.format(key))

print()

# 2nd

for key, value in members_dict.items():
    if value >= 40:
        print('{0}님은 40대 이상 입니다'.format(key))
    elif value >= 30:
        print('{0}님은 30대 입니다'.format(key))
    elif value >= 20:
        print('{0}님은 20대 입니다'.format(key))
    elif value >= 10:
        print('{0}님은 10대 입니다'.format(key))
    else:
        print('{0}님은 10살 미만 입니다.'.format(key))
        
    if key == '이규민':
        print(key)
    else:
        print('규민 아님')

'''
1st 와 2nd 는 완벽히 동일한 결과를 출력한다.

if-(elif)-(else) 구조를 잘 기억하자.
if 문을 쓸때, elif 와 else 문은 선택적으로 쓸수 있다.

따라서 if 문은 단독으로 쓰일 수 있지만, elif 와 else 는 단독으로 쓰일 수 없고, 반드시 if 뒤에 와야 한다. 


if 가 여러개 쓰인 경우, 각각의 if 를 이전의 결과와 상관없이 모두 실행하지만,
if-elif 인 경우 조건이 만족되면 그 아래의 elif 와 else 는 모두 패스한다.


이렇듯 elif 를 적절히 활용하면, 보다 코드가 간결해진다.
'''



'''
Exercise!


1.
1 부터 10 까지 모두 더한 합을 구하시오


2.
다음을 출력하시오:
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *


3.
nums = [6,1,20,11,45,22,34,76,51,39]
와 같이 list 가 주어질 때,

가장 큰 값을 구하는 코드를 작성하시오.

hint: 순회하면서 더 큰값이 나오면 업데이트, 아니면 패스


4.
가장 작은 값을 구하는 코드를 작성하시오.


5.
어떤 수 n 이 주어질 때, n 이 소수인지 판별하시오

소수: 2,3,5,7,11,13,17,23, ...
'''






    
    
    
