# Ejercicio Tarea: Hacer un programa que la máquina de un número y el usuario intente adivinarlo.


print("-----------------------------------------")
print("------------Adivinar Número--------------")
print("-----------------------------------------")

import random

# input

num_maq = random.randint(1,500)
while True:
    x = int(input("Digita el número que creas que es el indicado de 1 a 500: "))
    if x == num_maq:
        print("Enhorabuena!!!! Adivinaste el número.")
        break
    
    elif (x<num_maq):
        print("El número es mayor al que digitaste, por favor sigue intentando.")
        
    elif (x>num_maq):
        print("El número es menor al que digitaste, por favor sigue intentando.")



