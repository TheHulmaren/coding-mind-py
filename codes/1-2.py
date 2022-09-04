#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 00:32:02 2022

@author: igyumin
"""
import math
import random

def myPrint(param):
    print('\n# ' + param + '\n')




a = 13
b = 4
c = 2
d = 0

myPrint('0으로 나누면?')


print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

myPrint('사칙연산 순서는?')

print(3 + 1 * 2 / 2)


myPrint('그외 유용한 숫자 함수들')


print(abs(-10))

print(math.ceil(1.5))
print(math.ceil(-14.9))

print(math.floor(1.5))
print(math.floor(-5.5))


'''
18.2 -> 18
5.9 -> 5

-14.8 -> -14

math.ceil, math.floor 쓰지 말고!
'''


myPrint('잘 만들어진 함수란..')

print(max(2, 10, 7)) # 기본 형태
print(max([2,10,7])) # 리스트
print(max((2,10,7))) # 튜플
print(max({2,10,7})) # 집합

print(min(2,10,7))


print(math.pow(3, 3))
print(math.sqrt(2))


myPrint('랜덤한 숫자는 어떻게 뽑을까?')

print(random.randrange(1,101))

abc = ['a', 'b', 'c', 'd', 'e']
random.shuffle(abc)
print(abc)

print(random.choice(abc))

print(random.random() * 100)


myPrint('문자열을 다뤄보자!')

print('Hello, Python')
print("Hello, Python")

myPrint('따옴표 문자열에 포함시키기')

print("It's mine, and that's yours")
print('That is fucking "real"')

myPrint('혹은 슬래시를 써도 됨')

print('It\'s mine, and that\'s yours')
print("That is fucking \"real\"")

myPrint('슬래시도 출력하고 싶다면?')

print('It\\\'s mine, and that\\\'s yours')


print('그외 escape code 의 활용')

print('Under is\nNew line')
print('\tIt is tab')
#print('뾲\a\a')

myPrint('문자열을 조작해보자')

myPrint('문자열 연결')

head = '머리'
body = '몸통'
tail = '꼬리'

print(head + body + tail)

print(50 * head)


myPrint('문자열 곱')

print('hi' * 10)




myPrint('문자열 길이')

a = '몇글자인지 세봐 병신아ㅋㅋㅋㅋ'
print(len(a))



myPrint('문자열 인덱싱')

a = '인생은 짧아, 그러니 파이썬을 하자'

print(a[0] + a[1] + a[2])
print(a[-2] + a[-1])

print(a[0:3])
print(a[-7:-3])

print(a[5:])
print(a[:10])

print(a[:])

myPrint('슬라이싱한 부분만 바꿀 수 있을까?')


b = a[:-7] + '씨뿔뿔을' + a[-3:]

print(b)



myPrint('문자열 포매팅')

print('나는 {0} 대통령이 좋아'.format("노무현"))
print('나는 {0} 대통령이 좋아, {1}은 싫어'.format("노무현", "문재인"))

sentence = '나는 {0} 대통령이 좋아, {1}은 싫어'
n = '노무현'
m = '문재인'

print(sentence.format(n,m))
print(sentence.format(m,n))

print("난 {정책명}에 {입장}해".format(정책명 = '검수완박', 입장 = '반대'))

name = 'kyumin'
age = 21.1231254


a = f'{name} is {age} years old'
b = '{name} is {age} years old'.format(name=name, age=age)

print(a)
print(b)

myPrint('정렬하기')

print('{number:>10}'.format(number = '오른쪽'))
print("{0:^10}".format('중간'))
print("{0:<10}".format('왼쪽'))

a = [ 1,100,30,4,12]

for i in a:
    print(f'{i:>3}')


myPrint('소수점 표현')

print("{0:<15.4f}".format(math.pi))
print("{0:^15.4f}".format(math.pi))
print("{0:>15.4f}".format(math.pi))



myPrint('유용한 문자열 관련 함수들')

myPrint('문자 갯수 세기')

a = '검찰은 검수완박을 싫어해. 완전 비상식적 이거든.'
print(a.count('검'))
print(a.count('완'))



myPrint('위치 찾기')

print(a.find('완'))
print(a.rfind('완'))

print(a.index('검'))
print(a.rindex('검'))

print(a.find('경'))




myPrint('부분 문자열 포함 여부')

print('바나나' not in '나는 바나나가 좋아')




myPrint('문자열 삽입')

print('.'.join('슈슈슉'))

a = ['슉', '슈슈슉', '슈슉', '시발롬아']


print(".".join(a))




myPrint('문자열 일부 교체')

a = '병신들아, 잘 지내냐'
print(a)
a = a.replace('병신', '여러분')
a = a.replace('냐', '세요?')
print(a)





myPrint('문자열 쪼개기')

a = '이 문자열을, 열심히 성심껏, 쪼개주시면 됩니다. 하하'

print(a.split())
print(a.split(','))
print(a.split('성심껏'))



myPrint('그외 재밌는 함수들')

myPrint('대문자, 소문자 전환')

a = 'aBcDeFgHrJkL'

print(a)
print(a.title())
print(a.swapcase())
print(a.upper())
print(a.lower())


