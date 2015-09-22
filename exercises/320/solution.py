# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 20:46:05 2015

@author: Aamir Abbasi
"""
import string
letters = string.ascii_letters
file = open('words.txt', 'r')
txtSize = 0
for alphabet in range(0, len(letters)):
    counter = 0
    for line in file:
        txtSize = txtSize + len(line)
        for l in range(0, len(line)):
            if line[l] == letters[alphabet]:
                counter = counter + 1
    print(letters[alphabet], ':', counter/txtSize)
