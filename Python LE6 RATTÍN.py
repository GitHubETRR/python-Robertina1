import random

run = True

def juego():
    numero = random.randrange(1,100)

    adivinar = 0
    intentos = 0
    while adivinar != numero:
        intentos+=1

        adivinar = int(input("Intenta adivinar el número, es del 1 al 100: "))

        if adivinar > numero:
            print("El número es mas chico, intente de nuevo")
        elif adivinar < numero:
            print("El número es más grande, intente de nuevo")
        else:
            print("¡Adivinaste!, tardaste:", intentos, " intentos")
       

while run:
    juego()
    run = int(input("Si queres volver a jugar, presione cualquier número, sino, presione 0: "))
    if run == 0:
        print("Gracias por jugar!")
