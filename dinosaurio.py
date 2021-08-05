# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 13:55:30 2021

@author: Omen 15
"""

L = []
for i in range(0, 15):
    L.append([0]*15)
    
NumComida = int(input("Ingrese cantidad de comida: "))
NumAgujeros = int(input("Ingrese cantidad de agujeros: "))

for comida in range(1, NumComida+1):   
    Sw = 1
    while Sw == 1:     
        Sw = 0
        print("Ingrese coordenadas (fila, columna) de comida ", comida)
        fC = int(input("Fila: "))
        cC = int(input("Columna: "))
        if (L[fC][cC] == 1) or (fC == 12 and cC == 0) or (fC == 0 and cC == 12) : 
            print("Error en coordenas, reingréselas")
            Sw = 1
        else: 
            L[fC][cC] = 1
        
print()
for Aguj in range(1, NumAgujeros+1):   
    print("Ingrese coordenadas (fila, columna) de agujero ", Aguj)
    fA = int(input("Fila: "))
    cA = int(input("Columna: "))
    while (L[fA][cA] == 1) or (L[fA][cA] == 2) or (fA == 12 and cA == 0) or (fA == 0 and cA == 12) : 
        print("Error en coordenas, reingréselas")
        fA = int(input("Fila: "))
        cA = int(input("Columna: "))
    L[fA][cA] = 2



    
input()
print([L])

print()
for i in range (0,15) : 
    for j in range (0, 15) : 
        print(str.rjust(str(L[i][j]), 4), end = "")
    print(); print()
input()
    
