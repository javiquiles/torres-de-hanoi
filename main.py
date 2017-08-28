def hanoi(n, origen=1, auxiliar=2, destino=3):

    if n > 0:
        hanoi(n-1, origen, destino, auxiliar) # n-1 discos de la torre origen a la torre auxiliar.
        print "Se mueve el disco %d de torre %d a la torre %d" % (n, origen, destino) # disco n a la torre destino.
        hanoi(n-1, auxiliar, origen, destino) # n-1 discos de la torre auxiliar a la torre final.

discos = int(input("Ingrese cantidad de discos: "))

if (discos > 0):
    hanoi(discos)
else:
    print "Ingrese una cantidad mayor a 0"
