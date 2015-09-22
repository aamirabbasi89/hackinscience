# -*- coding: utf-8 -*-
"""
Exercise 20
Created on Mon Sep 21 17:05:14 2015

@author: Aamir Abbasi
"""
import sys
if (len(sys.argv) < 2):
    print("usage: python3 solution.py OP1 OP2")
else:
    print(str(int(sys.argv[1]) - int(sys.argv[2])))
