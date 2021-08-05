# -*- coding: utf-8 -*-
import random

import os
os.system ('cls')

from colorama import init
init()

Estatafador = 'E'
Agente = 'A'
ColAgente = 0
FilAgente = 0
ColEstafador = 0
FilEstafador = 0
Tiempo = 0
SW = 0
cont_pasos_E = 0
cont_pasos_A = 0
def pos(x,y):
    print("\033[" + str(x) + ";" + str(y) + "H", sep="", end ="")
    return None
while SW == 0 :
    SW = 1 
    ColAgente = random.randint(1, 20); FilAgente = random.randint(1, 20)
    ColEstafador = random.randint(1, 20) ; FilEstafador = random.randint(1, 20)
    if FilAgente == FilEstafador - 2 and ColAgente == ColEstafador :
        SW = 1
        if FilAgente == FilEstafador and ColAgente == ColEstafador - 2 :
            SW = 1
            if FilAgente == FilEstafador + 2 and ColAgente == ColEstafador :
                SW = 1
                if FilAgente == FilEstafador and ColAgente == ColEstafador + 2 :
                    SW = 1
                    if FilAgente == FilEstafador and ColAgente == ColEstafador :
                        SW = 1
input ()
########################## M O V I E N T O S #########################
print ("Ha comenzado: Atrapame Si Puedes")
input ()
os.system ('cls')
while Tiempo < 70:
    mov = random.randint(1, 2) 
    # Random para determinar quien se mueve
    # 1 = Estafador
    # 2 = Agente
    if mov == 1:
        
        pos (21,21) ; print ("Estafador se comienza a mover")
        cont_pasos_E = cont_pasos_E + 1
        Tiempo = Tiempo + 1
        
        #Casos de movimientos Rectos
        #OESTE            
        if FilEstafador == FilAgente and ColEstafador < ColAgente:
            ColEstafador = ColEstafador - 1 
        #ESTE    
        if ColEstafador > ColAgente and FilEstafador == FilAgente:
            ColEstafador = ColEstafador + 1
        #NORTE
        if FilEstafador < FilAgente and ColEstafador == ColAgente:
            FilEstafador = FilEstafador - 1
        #SUR    
        if FilEstafador > FilAgente and ColEstafador == ColAgente:
            FilEstafador = FilEstafador + 1
        # Casos movimiento Diagonales 
        #SurOeste:
        if ColEstafador < ColAgente and FilEstafador > ColAgente:
            ColEstafador = ColEstafador - 1
            FilEstafador = FilEstafador + 1
        #SurEste:
        if ColEstafador > ColAgente and FilEstafador > ColAgente:
            ColEstafador = ColEstafador + 1
            FilEstafador = FilEstafador + 1
        #NorEste:
        if ColEstafador > ColAgente and FilEstafador < ColAgente:
            ColEstafador = ColEstafador + 1
            FilEstafador = FilEstafador - 1
        #NorOeste:
        if ColEstafador < ColAgente and FilEstafador < ColAgente:
            ColEstafador = ColEstafador - 1
            FilEstafador = FilEstafador - 1
        if ColEstafador > 20 or ColEstafador < 1:
            ColEstafador  = random.randint(1, 20) ; FilEstafador  = random.randint(1, 20)
        if FilEstafador > 20 or FilEstafador < 1:
            FilEstafador  = random.randint(1, 20) ; ColEstafador  = random.randint(1, 20)
        # Caso en que se sale de los parametros 
        pos (21,21) ; print("La persecución tuvo una duración de: ", Tiempo, "segundos.")
        pos (21,21) ; print("Cantidad de pasos del estafador: ", cont_pasos_E)
        pos(ColEstafador, FilEstafador); print("E")        
        pos(ColAgente, FilAgente); print("A")
        input()
        os.system('cls')
       
    if mov == 2 : 
        pos (21,21) ; print ("Agente se comienza a mover")
        cont_pasos_A = cont_pasos_A + 1
        Tiempo = Tiempo + 1
        # El turno de movimiento es para el AGENTE
        # Casos de movimientos Rectos
        #ESTE        
        if ColAgente < ColEstafador and FilAgente == FilEstafador:
            ColAgente = ColAgente + 1
        #OESTE    
        if ColAgente > ColEstafador and FilAgente == FilEstafador:
            ColAgente = ColAgente - 1
        #SUR   
        if FilAgente < FilEstafador and ColAgente == ColEstafador:
            FilAgente = FilAgente + 1
        #NORTE
        if FilAgente > FilEstafador and ColAgente == ColEstafador:
            FilAgente = FilAgente - 1
        # Casos de movimientos Diagonales
        #SurOeste:
        if ColAgente > ColEstafador and FilAgente < FilEstafador:
            ColAgente = ColAgente - 1
            FilAgente = FilAgente + 1
        #SurEste:
        if ColAgente < ColEstafador and FilAgente < FilEstafador:
            ColAgente = ColAgente + 1
            FilAgente = FilAgente + 1
        #NorEste:
        if ColAgente < ColEstafador and FilAgente > FilEstafador:
            ColAgente = ColAgente + 1
            FilAgente = FilAgente - 1
        #NorOeste:
        if ColAgente > ColEstafador and FilAgente > FilEstafador:
            ColAgente = ColAgente - 1
            FilAgente = FilAgente - 1 
        pos (21,21); print("La persecución tuvo una duración de: ", Tiempo, "segundos.")
        pos (21,21) ; print("Cantidad de pasos del agente: ", cont_pasos_A)
        
        pos(ColEstafador, FilEstafador); print("E")
        pos(ColAgente, FilAgente); print("A")
        input()
        os.system('cls')

if Tiempo == 70:                      
#Parametros de Agente
#Agente = ColAgente + FilAgente 
    if ColAgente > 20:
        ColAgente = 1
        if FilAgente > 20:
            FilAgente = 1
            if FilAgente < 1:
                FilAgente = 20
                if ColAgente < 1:
                    ColAgente = 20   
        #presentar en pantalla
#print (ColAgente, FilAgente)       
#print (ColEstafador, FilEstafador)
#print (Tiempo)
    if FilAgente == FilEstafador and ColAgente == ColEstafador :
        print ("El Agente logro atrapar al estafador")
        input()
    if FilAgente != FilEstafador and ColAgente != ColEstafador:       
        print ("El estafador ha logrado escapar")
        input ()    