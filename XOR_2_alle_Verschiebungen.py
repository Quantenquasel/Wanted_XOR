# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 07:51:22 2021

@author: A.K.
"""
#Pythoncode (zunächst für die Cäsar-Chiffre: Liste L_3 und dann für alle Verschiebungen):
import collections
L = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
print()
L_3 = collections.deque(L)
L_3.rotate(3)
print("L_3:",list(L_3))
for i in range(1,27):
    L1 = collections.deque(L)
    L1.rotate(i)
    print(L,'\n\n',list(L1),"\n\nUrsprungsliste um: ",i," Stellen nach rechts verschoben.\n")
