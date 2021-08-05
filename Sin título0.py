# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 16:36:51 2021

@author: Omen 15
"""

PAL = input("ingrese una palabra")
Voc = 0
Con = 0
#for i in range (0, len(PAL)):
#    if PAL[i] == "A" or PAL[i] == "E" or PAL[i] == "I" or PAL[i] == "O" or PAL[i] == "U"
#       Voc = Voc + 1
#    else:
#       Con = Con + 1

for i in range ( 0, len(PAL)):
    if PAL[i] in "AEIOUaeiou":
        Voc = Voc + 1
    else:
        Con = Con + 1
        
print("Cantidad de vocales = ", Voc)
print("Cantidad de consonantes = ", Con)
    
print (); input()
        