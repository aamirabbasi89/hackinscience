# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 17:50:10 2015

@author: Aamir Abbasi
"""


def caesar_cypher(s, key, method):
    import string
    alphabet = string.ascii_lowercase
    if method == 'forward':
        shifted_alphabet = alphabet[key:] + alphabet[:key]
    else:
        shifted_alphabet = alphabet[key:] - alphabet[:key]
    table = string.maketrans(alphabet, shifted_alphabet)
    return s.translate(table)
