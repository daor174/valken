# -- coding: utf-8 --
"""
Created on Thu Jul 29 17:30:16 2021
Problema 2 guía 29-07-2021 (COMPLETAR)
@author: dagob
"""
print("Ingrese string con símbolos raros: ")
ST = input()

ST = "+(ESTE$+ES= EL-STRING++QUE;--:DEBE(SER)=DESCUBIERTO-ES=TODO$LO)QUE,ES"
#quitar signos
RESULT = ""
RESULT4 = [] 
i = 0
while i < len(ST) : 
    if ST[i] in ",.;:()=+-$ " :
        if not(ST[i-1] in ",.;:()=+-$ ") :
            RESULT = RESULT + " "
    else: 
        RESULT = RESULT + ST[i]
    i = i + 1

if RESULT[0] == " ": 
    RESULT2 = RESULT[1:len(RESULT)]


RESULT2 = RESULT2 + ""

print(ST)
print(RESULT2)

print('')
RESULT2 = RESULT2.split(' ')
#ordenar de menor a mayo en direccion vertical
i = 0
while i <= 11:
    if len(RESULT2[i]) > len(RESULT2[i + 1]):
        b = RESULT2[i]
        RESULT2[i] = RESULT2[i + 1]
        RESULT2[i + 1] = b
        i = -1

    i = i + 1 
 #sacar palabras repetidas   
for i in range(len(RESULT2)):
    print(RESULT2[i])
    
RESULT3 = []
for i in range(len(RESULT2)):
    if RESULT2[i] in RESULT3:
        pass
    else:
        RESULT3.append(RESULT2[i])
        
RESULT4 = []
for i in range(len(RESULT3)):
    for j in range(len(RESULT4)):
        RESULT3[i] == RESULT4[j]
        print(RESULT4[j])
        input()
        






for i in range(len(RESULT3)):
    print("*",RESULT3[i], "*")


input()
