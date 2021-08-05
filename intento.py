# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 17:36:29 2021

@author: Omen 15
"""


string1 = "BANANA CASA LUNA MARQUESINA TORRE ZAPATO"
string2 = "ARENA FLOR GONDOLA LAPIZ NARANJA PLATANO VIVIENDA"
string3 = string1 + " " + string2

string3 = string3.split(' ')
i = 0
while i <= 11:
    if string3[i] > string3[i + 1]:
        b = string3[i]
        string3[i] = string3[i + 1]
        string3[i + 1] = b
        i = -1
    i = i + 1


                                
            
        
    


   
        
print(string3)
print()

input()



