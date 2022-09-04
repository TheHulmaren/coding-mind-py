#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 22 00:30:23 2022

@author: igyumin
"""
import re
import random
words = ['apple','banana','orange']
answer_save = ""
quiz_word = random.choice(words)
hide_word = len(quiz_word) * "_"
b = "a"
while not hide_word == quiz_word:
    answer = input()
    if answer in quiz_word:
        print("Correct")
        answer_save += answer
        index = quiz_word.index(answer)
        hide_word = hide_word[0:index] + answer + hide_word[index+len(answer):]
        
    else:
        print("Wrong")
    print(hide_word)
print("Success")

