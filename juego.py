import time

def jugar():
    personajes = ['Vikingo', 'Lobo', 'Caperucita', 'Uvas']
    estado = ["L"] * 5  # Todos en la izquierda inicialmente

    def mostrar_estado():
        barco_pos = estado[4] == 'R'
        personas_izq = ", ".join(p for i, p in enumerate(personajes) if estado[i] == "L")
        personas_der = ", ".join(p for i, p in enumerate(personajes) if estado[i] == "R")
        print(f"\n[{personas_izq}] {'=' * (20 if barco_pos else 1)}[]{'=' * (1 if barco_pos else 20)} [{personas_der}]")

    def animar_barco():
        inicio = 0 if estado[4] == 'L' else 20
        fin = 21 if estado[4] == 'L' else -1
        paso = 1 if estado[4] == 'L' else -1
        for i in range(inicio, fin, paso):
            print(f"[{', '.join(p for i, p in enumerate(personajes) if estado[i] == 'L')}] {'=' * i}[]{'=' * (20 - i)} [{', '.join(p for i, p in enumerate(personajes) if estado[i] == 'R')}]")
            time.sleep(0.1)  # Espera para simular movimiento

    def es_valido():
        if estado[1] == estado[2] != estado[0]: return False, "El lobo se comió a Caperucita."
        if estado[2] == estado[3] != estado[0]: return False, "Caperucita se comió las uvas."
        return True, ""

    def mover(eleccion):
        animar_barco()  # Anima el movimiento antes de cambiar el estado
        estado[0] = estado[4] = "R" if estado[4] == "L" else "L"
        if eleccion > 0: estado[eleccion] = estado[4]

    while True:
        mostrar_estado()
        valido, mensaje = es_valido()
        if not valido:
            print(mensaje)
            break
        if all(x == "R" for x in estado[1:]):
            print("¡Felicidades! Todos han cruzado el río con éxito.")
            break

        opciones = [i for i in range(4) if estado[i] == estado[4] or i == 0]
        print("\n¿Qué quieres hacer?")
        for idx, opt in enumerate(opciones):
            print(f"{idx + 1}. Cruzar {'solo' if opt == 0 else 'al ' + personajes[opt]}")
        eleccion = int(input("Elige una opción: ")) - 1
        mover(opciones[eleccion])
        input("Presiona Enter para continuar...")

jugar()
