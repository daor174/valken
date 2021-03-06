# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 17:27:46 2021

@author: Inso

0 = vacio 
1 = muralla (no avanza)
2 = foso (muere)
3 = lugar de partida 
5 = lugar de escape 

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

def regenerarLaberinto():
    global thomas_col, thomas_fil, matriz
    generarMatriz()
    
    matriz[10][0] = 3
    matriz[5][5] = 5
    
    murallas = 0
    while murallas < 50:
        muralla_fil = randint(0,10)
        muralla_col = randint(0,10)
        if  matriz[muralla_fil][muralla_col] != 3 and matriz[muralla_fil][muralla_col] != 5 and matriz[muralla_fil][muralla_col] != 1:
            matriz[muralla_fil][muralla_col] = 1
            murallas += 1
    
    fosos = 0
    
    while fosos < 8:
        foso_fil = randint(0,10)
        foso_col = randint(0,10)
        if matriz[foso_fil][foso_col] != 3 and matriz[foso_fil][foso_col] != 5 and matriz[foso_fil][foso_col] != 1 and matriz[foso_fil][foso_col] != 2:
            matriz[foso_fil][foso_col] = 2
            fosos += 1


def movimientoThomas():
    global thomas_col, thomas_fil, matriz
    sw = True
    razon = ''
    """
    mov = 0 derecha
    mov = 1 izquierda
    mov = 2 arriba
    mov = 3 abajo
    """
    movimiento = randint(0,3)
    if movimiento == 0 and matriz[thomas_fil][thomas_col + 1] != 1 and (thomas_col + 1) != 11 :
        if matriz[thomas_fil][thomas_col + 1] == 2:
            sw = False
            razon = 'Cae en un foso'
            thomas_col += 1
        elif matriz[thomas_fil][thomas_col + 1] == 5:
            sw = False
            razon = 'Lleg?? a la meta'
            thomas_col += 1
        else:
            thomas_col += 1
    
    if movimiento == 1 and matriz[thomas_fil][thomas_col - 1] != 1 and (thomas_col - 1) != -1:
        if matriz[thomas_fil][thomas_col - 1] == 2:
            sw = False 
            razon = 'Cae en un foso'
            thomas_col -= 1
        elif matriz[thomas_fil][thomas_col -1] == 5:
            sw = False
            razon = 'Lleg?? a la meta'
            thomas_col -= 1
        else:
            thomas_col -= 1
            
    if movimiento == 2 and matriz[thomas_fil - 1][thomas_col] != 1 and (thomas_fil - 1) != -1:
        if matriz[thomas_fil - 1][thomas_col] == 2:
            sw = False
            razon = 'Cae a un foso'
            thomas_fil -= 1
        elif matriz[thomas_fil - 1][thomas_col] == 5:
            sw = False
            razon = 'Lleg?? a la meta'
            thomas_fil -= 1
        else:
            thomas_fil -= 1
    
    if movimiento == 3  and (thomas_fil + 1) != 11:
        if matriz[thomas_fil + 1][thomas_col] != 1:
            
            if matriz[thomas_fil + 1][thomas_col] == 2:
                sw = False
                razon = 'Cae a un foso'
                thomas_fil += 1
            elif matriz[thomas_fil + 1][thomas_col] == 5:
                sw = False
                razon = 'Lleg?? a la meta'
                thomas_fil += 1
            else:
                thomas_fil += 1
            
    return sw,razon

def movimientoLaberinto():
    global matriz
    regenerarLaberinto()
    print('\tMatriz generada')
    mostrarMatriz()
    input()
    sw = True
    while sw == True:
        segundos = 0 ;
        print()
        print('\tSe regenera laverinto')
        regenerarLaberinto()
        system("cls")
        mostrarMatriz()
        input()
        while segundos < 10:
            
            print()
            print('\t Movimiento en matriz ',segundos+1)
            sw,razon = movimientoThomas()
            system("cls")
            mostrarMatriz()
            input()
            if sw == False:
                segundos = 10
            segundos += 1
        input()
    return razon

#####################################PROGRAMA PRINCIPAL###########################################

thomas_col = 0
thomas_fil = 10
print(movimientoLaberinto())
input()