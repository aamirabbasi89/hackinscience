# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 19:36:46 2015

@author: Aamir Abbasi
"""
try: 
    import requests
    req = requests.get('http://mdk.fr/ip')
    print(req)
except:
    print("No internet connectivity.")
