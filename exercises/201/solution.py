# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 16:50:47 2015

@author: Aamir Abbasi
"""


def is_alpha(input):
    import string
    letters = string.ascii_letters
    flag = 0
    for i in range(0, len(input)):
        for j in range(0, len(letters)):
            if input[i] == letters[j]:
                flag += 1
    if flag == len(input):
        return True
    else:
        return False
