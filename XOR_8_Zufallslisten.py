# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 09:24:26 2021

@author: A.K.
"""
import random
L_Petra_bin2= [[1, 0, 1, 0, 0, 0, 0], [1, 1, 0, 0, 1, 0, 1], [1, 1, 1, 0, 1, 0, 0], [1, 1, 1, 0, 0, 1, 0], [1, 1, 0, 0, 0, 0, 1]]
L_Zufall = []
def Zufallsliste(x):
    L = []
    for i in range(x):
        z = random.randint(0,1)
        L.append(z)
    return L
for i in range(len(L_Petra_bin2)):
    r = Zufallsliste(7)
    L_Zufall.append(r)
print("L_Zufall: ",L_Zufall)
