import random
#1 tijera
#2 papel
#3 piedra

#inicializar los contadores
victoria_jugador1 = 0
victoria_jugador2 = 0
empate = 0

#asignamos valores al azar a las variables
jugador1 = random.randint(1,3) #1
jugador2 = random.randint(1,3) #2

#hacemos la condicion del juego del cachipun
while jugador1==jugador2:
    if (jugador1==1 and jugador2==2) or (jugador1==2 and jugador2==3) or (jugador1==3 and jugador2==1): #evaluamos jugador 1
        victoria_jugador1 += 1
        print("Gana el jugador 1")
    elif (jugador2==1 and jugador1==2) or (jugador2==2 and jugador1==3) or (jugador2==3 and jugador1==1): #evaluamos jugador 2
        victoria_jugador2 += 1
        print("Gana el jugador 2")
    else:
        empate += 1 #evaluamos el empate
        print("Se produjo un empate")
        
total_juegos = victoria_jugador1 + victoria_jugador2 + empate
print(f"La cantidad total de juegos que se jugaron fue de {total_juegos}")





