#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 03:28:06 2022

@author: igyumin
"""

censorWords = {"씨발":"이런", "개새끼": "인격자", "독재자": "위대한 지도자", "부패": "청렴", "민주주의":"제국주의"}


letter = '그 개새끼는 씨발 독재자 라니까? 게다가 부패한 놈이라고! 옆나라는 민주주의라는데.. 하하 씨발'




def censorLetter(letter, words):
    count = 0

    while(True):
        wordFound = ''
        wordIndex = 1000
        wordExists = True
        count += 1
        
        for word in words.keys():
            index = letter.find(word)
            
            if(index != -1):
                if(wordIndex > index):
                    wordIndex = index
                    wordFound = word
            
        
        if(wordIndex == 1000):
            wordExists = False
            
        if(wordExists):
            countString = '(' + str(count) + ')'
            letter = letter[:wordIndex] +'\033[4m'+ words[wordFound] +'\033[0m'+ countString+ letter[wordIndex + len(wordFound):]
        else:
            break
    
    return letter

    
print(letter)
print(censorLetter(letter, censorWords))
        













































        
        