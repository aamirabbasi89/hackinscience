# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 15:50:24 2015

@author: Aamir Abbasi
"""


def is_prime(num):
    if num == 0 or num == 1:
        return False
    if num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
