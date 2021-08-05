import os
os.system('cls')

DICCIONARIO = "/PUERCO:MARRANO=ANIMAL COCHINITO/CASA:HOGAR VIVIENDA LAR=LUGAR EN QUE SE VIVE/BANANA:PLATANO=FRUTA TROPICAL/COMPUTADOR:PC COMPUTADORA NOTEBOOK LAPTOP=MAQUINA PARA PROCESAR"

# LISTAR EL DICCIONARIO MOSTRANDO LAS PALABRAS Y SU SIGNFICADO.
print("DICCIONARIO:")
Slash     = DICCIONARIO.find("/")
DosPuntos = DICCIONARIO.find(":")
Igual     = DICCIONARIO.find("=")
while Slash != -1: #TERMINA CUNADO NO ENCUENTRA NINGUNO
    Palabra     = DICCIONARIO[Slash+1:DosPuntos] # TOMA LA PALABRA DESDE EL PRIMER SLASH HASTA LOS SGTES DOSPUNTOS
    Slash       = DICCIONARIO.find("/", Slash+1) # SE VA AL SIGUIENTE SLASH
    Significado = DICCIONARIO[Igual+1:Slash] # TOMA EL SIGIFICADO DESDE EL SIGUIENTE IGUAL HASTA EL SIGUIENTE SLASH
    print("   -", Palabra,":",Significado)
    DosPuntos   = DICCIONARIO.find(":", DosPuntos+1)
    Igual       = DICCIONARIO.find("=", Igual+1)
    
# BUSCAR PALABRA EN EL DICCIONARIO.
Continuar = "S"
while Continuar == "S":
    print()
    print("Ingrese la palabra por buscar: ", end="")
    PalabraBuscada = input().upper()
    Slash     = DICCIONARIO.find("/")
    DosPuntos = DICCIONARIO.find(":")
    Igual     = DICCIONARIO.find("=")
    Existe    = False
    while Slash != -1:
        Palabra   = DICCIONARIO[Slash+1:DosPuntos]
        input(f"Palabra:  {Palabra}")
        Slash     = DICCIONARIO.find("/", Slash+1)   
        input(f"Slash:  {DICCIONARIO[Slash:Slash+10]}")
        if PalabraBuscada == Palabra:
            Existe = True
            print()
            print("Palabra Buscada:", Palabra)
            Significado = DICCIONARIO[Igual+1: Slash]
            print("Significado:", Significado)
            print("Sinónimos:")
            Sinonimos = DICCIONARIO[DosPuntos+1:Igual].split(" ")
            for Sinonimo in Sinonimos:
                print("   -", Sinonimo)
        DosPuntos = DICCIONARIO.find(":", DosPuntos+1) 
        input(f"DosPuntos:  {DICCIONARIO[DosPuntos:DosPuntos+10]}")
        Igual     = DICCIONARIO.find("=", Igual+1)
        input(f"Igual:  {DICCIONARIO[Igual:Igual+10]}")
    if not Existe:
       print("La palabra", PalabraBuscada,"no existe")
       
    print()
    print("¿Desea buscar otra palabra (S/N)?: ", end="")
    Continuar = input().upper()
    while Continuar not in ["S","N"]:
        print("La respuesta debe ser S o N, reingrese: ", end="")
        Continuar = input().upper()
    print()


print()
input("Pausa")