#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  7 23:38:40 2022

@author: igyumin
"""

from inspect import currentframe, getframeinfo
import copy


def print_indent(param):
    edited = '\n > ' + param
    
    print(edited)
    
    
def print_section(param, align = '<'):
    lines = [x.strip() for x in param.split('\n')]
    line_count = len(lines)
    line_max_len = max([len(line) for line in lines])
    
    print()
    for v in range(line_count+2):
        if v == 0:
            print('«' * (line_max_len + 10), end='')
        elif v == line_count + 1:
            print('«' * (line_max_len + 10), end='')
        else:
            print(f'«    {lines[v-1]:{align}{line_max_len}}', end='')
        print()




print_section('''
              오늘의 주제: 변수에 대한 이해
              
              우리가 변수를 선언하고 사용할 때, 
              변수가 메모리 상에 어떻게 저장되고 변경되는지 알아보자!
              ''')
              
print_indent('변수는 앞서 배웠듯이 immutable 과 mutable 로 나뉜다')

              
print_indent('immutable 은 \"변할 수 없는\" 이라는 뜻이 담겨 있으며, 변수가 가리키는 값을 변경할 수 없다')

print_section('''
              immutable 변수에는 다음이 포함된다:
                  string(문자열), integer(정수), float(실수), tuple
              ''')



print_indent('mutable 은 \"변할 수 있는\" 이라는 뜻이 담겨 있으며, 변수가 가리키는 값을 변경 가능하다')

print_section('''
              mutable 변수에는 다음이 포함된다:
                  list, dictionary, set
              ''')
              
              
print_indent('코드를 통해 자세히 알아보자')

print()


print_section('''
              immutable 한 변수는 값이 변하지 않는다.
             
              따라서, 값이 변하지 않기에 \"대부분의 경우\" dictionary 의 key 값으로 사용될 수 있다.
              key 값은 열쇠와 같은 역할을 하기에, 도중에 값이 변경되어선 안되기 때문이다.
              
              파여진 홈의 패턴이 계속해서 변하는 열쇠를 쓸 수 있을까? 비슷한 논리!
              
              ..허나 한가지 주의점이 존재한다.
              ''')

a = ([1,2], 3, 4)

#b = {a:'one', 2: 'two'}

print_indent('위 구문을 실행해보면 알겠지만, 에러가 발생함을 알수 있다.')

print_indent('이는 위의 튜플 a 에 배열 [1,2] 가 요소로 포함되어 있기 때문이다.')

print_indent('key 값은 변하지 않아야 하는데, mutable 인 list 가 있기에 결국 변할 수 있다고 보는 것이다.')

print_indent('즉, 엄밀히 말하면 key 값으로 사용되기 위해서는 hashable 해야 한다.')

# https://mangkyu.tistory.com/102

print_section('''
              immutable 중 아래의 경우는 hashable:
                  string, integer, tuple without mutable element
                  
                 예) ((1,2), (3,4))
              
              immutable 중 아래의 경우는 unhashable:
                  tuple with mutable element
                  
                  예) ([1,2,3], [4,5,6]), ('하나', '둘', {3: '셋', 4: '넷'})
              ''')
              
print_section('''
              추가)
              파이썬은 일부 immutable 변수의 경우 같은 값이면 같은 메모리상의 주소에 저장한다.
              
              -5 에서 256 까지의 정수나, 20자 미만의 문자열 등이 그에 해당한다.
              
              이러한 범위의 변수는 보편적으로, 상당히 자주 사용되기 때문에,
              메모리 사용량 최적화를 위해 그렇게 해놓은것.
              
              
              흔히 이러한 동작을 object interning 이라고 한다.
              
              
              값이 유동적으로 변할 것을 상정하는 mutable 의 경우는 이에 해당하지 않는다.
              ''')      
              
a = 1
b = 2
c = 2

print(a)
print(b)
print(c)

print('id(a):', id(a))
print('id(b):', id(b))
print('id(c):', id(c))

A = 'abc'
B = 'abc'
C = 'ab'

print()

print(A)
print(B)
print(C)

print('id(A):', id(A))
print('id(B):', id(B))
print('id(C):', id(C))


print_section('''
              mutable 한 변수는 기본적으로 (서로간의 할당이 아닐경우) 주소값이 각각 다르다
              
              (사실 파이썬의 변수는 원칙적으로 모두 그렇지만, 위의 일부 예외가 존재하는 것이다.)
              
              즉, 값이 같다고 해도 서로 다른 메모리 상의 위치를 가리킨다.
              
              또한, 값이 변할 수 있기에 dictionary 의 key 값으로는 사용될 수 없다.
              ''')
              
# https://stackoverflow.com/questions/1504717/why-does-comparing-strings-using-either-or-is-sometimes-produce-a-differe

A = [1,2,3]
B = [1,2,3]
C = [1,2]

print()

print(A)
print(B)
print(C)

print('id(A):', id(A))
print('id(B):', id(B))
print('id(C):', id(C))

print_indent('위와 같이, 각각 주소값이 상이하다. 그러나 B = A 등으로 할당하게 되면 주소값을 공유하게 된다.')


A = ['one', 'two', 'three']
B = A

print('id(A):', id(A))
print('id(B):', id(B))

print_indent('위를 통해 알 수 있는 것은, python 에서는 변수간에 할당을 할 시,')

print_indent('값 그 자체가 아닌 메모리 상의 주소를 할당한다는 점이다')

print_indent('그러나 그와 같은 기본동작에는 아래와 같은 단점이 존재한다.')

A = [1,2,3]

B = A

print(B)

A[0] = 5

print(B)

print_indent('A를 B에 할당한 후, 단지 A의 요소를 수정하기만 했을 뿐인데, B의 값도 변경되어 버렸다')

print_indent('이렇듯, 주소를 공유하면 서로간의 의도치 않은 영향을 주고 받을 수 있다')

print_indent('이는 다음과 같은 방법으로 해결할 수 있다.')

A = [1,2,3]

B = copy.deepcopy(A)

print(B)

A[0] = 5

print(B)

print_indent('이번에도 할당 후 A의 값이 변경되었지만, B의 값은 바뀌지 않았다.')

print_section('''
              deep copy V.S. shallow copy
              (깊은 복사 vs 얕은 복사)
              ''')
              
print_section('''
              깊은 복사(deep copy)는 변수의 값 자체를 복사하는 것이다.
              
              깊은 복사가 이루어지면, 메모리 상에 새로운 공간이 마련되고,
              그곳에 복사되는 대상의 값이 그대로 저장된다.
              
              뿌리채 뽑아서 옮겨준다고 생각하면 편하다.
              
              결과적으로 다른 주소를 가리키고, 같은 값을 가지게 된다.
              그렇기에 주소를 공유함으로서 발생하는 문제를 미연에 차단 가능하다.
              
              일반적으로 deepcopy() 함수, 혹은 list 의 경우 [:](슬라이싱)으로도 시행할 수 있다.
              ''')

print_section('''
              얕은 복사(shallow copy)는 변수의 주소만을 복사해 공유하는 것이다.
              
              얕은 복사가 이루어지면, 복사되는 변수의 메모리 상의 주소값 만을 가져온다.
              
              결과적으로 같은 주소를 가지게 되며, 메모리 상의 동일한 곳을 가리키게 된다.
              깊은 복사에 비해 성능상 빠르지만, 주소를 공유함에 따른 문제점이 발생할 수 있다.
              
              파이썬에서는 일반적인 변수간의 할당에는 얕은 복사가 쓰인다.
              ''')
              
   
print_indent('위에서 list 는 deepcopy 가 이루어짐을 확인했다. immutable 도 deepcopy 가 가능할까?')

print_indent('tuple 중 요소에 list 가 들어간 경우 deepcopy 가 이루어질까?')


















