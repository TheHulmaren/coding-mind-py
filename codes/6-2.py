#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 21:34:46 2022

@author: igyumin
"""

'''
[클래스의 심화]

이전 시간에, 간단히 클래스의 설계와 구조를 알아보았다.
하지만 파이썬에서는 그 이외에도 다양하게 클래스를 꾸미는 방법을 제공한다.

오늘은 아래의 것들을 중점적으로 다룬다:
    1. 연산자 오버로딩
    2. 상속
    3. 함수 캐스케이딩 (시간이 되려나?)

'''


'''
[연산자 오버로딩]

overloading (오버로딩) 이란,
쉽게말해 클래스를 +, -, *, in 등등의 다양한 연산자를 통해 '연산될 수 있도록' 해주는 것이다.

+ 연산자의 기능을 확장(over)한다는 식의 이해를 해도 좋다.


아래 예시를 통해 알아보자

'''

class Cocktail:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = set(ingredients)
    
    def add_ingredient(self, liquor):
        if type(liquor) == str:
            self.ingredients.add(liquor)
        elif type(liquor) == list:
            self.ingredients = self.ingredients | set(liquor)
    
    def explain(self):
        print(f'{self.name}: ' + ', '.join(self.ingredients))



c_0 = Cocktail('Ladykiller', ['Vodka', 'Whisky', 'Rum'])
c_1 = Cocktail('Seoulsoul', ['Soju', 'Beer'])

c_0.add_ingredient('White Wine')
c_0.add_ingredient(['Wine', 'Absolute'])

c_0.explain()
c_1.explain()

print()

'''
위와 같이 Cocktail 클래스가 있고, 그 객체들이 있을때,

만약 
c_0 + c_1
과 같이 연산해서 새로운 칵테일을 만드려면 어떻게 해야할까?

Cocktail 에는 아직 + 연산자에 대한 정의가 없기 때문에, 우리가 직접 함수로서 정의해주어야 한다.

'''


class Cocktail:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = set(ingredients)
    
    def add_ingredient(self, liquor):
        self.ingredients.add(liquor)
        
    def explain(self):
        print(f'{self.name}: ' + ', '.join(self.ingredients))

    # 아래와 같이 __add__ 함수를 통해 더하기 연산을 정의해줄 수 있다.
    def __add__(self, other):
        added = self.ingredients | other.ingredients
        return Cocktail(self.name, added)


c_0 = Cocktail('Ladykiller', ['Vodka', 'Whisky', 'Rum'])
c_1 = Cocktail('Seoulsoul', ['Soju', 'Beer'])

c_2 = c_0 + c_1
c_3 = c_1 + c_0

c_0.explain()
c_1.explain()
c_2.explain()
c_3.explain()

print()

'''
결과적으로 우리는 
c_0 + c_1 을 했을때, 
둘의 재료를 모두 가지면서, 앞에 있는 c_0 의 이름을 가지는 새로운 Cocktail 객체를 반환하는 식으로 + 연산을 정의해 주었다.

그러나 어떻게 정의하는가는 엿장수 맘대로 이므로, 아무렇게나 다르게 정의해도 된다.


아무튼, 빼기와 곱하기, 나눗셈 등등도 비슷하게 정의해줄 수 있다.
str 화 시켰을 때 어떤 값을 반환할 지도 정의 가능하다.

+=, -=, 등의 연산자도 따로 정의해 줄 수 있다.
'''


class Cocktail:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = set(ingredients)

    def add_ingredient(self, liquor):
        self.ingredients.add(liquor)


    # 아래와 같이 __add__ 함수를 통해 더하기 연산을 정의해줄 수 있다.
    def __add__(self, other):
        if type(other) == Cocktail:
            added = self.ingredients | other.ingredients
            return Cocktail(self.name, added)
        elif type(other) == str:
            self.add_ingredient(other)
            return self
        elif type(other) == list:
            self.ingredients = self.ingredients.union(set(other))
            return self
        else:
            return self

    def __radd__(self, other):
        return self + other


    # += 을 정의
    def __iadd__(self, other):
        return self + other


    # 아래와 같이 __sub__ 함수를 통해 빼기 연산을 정의해줄 수 있다.
    def __sub__(self, other):
        if type(other) == Cocktail:
            sub = self.ingredients - other.ingredients
            return Cocktail(self.name, sub)
        else:
            return self

    # -= 을 정의 
    def __isub__(self, other):
        return self - other


    # str() 함수를 적용 시켰을 때 어떤 값을 반환할 지를 정의
    def __str__(self):
        return f'[{self.name}: ' + ', '.join(self.ingredients) 


c_0 = Cocktail('Ladykiller', ['Vodka', 'Whisky', 'Soju'])
c_1 = Cocktail('Seoulsoul', ['Soju', 'Beer'])

c_2 = c_0 - c_1
c_1 += c_0

c_0 = 'Makguli' + c_0
c_0 = c_0 + ['ABC', 'DEF']


print(str(c_2))
print(str(c_1))
print(str(c_0))

print()

'''
[상속]

inheritance (상속) 이란,
어떤 클래스의 기능을 다른 클래스가 받아 쓸수있게 "상속해주는" 것이라고 이해하면 된다.

이때, 
기능을 주는 쪽을 '기초 클래스' 혹은 '부모 클래스',
기능을 받는 쪽을 '파생 클래스' 혹은 '자식 클래스'
라고들 흔히 부른다.


관계를 비유하자면 아래와 같다(오른쪽으로 갈수록 파생 클래스):
    동물 - 인간 - 교사 - 체육교사
    동물 - 인간 - 경찰 - 형사
    도형 - 사각형 - 직사각형 - 정사각형
    도형 - 사각형 - 마름모
    
    
위의 관계를 만약 코딩으로 개념상 구현한다고 생각하면,
'체육교사' 클래스와 '형사' 클래스는 다른점도 있겠지만, 같은 '동물'이고, '인간'이니 만큼 공통점도 많을 것이다.

예컨데 '체육교사' 클래스에는 '체육 가르치기', '형사' 클래스에는 '수사하기' 가 필요하다는 점이 다르겠지만,
'밥먹기', '숨쉬기', '인사하기' 등등의 기능은 동일하게 필요할 것이다.

그럴때, 일일이 그런 다른 점을 따로 구현해줄 필요 없이, 
'인간' 이라는 클래스에 '밥먹기', '숨쉬기', '인사하기'를 구현해 주고,
"파생 클래스"로서 '체육교사' 클래스와 '형사' 클래스를 만든다면 한결 구현이 간편하고, 구조가 체계화 될 것이다.

    
상속은 객체지향 프로그래밍의 핵심 개념으로서, 확실히 숙지해두는 편이 좋다.
아래의 코드를 통해 이해해 보자.

'''


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def older(self):
        self.age += 1
        print(f'{self.name} 이 {self.age} 살이 되었습니다.')
        
    def shit(self, place):
        print(f'{self.name} 이 {place} 에서 똥을 쌉니다.')
        
    def introduce(self):
        text = f'{self.name} 입니다. 나이는 {self.age} 입니다.'
        
        print(text)

class Student(Person):
    def __init__(self, name, age, major, grade):
        self.name = name
        self.age = age
        self.major = major
        self.grade = grade
        
    def change_major(self, major):
        self.major = major
        print(f'{self.name} 학생의 전공이 {major} 로 바뀌었습니다.')
    
    def introduce(self):
        print(f'{self.name} 학생의 전공은 {self.major} 이고, 등급은 {self.grade} 입니다.')
    

s_0 = Student('규민', 22, '수학', 'A-')

s_0.introduce()
s_0.shit('광화문')
s_0.older()


print()

'''
보다시피, Student 클래스에서는 따로 introduce, shit 혹은 older 함수를 정의해주지 않았지만,
Student 는 Person 을 상속받기 때문에 Person 의 함수들을 모두 호출할 수 있다.


또한 상속을 받을때에는, 단순히 부모 클래스의 함수를 호출할 수 있을 뿐만 아니라,
자식클래스의 필요에 맞게 함수를 수정할 수 있다.

이를 함수 오버라이딩(function overriding) 이라고 부른다.

위의 코드를 보면 Person 과 Student 모두 introduce 함수가 있지만,
Student의 객체에서 introduce 를 호출하면 Student 클래스에서 오버라이딩된 버전이 호출된다.
'''



'''
[상속의 연쇄]

우리는 위에서 Person 의 자식 클래스로 Student 를 만들었는데,
마찬가지로 Student 를 부모 클래스로 하는 또다른 자식 클래스를 만들수도 있다.

'''

class ForeignStudent(Student):
    def __init__(self, name, age, major, grade, country):
        self.name = name
        self.age = age
        self.major = major
        self.grade = grade
        self.country = country
        
    def shit(self, place):
        print(f'{self.country} 에서 온 {self.name} 이 {place} 에서 똥을 쌉니다.')
    
    def learn_korean(self):
        print(f'{self.country} 에서 온 {self.name} 학생이 한국어를 배웁니다.')
    
    
f_0 = ForeignStudent('응우옌', 23, '경제학', 'B+', '베트남')
f_0.shit('남산 타워')
f_0.learn_korean()
f_0.change_major('사회학')
f_0.older()



'''
[다중 상속]

파이썬에서는 다중 상속을 지원하지만, 일부 언어에서는 지원하지 않는다.
이는 함수간의 충돌 가능성이 있기 때문인데, 파이썬에서는 아래와 같이 그 문제를 회피한다.

그러나 설계상 좋지 않은 구조이기에, 다중 상속구조는 되도록 지양하는 것이 바람직하다.
'''

class A:
    def test(self):
        print('A')
    
class B:
    def test(self):
        print('B')


class C(B, A):
    def say(self):
        print('hello')
    
    
c = C()
c.test()






'''
[퀴즈]

1.
아래의 기능을 할 수 있도록 Cocktail 클래스를 수정하시오:
    1. c_0 + 'White Wine' 과 같이 Cocktail + String 형태의 덧셈 연산을 수행할 수 있도록 하기.
       이 경우에는 재료에 'White Wine' 이 추가되어야 한다.
    
    2. c_0 > c_1, c_0 < c_1 꼴의 부등호 연산이 가능하도록 하기.
        재료의 가짓수를 기준으로 크고 작음을 판단 할것.

'''


























































