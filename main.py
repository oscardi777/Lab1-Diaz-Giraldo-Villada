from playerGame import userGame
from botGame import replicaGame
import random

def menu():
#Inicio de la funcion de menu
    machineWinPlayer = 0
    gamesPlayer = 0
    machineWinReplica = 0
    gamesReplica = 0
    while True:
        p = random.randint(0,100)
        sesgo = False

        print("\nMenú:")
        print("1. User VS la máquina")
        print("2. Réplica VS la máquina")
        print("3. Resultados")
        print("4. Salir")

        opcion = input("Elige una opción: ")  # Solicita la opción al usuario

        if opcion == "1":
            print("Has elegido jugar contra la máquina.")
            if p>=90:
                sesgo = True
            machineWinPlayer = userGame(machineWinPlayer, sesgo)  # Inicia el modo 'Usuario vs Máquina'
            gamesPlayer +=1
        elif opcion == "2":
            print("Has elegido la réplica contra la máquina.")
            if p>=90:
                sesgo = True
            machineWinReplica = replicaGame(machineWinReplica, sesgo)    # Inicia el modo 'Replica vs Máquina'
            gamesReplica +=1
        elif opcion == "3":
            print("Resultados del modo Replica VS maquina")
            print(f"Total Juegos jugados: {gamesReplica}")
            print(f"Total ganados por la maquina: {machineWinReplica}")
            print("Resultados del modo User VS maquina")
            print(f"Total Juegos jugados: {gamesPlayer}")
            print(f"Total ganados por la maquina: {machineWinPlayer}")
        elif opcion == "4":
            print("Saliendo del juego...")
            break  # Sale del bucle y finaliza el programa
        else:
            print("Opción no válida, intenta de nuevo.")  # Mensaje de error si la opción no es válida

#Fin de la funcion de menu

if __name__ == "__main__":
    menu()

