#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 30 10:11:52 2022

@author: igyumin
"""

'''
[클래스의 기초]

클래스는 설계도와 같다.
그리고 그 설계도를 가지고 계속해서 객체들을 만들어낼 수 있다.

레시피 - 케잌
청사진 - 건물
설계도 - 자동차

..의 관계라고 생각하면 이해가 쉽다.

기존에 배운 string, list, tuple, dictionary, int, float 등등 도 클래스이다.
다만 이들은 프로그램에서 자체적으로 제공하는 클래스이기도 하고, 매우 기초적인 기능을 담고 있기 때문에,
Primitive Class 라고 불린다.
(원시 클래스)


만약 클래스가 없다면 어떤점이 불편할까?

예를들어, 여러 사람의 정보를 각각 담고 그것들을 수정/가공하는 프로그램을 만든다고 하자.
지금까지 배운 방식만을 사용하면, 아래와 같이 해야한다.

'''


name0 = 'Kyumin'
age0 = 22
sex0 = 'Male'
job0 = 'Student'

name1 = 'Junseok'
age1 = 41
sex1 = 'Male'
job1 = 'The leader of PPP'

name2 = 'Jihyeon'
age2 = 29
sex2 = 'Female'
job2 = 'Feminist'


'''
클래스가 없다면 위에서 보다시피, 
일일이 늘여써야 하며, 각개 변수를 다르게 지정하고 써야하기 때문에 복잡성과 귀찮음이 늘어난다.

데이터가 파편화 되어 있기에 추후에 문제가 발생할 수도 있을 것이다.



우리는 Person 이라는 클래스를 만들어 위 코드를 아래와 같이 바꿔볼 수 있다.
간략히 개인정보를 저장하고, 자기소개를 출력하는 기능이 있는 클래스이다.

'''


class Person:
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job
        
    def introduce(self):
        text = f'{self.name} 입니다.\n나이는 {self.age} 이고, 직업은 {self.job}입니다.'
        
        print(text)


person_0 = Person('Kyumin', 21, 'Student')
person_1 = Person('Junseok', 41, 'The leader of PPP')
person_2 = Person('Jihyeon', 29, 'Feminist')

person_0.introduce()
Person.introduce(self = person_0)




'''
위와 같이 한번 클래스를 설계해 놓으면, 
그 이후로는 매우 손쉽게 Person 객체를 생성해 클래스에 정의된 함수를 이용할 수 있다.


Person 에 다음과 같이 다른 함수를 추가할 수도 있다.

get_generation 은 나이에 따른 통상적인 세대를 구분해 구해주는 함수고,
get_bmi 는 몸무게와 키를 바탕으로 bmi 지수를 계산해주는 함수다.
'''




class Person:
    def __init__(self, name, age, job, weight, height):
        self.name = name
        self.age = age
        self.job = job
        self.weight = weight
        self.height = height
    
    def introduce(self):
        text = f'{self.name} 입니다.\n나이는 {self.age} 이고, 직업은 {self.job}입니다.'
        
        print(text)
    
    def get_generation(self):
        if self.age < 10:
            return 'Alpha'
        elif self.age < 25:
            return 'Z'
        elif self.age < 40:
            return 'M'
        elif self.age < 50:
            return '486'
        elif self.age < 70:
            return 'Babyboom'
        else:
            return 'Greatest'
    
    def get_bmi(self):
        return self.weight**2 / self.height


person_0 = Person('Kyumin', 21, 'Student', 72, 170)
person_2 = Person('Juhyeon', 29, 'Feminist', 58, 163)


print(person_0.get_generation())
print(person_0.get_bmi())

print(person_2.get_generation())
print(person_2.get_bmi())


'''
이번에는 Circle 클래스를 같이 만들어 보자

이 클래스는 다음과 같은 기능을 한다:
    1. 반지름, 중심좌표 저장 (__init__)
    2. 넓이 구하기 (get_area)
    3. 다른 Circle 과의 크기 비교 (compare)
    4. 어떤 점이 원 내부에 속하는지 여부 판별 (contains)
'''



class Circle:
    def __init__(self, radius, xy):
        self.radius = radius
        self.xy = xy
    
    def get_area(self):
        return self.radius**2 * 3.141592
    
    def compare(self, other):
        self_area = self.get_area()
        other_area = other.get_area()
            
        if self_area > other_area:
            return 1
        elif self_area < other_area:
            return -1
        else:
            return 0


c_0 = Circle(6, (0,0))
c_1 = Circle(6, (0,0))

print(c_0.get_area())
print(c_1.get_area())

print(c_0.compare(c_1))






'''
[퀴즈]

1.
다음 기능을 하는 클래스 Rectangle을 설계하라:
    1. 높이, 폭 을 저장 (__init__)
    2. 넓이 구하기 (get_area)
    3. 대각선 길이 구하기 (get_diagonal)
    4. 다른 Rectangle 객체와의 크기 비교 (compare)
    5. 정사각형인지 판별 (is_square)


2.
위에서 만든 Person 클래스를 이용해,
다음 기능을 하는 클래스 Group 을 만드시오:
    1. 그룹 이름 저장 (__init__)
    2. 그룹 멤버(Person 객체) 추가, 삭제 (add, delete)
    3. 어떤 Person 이 소속됐는지 여부 판별 (contains)
    4. 소속된 멤버들의 이름과 나이, 직업을 모두 출력하시오 (introduce_all)
    5. 다른 Group과 합치기 (merge)
'''


class Group:
    def __init__(self, name):
        self.name = name
        self.members = []
    
    def add(self, person):
        self.members.append(person)
    
    def delete(self, person):
        self.members.remove(person)
    
    def contains(self, person):
        return person in self.members
    
    def introduce_all(self):
        print(f'[{self.name}]')
        for member in self.members:
            text = f'Name: {member.name}, Age: {member.age}, Job: {member.job}'
            print(text)

    def merge(self, other):
        self.members = self.members + other.members



person_0 = Person('Kyumin', 21, 'Student', 72, 170)
person_1 = Person('Hanyoung', 41, 'Cooker', 72, 170)
person_2 = Person('Juhyeon', 29, 'Feminist', 58, 163)
person_3 = Person('Seokyeol', 30, 'Professor', 72, 170)
person_4 = Person('Zelensky', 40, 'President', 72, 170)


group = Group('IOS')

group.add(person_1)
group.add(person_0)
group.add(person_4)

group.introduce_all()

group.delete(person_0)
print()

group.introduce_all()

group_new = Group('Android')

group_new.add(person_2)
group_new.add(person_3)

group_new.introduce_all()

group.merge(group_new)
print()

group.introduce_all()



































