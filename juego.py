import time
from os import system, name

# Definición de los personajes
VIKINGO = 0
LOBO = 1
CAPERUCITA = 2
UVAS = 3
BARCO = 4

# Estado inicial
estado_inicial = ["L", "L", "L", "L", "L"]

def mostrar_estado(estado):
    izquierda = []
    derecha = []
    personajes = ['Vikingo', 'Lobo', 'Caperucita', 'Uvas']
    for i, lugar in enumerate(estado[:-1]):
        if lugar == "L":
            izquierda.append(personajes[i])
        else:
            derecha.append(personajes[i])
    
    barco = "Izquierda" if estado[BARCO] == "L" else "Derecha"
    print("[{}] ================= [{}]".format(", ".join(izquierda), ", ".join(derecha)))
    print("El barco está en la orilla: {}".format(barco))

def verificar_reglas(estado):
    # Reglas de peligro
    if estado[LOBO] == estado[CAPERUCITA] and estado[VIKINGO] != estado[LOBO]:
        return False, "El lobo se comió a Caperucita."
    if estado[CAPERUCITA] == estado[UVAS] and estado[VIKINGO] != estado[CAPERUCITA]:
        return False, "Caperucita se comió las uvas."
    return True, ""

def mover(estado, eleccion):
    nuevo_estado = estado[:]
    nuevo_estado[VIKINGO] = "R" if estado[BARCO] == "L" else "L"
    nuevo_estado[BARCO] = "R" if estado[BARCO] == "L" else "L"
    if eleccion != "solo":
        nuevo_estado[eleccion] = "R" if estado[BARCO] == "L" else "L"
    return nuevo_estado

def obtener_opciones(estado):
    opciones = ["solo"]
    for i in [LOBO, CAPERUCITA, UVAS]:
        if estado[i] == estado[BARCO]:
            opciones.append(i)
    return opciones

def jugar():
    estado = estado_inicial[:]
    continuar = True
    while continuar:
        mostrar_estado(estado)
        valido, mensaje = verificar_reglas(estado)
        if not valido:
            print(mensaje)
            break
        if estado[1:] == ["R", "R", "R", "R"]:
            print("¡Felicidades! Todos han cruzado el río con éxito.")
            break
        
        print("\n¿Qué quieres hacer?")
        opciones = obtener_opciones(estado)
        for idx, opcion in enumerate(opciones):
            nombre = ["solo", "al lobo", "a Caperucita", "a las uvas"][opcion] if isinstance(opcion, int) else opcion
            print(f"{idx + 1}. Cruzar {nombre}")
        
        eleccion = int(input("Elige una opción: ")) - 1
        estado = mover(estado, opciones[eleccion])
        limpiar_pantalla()

def limpiar_pantalla():
    # Limpia la consola
    _ = system('cls' if name == 'nt' else 'clear')

jugar()
