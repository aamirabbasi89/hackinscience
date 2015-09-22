# -*- coding: utf-8 -*-
"""
Exercise 097
Created on Tue Sep 22 10:29:26 2015

@author: Aamir Abbasi
"""

def love_meet(bob,alice):
    CommonList = []
    for i in range(0,len(bob)):
        for j in range(0,len(alice)):
            if bob[i] == alice[j]:
                CommonList = [CommonList, bob[i]]
    print(CommonList)

def affair_meet(bob,alice,silvester):
    CommonList = []
    for i in range(0,len(alice)):
        for j in range(0,len(bob)):
            for k in range(0,len(silvester)):
                if alice[i] != bob[j] & alice[j] == silvester[k]:
                    CommonList = [CommonList, alice[i]]
    print(CommonList)
    