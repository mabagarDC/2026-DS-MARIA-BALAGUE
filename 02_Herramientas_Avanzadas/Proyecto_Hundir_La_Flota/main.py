from utils import *

# Crear tablero del jugador hasta que acepte
while True:

    #Creamos un tablero nuevo y colocamos los barcos aleatoriamente
    tablero_jugador = crear_tablero ()
    tablero_jugador = colocar_barcos (tablero_jugador)

    #Mostramos el tablero para que el jugador pueda revisar las posiciones
    print(tablero_jugador)

    # Pedimos al jugador que confirme si acepta la distribución
    # strip() elimina espacios y upper() convierte la respuesta a mayúsculas
    respuesta = input ("¿Te gustan estas posiciones? (S/N): ").strip().upper()

    #Validamos que la respuesta solo pueda ser "S" o "N"
    while respuesta not in ["S", "N"]:
        respuesta = input("Respuesta no válida. Escribe S o N: ").strip().upper()
        
    #Si el jugador acepta, salimos del bucle
    if respuesta == "S":
        break

#Creamos el tablero de la máquina y colocamos sus barcos aleatoriamente
tablero_maquina = crear_tablero()
tablero_maquina = colocar_barcos(tablero_maquina)

# Tablero enemigo visible
tablero_maquina_visible = crear_tablero()


mostrar_tableros(tablero_jugador, tablero_maquina_visible)

# Partida

while True:

    print("\n--- TU TURNO ---")

    tablero_maquina, tablero_maquina_visible = turno_jugador(tablero_maquina, tablero_jugador, tablero_maquina_visible)

    if ganar(tablero_maquina):
        print("Has ganado!")
        break

    print("\n--- TURNO DE LA MÁQUINA ---")
    
    tablero_jugador = turno_maquina(tablero_jugador, tablero_maquina_visible)

    if ganar(tablero_jugador):
        print("Ha ganado la máquina :(!")
        break
