#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 10 19:32:53 2022

@author: igyumin
"""


# 1
print('\n# 1\n')

n = 4

for i in range(n+2):
    if i == n+1:
        print('#' * (n+2))
    else:
        print('#{0}#'.format(' '*i))

        
        
# 2
print('\n# 2\n')

N = [4, 12, 78, 13, 4, 6, 102, 901, 1, 34]

mean = sum(N)/len(N)

N.sort()

median = N[len(N) // 2]

print('평균:', mean)
print('중간값:', median)


# 3
print('\n# 3\n')

transfer_dict = {'ICN': 'EFN',
                 'SEX': 'RFC',
                 'HKN': 'SEX',
                 'EFN': 'HKN',
                 'RFC': 'JFK'}

current_temp = 'ICN' # 초기값 ICN 으로 설정

print('환승표:', transfer_dict)
print('경유:', end=' ')

while(True):
    print(current_temp, end = '') # 현재 공항 출력
    
    if current_temp == 'JFK': # JFK 가 나올때 까지 반복
        break
    
    current_temp = transfer_dict[current_temp] # 다음 루프를 위한 현재 공항 업데이트
    
    print(' -> ', end = '') # 화살표 출력
    
print()

# 4
print('\n# 4\n')

price = 125350
given = 182910
change = given - price

units = [10000, 5000, 1000, 500, 100, 50, 10] # 화폐 단위 내림차순으로 설정
temp = change 

result = dict()

for unit in units:
    if temp // unit == 0: # 해당 화폐 단위보다 남아있는 액수가 작으면 다음으로..
      continue
    result[unit] = temp // unit
    temp = temp % unit
    
print('- 가격: {0} 원'.format(price))
print('- 받은 돈: {0} 원'.format(given))
print('- 거슬러 줄 액수: {0} 원'.format(change))

print('- 결과:')

for key, value in result.items():
    print('\t{0:>5} 원 x {1:>3} 개'.format(key, value))









    
    