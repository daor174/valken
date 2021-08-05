
"""
Created on Thu Jun  3 12:05:37 2021
Juego Toque y Fama. CP es un arreglo de 6 elementos en que el computador pondrá al azar 6 cifreas diferentes.
US será el arreglo en que el usuario pondrá sus 6 cifras (que deben ser diferentes)
@author: dagob
"""

import random
CP = [-1, -1, -1, -1, -1, -1]
CP[0] = random.randint(0,9)
i = 1
while i < 6: 
    CP[i] = random.randint(0,9)
    j = 0; Sw = 0
    while j < i :
        if CP[i] == CP[j]: 
            Sw = 1
        j = j + 1
    if Sw == 0 : 
        i = i + 1
        
print(CP)  # Después hay que quitar esta instrucción
 
# Aquí hay que programar el juego. 
# El usuario tendrá hasta 20 intentos para adivinar. Debe ir ingresando 6 dígitos diferentes
US = [-1, -1, -1, -1, -1, -1]
Intentos = 0
Famas = 0
while Intentos < 20 and Famas < 6: 
    print("Intento ", Intentos + 1, " Ingrese sus 6 cifras diferentes: ")
    for i in range (0, 6): 
        US[i] = int(input())
        
    print("El usuario ingresó ", US)   
        
    Famas = 0
    for i in range (0, 6): 
        if US[i] == CP[i] : 
            Famas = Famas + 1
            
    Toques = 0
    i = 0
    while i < 6 : 
        for j in range (0, 6): 
            if (US[i] == CP[j]) and (i != j): 
                Toques = Toques + 1
                
        i = i + 1 
    
    print("Obtuvo ", Famas, " famas  y ", Toques, " toques")
        
    
    Intentos = Intentos + 1
    
    
    
print(); input("FIN DE PROCESO")
        
input("presione enter para finalizar...")
