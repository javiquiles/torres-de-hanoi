# coding=utf-8

import time


# Dibuja las torres.
def dibujarTorres():
    for fila in torres:
        for col in fila:
            if col == 0:
                print("            |            ", end="")
            elif col == 1:
                print("          [///]          ", end="")
            elif col == 2:
                print("         [/////]         ", end="")
            elif col == 3:
                print("        [///////]        ", end="")
            elif col == 4:
                print("       [/////////]       ", end="")
            elif col == 5:
                print("      [///////////]      ", end="")
            elif col == 6:
                print("     [/////////////]     ", end="")
            elif col == 7:
                print("    [///////////////]    ", end="")
        print()
    print("="*77)
    print("            1                        2                        3            ")
    time.sleep(1)

# Nos devuelve el disco de arriba de la columna col, sino devuelve 0.
def buscarDiscoArriba(col):
	fila = 0
	while fila <= discos and torres[fila][col] == 0:
		fila += 1
	if fila <= discos:
		return torres[fila][col]
	else:
		return 0

# Nos devuelve el espacio vacio de arriba de la columna col.
def buscarEspacioArriba(col):
	fila = 0
	while fila <= discos and torres[fila][col] == 0:
		fila += 1
	return fila - 1

# Elimina el disco de arriba de la columna col.
def eliminarDiscoArriba(col):
    fila = 0
    while fila <= discos and torres[fila][col] == 0:
        fila += 1
    torres[fila][col] = 0

# Representación gráfica.
def hanoiGrafico(n, origen=1, auxiliar=2, destino=3):

    if n > 0:
        hanoiGrafico(n-1, origen, destino, auxiliar) # n-1 discos de la torre origen a la torre auxiliar.
        disco = buscarDiscoArriba(origen-1)
        eliminarDiscoArriba(origen-1)
        torres[buscarEspacioArriba(destino-1)][destino-1] = disco
        print("\n"*40)
        dibujarTorres()
        hanoiGrafico(n-1, auxiliar, origen, destino) # n-1 discos de la torre auxiliar a la torre final.

# Representación en modo texto.
def hanoiTexto(n, origen=1, auxiliar=2, destino=3):

    if n > 0:
        hanoiTexto(n-1, origen, destino, auxiliar) # n-1 discos de la torre origen a la torre auxiliar.
        print("Se mueve el disco %d de torre %d a la torre %d" % (n, origen, destino)) # disco n a la torre destino.
        hanoiTexto(n-1, auxiliar, origen, destino) # n-1 discos de la torre auxiliar a la torre final.

print("\n"*40)
print("     TORRES DE HANOI     ")
print("*"*25)
modo = int(input("Ingrese la opcion deseada:\n\n1) Modo grafico\n2) Modo texto\n\n"))

if modo == 1:
    discos = int(input("\nIngrese entre 1 y 7 discos: "))

    # Defino la matriz para el gráfico
    if discos > 0 and discos < 8:
        if discos == 1:
            torres = [[0,0,0],[1,0,0]]
        elif discos == 2:
            torres = [[0,0,0],[1,0,0],[2,0,0]]
        elif discos == 3:
            torres = [[0,0,0],[1,0,0],[2,0,0],[3,0,0]]
        elif discos == 4:
            torres = [[0,0,0],[1,0,0],[2,0,0],[3,0,0],[4,0,0]]
        elif discos == 5:
            torres = [[0,0,0],[1,0,0],[2,0,0],[3,0,0],[4,0,0],[5,0,0]]
        elif discos == 6:
            torres = [[0,0,0],[1,0,0],[2,0,0],[3,0,0],[4,0,0],[5,0,0],[6,0,0]]
        elif discos == 7:
            torres = [[0,0,0],[1,0,0],[2,0,0],[3,0,0],[4,0,0],[5,0,0],[6,0,0],[7,0,0]]

        print("\n"*40)
        dibujarTorres()
        hanoiGrafico(discos)
    else:
        print("\nERROR! Solo se permiten de 1 a 7 discos para el modo grafico.")
elif modo == 2:
    discos = int(input("\nIngrese numero de discos: "))

    if discos > 0:
        print()
        hanoiTexto(discos)
    else:
        print("\nERROR! Ingrese un numero mayor a 0.")
else:
    print("\nERROR! La opcion ingresada es incorrecta.")
