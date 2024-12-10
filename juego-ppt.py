nombre1 = input("Escribe el nombre del jugador 1 ")
nombre2 = input("Escribe el nombre del jugador 2 ")
contadorJugador1 = 0
contadorJugador2 = 0
contadorRonda = 1


while not contadorJugador1 == 2 or contadorJugador2 == 2:

    jugador1 = input(f"¡Hola {nombre1}! ¿Qué eliges? ¿Piedra, papel, o tijera?: ").lower()
    jugador2 = input(f"¡Hola {nombre2}! ¿Qué eliges? ¿Piedra, papel, o tijera?: ").lower()

    condicion1 = jugador1 == "piedra" and jugador2 == "tijera"
    condicion2 = jugador1 == "papel" and jugador2 == "piedra"
    condicion3 = jugador1 == "tijera" and jugador2 == "papel"

    print("En la ronda ", contadorRonda)

    if jugador1 == jugador2:
        print("Ha sido un empate")
    elif condicion1 or condicion2 or condicion3:
        print("Ha ganado: ", nombre1)
        contadorJugador1 += 1
    else:
        print ("Ha ganado: ", nombre2)
        contadorJugador2 += 1

    contadorRonda += 1
    
if contadorJugador1 == 3:
    print("El ganador es", nombre1)
elif contadorJugador2 == 3:
    print("El ganador es", nombre2)