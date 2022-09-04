#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 16 21:20:07 2022

@author: igyumin
"""

# 1.

# 1,2




# 2.

N = 'pythonlanguage'

M = list(N)

M.sort()

print(''.join(M))



# 3.

import string

upper = string.ascii_uppercase # 대문자 모음
lower = string.ascii_lowercase # 소문자 모음

index = 0 # 알파벳 순서 

for i in range(6):
    for j in range(i+1):
        if index % 2 == 0: # index 홀짝 번갈아 가며 대문자 소문자 출력
            print(upper[index], end='')
        else:
            print(lower[index], end='')
        index += 1 # 다음 알파벳을 출력하기 위해 index 업데이트
    print()
            
        
    

# 4.

import random

A = set()

while(True):
    ran_num = random.randrange(1,100)
    A.add(ran_num) # 랜덤하게 뽑은 숫자를 집합에 삽입
    
    # 랜덤하게 뽑은 숫자가 기존에 뽑은 숫자와 중복될 수 있으므로, while 문을 통해 계속 반복하다가..
    if len(A) == 10: # ..집합의 길이가 목표한 10이 되면 while 탈출
        break
    
print(A)



# 5.

import math

n = 5

for i in range(n):
    print('{pi:>{space}.{digit}f}'.format(pi=math.pi, space=n+1, digit=i))



# 6.

A = [('+', 1), ('-', 3), ('*', 2), ('/', 4)]

temp = 10

for op, num in A:
    if op == '+':
        temp += num
    elif op == '-':
        temp -= num
    elif op == '*':
        temp *= num
    elif op == '/':
        temp /= num

print(temp)




# 7.

n = 12

print('A B C\n-----')

for i in range(1,7):
    for j in range(1,7):
        for k in range(1,7):
            if i+j+k == n:
                print(i,j,k)



# 8.

N = [[4,3,5],[1,2,3],[9,2,1],[7,6,5],[6,8,10]]


for tri in N:
    tri_sorted = tri.copy()
    tri_sorted.sort() # 세 변을 오름차순으로 정렬
    
    a, b, c = tuple(tri_sorted) # c 가 가장 긴 변
    
    if a**2 + b**2 < c**2:
        print(str(tri) + ': 둔각')
    elif a**2 + b**2 == c**2:
        print(str(tri) + ': 직각')
    elif a**2 + b**2 > c**2:
        print(str(tri) + ': 예각')



# 9.

import math

N = [((1, 2), (2, 1)), ((-2, 4), (-10, -1)), ((1, 4), (-3, -1)), ((-2, 7), (9, -1)), ((-2, 0), (0, -1))]

temp = 0 
longest = tuple() # 최대 길이 선분 저장

for line in N:
    dist = math.sqrt((line[0][0] - line[1][0])**2 + (line[0][1] - line[1][1])**2) # 길이 계산
    if dist > temp: # 순회하며 가장 긴 선분인지 비교
        temp = dist
        longest = line # 현재 시점 가장 긴 선분 업데이트

print(longest,':',temp)



# 10.

heights = [183, 156, 140, 159, 172, 174, 167, 143, 185, 179, 141, 165, 143, 173, 166, 162, 186, 171, 146, 164, 188, 144, 173, 142, 176, 165, 152, 152, 157, 159]

arith_temp = 0
geo_temp = 1
mode_temp = 0
mode_count_temp = 0


for h in heights:
    arith_temp += h # 모든 요소를 합
    geo_temp *= h # 모든 요소를 곱
    
    if heights.count(h) > mode_count_temp: # 순회하며 최빈값인지 비교
        mode_temp = h
        mode_count_temp = heights.count(h) # 현재시점 최빈값 업데이트
    
arith_mean = arith_temp/len(heights) # 산술평균 계산
geo_mean = geo_temp**(1/len(heights)) # 기하평균 계산

median = (heights[15] + heights[16])/2 # 중간값 계산 (배열의 길이가 30으로 고정이므로 그냥 상수로 인덱싱)


print('산술평균: {0:>6.2f}'.format(arith_mean))
print('기하평균: {0:>6.2f}'.format(geo_mean))
print('최빈값: {0:>6.2f}'.format(mode_temp))
print('중앙값: {0:>6.2f}'.format(median))








