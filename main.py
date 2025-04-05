from playerGame import userGame
from BotGame import replicaGame
def menu():
#Inicio de la funcion de menu
    
    while True:
        print("\nMenú:")
        print("1. User VS la máquina")
        print("2. Réplica VS la máquina")
        print("3. Salir")

        opcion = input("Elige una opción: ")  # Solicita la opción al usuario

        if opcion == "1":
            print("Has elegido jugar contra la máquina.")
            userGame()  # Inicia el modo 'Usuario vs Máquina'
        elif opcion == "2":
            print("Has elegido la réplica contra la máquina.")
            replicaGame()  # Inicia el modo 'Replica vs Máquina'
        elif opcion == "3":
            print("Saliendo del programa...")
            break  # Sale del bucle y finaliza el programa
        else:
            print("Opción no válida, intenta de nuevo.")  # Mensaje de error si la opción no es válida

#Fin de la funcion de menu

if __name__ == "__main__":
    menu()
