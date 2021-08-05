import random

P = []

for i in range(0,13):
    P.append( [0]*13 )

    
CantCajones = int(input("ingrese la cantidad de cajones : "))
CantAgujeros = int(input("ingrese la cantidad de agujeros : "))


for cajon in range(1, CantCajones+1):
    print("ingrese cordenadas (fila, columna) de cajon", cajon)
    fila = int(input("fila: "))
    columna = int(input("columna: "))
    P[fila][columna] = 1
    while (fila == 12 and columna == 0) or (fila == 0 and columna == 12) or (P[fila][columna] == 1) :
        print("error, ingrese las cordenadas")
        fila = int(input("fila:"))
        columna = int(input("columna:"))
    P[fila][columna] = 1
    
    
print()
       
for agujero in range(1, CantAgujeros+1):
    print("ingrese cordenadas (fila, columna) de agujero", agujero)
    fila = int(input("fila: "))
    columna = int(input("columna: "))
    P[fila][columna] = 2
    while agujero == cajon :
        print("error, ingrese las cordenadas")
        fila = int(input("fila:"))
        columna = int(input("columna:"))
    P[fila][columna] = 2
print()








print()
for i in range(0,13):
    for j in range (0, 13):
        print(str.rjust(str(P[i][j]), 4), end = "")
        print(); print()
input()