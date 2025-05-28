#Simula una competencia entre dos jugadores lanzando un dado (números del 1 al 6).
import random

victoria_jugador1 = victoria_jugador2 = empate = cantidad_juegos = 0

while victoria_jugador1!=3 and victoria_jugador2!=3:
    dadojugador1 = random.randint(1,6) 
    dadojugador2 = random.randint(1,6)
    
    if dadojugador1>dadojugador2:
        victoria_jugador1 += 1
    elif dadojugador2>dadojugador1:
        victoria_jugador2 += 1
    else:
        empate += 1
        
cantidad_juegos = victoria_jugador1 + victoria_jugador2 + empate
prob_empate = empate/cantidad_juegos
   
if victoria_jugador1>victoria_jugador2:
    print("El primer jugador ganó")
else:
    print("El segundo jugador ganó")
    
print(f"En total hubo {cantidad_juegos} rondas")
print(f"Hubo un total de {empate} empates")
print(f"La probabilidad de empate fue de {prob_empate:.2%}")

