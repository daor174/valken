# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 01:36:39 2021

@author: Omen 15
"""
'''
Se pide realizar un programa en  PYTHON  que lea un String (de menos de 80 caracteres) que contiene palabras (sólo letras mayúsculas, sin la letra Ñ y sin vocales con tilde), 
además de otros caracteres ( , . ; : ( ) = + - $   ) (coma, punto, punto y coma, dos puntos, paréntesis, igual, más, guión, peso, espacio en blanco). 
Se pide obtener los siguientes resultados:
a)	String resultante si se anotan todas las palabras, en el mismo orden que están. Las palabras deben ir separadas por un espacio en blanco entre ellas y la línea debe terminar con un punto.
b)	Lista de palabras separadas (hacia abajo), ordenadas por largo de palabras (menor a mayor).
c)	Misma lista de palabras, pero en que cada palabra esté una sola vez.
d)	Cómo queda el string resultante (caso a) si se omiten las palabras repetidas.


Ejemplo:
 
String a leer: 
+(ESTE$+ES= EL-STRING++QUE;--:DEBE(SER)=DESCUBIERTO-ES=TODO$LO)QUE,ES

 
String resultante (a): 
ESTE ES EL STRING QUE DEBE SER DESCUBIERTO ES TODO LO QUE ES.
 
Lista de palabras (b):             
ES						
EL						
ES						
LO						
ES						
QUE						
QUE						
SER						
ESTE						
DEBE						
TODO
STRING
DESCUBIERTO

Lista de palabras (c):
ES
EL
LO
QUE
SER
ESTE
DEBE
TODO
STRING
DESCUBIERTO

String resultante sin palabras repetidas (d): 
ESTE ES EL STRING QUE DEBE SER DESCUBIERTO TODO LO.

'''
print();print('   PROBLEMA 2   ');print()
string     = '+(ESTE$+ES= EL-STRING++QUE;--:DEBE(SER)=DESCUBIERTO-ES=TODO$LO)QUE,ES'
caracteres = ' , . ; : ( ) = + - $   '
# a) 
# Quitar caracteres raros
string2 = '' ; cont = 0
while cont < len(string):
    
    if string[cont] in caracteres:
        pass
    
    else:
        if string[cont-1] in caracteres:
            string2 = string2 + ' '
        
        string2 = string2 + string[cont]
        
    cont += 1

# De haber un espacio al comienzo quitarlo
if string2[0] == ' ':
    string2 = string2[1 : ]

# Imprimir con un punto al final
print(string2 + '.')

# b) con split

string2 = string2.split(' ')
sw = True;cont = 1

# Buscar palabra mas grande
mayor = 0
for i in range(len(string2)):
    if len(string2[i]) > mayor:
        mayor = len(string2[i])
        

# Imprimir en orden de tamaño
print()
while cont <= mayor:
    for i in range(len(string2)):
        
        if len(string2[i]) == cont:
            print(string2[i])
    cont = cont+ 1
    
# c) con split
# Crear nuevo string sin palabras repetidas.

string3 = []
for i in range (len(string2)):
    if string2[i] in string3:
        pass
    else:
        string3.append(string2[i])
print(string3)
        

#imprimir en orden de tamaño
print()
cont = 0
while cont <= mayor:
    for i in range(len(string3)):
        if len(string3[i]) == cont:
            print(string3[i])
            
    cont = cont+ 1


#imprimir string final
print()
for i in range(len(string3)):
    if i == len(string3)-1:
        print(string3[i] + '.')
    else:
        print(string3[i] + ' ' , end = '')
input()