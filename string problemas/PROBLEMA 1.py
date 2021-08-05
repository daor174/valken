# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 02:42:11 2021

@author: Omen 15
"""
''' 
Se pide realizar un programa en Python que lea dos Strings compuestos por palabras separadas por un espacio en blanco y ya ordenadas alfabéticamente, y que genere un tercer string (resultado) que contenga todas las palabras ordenadas.
 
Ejemplo:
 
String 1:  BANANA CASA LUNA MARQUESINA TORRE ZAPATO.
String 2:  ARENA FLOR GONDOLA LAPIZ NARANJA PLATANO VIVIENDA.

Resultado: ARENA BANANA CASA FLOR GONDOLA LAPIZ LUNA MARQUESINA NARANJA PLATANO TORRE VIVIENDA ZAPATO.


Observaciones:
-	Cada string está terminado en un punto y el string resultante debe terminar en punto (uno solo).
-	Las palabras tienen solo letras mayúsculas y no existen tildes (vocales acentuadas) ni la letra Ñ.
-	No es necesario utilizar arreglos (PERO PUEDEN USARSE).
-	Ayuda: El computador sabe que “LAPIZ” es menor que “LUNA”.
-	No utilizar función sort del Python.

'''

string1  = 'BANANA CASA LUNA MARQUESINA TORRE ZAPATO.'
string2 = 'ARENA FLOR GONDOLA LAPIZ NARANJA PLATANO VIVIENDA.'
string3 = ''
sw = True
#string1 = input('')
#string2 = input('')
while sw == True:
    
    stringIndice1 = string1.find(' ')
    stringIndice2 = string2.find(' ')
    
    if stringIndice1 == -1:
        
        if string1.find('.') != -1:
            palabra1 = string1[0: ]
            
    else:
        palabra1 = string1[0:stringIndice1]

    if stringIndice2 == -1:
        
        if string2.find('.') != -1:
            palabra2 = string2[0: ]
            
    else: 
        palabra2 = string2[0:stringIndice2]

    if palabra1.find('.') == -1 and palabra2.find('.') == -1:

        if palabra1 < palabra2:
            string3 = string3 + palabra1 + ' '
            string1 = string1[stringIndice1 + 1: ]
            
        else:
            string3 = string3 + palabra2 + ' '
            string2 = string2[stringIndice2 + 1: ]
  
    else:

        if palabra1.find('.') == -1:
            
            if palabra1 < palabra2:
                string3 = string3 + palabra1+ ' '
                string1 = string1[stringIndice1 + 1: ]
                
            else:
                string3 = string3 + palabra2[0:len(palabra2)-1] + ' '
                string2 = 'á.'
              
        else:
            
            if palabra2 < palabra1:
                string3 = string3 + palabra2 + ' '
                string2 = string2[stringIndice2 + 1: ]
                
            else:
                
                string3 = string3 + palabra1[0:len(palabra1)-1] + ' '
                string1 = 'á.'
  
    if palabra1.find('.') != -1 and palabra2.find('.') != -1:
        sw = False
        
print(string3)
input()