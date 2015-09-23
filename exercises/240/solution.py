# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 18:46:00 2015

@author: Aamir Abbasi
"""
n1 = 1
n2 = 2
alist = [n1, n2]
for i in range(0, 8):
    n3 = n1 + n2
    alist.append(n3)
    n1 = n2
    n2 = n3
for i in range(0, len(alist)):
    if i < len(alist)-1:
        print(alist[i], ',', end=' ')
    else:
        print(alist[i], '.')
