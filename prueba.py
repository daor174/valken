# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 23:53:39 2021

@author: Omen 15
"""

import random
from colorama import init
init()
 
def pos(x,y):
    return "\033[" + str(x) + ";" + str(y) + "H"
 
def DIM_MATRIZ(Filas, Columnas):
    ARREGLO = []
    for i in range(0, Filas):
        ARREGLO.append([])
        for j in range(0, Columnas):
            ARREGLO[i].append(0)
    return ARREGLO
 
def mostrarTablero():
    global tablero
    print(pos(2,40) + "1  2  3  4  5  6")
    for fila in range(0,20):
        print(pos(fila+4, 35) + str(fila+1))
        for columna in range (0,6):
            print(pos(fila+4, columna*3+40) + str(tablero[fila][columna]))
 
def ingresocoord():
    filaCoor =int(input("INGRESE FILA: "))
    while (filaCoor < 1) or (filaCoor > 20):
        filaCoor = int(input("error porfavor reingrese fila entre 1 y 20: "))
 
    columnaCoor = int(input("INGRESE COLUMNA: "))
    while (columnaCoor < 1) or (columnaCoor > 6):
        columnaCoor = int(input("error porfavor reingrese datos entre 1 y 6: "))
    return filaCoor, columnaCoor
 
#def repeticion():
 
 
 
################### PROGRAMA PRINCIPAL #########################
# DIMENSIONAR LOS ARREGLOS TABLERO Y PIEZAS.
tablero = DIM_MATRIZ(20,6)
for fila in range(0,20):
    contador = 3
    while contador == 3:
        for columna in range(0,6):
            caracter = random.randint(1,6)
            if caracter ==6: tablero[fila][columna] = chr(9786)
            if caracter ==5: tablero[fila][columna] = chr(9787)
            if caracter ==4: tablero[fila][columna] = chr(9829)
            if caracter ==3: tablero[fila][columna] = chr(9827)
            if caracter ==2: tablero[fila][columna] = chr(9830)
            if caracter ==1: tablero[fila][columna] = chr(9824)
        numero   = tablero[fila][0]
        contador = 1
        columna  = 1
        while (columna < 6 and contador != 3):
            if tablero[fila][columna] == numero:
                contador = contador + 1
            else:
                numero = tablero[fila][columna]
                contador = 1
            columna = columna + 1
#repeticion()
mostrarTablero()
intentos = 1
while intentos < 20:
    ingresocoord()
