#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 21 21:22:30 2022

@author: igyumin
"""


'''
[함수]

함수는 "코드의 묶음" 이라고 생각하면 쉽다.
일정한 기능을 수행하는 코드를 묶어, 재사용이 가능하도록 만든 것.

이전에 숙제한 것을 떠올려 보자, 함수로 묶지않으면 재사용하기가 힘들다.


일반적으로 함수는 코드 논리흐름의 기본 단위가 된다.


(첫시간에 했던 계란후라이의 예시를 떠올려보자!)

'''


def print_hello():
    print('Hello!')
    return None
    

A = print_hello()
print(A)



'''
위의 함수는 매개변수가 없고, 반환값도 없다.
파이썬에서 가장 간단한 형태의 함수라고 생각하면 된다.


매개변수를 추가해보면 아래와 같이 된다.
'''

def print_hello(name):
    print('Hello,' + str(name) + '!')


print_hello(5)
print_hello('Biden')



'''
위와같이, 매개변수를 넣어주면 함수 호출의 결과도 그에따라 변할 수 있다.

매개변수가 없는 함수가 상수함수라면,
매개변수가 있는 함수는 변수함수라고 할 수 있다.


한편, 아직 print() 함수로 문장을 출력하기만 했을뿐, 명시적인 '결과값'을 돌려받지는 못했다.
'''

def say_hello(name):
    return 'Hello,' + name + '!'


print(say_hello('Hanyoung'))

a = say_hello('Yubin')
print(a)


'''
이렇듯, return 함수를 통해 특정한 값을 반환해줄 수 있다.
함수는 return 이 이루어지는 순간 실행을 종료한다.


(엄밀하게 말해, return 명령어가 쓰이지 않더라도 None 을 암묵적으로 리턴한다)
'''


'''
아래는 지금까지 우리가 풀었던 문제들의 코드를 함수로 만들어봄
'''


# 숫자 배열을 매개변수로 받아 평균값을 반환해주는 함수
def average(nums):
    temp = 0
    
    for num in nums:
        temp+= num
    
    result = temp / len(nums)
    return result


# 삼각형의 높이와 출력할 문자를 매개변수로 받아 피라미드 형태의 삼각형 출력
def print_triangle(level = 5, char = '*'):
    for i in range(level):
        print(' '*(level-i-1) + char*(2*i+1))


# 문자열을 뒤집은 새로운 문자열을 반환하는 함수
def str_reversed(word):
    result = ''
    for char in word:
        result = char + result
    
    return result



# 위의 함수들을 호출해보자
avg = average([1,10,5,6])
C = average([6,1,31])

print(avg)
print(C)


print_triangle(level=4, char='@')


N = 'Try reversing this'
N = str_reversed(N)
print(N)



A = 'Fuck you'
A = str_reversed(A)
print(A)



'''
다음 기능을 하는 함수를 작성해 보시오.

1.
두 수를 매개변수로 받아 합을 반환하는 함수

2.
두 수를 매개변수로 받아 앞의 수가 더 크면 1, 같으면 0, 작으면 -1 을 반환하는 함수
'''


'''
[매개변수 심화]

함수에 주어지는 매개변수는 여러개일 수도 있다.
그럴때는 필요한 만큼 매개변수를 설정해주면 되지만, 만약 몇개가 들어갈지 알 수 없다면?

그런 상황을 위해 파이썬에서는 다음과 같은 기능을 제공한다.
'''



# 매개변수의 이름앞에 *를 써주면 이후의 매개변수를 모두 해당 이름의 튜플에 집어넣는다
def add_all(*nums):
    result = 0
    for num in nums:
        result += num
    return result

a = add_all(3,2,1,4)
print(a)

b = add_all(3,2,1,4,-5,6)
print(b)



def calc(op, *nums):
    result = 0
    if op == '*':
        result = 1

    for num in nums:
        if op == '+':
            result += num
        elif op == '*':
            result *= num
    
    return result


a = calc('+', 1, 3, 2, 4)
b = calc('*', 1, 3, 2, 4)

print(a)
print(b)


'''
3-1주차에서 배웠다시피, 
어떤 변수에 배열을 할당하면 그 변수는 배열과 같은 주소를 가르키게 된다.

따라서 배열의 값이 바뀌면 해당 배열을 참조하는 변수 모두의 값이 바뀐다.

매개변수에 mutable 변수를 전달할때도 이점을 주의해야 한다.
'''
import copy

def change_first(target):
    result = copy.deepcopy(target)
    
    result[0] = 100
    return result
    
A = [1,2,3]
B = change_first(A) # target 과 A 는 같은 주소를 참조하므로, A의 값도 바뀌어 버린다.
print(B)

print(A)


# 우리가 써왔던 sort() 함수가 바로 이점을 이용한 것이다.


'''
[오늘의 도전과제]


1. 
이름과 나이, 직업을 매개변수로 받고, 아래와 같이 자기소개를 담은 문자열을 반환하는 함수를 작성하시오.


입력: ('이규민', 21, '프로그래머')

반환값: 
"제 이름은 이규민이고,
 올해로 21세 입니다.
 직업은 프로그래머 입니다."
 
 

2.
학급의 이름과 학생들의 이름을 매개변수로 받고, 학급의 정보를 다음과 같이 출력하는 함수를 작성하시오.


예시 1.
입력: ('해바라기', '이규민', '조한영', '임유빈', '기도율', '이진영')

출력: 해바라기 반의 정원은 5명이며, 이규민, 조한영, 임유빈, 기도율, 이진영 학생이 소속되어 있습니다.


예시 2.
입력: ('해병짜장', '무모칠', '황근출', '톤톤정')

출력: 해병짜장 반의 정원은 3명이며, 무모칠, 황근출, 톤톤정 학생이 소속되어 있습니다.

'''





# 1.

def introduce_myself(name, age, job):
    result = f'제 이름은 {name}이고,\n 올해로 {age}세 입니다.\n 직업은 {job}입니다.'
    return result


print(introduce_myself('조한영', 87, 'CEO'))
print(introduce_myself('임유빈', 31, '갓물주'))



# 2.

def print_class(title, *students):
    student_str = ', '.join(students)
    
    result = f'{title} 반의 정원은 {len(students)}명이며, {student_str} 학생이 소속되어 있습니다.'
    print(result)


print_class('해바라기', '이규민', '조한영', '임유빈', '기도율', '이진영')
print_class('해병짜장', '무모칠', '황근출', '톤톤정')























