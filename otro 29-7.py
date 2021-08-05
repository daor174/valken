# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 16:35:08 2021

@author: Omen 15
"""

print("ingrese strincon simbolos raros;  ")
ST = input()

ST = "+(ESTE$+ES= EL-STRING++QUE;--:DEBE(SER)=DESCUBIERTO-ES=TODO$LO)QUE,ES"

RESULT = ""
j = 0
i = 0
while i < len(ST):
    if ST[i] in "( , . ; : ( ) = + - $":
        if not(ST[i-1] in "( , . ; : ( ) = + - $"): 
            RESULT = RESULT + " "
    else:
        RESULT = RESULT + ST[i]
    i = i + 1

if RESULT[0] == " ":
    RESULT2 = RESULT[1:len(RESULT)]
    
    
for i in RESULT2.find(" "):
    

RESULT2 = RESULT2 + "."   


    
    
    
    
   

    
    print(ST)
print(RESULT2)
print(PalabraU)
input()
