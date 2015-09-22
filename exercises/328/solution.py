# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 21:07:11 2015

@author: Aamir Abbasi
"""


def mul(alist):
    multiple = alist[0]
    for i in range(0, len(alist) - 1):
        multiple = multiple * alist[i + 1]
    print(multiple)
