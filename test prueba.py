import random


L = []
for i in range(0,13):
    L.append( [0]*13 )

NumCajones = int(input("Ingrese cantidad de cajones: "))
NumAgujeros = int(input("Ingrese cantidad de agujeros: "))

for Caj in range(1, NumCajones+1):   
    Sw = 1
    while Sw == 1:     
        Sw = 0
        print("Ingrese coordenadas (fila, columna) de cajón ", Caj)
        fC = int(input("Fila: "))
        cC = int(input("Columna: "))
        if (L[fC][cC] == 1) or (fC == 12 and cC == 0) or (fC == 0 and cC == 12) : 
            print("Error en coordenas, reingréselas")
            Sw = 1
        else: 
            L[fC][cC] = 1
        
print()
for Aguj in range(1, NumAgujeros+1):   
    print("Ingrese coordenadas (fila, columna) de agujero ", Aguj)
    fA = int(input("Fila: "))
    cA = int(input("Columna: "))
    while (L[fA][cA] == 1) or (L[fA][cA] == 2) or (fA == 12 and cA == 0) or (fA == 0 and cA == 12) : 
        print("Error en coordenas, reingréselas")
        fA = int(input("Fila: "))
        cA = int(input("Columna: "))
    L[fA][cA] = 2
    
     
    
print()
for i in range (0,13) : 
    for j in range (0, 13) : 
        print(str.rjust(str(L[i][j]), 4), end = "")
    print(); print()
input()