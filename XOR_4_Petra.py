# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 08:02:03 2021

@author: A.K.
"""
Z = ord("P")#ganze Zahl, die für den Buchstaben „A“ steht.
Z_bin = bin(Z)#Überführung des Buchstaben „A“ in eine Binärdarstellung
print(Z_bin)#string!!
L = []#Definition einer leeren Liste
for i in Z_bin:
    L.append(i)
print(L)
#Ergebnis:['0', 'b', '1', '0', '0', '0', '0', '0', '1']
print()
L1 = []#leere Liste
for i in range(2,len(Z_bin)):#die ersten beiden Zeichen weglassen 0,b!!
    L1.append(Z_bin[i])#Liste füllen
print("L1: ",L1)#
print()
#Prinzip des "perfekten Löschens“
for i in range(len(L1)):
    L1[i] = int(L1[i])^int(L1[i])# ^ - das ist in Python der XOR - Operator
print(L1)
# Ergebnis: [0, 0, 0, 0, 0, 0, 0]
