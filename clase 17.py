# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 14:45:45 2021
Problema de Alberto y Benito
@author: dagob
"""
A = [0];  B = [0]
N1 = int(input("Ingrese cantidad de datos que anotó Alberto: "))
N2 = int(input("Ingrese cantidad de datos que anotó Benito: "))

i = 0
while i < N1 : 
    A[i] = int(input("Ingrese dato anotado por Alberto: "))
    i = i + 1
    A.append(0)
    
for i in range(0, N2): 
    B[i] = int(input("Ingrese dato anotado por Benito: "))
    B.append(0)
i = 0
while i < N2:
    j = 0
    while j < N1 :
        if A[j] == B[i] :
            B[i] = 0
            
            
        j = j + 1
    
    
    
    i= i + 1
print(); print ("listado de articulos obsoletos que estan en bodega")
for i in range(0, N1):
    print(A[i])
for i in range (0, N2):
    if B[i] != 0:
       print(B[i])
    
          