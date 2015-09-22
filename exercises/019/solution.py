# -*- coding: utf-8 -*-
"""
Exercise 19
Created on Mon Sep 21 16:50:47 2015

@author: Aamir Abbasi
"""
import sys

if (len(sys.argv) < 2):
     print("usage: python3 solution.py PARAM.")
else:
    print(str(int(sys.argv[1]) + int(sys.argv[2]))) 
    