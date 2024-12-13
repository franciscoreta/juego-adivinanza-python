import random


numero_secreto = random.randint(1,100)
cantidad_intentos= 0
cantidad_max_intentos = 5
adivinado = False 

print ("Bienvenido al juego de adivinar el número secreto!")

while not adivinado and cantidad_intentos < cantidad_max_intentos :
    numero = int(input("introduce un número del 1 al 99: "))

    if numero == numero_secreto:
        print("Felicitaciones has adivinado el numero secreto!")
        adivinado = True
    elif numero < numero_secreto:
        print("El número es mayor al ingresado")
    else:
        print("El número es menor al ingresado")
    cantidad_intentos += 1

if cantidad_intentos >= cantidad_max_intentos:
    print("Game over! No has podidos adivinar dentro de los 5 intentos")