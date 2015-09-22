# -*- coding: utf-8 -*-
"""
Exercise 080
Created on Mon Sep 21 15:54:32 2015

@author: Aamir Abbasi
"""
import string
alphaList = string.ascii_lowercase
aO = 0
for i in range(0, 26):
    aO = aO + 1
    for j in range(aO, 26):
        print(alphaList[i] + alphaList[j])
