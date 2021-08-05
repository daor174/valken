# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 13:31:46 2021

@author: Omen 15
"""
Palcifrada = input("ingrese palabra")
String1 = "QX68eRCNÑP2ÚSúÁOka0ÍKtxEWuÉv 13VUpMwf9áYHczñ4hyIJiTórsLg7FDjdBZG5qlnbAíoÓmé"
String2 = "rGvzOásÚ2q9kaetdÁxiVWDEwbyQMj4Jg7fTl0ñRB13CSpícUnuÓÉAú6o HFLhIXóKÑ85ZémPNYÍ"
String3 = "gcRi1ZmGó8bKéÁe4hBÑ6úMrzvpAluoPíDWwCnJfjEkIHqÚL9ÉxOXQÍáÓ7FTt0 NS5U2dVñyYs3a"
String4 = "H9t7gúLwéTNZÉ2K ñdl14UÁIoXfRmÍs8h3áDueQCiWSjí0ÓMB6cyYxOqÚóJrnEPGpbkzAF5ÑVav"


#Palcifradas = Palcifrada.split('')

posicion = 0
caracter = 0
for i in range(len(String1)):
    for j in range(len(Palcifrada)):
        if Palcifrada[j] == String1[i]:
            posicion = i
            print(i)
            input()
for i in range(len(posicion)):
    for j in range(len(String2)):
        if posicion[i] in String2[j]:
            caracter = String2
            print(caracter)
            input()
            
print("la palabra que ingreso",Palcifrada)
print(posicion)
print(caracter)
            