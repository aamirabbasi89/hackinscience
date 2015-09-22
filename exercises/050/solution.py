# -*- coding: utf-8 -*-
"""
Exercise 050
Created on Mon Sep 21 15:21:48 2015

@author: Aamir Abbasi
"""
s = 0
for i in range(0, 1001):
    if i % 3 == 0 | i % 5 == 0:
        s = s + i
print(s)
