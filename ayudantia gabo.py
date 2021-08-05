# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 18:20:10 2021

@author: Omen 15
"""
#PericoLosPalotes31*
import string
from random import randint as azar
abecedario = list(string.ascii_lowercase)




contraseña = input("ingrese contraseña a encriptar:  ")
num = azar(1,len(abecedario))
cesar = []
encriptado = []
#el for itera en cada elemento de "contraseña, y cada elemntro queda en la
#variable "letra"
for letra in contraseña:
    cesar.append(letra)

simbolos = ["*","#","$","&","!","?"]
# abecedario = 26
#num = 5
#j = x = 23

for i in range(len(contraseña)):
    for j in range(len(abecedario)):
        if contraseña[i].lower() == abecedario[j]:
            if j+num < len(abecedario):
                if contraseña[i].isupper():
                    letra = abecedario[j+num].upper()
                else:
                    letra = abecedario[j]
                encriptado.append(letra)
            else:
                dif = j + num - len(abecedario)
                if contraseña[i].isupper():
                    letra = abecedario[dif].upper()
                else:
                    letra = abecedario[dif]
                encriptado.append(letra)
    if contraseña[i].isdigit():
        encriptado.append(contraseña[i])
    if contraseña[i] in simbolos:
        encriptado.append(contraseña[i])
        
        



print(abecedario)
print(encriptado)            
            
    
print(cesar)
input()






