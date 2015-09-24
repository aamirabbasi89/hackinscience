# -*- coding: utf-8 -*-
"""
Exercise 097
Created on Tue Sep 22 10:29:26 2015

@author: Aamir Abbasi
"""


def love_meet(bob, alice):
    CommonList = []
    for i in range(0, len(bob)):
        for j in range(0, len(alice)):
            if bob[i] == alice[j]:
                CommonList.append(bob[i])
    return (set(CommonList))


def affair_meet(bob, alice, silvester):
    CommonList = []
    for i in range(0, len(alice)):
        for j in range(0, len(bob)):
            for k in range(0, len(silvester)):
                if alice[i] != bob[j] and alice[i] == silvester[k]:
                    CommonList.append(alice[i])
    return (set(CommonList))
