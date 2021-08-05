# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 13:57:24 2021

@author: Omen 15
"""

import random
P = []
for i in range(0,10):
    P.append( [0]*10 )

for f in range (0, 10):   # Se puede evitar líneas 11 a 13, simplemente poniendo un 1 en lugar de 0 en línea 9. 
    for c in range (0, 10): 
        P[f][c] = 1

print()
for i in range (0,10) : 
    for j in range (0, 10) : 
        print(str.rjust(str(P[i][j]), 4), end = "")
    print(); print()
input()

misil = 1
while misil <= 10 : 
    fM = random.randint(0,9)
    cM = random.randint(0,9)
    P[fM][cM] = 0    
    if fM > 0 and cM > 0    :   P[fM-1][cM-1] = 0
    if fM > 0               :   P[fM-1][cM]   = 0
    if fM > 0 and cM < 9    :   P[fM-1][cM+1] = 0
    if cM < 9               :   P[fM][cM+1]   = 0
    if fM < 9 and cM < 9    :   P[fM+1][cM+1] = 0
    if fM < 9               :   P[fM+1][cM]   = 0
    if fM < 9 and cM > 0    :   P[fM+1][cM-1] = 0
    if cM > 0               :   P[fM][cM-1]   = 0    
    misil = misil + 1
    print()
    for i in range (0,10) : 
        for j in range (0, 10) : 
            print(str.rjust(str(P[i][j]), 4), end = "")
        print(); print()
    input()   

# Completar desde aquí...

fNave = random.randint(0, 9) 
cNave = random.randint(0, 9)
print(); print("la nave cayó en coordenadas ", fNave, cNave)
if P[fNave][cNave] == 1 : 
    print("La nave es destruida")
    VidaNave = 0
    P[fNave][cNave] = 0
else: 
    VidaNave = 1

Terminar = "No"    
fR = random.randint(0, 9)
cR = random.randint(0, 9)
print("El robot cae en las coordenadas ", fR, cR)
if fR == fNave and cR == cNave : 
    print("Mensaje hacia Tierra: Se encontró la nave en las coordenadas ", fNave, cNave)
    if VidaNave == 0:    print("Está destruida")
    else :               print("Está bien")
    Terminar = "Sí"

Tiempo = 0; Carga = 120    
while Terminar == "No" : 
    Dir = random.randint(1, 4)    # 1= Arriba  2=Derecha    3=Abajo   4=Izquierda
    Tiempo = Tiempo + 1
    
    if Dir == 1 and fR > 0 and P[fR-1][cR] == 0 : 
        fR = fR - 1
        Carga = Carga - 1
        
    if Dir == 2 and cR < 9 and P[fR][cR+1] == 0 : 
        cR = cR + 1
        Carga = Carga - 1
         
    if Dir == 3 and fR < 9 and P[fR+1][cR] == 0 : 
        fR = fR + 1
        Carga = Carga - 1
         
    if Dir == 4 and cR > 0 and P[fR][cR-1] == 0 : 
        cR = cR - 1
        Carga = Carga - 1
    
    print(); print("El robot queda en coordenadas ", fR, cR)
    
    for i in range (0,10) : 
        for j in range (0, 10) : 
            if i == fR and j == cR : 
                print(str.rjust("*", 4), end = "")
            else: 
                print(str.rjust(str(P[i][j]), 4), end = "")
        print(); print()   
    
    if Carga == 0 or (fR == fNave and cR == cNave) or Tiempo == 180 :
        Terminar = "Sí"
     
if Tiempo == 180 : 
    print("Se acabó el tiempo de 3 horas")
if fR == fNave and cR == cNave : 
        print("El robot llegó a la nave en ", Tiempo, " minutos")
if Carga == 0 :  
        print("Robot se quedó sin carga en coordenadas ", fR, cR)

print()
for i in range (0,10) : 
    for j in range (0, 10) : 
        print(str.rjust(str(P[i][j]), 4), end = "")
    print(); print()    

input()