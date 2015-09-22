# -*- coding: utf-8 -*-
"""
For Exercise on STRINGS
Created on Mon Sep 21 11:03:39 2015

@author: Aamir Abbasi
"""
'"Isn\'t", she said.'
print('"Isn\'t", she said.')
s = 'First line. \nSecond line.'  # \n means new line
print(s)
print('C:\some\name')
print(r'C:\some\name')
print("""\
Usage: thingy[OPTIONS]
       -h                 Display this usage message
       -H                     Hostname to connect to
""")
string = 3 * 'un' + 'ium'
print(string)
print('Py' 'thon')
text = ('This' ' ' 'is' ' ' 'a' ' ' 'lovely' ' ' 'morning')
print(text)
word = 'Paris'
print('first character' ' ', word[0])
print('third character' ' ', word[3])
print('last character' ' ', word[4])
print('last character' ' ', word[-1])  # last character
print('second last character' ' ', word[-2])  # second last character
print(word[0:3])
print(word + ' ' "Je t'aime")
newString = word + ' ' "Je t'aime"
print(len(newString))
