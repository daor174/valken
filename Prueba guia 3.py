# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 13:58:53 2021

@author: Omen 15
"""

import random
L = []
for i in range(0,13):
    L.append( [0]*13 )

NumCajones = int(input("Ingrese cantidad de cajones: "))
NumAgujeros = int(input("Ingrese cantidad de agujeros: "))

for Caj in range(1, NumCajones+1):   
    Sw = 1
    while Sw == 1:     
        Sw = 0
        print("Ingrese coordenadas (fila, columna) de cajón ", Caj)
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
    
     
    
print()
for i in range (0,13) : 
    for j in range (0, 13) : 
        print(str.rjust(str(L[i][j]), 4), end = "")
    print(); print()
input()


fR = 12; cR = 0     # Robot parte en coordenadaa  12, 0
Terminar = "No"; Tiempo = 0;  Carga = 250
while Terminar == "No" : 
    Tiempo = Tiempo + 1
    Sw = 0
    while Sw == 0 : 
    
        Dir = random.randint(1, 4)   # 1 = Arriba   2 = Derecha    3 = Abajo    4 = Izquierda. 

        if Dir == 1 and fR > 0 and L[fR-1][cR] != 1 : 
            fR = fR - 1; Sw = 1; Carga = Carga - 10
        
        if Dir == 2 and cR < 12 and L[fR][cR+1] != 1 :
            cR = cR + 1; Sw = 1; Carga = Carga - 10
        
        if Dir == 3 and fR < 12 and L[fR+1][cR] != 1 : 
            fR = fR + 1; Sw = 1; Carga = Carga - 10
        
        if Dir == 4 and cR > 0 and L[fR][cR-1] != 1 : 
            cR = cR - 1; Sw = 1; Carga = Carga - 10
        
    print("En tiempo ", Tiempo, "Robot queda en las coordenadas ", fR, cR)
    if Carga <= 0 : 
        Terminar = "Sí"
        print("El robot quedó sin carga en tiempo ", Tiempo)
    if fR == 0 and cR == 12 : 
        Terminar = "Sí" 
        print("Robot llegó a la meta")
    if L[fR][cR] == 2 : 
        Terminar = "Sí"
        print("Robot cae en un agujero en tiempo ", Tiempo)

input()

