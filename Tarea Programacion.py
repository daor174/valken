# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 18:02:13 2021

@author: Omen 15
"""

import random
import os
os.system ('cls')

Estatafador = 'E'
Agente = 'A'
ColAgente = 0
FilAgente = 0
ColEstafador = 0
FilEstafador = 0
Tiempo = 0
SW = 1
ColAgente = random.randint(1, 20); FilAgente = random.randint(1, 20)
FilEstafador = random.randint(1, 20); ColEstafador = random.randint(1, 20)
while SW == 1 :
    c = ColAgente
    f = FilAgente
    if FilAgente == FilEstafador - 2 and ColAgente == ColEstafador :
        SW = 1
    if FilAgente == FilEstafador and ColAgente == ColEstafador - 2 :
        SW = 1
    if FilAgente == FilEstafador + 2 and ColAgente == ColEstafador :
        SW = 1
    if FilAgente == FilEstafador and ColAgente == ColEstafador + 2 :
        SW = 1
    if FilAgente == FilEstafador and ColAgente == ColEstafador :
        SW = 0

if ColAgente > 20 :
        
else :
    Agente = FilAgente == 1
if ColEstafador > 20 and FilEstafador > 20 :
    ColEstafador = random.randint(1,20)
    FilEstafador = random.randint(1,20)

while Tiempo <= 70 :
    m = random.randint(A,E)
    if m == A :
      if ColEstafador != ColAgente :
          ColAgente = ColAgente + 1
    print() 
    while A > 20 :
        if FilAgente = 1 and ColAgente = 21:
            FilAgente = 1 and ColAgente = 1
            if FilAgente = 2 and ColAgente = 21:
                filAgente = 2 and ColAgente = 1
                if filAgente = 3 and ColAgente = 21:
                    filAgente = 3 and ColAgente = 1
                    if filAgente = 4 and ColAgente = 21:
                        filAgente = 4 and ColAgente = 1
                        if filAgente = 5 and ColAgente = 21:
                            filAgente = 5 and ColAgente = 1
                            if filAgente = 6 and ColAgente = 21:
                                filAgente = 6 and ColAgente = 1
                                if filAgente = 7 and ColAgente = 21:
                                    filAgente = 7 and ColAgente = 1
                                    if filAgente = 8 and ColAgente = 21:
                                        filAgente = 8 and ColAgente = 1
                                        if filAgente = 9 and ColAgente = 21:
                                            filAgente = 9 and ColAgente = 1
                                            if filAgente = 10 and ColAgente = 21:
                                                filAgente = 10 and ColAgente = 1
                                                if filAgente = 11 and ColAgente 21:
                                                    filAgente = 11 and ColAgente 1
                                                    if filAgente = 12 and ColAgente = 21:
                                                        filAgente = 12 and ColAgente = 1
                                                        if filAgente = 13 and ColAgente = 21:
                                                            filAgente = 13 and ColAgente = 1
                                                            if filAgente = 14 and ColAgente = 21:
                                                                filAgente = 14 and ColAgente = 1
                                                                if filAgente = 15 and ColAgente = 21:
                                                                    filAgente = 15 and ColAgente = 1
                                                                    if filAgente = 16 and ColAgente = 21:
                                                                        filAgente = 16 and ColAgente = 1
                                                                        if filAgente = 17 and ColAgente = 21:
                                                                            filAgente = 17 and ColAgente = 1
                                                                            if filAgente = 18 and ColAgente = 21:
                                                                                filAgente = 18 and ColAgente = 1
                                                                                if filAgente = 19 and ColAgente = 21:
                                                                                    filAgente = 19 and ColAgente = 1
                                                                                    if filAgente = 20 and ColAgente = 21:
                                                                                        filAgente = 20 and ColAgente = 1
                                                                                        else:
                                                                                            no se que wea jaja XD
                    

    Tiempo = Tiempo + 1


print('A transcurrido: ', Tiempo, 'segundos')