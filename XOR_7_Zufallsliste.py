# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 09:19:07 2021

@author: A.K.
"""
import random

def Zufallsliste(x):
    L = []
    for i in range(x):
        z = random.randint(0,1)
        L.append(z)
    return L
print(Zufallsliste(7))
#[1, 1, 0, 0, 0, 0, 1]
