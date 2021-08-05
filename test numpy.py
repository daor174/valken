# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 18:35:58 2021

@author: Omen 15
"""
import numpy as np

def llenarmatriz(filas, columnas):
    M=np.random.randint(0,1,(filas,columnas))
    return M

def asientoportipo(mtren):
    mBool=mtren==0
    

mat=llenarmatriz(14,14)


print(mat)
input()
