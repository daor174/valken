# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 15:09:12 2021

@author: Omen 15
"""
### Daniel Rozas Ralil Paralelo 192 - A
### En la primera parte va el movimiento en el cual los numero son: #1 abajo izquierda; 2abajo ; 3 abajo derecha
###Despues se selecciona el numero de agujeros y resortes para seleccionarlos manualmente en la matriz con su respectivo puntaje
### A continuacion se coloco lo teletransporte negando la ida de uno al otro para que no caiga en un bucle
### Finalmente puse la comida con los cajones aleatoriamente con la comida en su valor al azar
### Profesor dagoberto en la fila 75 no se cual es el error pero me habria gustado probar el problema o quizas si es que tiraba el movimiento al final podria funcionar
###pero esta todo lo que pidio creo, no se si se me paso algo
#muchas gracias




import random
P = []
for i in range(0,21):
    P.append( [0]*10 )
    
print()
for i in range (0,21) : 
    for j in range (0, 10) : 
        print(str.rjust(str(P[i][j]), 4), end = "")
    print(); print()
input()
comidavalor = random.randint(5, 10)
Tiempo = 1000
FB = random.randint(0, 9)     
CB = 0
BPuntos = 0
Terminar = "No"
while Terminar == "No" :
    Dir = random.randint(1, 3) 
    if Dir ==  1 and (FB > 0)  and  (FB < 21) :
         FB = FB - 1 ; CB = CB + 1
    tiempo = tiempo - 1             
    if Dir == 2 and ( CB < 21) :
         CB = CB + 1
    tiempo = tiempo - 1
    if Dir == 3  and (CB < 21) and (FB < 9) :
         FB = FB + 1 ; CB = CB + 1
    tiempo = tiempo - 1     
    print(); print("la bola queda en coordenadas ", FB, CB)
    
NumAgujeros = int(input("Ingrese cantidad de agujeros: "))
Numresortes = int(input("Ingrese cantidad de resortes: "))

for Aguj in range(1, NumAgujeros+1):   
    print("Ingrese coordenadas (fila, columna) de agujero ", Aguj)
    FA = int(input("Fila: "))
    CA = int(input("Columna: "))
    while (P[FA][CA] == -1) or (P[FA][CA] == -2) or (P[FA][CA] == -3):
        print("Error en coordenas, reingréselas")
        FA = int(input("Fila: "))
        CA = int(input("Columna: "))
        
    if FA == FB and CA == CB :
        BPunto = BPunto + 200
        Termina = "Si"
        
        
    P[FA][CA] = -1    
        
for spring in range(1, Numresortes+1):   
    print("Ingrese coordenadas (fila, columna) de agujero ", spring)
    FR = int(input("Fila: "))
    CR = int(input("Columna: "))
    while (P[FR][CR] == -2) or (P[FR][CR] == -1):
        print("Error en coordenas, reingréselas")
        FR = int(input("Fila: "))
        CR = int(input("Columna: "))
    if FR == FB and CR == CB :
        FB = random.randint(0,9) and CB = random.randint(0, 21) and (CB > CR)
        BPunto = BPuntos + 30
        
        
        
    P[FR][CR] = -2

 
       
for Tele in range(1, 2):
    print("Ingrese coordenadas (fila, columna) del primer Teletransporte ", Tele)
    FT1 = int(input("Fila: "))
    CT1 = int(input("Columna: "))
    print("Ingrese coordenadas (fila, columna) del segundo Teletransporte ", Tele)
    FT2 = int(input("Fila: "))
    FT2 = int(input("Columna: "))
    if FT1 == FB and CT1 == CB:
        P[FB][CB] = P[FT2][FC2] and not P[FT1][CT1]
        BPuntos = BPuntos + 150
    if FT2 == FB and FC2 == CB:
        P[FB][CB] = [FT1][CT1] and not P[FT2][FC2]
        BPuntos = BPuntos + 150
        
        




     
    P[FT1][CT1] = -3
    P[FT2][CT2] = -3
    
for comida in range(0,20) : 
    FComida = random.randint(1,9)
    CComida = random.randint(0,21)
    if FB == FComida and CB == CComida:
        P[Fcomida][CComida] = 0
    
    
    P[FComida][CComida] = comidavalor
    
    
print("En tiempo ", Tiempo, "La bola queda en las coordenadas ", FB, CB) 
print("el puntaje obtenido es" , BPuntos)      


print()
for i in range (0,21) : 
    for j in range (0, 10) : 
        print(str.rjust(str(P[i][j]), 4), end = "")
    print(); print()
input()