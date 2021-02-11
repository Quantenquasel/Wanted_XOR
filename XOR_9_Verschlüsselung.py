# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 09:55:24 2021

@author: A.K.
"""
L_Petra_bin2 = [[1, 0, 1, 0, 0, 0, 0], [1, 1, 0, 0, 1, 0, 1], [1, 1, 1, 0, 1, 0, 0], [1, 1, 1, 0, 0, 1, 0], [1, 1, 0, 0, 0, 0, 1]]

L_Zufall = [[1, 1, 1, 0, 1, 0, 0], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 1, 0], [1, 1, 1, 1, 0, 0, 1], [1, 0, 1, 1, 0, 1, 0]]

def Verschlüsselung(L1,L2):
    L_crypt = []
    f = lambda i,j: i^j
    for s in range(len(L_Zufall)):
        Ergebnis = map(f,L1[s],L2[s])
        L_crypt.append(list(Ergebnis))
    return L_crypt

print("L_crypt: ",Verschlüsselung(L_Petra_bin2,L_Zufall))
