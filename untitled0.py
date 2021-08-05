# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 16:56:20 2021
Programa que resuelve problema de viajes en bote (192-A)
@author: dagob
"""
N = int(input("Ingrese cantidad de personas: "))
NOM = ["***"];    PE = [0]
i = 0
while i < N : 
    print("Ingrese datos de persona ", i+1)
    NOM[i] = input("Nombre: ")
    PE[i] = int(input("Peso: "))
    i = i + 1
    NOM.append("***")
    PE.append(0)

print()
Viaje = 1; Sw = 0; j = 0

while  Sw == 0 : 
    print(); print("Lista de pasajeros en viaje ", Viaje)
    
    SumaPesos = 0; CantPersonas = 0
    while SumaPesos <= 300 and j < N : CantPersonas < 5
        SumaPesos = SumaPesos + PE[j]
        if SumaPesos <= 300 and CantPersonas <= 5 : 
            print(NOM[j])
            j = j +1
            CantPersonas = cantPersonas + 1
    
    Viaje = Viaje + 1
    if j == N :
        Sw = 1

    

        
print(); input("FIN DEL PROGRAMA")
 