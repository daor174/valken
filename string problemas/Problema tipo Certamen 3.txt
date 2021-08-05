# -*- coding: utf-8 -*-
'''
Created on Sun A'ug  1 15:17:00 2021

@author: Inso

PROBLEMA:

Se pide un programa en lenguaje Python, que maneje un diccionario de palabras (con sinónimos y significado de esas palabras) y que permita buscar palabras en ese diccionario.
 
Especificaciones:
Al principio el programa deberá leer un string (máximo = 200 caracteres) con el siguiente formato:
      /palabra1:sinónimos=significado/palabra2:sinónimos=significado …

Siempre una palabra del diccionario va antecedida por un slash (“/”) y siempre va seguida por un dos puntos (“:”). Luego están los sinónimos separados siempre por un espacio en blanco y finalizados por un igual (“=”).
A continuación está el significado de la palabra terminado por un slash (si es que sigue otra palabra). No es necesario validar esta estructura. Una palabra puede tener uno o más sinónimos. 

Ejemplo:
  
/PUERCO:MARRANO=ANIMAL COCHINITO/CASA:HOGAR VIVIENDA LAR=LUGAR EN QUE SE VIVE/BANANA:PLATANO=FRUTA TROPICAL

El programa debe hacer lo siguiente: 
 
a)	Aceptar (leer el string que contiene el diccionario). 
b)	Indicar listado de palabras que están en el diccionario acompañadas de su significado (sin los sinónimos), en el ejemplo debería resultar: 
PUERCO = ANIMAL COCHINITO
CASA = LUGAR EN QUE SE VIVE
BANANA = FRUTA TROPICAL
c)	Permitir iterativamente buscar palabras en el diccionario. Si no está esa palabra debe indicar un mensaje de error. Si la encuentra, debe entregar el resultado en el siguiente formato:

Palabra buscada: Palabra
Significado       : Escribir el significado
Sinónimos        :
1)	Sinónimo 1
2)	Sinónimo 2
                  …
Por ejemplo, si la palabra buscada es CASA, el resultado debería ser:
 
Palabra buscada: CASA
Significado          : LUGAR EN QUE SE VIVE
Sinónimos           :
1)	HOGAR
2)	VIVIENDA
3)	LAR

Observaciones: 
-	Para facilitar las cosas, en el diccionario solo se incluirán palabras con MAYUSCULAS, pero sin tildes (no hay vocales acentuadas), eso sí puede estar incluida la letra Ñ. 
-	La palabra a buscar se puede ingresar con mayúsculas, minúsculas o una mezcla de ellas (pero sin vocales acentuadas). Por ejemplo, se podría haber ingresado CASA, Casa o casa. 

'''

# a)
# string = input()

string = '/PUERCO:MARRANO=ANIMAL COCHINITO/CASA:HOGAR VIVIENDA LAR=LUGAR EN QUE SE VIVE/BANANA:PLATANO=FRUTA TROPICAL'
listaPalabras = string[1:].split('/')

# b)

for i in range(len(listaPalabras)):#Lee cada palabra
    #Separar la palabra
    indicePalabra = listaPalabras[i].find(':')
    palabra = listaPalabras[i][0:indicePalabra]
    indiceSignificado = listaPalabras[i].find('=')
    significado = listaPalabras[i][indiceSignificado + 1: ]
    #Aqui tengo la palabra 
    print(palabra,'=',significado)

# c)
# Buscar la palabra c.1
print()
res = 'S'
sw  = True
while res == 'S':
    buscarPalabra = input('Ingrese palabra a buscar en el diccionario: ',).upper();print()
    sw = True
    while sw == True:
        
        for i in range(len(listaPalabras)):
            
            indicePalabra = listaPalabras[i].find(':')
            palabra = listaPalabras[i][0:indicePalabra]
            
            if buscarPalabra == palabra:
                
                print('Palabra buscada :',palabra)
                
                indiceSignificado = listaPalabras[i].find('=')
                significado = listaPalabras[i][indiceSignificado + 1: ]
                print('Significado     :',significado)
                
                #Imprimir sinonimos
                sinonimos = listaPalabras[i][indicePalabra + 1 : indiceSignificado]
                sinonimos = sinonimos.split(' ')
                print('Sinonimos       :')
                for i in range(len(sinonimos)):
                    print (str(i + 1) + ') ' + sinonimos[i])
                sw = False
                
        if sw == True:
            print('ERROR palabra no esta en el diccionario ingrese nuevamente.')
            buscarPalabra = input()
            
    print();res = input('Desea continuar? (S/N)').upper();print()

input('FIN DLE PROGRAMA')