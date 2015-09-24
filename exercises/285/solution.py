# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 15:06:29 2015

@author: Aamir Abbasi
"""


try:
    import requests
    r = requests.get('http://mdk.fr/ip')
    print(r.headers['content-type'])
except:
    print('No internet connectivity.')
