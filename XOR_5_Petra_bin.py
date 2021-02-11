# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 08:13:52 2021

@author: A.K.
"""
s1 ="Petra"
L_Petra = list(s1)
L_Petra_bin = []
for j in L_Petra:
    t = ord(j)
    s = "{:b}".format(t)#ohne lästige 0b!!
    L_Petra_bin.append(s)
print("L_Petra: ",L_Petra)
print("L_Petra_bin: ",L_Petra_bin)
