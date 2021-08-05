import os
os.system('cls')

'''
Ejercicio: Realizar un codigo que permita realizar una cantidad 
determinada por el usuario de iteraciones. y que en cada fila
esten los datos de una persona. Los datos son, nombre, sexo, edad

Al final debe mostrar por pantalla el contenido de la matriz

'''

cantpers = int(input('Ingrese cantidad de personas: '))
matriz = []
for fila in range(cantpers):
    matriz.append([])
    for columna in range(3): 
        if columna == 0:
            matriz[fila].append(input("Ingrese nombre: "))
        elif columna == 1:
            matriz[fila].append(input("Ingrese sexo: "))
        else:
            matriz[fila].append(int(input("Ingrese edad: ")))
edadmenor = 200 
edades = 0
edadMayor = 0
for fila in range(cantpers):
    if matriz[fila][2] > edadMayor:
        edadMayor = matriz[fila][2]
        nombremayor = fila
    edades = edades + matriz[fila][2]
    

for fila in range(cantpers):
    if matriz[fila][2] < edadmenor:
        edadmenor = matriz[fila][2]
        nombremenor = fila
    edades = edades + matriz[fila][2]
        
print('Promedio de edades es: ',edades/cantpers)

print('La persona mayor es',matriz[nombremayor][0],'y tiene',edadMayor,'años')
print('La persona mayor es',matriz[nombremenor][0],'y tiene',edadmenor,'años')

