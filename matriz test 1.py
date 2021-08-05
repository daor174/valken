# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 20:25:50 2021

@author: Omen 15
"""

matriz = []
for i in range(0,11):
    matriz.append([]*11)
    

print()        
for i in range (0,11):
    for j in range (0, 11) :
        print(str.rjust(str(matriz[i][j]), 5), end = "")
    print(); print()
input()