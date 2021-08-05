import os

from colorama.ansi import clear_screen 
os.system('cls')
import random
from colorama import init, Back, Fore
init()

def pos(x,y):
    print("\033[" + str(x) + ";" + str(y) + "H", sep="", end="")
    return None

def DIM_MATRIZ(Filas, Columnas, ValorInicial=None):
    Arreglo = []
    for Fila in range(Filas):
        Arreglo.append([])
        for Columna in range(Columnas):
            Arreglo[Fila].append(ValorInicial)
    return Arreglo

def PoblarTablero(Tablero):
    for Fila in range(20):
        for Columna in range(9):
            Tablero[Fila][Columna] = random.randint(1,6)
    return Tablero

########################## PROGRAMA PRINCIPAL ##########################
Colores = [Fore.BLACK, Fore.RED, Fore.BLUE, Fore.MAGENTA, Fore.YELLOW, Fore.GREEN]
Figuras = ["☺","☻","♥","♣","♦","♠"]
Tablero = DIM_MATRIZ(20, 9)
Tablero = PoblarTablero(Tablero)

def tab():
    pos(2,1);  print("   1  2  3  4  5  6  7  8  9")
    pos(3,1);  print(" 1", Back.WHITE + "                        " + Back.BLACK)
    pos(4,1);  print(" 2", Back.WHITE + "                        " + Back.BLACK)
    pos(5,1);  print(" 3", Back.WHITE + "                        " + Back.BLACK)
    pos(6,1);  print(" 4", Back.WHITE + "                        " + Back.BLACK)
    pos(7,1);  print(" 5", Back.WHITE + "                        " + Back.BLACK)
    pos(8,1);  print(" 6", Back.WHITE + "                        " + Back.BLACK)
    pos(9,1);  print(" 7", Back.WHITE + "                        " + Back.BLACK)
    pos(10,1); print(" 8", Back.WHITE + "                        " + Back.BLACK)
    pos(11,1); print(" 9", Back.WHITE + "                        " + Back.BLACK)
    pos(12,1); print("10", Back.WHITE + "                        " + Back.BLACK)
    pos(13,1); print("11", Back.WHITE + "                        " + Back.BLACK)
    pos(14,1); print("12", Back.WHITE + "                        " + Back.BLACK)
    pos(15,1); print("13", Back.WHITE + "                        " + Back.BLACK)
    pos(16,1); print("14", Back.WHITE + "                        " + Back.BLACK)
    pos(17,1); print("15", Back.WHITE + "                        " + Back.BLACK)
    pos(18,1); print("16", Back.WHITE + "                        " + Back.BLACK)
    pos(19,1); print("17", Back.WHITE + "                        " + Back.BLACK)
    pos(20,1); print("18", Back.WHITE + "                        " + Back.BLACK)
    pos(21,1); print("19", Back.WHITE + "                        " + Back.BLACK)
    pos(22,1); print("20", Back.WHITE + "                        " + Back.BLACK)
    pos(5,40); print(Back.WHITE + Fore.BLACK + " ☺" + " = 1 ")
    pos(6,40); print(Back.WHITE + Fore.RED + " ☻" + " = 2 ")
    pos(7,40); print(Back.WHITE + Fore.BLUE + " ♥" + " = 3 ")
    pos(8,40); print(Back.WHITE + Fore.MAGENTA + " ♣" + " = 4 ")
    pos(9,40); print(Back.WHITE + Fore.YELLOW + " ♦" + " = 5 ")
    pos(10,40);print(Back.WHITE + Fore.GREEN + " ♠" + " = 6 ")
        
    for Fila in range(20):
        for Columna in range(9):
            Figura = Tablero[Fila][Columna] - 1
            pos(Fila+3, (Columna*3)+4)
            print(Back.WHITE + Colores[Figura] + Figuras[Figura] + Back.BLACK + Fore.WHITE)
tab()
SW = 0 ; Intento = 20 ; Puntaje = 0 ; A = []; CantFiguras = 0 
i = 0

while SW == 0:
    x = 1 ; z = 0
    os.system('cls')
    tab()
    pos(24,1); print("- Ingrese Coordenadas: ")   
    pos(25,1); print("Intento = ", Intento)
    Intento = Intento - 1 
    pos(26,1); print("Puntaje = ", Puntaje)
    
    pos(27,1); Col = int(input("Columna = "))
    pos(28,1); Fil = int(input("Fila = "))
    Col = Col - 1
    Fil = Fil - 1
    Fi = Fil + 1
    for i in range(Fi):
        Ant = Tablero[Fil - x][Col]
        Tablero[Fil - z][Col] = Ant
        x = x + 1
        z = z + 1
    Tablero[0][Col] = random.randint(1,6)
    tab()
    input()
    ##CHECK PARA VER SI HAY GRUPOS
    for Fila in range(19, 0, -1):
        CantFiguras = 0
        for h in range(7):
    
            Monito = Tablero[Fila][h]
            if Tablero[Fila][h] == Tablero[Fila][h+1]:
                
                
                
                if Tablero[Fila][h] == Tablero[Fila][h+2]:
                    CantFiguras = 3
                    
                    
                    
                    if Tablero[Fila][h] == Tablero[Fila][h+3]:
                        CantFiguras = 4
                        if h > 8:
                            h = h - 2
                            
                            
                            
                        if Tablero[Fila][h] == Tablero[Fila][h+4]:
                            CantFiguras = 5
                            Puntaje = Puntaje + (Monito * CantFiguras)
                            if h > 8:
                                h = h - 3
                                
                                
                                
                            if Tablero[Fila][h] == Tablero[Fila][h+5]:
                                CantFiguras = 6
                                Puntaje = Puntaje + (Monito * CantFiguras)
                                if h > 8:
                                    h = h - 4
                                    
                                
                                
                                if Tablero[Fila][h] == Tablero[Fila][h+6]:
                                    CantFiguras = 7
                                    Puntaje = Puntaje + (Monito * CantFiguras)
                                    if h > 8:
                                        h = h - 5
                                        
                                        
                                    
                                    if Tablero[Fila][h] == Tablero[Fila][h+7]:
                                        CantFiguras = 8
                                        Puntaje = Puntaje + (Monito * CantFiguras)
                                        if h > 8:
                                            h = h - 6
                                        
                                        if Tablero[Fila][h] == Tablero[Fila][h+8]:
                                            CantFiguras = 9
                                            Puntaje = Puntaje + (Monito * CantFiguras)
                                            if h > 8:
                                                h = h - 7

                    else:
                        Puntaje = Puntaje + (Monito * CantFiguras) 
                        for p in range(CantFiguras):
                            x = 1 ; z = 0
                            for i in range(Fil):
                                Ant = Tablero[Fil - x][h+p]
                                Tablero[Fil - z][h+p] = Ant
                                x = x + 1
                                z = z + 1
                            Tablero[0][h + p] = random.randint(1,6)
                        tab()
                                    
                        
                        
                        
                        
                        
    input()
    
    
        
    
    