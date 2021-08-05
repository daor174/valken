# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 06:16:33 2021

@author: Omen 15
"""

P = []

for i in range(0,13):
    P.append( [0]*13 )
    
NumCajones = int(input("ingrese la cantidad de cajones : "))
NumAgujeros = int(input("ingrese la cantidad de agujeros : "))

    
    
    
for cajon in range(1, NumCajones+1):
    Sw = 1
    while Sw == 1:
        Sw = 0
        print("ingrese la fila y columna de cajones", cajon)
        FilaCajon = int(input("fila:"))
        ColumnaCajon = int(input("columna:"))
        
        if (P[FilaCajon][ColumnaCajon] == 1) or (FilaCajon == 12 and ColumnaCajon == 0) or (FilaCajon == 0 and ColumnaCajon == 12):
            print("error de cordenadas reingreselas")
            Sw = 1
        else: 
            P[FilaCajon][ColumnaCajon] = 1
print()            
            
for agujero in range(1, NumAgujeros+1):
    print("ingrese la fila y columna del agujero", agujero)
    AgujFil = int(input("fila"))
    AgujCol = int(input("columna"))
    while (P[AgujFil][AgujCol] == 1) or (AgujFil == 12 and AgujCol == 0) or (AgujFil == 0 and AgujCol == 12):
        print("error de cordenadas reingreselas")
        AgujFil = int(input("fila"))
        AgujCol = int(input("columna"))
            
        P[AgujFil][AgujCol] = 2
        








print()
for i in range (0,13) : 
    for j in range (0, 13) : 
        print(str.rjust(str(P[i][j]), 4), end = "")
    print(); print()
input()            