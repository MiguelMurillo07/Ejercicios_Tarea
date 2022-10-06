# Ejercicio Tarea 2: Elabora un programa que se base en el juego de cartas llamado BlackJack.


print("-------------------------")
print("-------BlackJack 21------")
print("-------------------------")

import random

print("\nBienvenido a este juego llamado BlackJack. Dadas 2 cartas debes intentar llegar al número 21 o el más cercano sin pasarte.")
# Con un mínimo de 2 cartas tienes que llegar o acercarte al número 21, si te hace falta puedes pedir más al repartidor.

carta1 = int(random.uniform(1,12))
contador1 = carta1

print("\nEl repartidor te ha dado como carta " +str(carta1))

print("\nEstas son las opciones disponibles para ejecutar:")
# Se despliega el menú de opciones para que pueda decidir el jugador:
print("1. Pedir Carta.")
print("2. Plantarse.")

# input
opcion = int(input("\nDime la opción que quieras ejecutar. "))

while opcion ==1:
    carta2 = random.randint(1,12)
    contador1 = contador1 + carta2
    print("Sus cartas dan un total de " +str(contador1))
    if contador1<21:
            print("Tu posición fue menor a 21. ¿Quieres otra carta?")
            #Se vuelve a desplegar el menú de opciones:
            print("1. Pedir Carta.")
            print("2. Plantarse.")
            opcion2 = int(input("Digita la opción que quieras realizar: "))
            if opcion2 == 1:
                carta3 = random.randint(1,12)
                contador2 = contador1 + carta3
                print("Sus cartas dan un total de "+str(contador2))
                opcion3 = int(input("Digita la opción que quieras realizar: "))
                print("1. Pedir Carta.")
                print("2. Plantarse")
                if opcion3 == 1:
                    carta4 = random.randint(1,12)
                    contador3 = contador2 + carta4
                    print("Sus cartas dan un total de "+str(contador3))
            else:
                print("Sus cartas dan un total de "+str(contador1))
    else:
        print("Fin de su turno, el resultado final fue de "+str(contador2))
else:
    print("Sus cartas dan un total de "+str(contador1))
           

