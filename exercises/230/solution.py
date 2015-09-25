# -*- coding: utf-8 -*-
"""
Exercise 230
Created on Fri Sep 25 10:09:43 2015

@author: Aamir Abbasi
"""
import chkprim
for i in range(100000000, 100000008):
    if chkprim.is_prime(i) is True:
        print(i)
        break
