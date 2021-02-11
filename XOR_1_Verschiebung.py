# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 07:47:03 2021

@author: A.K.
"""
import collections
import string#Modul, mit dem man unter anderem auch die Liste L erzeugen kann

L = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
L1 = collections.deque(L)
print(L1.rotate(3))
print(L,'\n\n',list(L1))
