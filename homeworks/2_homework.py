#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  4 12:46:56 2022

@author: igyumin
"""



# 2
print('\n# 2\n')

line = "Lorem ipsumer doelor resit ramet consectetur adipisrecing elrit serd doer eiusmord tempor incididunter rute labore ert dolore margnae alirquae Urte enrim aerd mineirm veniamer quiser noerstrud exercitation ullamerco laboreis nisire uter alirquipe exr ear commoerdo conserquat"




# 2-1
print('\n# 2-1\n')


line_lower = line.lower() # 소문자로
line_chars = line_lower.replace(' ', '') # 공백 제거
line_len = len(line_chars) # 공백 제거한 길이 저장

line_set = set(line_chars) # 공백 제거한 소문자 문자열을 집합으로

print(line_set)




# 2-2
print('\n# 2-2\n')


for e in list(line_set):
    print('{a}: {b:>6.2f}%'.format(a = e,b = line_chars.count(e)/line_len * 100)) # 형식에 맞게 출력




# 2-3
print('\n# 2-3\n')


line_split = line_lower.split()
print(line_split)

char_dict = dict() # 비어있는 dictionary 선언

print(line_set)

for e in list(line_set):
    char_dict[e] = [] # 우선 빈 배열 선언
   
    for word in line_split:
        if(word[0] == e):
            char_dict[e].append(word) # 조건이 충족하면 배열에 덧붙이기
            
    
            
for key, value in char_dict.items(): # dictionary 를 형식에 맞게 출력
    print('{0}: {1}'.format(key, str(value))) 
    




# 2-4
print('\n# 2-4\n')
        

temp_set = line_set # line_set 을 그대로 써도 여기선 무방하지만, 그래도 편의상 temp_set 을 따로 선언

for word in line_split: # 각 단어를 순회하면서 순차적으로 교집합 연산
    temp_set = temp_set & set(word) # 연산 후 결과값으로 temp_set 을 업데이트


print(temp_set)

