# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 19:01:40 2021

@author: Omen 15
"""
import math

N = int(input("ingrese el tope de la lista: "))

A = [0]
for i in range(0, 51) :
    A[i] = i
    A.append(0)
    
print(A)

A[1] = 0

#i = 4
#while i <= N :
#    A[i] = 0
#    i=+ 2

#i = 6
#while i <= N:
#    A[i] = 0
#    i =+ 3

K = 2
while K <= int(math.sqrt(N))  :
    i = 2*K
    while i <= N :
        A[i] = 0
        i = i + K
    K = K + 1
    
print(); print ("lista de numeros primos desde 1 hasta", N )
print()
for i in range(0, N):
    if  A[i] != 0:
        print(A[i])
    

              
input()              