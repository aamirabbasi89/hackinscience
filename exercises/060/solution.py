# -*- coding: utf-8 -*-
"""
Exercise 060
Created on Mon Sep 21 15:27:35 2015

@author: Aamir Abbasi
"""
import string
alphaList = string.ascii_lowercase
for i in range(0, 26):
    for j in range(0, 26):
        print(alphaList[i] + alphaList[j])
