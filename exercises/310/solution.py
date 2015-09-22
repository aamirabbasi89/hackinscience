# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 20:29:03 2015

@author: Aamir Abbasi
"""
counter = 0
file = open('words.txt', 'r')
for line in file:
    for l in range(0, len(line)):
        if line[l] == 'e':
            counter = counter + 1
print(counter)