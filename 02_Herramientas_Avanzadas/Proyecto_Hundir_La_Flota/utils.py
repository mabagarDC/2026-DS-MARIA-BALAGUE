import numpy as np
import random

def crear_tablero (tamano : int =10):
    """
    Crea un tablero cuadrado del tamaño indicado.
    Args:
        tamano (int): Tamaño del tablero. Por defecto es 10.
    Returns:
        np.ndarray: Tablero relleno con "_".
    
    """
    return np.full((tamano,tamano), "_")


def colocar_barco(barco, tablero):
    """
    Coloca un barco en el tablero a partir de sus coordenadas.

    Args:
        barco (list): Lista de tuplas con las posiciones del barco.
                      Cada tupla tiene la forma (fila, columna).
        tablero (np.ndarray): Tablero donde se colocará el barco.

    Returns:
        np.ndarray: Tablero con el barco colocado.
    """
    # Recorremos cada coordenada que forma parte del barco
    for casilla in barco:
        # Obtenemos la fila y la columna de cada casilla
        fila = casilla[0]
        columna = casilla[1]
        
        tablero[fila, columna] = "O"

    return tablero


def disparar(casilla, tablero):
    """
    Realiza un disparo sobre una casilla del tablero.

    Args:
        casilla (tuple): Coordenada del disparo en formato (fila, columna).
        tablero (np.ndarray): Tablero sobre el que se realiza el disparo.

    Returns:
        np.ndarray: Tablero actualizado después del disparo.
    """
      
    fila = casilla[0]
    columna = casilla[1]

    if tablero[fila, columna] == "_":
        tablero[fila,columna] = "A"

    elif tablero[fila, columna] == "O":
        tablero[fila,columna] = "X"

    return tablero 

def crear_barco(eslora, tablero):
    """
    Crea un barco de forma aleatoria dentro del tablero,
    con orientación horizontal o vertical.
    Args:
        eslora (int): Número de casillas que ocupa el barco.
        tablero (np.ndarray): Tablero usado para conocer su tamaño.
    Returns:
        list: Lista de tuplas con las coordenadas que ocupa el barco.
    """

    #Lista donde guardaremos las coordenadas del barco
    barco = []
    #Obtenemos el tamaño del tablero
    tamano_tablero = len(tablero)
    #Calculamos la posición máxima desde la que puede empezar el barco
    #sin salirse del tablero
    max_inicio = tamano_tablero - eslora

    # 0 = vertical
    # 1 = horizontal
    orientacion = random.randint(0, 1)
    

    if orientacion == 1: 

        # Creamos las coordenadas del barco
        #Elegimos una fila aleatoria y una columna inicial válida
        fila = random.randint(0,tamano_tablero-1)
        columna = random.randint(0,max_inicio)

        for i in range(eslora):
            coordenada = (fila, columna + i) 
            barco.append(coordenada)

    else:
        
        fila = random.randint(0,max_inicio)
        columna = random.randint(0,tamano_tablero-1)
        
        for i in range(eslora):
            coordenada = (fila + i, columna) 
            barco.append(coordenada)

    return barco

def colocar_barcos (tablero):
    esloras = [2, 2, 2, 3, 3, 4]

    for eslora in esloras:   
       
        while True:
            barco = crear_barco(eslora, tablero)    
            colision = False 

            for casilla in barco:
                fila = casilla[0]
                columna = casilla[1]

                if tablero[fila, columna] == "O":
                    colision = True

            if colision == False:
                    break

        tablero_barco= colocar_barco(barco, tablero)
    
    return tablero_barco
        

def ganar (tablero):

  if np.any(tablero == "O"):
    return False
  
  else:
    return True  


def turno_jugador (tablero_maquina, tablero_jugador, tablero_maquina_visible):

    while True:
        
        disparo_jugador = input("Dime una coordenada en formato fila,columna (ejemplo: 3,5): ").strip().split(",")

        fila = int(disparo_jugador[0])
        columna = int(disparo_jugador[1])
        casilla = (fila, columna)

        contenido_casilla_maquina = tablero_maquina[fila, columna]

        if contenido_casilla_maquina in ["A", "X"]:
            print("Ya has disparado en esa casilla.")
            continue   

        disparar(casilla,tablero_maquina)      

        if contenido_casilla_maquina == "O":
            tablero_maquina_visible[fila, columna] = "X"
        else: 
            tablero_maquina_visible[fila, columna] = "A"
            
        print("TU TABLERO".ljust(45), "TABLERO ENEMIGO")

        for fila_jugador, fila_enemigo in zip(tablero_jugador, tablero_maquina_visible):
            print(f"{fila_jugador}     {fila_enemigo}")

        if contenido_casilla_maquina == "_":
            break

    return tablero_maquina, tablero_maquina_visible


def turno_maquina (tablero_jugador, tablero_maquina_visible):

    while True:

        fila = random.randint(0, len(tablero_jugador)-1)
        columna = random.randint(0, len(tablero_jugador)-1)
        casilla = (fila, columna)

        contenido_casilla_jugador = tablero_jugador[fila, columna] 

        if contenido_casilla_jugador == "A" or contenido_casilla_jugador == "X":
            continue

        disparar(casilla,tablero_jugador)
            
        print("TU TABLERO".ljust(45), "TABLERO ENEMIGO")

        for fila_jugador, fila_enemigo in zip(tablero_jugador, tablero_maquina_visible):
            print(f"{fila_jugador}     {fila_enemigo}")

        if contenido_casilla_jugador == "_":
            break

    return tablero_jugador


def mostrar_tableros(tablero_jugador, tablero_maquina_visible):
    """
    Muestra el tablero del jugador y el tablero enemigo uno al lado del otro.
    """

    print("\nTU TABLERO".ljust(30), "TABLERO ENEMIGO")

    for fila_jugador, fila_enemigo in zip(tablero_jugador, tablero_maquina_visible):
        fila_jugador_texto = " ".join(fila_jugador)
        fila_enemigo_texto = " ".join(fila_enemigo)

        print(f"{fila_jugador_texto.ljust(30)} {fila_enemigo_texto}")