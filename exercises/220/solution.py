# -*- coding: utf-8 -*-
"""
Exercise 220
Created on Tue Sep 22 17:26:28 2015

@author: Aamir Abbasi
"""
alist = []
for i in range(10000, 10050):
    for j in range(2, i):
        flag = 0
        if i % j == 0:
            flag = 1
        if flag == 1:
            break
    if flag == 0:
        alist.append(i)
for i in range(0, len(alist)):
    if i < len(alist)-1:
        print(alist[i], end=', ')
    else:
        print(alist[i], end=' ')
