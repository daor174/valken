# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 00:14:16 2021

@author: Omen 15
"""

FRASE1 = "TR DEJES QUE TWZXBC WYK SUEÑOS AL LHFRT QUE YRFGHVLZ MAS PQZC MAS CERCA ESTA EL CIELO."
FRASE2 = "NO AMAS IQUIQUE CAIGAN TUS MIENTRAS SUELO."
FRASE3 = ""

FRASE1 = FRASE1[0:len(FRASE1)-1]#sinpunto
FRASE2 = FRASE2[0:len(FRASE2)-1]#sinpunto


FRASES1 = FRASE1.split(" ")
FRASES2 = FRASE2.split(" ")
for i in range(len(FRASES1)):
    if "A" in FRASES1[i] or "E" in FRASES1[i] or "I" in FRASES1[i] or "O" in FRASES1[i] or "U" in FRASES1[i]:
        FRASE3 = FRASE3 + FRASES1[i]
    else:
        for j in range(len(FRASES2)):
            if len(FRASES1[i]) == len(FRASES2[j]):
                FRASE3 = FRASE3 + FRASES2[j] + " "

FRASE3 = FRASE3[0:len(FRASE3)-1] + '.'         
   
print(FRASE3)
input()
        
        
        
        
