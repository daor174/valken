# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 17:03:48 2021

@author: Omen 15
"""
'''
Se pide realizar un programa Python que lea 3 datos (tipo string): 1 palabra clave, 2 frases. 

Los 3 strings leídos contienen un verso disfrazado (hay que descubrir ese verso). 
 
El primer string  (palabra clave) es una palabra de menos de 10 letras, terminado por un punto. 
El segundo y tercer strings son una frase compuesta por palabras (separadas por 1 espacio en blanco) y terminada por un punto. Las frases formarán el verso y contienen palabras que están de más. 
 
El programa debe hacer lo siguiente: 
-	Leer los 3 strings. x         
-	Mostrar las dos frases sin la palabra clave. 
-	Componer el verso, partiendo con palabras de la primera frase y cambiando entre frases la secuencia cada vez que se encuentre la palabra clave. Mostrar cómo queda el verso. 
-	Quitar palabras que tengan más de 10 letras. Mostrar cómo queda el verso.       
-	Finalmente, indicar cuantas palabras tiene el verso.     
-	El ejemplo que está a continuación ilustra lo que se pide, pero el programa debe funcionar también con otros datos. 


Ejemplo: 


Strings a leer: 

OCTUBRE. 
ME GUSTAS CUANDO OCTUBRE ESTAS OCTUBRE ME ESPECTACULAR OYES OCTUBRE.
CALLAS PORQUE OCTUBRE COMO PRINCIPALMENTE AUSENTE Y OCTUBRE DESDE LEJOS.

Resultados: 

ME GUSTAS CUANDO ESTAS ME ESPECTACULAR OYES. 
CALLAS PORQUE COMO PRINCIPALMENTE AUSENTE Y DESDE LEJOS. 
 
ME GUSTAS CUANDO CALLAS PORQUE ESTAS COMO PRINCIPALMENTE AUSENTE Y ME ESPECTACULAR OYES DESDE LEJOS.
 
ME GUSTAS CUANDO CALLAS PORQUE ESTAS COMO AUSENTE Y ME OYES DESDE LEJOS. 

13 palabras. 


Observaciones:
-	Las palabras tienen solo letras mayúsculas y no existen tildes (vocales acentuadas) ni la letra Ñ.

'''

print('   PROBLEMA 3   ');print()
palabraClave = 'OCTUBRE.'
frase1 = 'ME GUSTAS CUANDO OCTUBRE ESTAS OCTUBRE ME ESPECTACULAR OYES OCTUBRE.'
frase2 = 'CALLAS PORQUE OCTUBRE COMO PRINCIPALMENTE AUSENTE Y OCTUBRE DESDE LEJOS.'
frase1list = frase1.split(' ')
frase2list = frase2.split(' ')
frase1new = []
frase2new = []
frase3 = []
frase4 = []

frase1list[-1] = frase1list[-1][0:len(frase1list[-1])-1] #quitandopunto
frase2list[-1] = frase2list[-1][0:len(frase2list[-1])-1] #quitandopunto
palabraClave = palabraClave[0:len(palabraClave)-1]       #quitandopunto

#Quitamos los octubres
for i in range (len(frase1list)):
    
    if frase1list[i] != palabraClave:
        frase1new.append(frase1list[i])

for i in range (len(frase2list)):
    
    if frase2list[i] != palabraClave:
        frase2new.append(frase2list[i])

#Imprimimos con un punto al final
for i in range(len(frase1new)):
    if i == len(frase1new) - 1:
        print(frase1new[i] , end = '.')
        print()
    else:
        print(frase1new[i] , end = ' ')

for i in range(len(frase2new)):
    if i == len(frase2new) - 1:
        print(frase2new[i] , end = '.')
        print()
    else:
        print(frase2new[i] , end = ' ')

#Componer verso
sw = True; cont1 = 0 ; cont2 = 0

while sw == True:
    
    sw1 = True; sw2 = True
    
    while sw1 == True and cont1 < len(frase1list):
        
        if frase1list[cont1] == palabraClave:
            sw1 = False
        else:
            frase3.append(frase1list[cont1])
            
        cont1 += 1
        
    while sw2 == True and cont2 < len(frase1list):
        
        if frase2list[cont2] == palabraClave:
            sw2 = False
        else:
            frase3.append(frase2list[cont2])
        cont2 += 1
        
    if cont1 == len(frase1list) and cont2 == len(frase2list):
        sw = False
    
#Imprimir verso
for i in range(len(frase3)):
    
    if i == len(frase3) - 1:
        print(frase3[i] , end = '.')
        print()
    else:
        print(frase3[i] , end = ' ')

#Identificar palabras que tengan 10 o mas letras
cont = 0
for i in range(len(frase3)):
    if len(frase3[i]) < 10:
        frase4.append(frase3[i])

#Imprimir verso sin esas palabras y punto al final

for i in range(len(frase4)):
    
    if i == len(frase4) - 1:
        print(frase4[i] , end = '.')
        print()
    else:
        print(frase4[i] , end = ' ')

#Mostrar cuantas palabras tiene el verso

print( len(frase4),' palabras.')
    
input()