import random

vict_jugador1=vict_jugador2=empate=0

while vict_jugador1==vict_jugador2:
    jugador1 = random.randint(0,2)
    jugador2 = random.randint(0,2)
    
    if (jugador1==0 and jugador2==1) or (jugador1==1 and jugador2==2) or (jugador1==2 and jugador2==0):
        vict_jugador1 += 1
    elif (jugador2==0 and jugador1==1) or (jugador2==1 and jugador1==2) or (jugador2==2 and jugador1==0):
        vict_jugador2 += 1
    else:
        empate += 1
        
total_rondas = vict_jugador1 + vict_jugador2 + empate
prob_empate = empate / total_rondas    
        
if vict_jugador1>vict_jugador2:
    print("El ganador es el primer jugador")
else:
    print("El ganador es el segundo jugador")
    
print(f"Total de rondas: {total_rondas}")
print(f"Cantidad de empates: {empate}")
print(f"Probabilidad de empate: {prob_empate:.2%}")#:.2%

