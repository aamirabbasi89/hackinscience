# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 20:46:05 2015

@author: Aamir Abbasi
"""
import string
letters = string.ascii_lowercase
txtSize = 0
file = open('words.txt', 'r')
for alphabet in range(0, len(letters)):
    counter = 0
    for line in file:
        for l in range(0, len(line)):
            if line[l] == letters[alphabet]:
                counter = counter + 1
        txtSize = txtSize + len(line)
    print(letters[alphabet], ':', counter/txtSize)
