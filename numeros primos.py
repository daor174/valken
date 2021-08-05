# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 19:14:24 2021

@author: Omen 15
"""
import math
N = int(input("ingrese el tope de los numeros primos: "))

L = [0]
for i in range(0, 50):
    L[i] = i
    L.append(0)
print(L)    
L[1] = 0

'''i = 4
while i <= N:
    L[i] = 0
    i = i + 2
    
i = 6
while i <= N:
    L[i] = 0
    i = i + 3'''
    
K = 2
while K <= int(math.sqrt(N)) :
    i = 2*K
    while i <= N:
        L[i] = 0
        i = i + K
    
    K = K + 1
print();print(L)
input()
    