# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 10:03:58 2021

@author: A.K.
"""
import random
random.seed(42)
def Eingabe():
    Text = []
    print("Ihr Text (am Ende bitte zweimal enter drücken): ","\n\n")
    while True:
        Zeile = input()
        if Zeile:
            Text.append(Zeile)
        else:
            break
    Eingabe1 = '\n'.join(Text)
    return Text
def Zufallsliste(x):
    L = []
    for i in range(x):
        z = random.randint(0,1)
        L.append(z)
    return L
def Verschlüsselung(L1,L2):
    L_crypt = []
    f = lambda i,j: i^j
    for s in range(len(Schlüssel)):
        Ergebnis = map(f,L1[s],L2[s])
        L_crypt.append(list(Ergebnis))
    return L_crypt
def Entschlüsselung(L1,L2):
     L_crypt = []
     f = lambda i,j: i^j
     for s in range(len(Schlüssel)):
        Ergebnis = map(f,L1[s],L2[s])
        L_crypt.append(list(Ergebnis))
        return L_crypt
def Encoding():
    pass
def Decoding():
    pass
s = Eingabe()
LT = []
print((s), type(s))
print()
for i in s:
    r = list(i)
    LT.append(r)
print(LT)
L_ord = []
for j in LT:
    for k in range(len(j)):
        l = ord(j[k])
        L_ord.append(l)
print()
print(L_ord)#Text als ganze Zahlen
print()
L_bin = []
for i in L_ord:
    r = list(bin(i))
    L_bin.append(r)
print("L_bin, len(L_bin):\n",L_bin, len(L_bin))#Text in Binärrepresentation
print()
L_bin2 = []
for i in L_ord:
    s = "{:b}".format(i)#ohne lästige 0b!!
    L_bin2.append(s)
print(L_bin2)
TL_b_L = []
for r in L_bin2:
    u = list(r)
    TL_b_L.append(u)
print()
print(TL_b_L, len(TL_b_L))
Zähler = 0
for i in TL_b_L:
    m = len(i)
    while m < 8:
        i.insert(0,"0")
        m +=1
print()
print(TL_b_L, len(TL_b_L))#Text in 8-Bitmuster
#Liste mit Liste aus Zufallsbytes!!
#Zufallsschlüsselerzeugung
print()
Schlüssel = []
k = len(TL_b_L)
for i in range(k):
    for j in range(8):
        TL_b_L[i][j] = int(TL_b_L[i][j])
print()
print("Text binär im 8-Bitmuster:\n\n",TL_b_L)
for i in range(k):
    t = Zufallsliste(8)#Liste darf natürlich nicht zufällig mit entsprechendem Textzeichen identisch #sein!!
    Schlüssel.append(t)
print()
print("Schlüssel:\n\n", Schlüssel, len(Schlüssel))
print()
#Text in Datei - sollte man aus Sicherheitsgründen nicht machen!
#pass -Schlüssel in Datei als kryptografischen Hashwert in einer Datei speichern
#pass -verschlüsselter Text in eine Datei schreiben
print("Verschlüsselung:\n",Verschlüsselung(TL_b_L,Schlüssel))
