# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 20:25:50 2021

@author: Omen 15
"""
from random import randint
from colorama import init, Fore, Back
from os import system
system("cls")
init()

def generarMatriz():
    global matriz
    matriz = []
    for fil in range (11):
        matriz.append([])
        for col in range (11):
            matriz[fil].append(0)
            
            
def mostrarMatriz():
    global matriz, thomas_col, thomas_fil
    for i in range (11):
        print()
        for j in range (11):
            if i == thomas_fil and j == thomas_col :
                print('  T', end = '')
            else:
                print(' ',matriz[i][j], end = '')

      
input()        
print()    

