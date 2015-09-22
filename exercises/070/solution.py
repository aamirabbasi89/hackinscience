# -*- coding: utf-8 -*-
"""Exercise 070
Created on Mon Sep 21 16:30:13 2015

@author: Aamir Abbasi
"""
import string
alphaList = string.ascii_lowercase
for i in range(0, 26):
    for j in range(0, 26):
        if alphaList[i] != alphaList[j]:
            print(alphaList[i] + alphaList[j])
