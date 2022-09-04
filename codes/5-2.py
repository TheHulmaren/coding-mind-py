#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 24 12:53:20 2022

@author: igyumin
"""



'''
[사용자 입력]

실행 시간에 콘솔창에서 사용자에게 값을 입력받으려면 어떻게 해야할까?

파이썬에서는 input 함수를 이용할 수 있다.

input 함수는 입력된 값을 string 의 형태로 반환한다.
'''

# =============================================================================
# a = input()
# print(f'{a} was typed')
# 
# 
# =============================================================================

# =============================================================================
# b = input('Here be input: ')
# print(f'{b} was typed')
# 
# =============================================================================


'''
1. 
정수 두개를 입력받아 그 합을 출력하는 함수를 작성하시오.
두 정수는 한 줄에서 입력받으며, 공백으로 구분한다.

사용자 입력: 5 4

출력: 9

'''


# =============================================================================
# 
# def add_two():
#     input_str = input('Type the two numbers with blank between them: ')
#     split = input_str.split()
#     a = int(split[0])
#     b = int(split[1])
#     
#     print(a+b)
# 
# 
# add_two()
# 
# 
# =============================================================================
'''
[파일 입출력]

위와같이 실행 시간에 실시간으로 값을 입력받을 수도 있지만,
때로는 파일을 읽어들이는 것이 필요할 때도 있다.

이를 위해 파이썬에서는 여러가지 기능과 함수를 제공한다.

'''


# 읽기 모드로 파일 불러오기
file = open(mode='r', file='sample.txt')

lines = file.readlines()

for line in lines:
    print(line) # 왜 사이에 공백이 생기지?

file.close() # 잊지 말것!



# 쓰기 모드로 파일 불러오기
file = open('test.txt', 'w')

content = 'This\nwill\nbe\nwritten\non\nthe\ntext\nfile'

file.write(content)

file.close()



# 추가 모드로 파일 불러오기
file = open('test.txt', 'a')

for i in range(5):
    text = f'\n{i}th line'
    file.write(text)

file.close()




# with 문과 함께 사용하기
# with 문이 끝나면 자동으로 file 객체가 close 된다.
with open('sample.txt', 'r') as file:
    for line in file.readlines():
        print(line.strip())





# 자, 같이 해봅시다.

# 1. 파일경로와 문자열을 매개변수로 입력받아,
#    해당 파일에 매개변수로 입력받은 문자열을 추가하는 함수를 작성하시오.











# 2. 회원 정보가 담긴 리스트와 파일경로를 매개변수로 입력받아,
#    해당 파일에 아래와 같이 회원 정보를 저장하시오.
'''
회원정보: [('Joe Biden', 34, 'Male', 'Premium'),
        ('Donald Trump', 56, 'Male', 'Limited'),
        ('Vladimir Putin', 69, 'Female', 'Terminated'),
        ('Volodimir Zelensky', 25, 'Male', 'VVIP'),
        ('Yoon Seokyul', 61, 'Male', 'Premium')]

저장된 내용:
    [Joe Biden]
    Age: 34, Sex: Male, Status: Premium
    [Donald Trump]
    Age: 56, Sex: Male, Status: Limited
    .
    .(중간 생략)
    .
    [Yoon Seokyul]
    Age: 61, Sex: Male, Status: Premium
    
'''


def save_members(filepath, members):
    with open(filepath, 'a') as file:
        for member in members:
            name, age, sex, status = member
            text = f'[{name}]\nAge: {age}, Sex: {sex}, Status: {status}\n'
            file.write(text)


M = [('Joe Biden', 34, 'Male', 'Premium'),
        ('Donald Trump', 56, 'Male', 'Limited'),
        ('Vladimir Putin', 69, 'Female', 'Terminated'),
        ('Volodimir Zelensky', 25, 'Male', 'VVIP'),
        ('Yoon Seokyul', 61, 'Male', 'Premium')]

save_members(filepath = '/Users/igyumin/Desktop/members.txt', members = M)



















# 3. 
'''
while 문과 input 을 이용해서
아래의 룰에 따라 진행되는 아주 간단한 게임의 코드를 작성하시오.

1. 1에서 100까지 중 랜덤하게 숫자를 하나 고른다.
2. 사용자가 반복해서 숫자를 입력한다.
3. 만약 입력한 숫자가 랜덤 숫자에 비교해 더 작다면 'Bigger!', 크다면 'Smaller!' 를 출력한다.
4. 일치한다면 'Correct!' 를 출력하고 게임을 끝낸다.
'''


import random


ran_num = random.randrange(1,101)

continued = True

while continued:
    input_num = int(input('\nInput the number: '))
    
    if input_num > ran_num:
        print("Smaller!")
    elif input_num < ran_num:
        print('Bigger!')
    else:
        print('Correct!')
        continued = False


