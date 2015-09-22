# -*- coding: utf-8 -*-
"""
Exercise 107
Created on Tue Sep 22 15:14:01 2015

@author: Aamir Abbasi
"""


def select_student(my_class, m):
    for i in range(0, len(my_class)):
        if my_class[i][2] < m:
            result= {'Accepted': my_class[i]}
        else:
            result= {'Rejected': my_class[i]}
    print(result)
