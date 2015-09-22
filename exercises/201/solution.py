# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 16:50:47 2015

@author: Aamir Abbasi
"""


def is_alpha(input):
    for i in range(0, len(input)):
        if i.isalpha():
            return True
        else:
            return False
