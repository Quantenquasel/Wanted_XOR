# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 10:09:58 2021

@author: A.K.
"""
#Module einbinden
import random
#Funktionen 
def encryption(L_1, L_2):
    Lk = []
    for i in range(len(L1)):
        t = L_1[i]^L_2[i]
        Lk.append(t)
    return Lk
def decryption(L_1, L_2):
    Lk = []
    for i in range(len(L1)):
        t = L_1[i]^L_2[i]
        Lk.append(t)
    return Lk

#Eingabe
a = input("Geben Sie die zu verschlüsselnde Zeichenkette ein:\n\n")#A
print()
b = list(a)#built-in list 
L = []#leere Liste definieren – brauchen wir später
L1=[]#dito
print("Nachrichtenstringliste: ",b)#['A']
print()#sieht auf der Konsole übersichtlicher aus
for i in b:# eine for Schleife
    r = bin(ord(i))#Binärdarstellung der i-ten Ordnungszahl
    print(r)#str- 0b1000001 - ASCII A
    rL = list(r)#
    del rL[1]#entfernt das b - bleiben 8 Listenelemente
    print()
    print(rL)#['0', '1', '0', '0', '0', '0', '0', '1']] aus ['0', 'b', '1', '0', '0', '0', '0', '0', '1']
    print()
    for i in rL:
        L1.append(int(i))
print("Nachrichtenbitliste und deren Länge in Bits: ", L1, len(L1), " Bits")#[0, 1, 0, 0, 0, 0, 0, 1] 8 - Nachrichtenbitliste mit Anzahl
print()
T = [0,1]
L_rand = []
for i in range(len(L1)):
    s = random.choice(T)
    L_rand.append(s)
print()
print()
print("Zufallsschlüssel:\n\n", L_rand, len(L_rand), " Bits")
print()
print("Ergebnis  XOR:\n\n ",encryption(L1,L_rand),len(encryption(L1, L_rand))," Bits")
print()
print()
E = encryption(L1,L_rand)
print("Entschlüsselung mit Zufallsschlüssel und Verschlüsselung: \n\n",L_rand,"\n\n",E)
print()
D = decryption(E,L_rand)
print("Entschlüsselungsergebnis: \n\n",D)
print()
#wieder Ursprungstext erzeugen
L_Text = []
n = 0#brauchen wir gleich, zum Durchlaufen der Liste
for j in range(int(len(D)/8)):#soviel Bytes haben wir!!
    L_t = []
    for k in range(8):
        L_t.append(D[n])
        n +=1
    L_Text.append(L_t)
print("L_Text: ",L_Text)
print()
f = ''
L_Text_2 = []
for s in L_Text:
    for i in range(len(s)):
        f += str(s[i])
    L_Text_2.append(f)
    f = ''
L_Text_3 = []
print(L_Text_2)
print()
for i in L_Text_2:
    s = int(i,2)#Besonderheit!string - Umwandlung in eine Dezimalzahl!
    print(s, chr(s))
    L_Text_3.append([i,s,chr(s)])
print()
print(L_Text_3)
print()
s = ''
for i in L_Text_3:
    s += i[2]
print(s)#Voila!