# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 08:20:42 2021

@author: A.K.
"""
s1 ="Petra"
L_Petra = list(s1)
L_Petra_bin = []
L_Petra_bin_1 = []
L_Petra_bin_2 = []
for j in L_Petra:
    t = ord(j)
    s = "{:b}".format(t)#ohne lästige 0b!!
    L_Petra_bin.append(s)
print("L_Petra: ",L_Petra)
print("L_Petra_bin: ",L_Petra_bin)
##
print("L_Petra_bin: ",L_Petra_bin)
#Liste aus Tupeln mit Buchstaben deren Binärdarstellung
L = list(zip(L_Petra,L_Petra_bin))
print()
print(L)
for i in L_Petra_bin:
    u = list(i)
    L_Petra_bin_1.append(u)
print()
print("L_Petra_bin_1: ",L_Petra_bin_1)
print()    
#Kleiner Schönheitsfehler – die Listeneinträge sind noch vom Typ string, das ändern wir jetzt:
for k in L_Petra_bin_1:
    v=[]
    for i in k:
        u = int(str(i))
        v.append(u)
    L_Petra_bin_2.append(v)
print("L_Petra_bin2: ",L_Petra_bin_2)
