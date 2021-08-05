# -- coding: utf-8 --
"""
Created on Thu Jul 29 17:30:16 2021
Problema 2 guía 29-07-2021 (COMPLETAR)
@author: dagob
"""
print("Ingrese string con símbolos raros: ")
ST = input()

ST = "+(ESTE$+ES= EL-STRING++QUE;--:DEBE(SER)=DESCUBIERTO-ES=TODO$LO)QUE,ES"

RESULT = ""
 
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
i = 0
while i <= 11:
    if len(RESULT2[i]) > len(RESULT2[i + 1]):
        b = RESULT2[i]
        RESULT2[i] = RESULT2[i + 1]
        RESULT2[i + 1] = b
        i = -1

    i = i + 1 
for i in range(len(RESULT2)):
    print(RESULT2[i])
    
k = 0


for i in range(len(RESULT2)):
    for j in range(5):
        if RESULT2[i] == RESULT2[j]:
            RESULT2.remove(RESULT2[j + 1])
            



print(":::::::::::::::::::::::::::")
for i in range(len(RESULT2)):
    print(RESULT2[i])
  


input()