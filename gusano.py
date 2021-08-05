# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 14:54:58 2021

@author: Omen 15
"""
import random
M = []
for i in range(0,15):
    M.append( [0]*15 )

CantAgujeros = int(input("Ingrese cantidad de agujeros: "))
CantComidas = int(input("Ingrese cantidad de comidas: "))
for i in range(1, CantAgujeros+1) : 
    print("Ingrese ubicación del agujero ", i)
    fila = int(input("Fila: "))
    col = int(input("Columna: "))
    M[fila][col] = -1
for i in range(1, CantComidas+1) : 
    print("Ingrese ubicación y cantidad de la comida ", i)
    fila = int(input("Fila: "))
    col = int(input("Columna: "))
    Cant = int(input("Cantidad: "))
    M[fila][col] = Cant
    
tiempo = 0; fG1 = 0; cG1 = 0; Gord1 = 1; fG2 = 0; cG2 = 14; Gord2 = 1; Vida1 = 1; Vida2 = 1

Terminar = "No"    ; Gusano = 1

while Terminar == "No" :    
    print(Gusano)

    tiempo = tiempo + 1
    Dir = random.randint(1, 4)  # 1: Arriba,  2: Derecha,  3: Abajo,   4: Izquierda
    if Gusano == 1 : 
        if Dir == 1 and fG1 > 0 : 
            fG1 = fG1 - 1
            if fG1 == fG2 and cG1 == cG2 and Gord1 <= Gord2 : 
                fG1 = fG1 + 1    
        if Dir == 2 and cG1 < 14 : 
            cG1 = cG1 + 1
            if fG1 == fG2 and cG1 == cG2 and Gord1 <= Gord2 : 
                cG1 = cG1 - 1
        if Dir == 3 and fG1 < 14 : 
            fG1 = fG1 + 1
            if fG1 == fG2 and cG1 == cG2 and Gord1 <= Gord2 : 
                fG1 = fG1 - 1    
        if Dir == 4 and cG1 > 0 : 
            cG1 = cG1 - 1
            if fG1 == fG2 and cG1 == cG2 and Gord1 <= Gord2 : 
                cG1 = cG1 + 1
        print("El gusano 1 quedó en coordenadas ", fG1, cG1)
        if M[fG1][cG1] == -1 : 
            Vida1 = 0
            print("Falleció el gusano 1")
        if fG1 == fG2 and cG1 == cG2 and Gord1 > Gord2 : 
            Vida2 = 0; Gord1 = Gord1 + Gord2
            print("Falleció el gusano 2")
        if M[fG1][cG1] > 0 : 
            Comida = M[fG1][cG1]
            if Comida > 5 : 
                Comida = 5
            Gord1 = Gord1 + Comida
            M[fG1][cG1] = M[fG1][cG1] - Comida
        
        
    if Gusano == 2 : 
        pass   # Completar
        
        
        
        
        
        
        
    if Gusano == 1 : 
        Gusano = 2
    else: 
        Gusano = 1
    
    if Vida1 == 0 and Vida2 == 0 : 
        Terminar = "Sí"
    
print("Tiempo transcurrido en segundos = ", tiempo)    
input()