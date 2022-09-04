#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  4 10:32:02 2022

@author: igyumin
"""


import math
import random

def myPrint(param):
    print('\n# ' + param + '\n')
    

    
myPrint('Dictionary')

myPrint('List 는 단점이 있다. 원하는 요소를 빠르게 찾기가 힘들다는 것!')

myPrint('그런 단점을 해결하기 위해, 리스트에 \'이름표\'를 붙여준게 Dictionary')

a = {1: '도율', 2: '유빈', 3:'한영'}
b = {'첫번째' : '규민', 2:'무현', '함수': (1,2,3)}

print(a[1])
print(b['첫번째'])
print(b['함수'])

myPrint('key 값으로 list 도 들어갈 수 있을까? Tuple 은?')


myPrint('쌍 추가')

a = {1:"one", 2: "two"}
a[3] = 'three'

print(a)


myPrint('쌍 삭제')

a = {1:"one", 2: "two", 3: "three"}

del a[2]

print(a)


myPrint('혹은..')

a = {1:"one", 2: "two", 3: "three"}

b = a.pop(2)
print(b)
print(a)


myPrint('딕셔너리 사용법')

myPrint('key를 통해 value를 얻는다 (열쇠 - 문)')

a = {1: '하나', 2: '둘', 3: '셋', 4: '넷'}

for key in a:
    print('{0}은 {1} (이)라고 읽습니다'.format(key, a[key]))


a = {(0,0): 'O', (0,1): 'X', (0,2): 'X',
     (1,0): 'O', (1,1): 'X' ,(1,2): 'O',
     (2,0): 'O', (2,1): 'O' ,(2,2): 'O'}

myPrint('tuple을 key로 쓸 수 있으므로..')

for i in range(3):
    for j in range(3):
        print(a[i,j], end='')
    
    print('\n')


myPrint('value를 통해 key를 얻을 수 있을까?')


myPrint('유용한 함수들')

myPrint('key 리스트 만들기')

a = {'일': '하나', '이': '둘', '삼': '셋', '사': '넷'}

print(a.keys())
b = list(a.keys())
print(b)
print(list(a.keys()))

myPrint('value 리스트 만들기')

print(a.values())
print(list(a.values()))


myPrint('key, value 쌍 얻기')

print(a.items())
print(list(a.items()))


for pair in a.items():
    print(pair)



myPrint('안전하게 key로 value 얻기')

print(a.get('일'))
print(a['일'])
print(a.get('칠'))
print(a.get('팔'))



myPrint('dictionary 두개 합치기')

a = {1:'1', 2:'2', 3:'3'}
b = {3:'three', 4:'4'}


a.update(b)

print(a)

myPrint('dictionary 청소하기')

a.clear()
print(a)


myPrint('집합')

"""

집합은 리스트와 달리 중복을 허용하지 않고, 순서가 없다

따라서 인덱싱이 불가능 하다.

하지만 mutable 하기 때문에 tuple과 달리 값의 변경은 가능하다


"""


sentence = "Hello,Banana!"

sentence_set = set(sentence)

print(list(sentence))
print(sentence_set)


myPrint('교집합')

first = {1,2,3,4,5}
second = {4,5,6,7,8}

print(first & second)

myPrint('합집합')

print(first | second)

myPrint('차집합')

print(first - second)
print(second - first)


myPrint('값 1개 추가')

first.add(6)

print(first)


myPrint('값 여러개 추가(업데이트)')

first.update(second)

print(first)


myPrint('값 제거')

first.remove(2)

print(first)


first = {1,2,3,4,5}

b = first.pop()

print(b)
print(first)

b = first.pop()

print(b)
print(first)

b = first.pop()

print(b)
print(first)

b = first.pop()

print(b)
print(first)

b = first.pop()

print(b)
print(first)

for i in range(5):
    if i == 3:
        print(i)
    else:
        print('3 아님')




