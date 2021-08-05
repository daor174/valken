# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 15:03:19 2021

@author: Omen 15
"""

'''
ST = "estamos en primavera"
i = len(ST) - 1
print("El largo del string es",len(ST))

while i > 0:
    print(i, "*", ST[i], "*")
    i = i - 1


    input()
'''
ST = "estamos en primavera"

RES = ""

for i in range(0,len(ST)):
    if ST[i] in "AEIOUaeiou":
        RES = RES + ST[i].upper()
    else:
        RES = RES + ST[i]



print(RES)


input()


































