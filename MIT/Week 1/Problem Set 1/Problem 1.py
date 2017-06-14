# -*- coding: utf-8 -*-
"""
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained 
in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
For example, if s = 'azcbobobegghakl', your program should print:

Number of vowels: 5

"""

vowels = 'aeiou'

s = 'azcbobobegghakl'

count = 0 #Keeps count of the vowels
iteration = 0 #Iteration variable

while iteration < len(s):
    
    for letter in s:
        
        if letter in vowels:
        
            count += 1
        
        iteration += 1
    
print("Number of vowels:", count)