# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 21:42:47 2021

@author: Omen 15
"""
'''
EJEMPLO: 
Frase 1: TR DEJES QUE TWZXBC WYK SUEÑOS AL LHFRT QUE YRFGHVLZ MAS PQZC MAS CERCA ESTA EL CIELO. 

Frase 2:  NO AMAS IQUIQUE CAIGAN TUS MIENTRAS SUELO. 

Verdadera frase:  NO DEJES QUE CAIGAN TUS SUEÑOS AL SUELO QUE MIENTRAS MAS AMAS MAS CERCA ESTA EL CIELO. 

Se pide realizar un programa en Python que lea dos Strings (las dos frases) y obtenga los siguientes resultados:
-	Cantidad de palabras de la primera frase (en el ejemplo 17). 
-	Cantidad de palabras de la primera frase que contienen solo consonantes (en el ejemplo 6).
-	Palabras incorrectas de la primera frase (las que solo contienen consonantes). ¡Escribirlas! (En el ejemplo, TR  TWZXBC  WYK  LHFRT  YRFGHVLZ  PQZC). 
-	Verdadera frase (la letra de la canción). (En el ejemplo: NO DEJES QUE CAIGAN TUS SUEÑOS AL SUELO QUE MIENTRAS MAS AMAS MAS CERCA ESTA EL CIELO).
''' 



#frase1 = input()
#frase2 = input()
frase1  = 'TR DEJES QUE TWZXBC WYK SUEÑOS AL LHFRT QUE YRFGHVLZ MAS PQZC MAS CERCA ESTA EL CIELO.'
frase2  = 'NO AMAS IQUIQUE CAIGAN TUS MIENTRAS SUELO.'
frase3  = ''

frase1 = frase1[0:len(frase1)-1]#sinpunto
frase2 = frase2[0:len(frase2)-1]#sinpunto

frase1s = frase1.split(' ')
frase2s = frase2.split(' ')

#verificar si no hay vocales en cada palabra de frase1 , de no tener comparar y escribir la correcta.

for i in range(len(frase1s)):
    
    if 'A' in frase1s[i] or 'E' in frase1s[i] or 'I' in frase1s[i] or 'O' in frase1s[i] or 'U' in frase1s[i]:
        frase3 = frase3 + frase1s[i] + ' '
    else:
        for j in range(len(frase2s)):
            if len(frase1s[i]) == len(frase2s[j]):
                frase3 = frase3 + frase2s[j] + ' '

frase3 = frase3[0:len(frase3)-1] + '.' 
print(frase3)
input()

