# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 13:07:51 2015

@author: Aamir Abbasi
"""
import mathtools
sum = 0
for i in range(0, 1000):
    if mathtools.is_prime(i) is True:
        sum += i
print(sum)
