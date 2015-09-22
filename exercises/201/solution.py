# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 16:50:47 2015

@author: Aamir Abbasi
"""


def is_alpha(input):   
    import string
    letters = string.ascii_letters
    for i in range(0, len(letters)):
        for j in range(0, len(input)):
            if input(j) != letters(i):
                flag = 1
    if flag == 1:
        return False
    else:
        return True
