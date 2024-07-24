import random

cpu = random.randint(1, 3)

print ("Bienvenido al juego Cachipun\n")
print ("Seleccione su Carta")
print ("1. Piedra")
print ("2. Papel")
print ("3. Tijera")
player = float(input("Su Opcion: \n"))

if cpu == 1:
    print ("CPU escogio Piedra")
elif cpu == 2:
    print ("CPU escogio Papel")
elif cpu == 3:
    print ("CPU escogio Tijera")

if player == 1:
    print ("Jugador escogio Piedra")
elif player == 2:
    print ("Jugador escogio Papel")
elif player == 3:
    print ("Jugador escogio Tijera")

if cpu == player:
    print ("Empatados!")
elif (player == 1 and cpu == 3) or \
     (player == 2 and cpu == 1) or \
     (player == 3 and cpu == 2):
    print ("Ganaste!")
else:
    print ("Perdiste!")