import os
os.system('cls')
import string
from random import randint as azar

#Benjajaja 2 sello
#kenneth 1 sello
"""
Contraseña = PericoLosPalotes31*

Numero al azar -> 5
Encriptacion Cesar -> UjwnhtQtxUfqtyjx31*

Intercalacion de mayusculas -> UjWnHtQtXUFqTyJx31*

Agregacion de numero al azar -> 5UjWnHtQtXUFqTyJx31*

* = ?
# = !
$ = &
& = $
! = #
? = *

Salt = #$%Fg6Der%4dfgdf

Contraseña Final = 5UjWnHtQtXUFqTyJx31?#$%Fg6Der%4dfgdf

"""
salt = "#$&Fg6Der$4dfgdf"
abecedario = list(string.ascii_lowercase)


contrasena = input('Ingrese contrasena a encriptar: ')
num = azar(1,len(abecedario))

cesar = []

#el for itera en cada elemento de 'contrasena',
#y cada elemento queda en la variable 'letra'
for letra in contrasena:
    cesar.append(letra)

input(f"cesar: {cesar}")
input(f"abecedario: {abecedario}")

simbolos = ['*','#','$','&','!','?']
encriptado = []

print('num es ',num)
for i in range(len(contrasena)):
    for j in range(len(abecedario)):
        if contrasena[i].lower() == abecedario[j]:
            if j+num < len(abecedario):
                if contrasena[i].isupper():
                    letra = abecedario[j+num].upper()
                else:
                    letra = abecedario[j+num]
                encriptado.append(letra)
            else:
                dif = j + num - len(abecedario)
                if contrasena[i].isupper():
                    letra = abecedario[dif].upper()
                else:
                    letra = abecedario[dif]
                encriptado.append(letra)
    if contrasena[i].isdigit():
        encriptado.append(contrasena[i])
    if contrasena[i] in simbolos:
        encriptado.append(contrasena[i])
input(f"encriptado {encriptado}")
for i in range(len(encriptado)):
    if i%2 == 0:
        encriptado[i] = encriptado[i].upper()

for i in range(len(encriptado)):
    if encriptado[i] in simbolos:
        for j in range(len(simbolos)):
            if encriptado[i] == simbolos[j]:
                input(f"pos simbolo ( {len(simbolos)}-1 ) - {j} = {(len(simbolos)-1) - j}")
                encriptado[i] = simbolos[(len(simbolos)-1) - j]
                break
                

print("su contrasena encriptada es: ",str(num)+ "".join(encriptado) + salt)




