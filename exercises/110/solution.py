# -*- coding: utf-8 -*-
"""
Exercise 110
Created on Tue Sep 22 15:29:58 2015

@author: Aamir Abbasi
"""
import sys
if (len(sys.argv)) < 4:
    print("usage: ./solution.py a_number (an_operator +-*/%^) a_number")
else:
    if sys.argv[2] == '+':
        print(int(sys.argv[1]) + int(sys.argv[3]))
    if sys.argv[2] == '-':
        print(int(sys.argv[1]) - int(sys.argv[3]))
    if sys.argv[2] == '/':
        print(int(sys.argv[1]) / int(sys.argv[3]))
    if sys.argv[2] == '*':
        print(int(sys.argv[1]) * int(sys.argv[3]))
    if sys.argv[2] == '%':
        print(int(sys.argv[1]) % int(sys.argv[3]))
    if sys.argv[2] == '^':
        print(int(sys.argv[1]) ** int(sys.argv[3]))
