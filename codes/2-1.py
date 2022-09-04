#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  2 09:40:00 2022

@author: igyumin
"""

import math
import random

def myPrint(param):
    print('\n# ' + param + '\n')
    
    

myPrint('리스트')

myPrint('다양한 형태의 리스트들')

a = [1, 3.141592, 5, 7]
b = []
c = ['Kyumin','Hanyeong','Yubin']
d = [1, 3, 5, [7, 9]]


myPrint('리스트의 인덱싱')

myPrint('리스트의 인덱싱은 문자열의 인덱싱과 매우 흡사하다(내부적으로는 같은 배열이기 때문)')

myPrint('차이점: string 은 immutable 하고 오직 문자만 들어갈 수 있다')


a = [1,2,3,4,5]

print(a[2])

print(a[0:-3])


myPrint('c 에서 Hanyeong의 Han 만을 출력하려면?')

print(c[1][0:3])
print(d[3][0])


myPrint('리스트 합치기')

head = ['이거 뒤에', '다음 배열이']
tail = ['이렇게', '착', '붙습니다', '!']


print(head + tail)
print(tail + head)


myPrint('리스트 곱하기')

a = [1,10,100]

b = a * 5

print(b)

myPrint('그럼 빼기나 나누기도 될까?')


myPrint('list 는 mutable 하다. 따라서..')

myPrint('요소 변경')

a = ['문재인', '박근혜', '이명박', '노무현']
print(a)

a[0] = '문크예거'

print(a)


myPrint('요소 삭제')

target = [5,6,7,8,9]
print(target)
del target[-2]

print(target)

myPrint('혹은..')

target = [5,6,7,8,9]
target.remove(8)
print(target)


myPrint('요소 추가')

a = ['earth', 'jupiter', 'mercury', 'saturn']

print(a)
a.append('venus')

print(a)
a.append(['moon', 'uranus', 'titan', 3.141592])

print(a)


myPrint('요소 정렬')

a = [2021,2022,2015,2000,2007,2010,2006,2004,2003,2006]
print(a)

a.sort()
print(a)

a.sort(reverse = True)
print(a)

myPrint('문자열은?')




a = ['avocado','banana','cucumber','durian','apple', 'bean']

print(a)
a.sort()

print(a)


myPrint('숫자와 문자열이 함께 있으면 정렬될까?')


myPrint('요소 찾기')

a = [2,4,6,8,10]

print(a.index(8))


myPrint('index 할때 해당 요소가 없다면?')

myPrint('요소 삽입')

a = [1,2,4,5]

print(a)
a.insert(2,7)

a[2:2] = [3,4]

print(a)

myPrint('최댓값, 최솟값')

a = [5, 4, 14, 10, 101, 7, 102, 46, 4]

print(max(a))
print(min(a))


myPrint('튜플(Tuple)')

myPrint('tuple 은 list 와 거의 같지만, immutable 하고, () 로 선언한다는 점이 다르다')

a = (1,2,3,4,5)
b = (1,)
c = (1,2, (3,4,5))

myPrint('a에 6을 추가한 튜플을 얻고 싶으면 어떻게 할까?')


myPrint('튜플은 리스트의 함수 중 요소를 바꾸는 것만 아니라면 대부분 그대로 사용가능')


myPrint('tuple unpacking')
(a, b, *c, d,e) = (1,2,3,4,5,6,7)

print(a,b,*c, d)

print(c)
print(d)
print(e)





a = [1.2, 4.5, 9.1]

index_a = a.index(4.5)
print(a[index_a])







a = [1,4,9,16,25,36,49,64,81,100]







b = [i**2 for i in range(1,11)]
print(b)



c = [[1],[1,2],[1,2,3],[1,2,3,4],[1,2,3,4,5]]

















































