"""import queue


cola = queue.Queue()
cp = queue.PriorityQueue()

cola.put(2)
cola.put([4, 6, 8])
cola.get()
cola.empty()

cp.put(3)
cp.put(5)
cp.put(1)

cp.get()

print(cp)"""

# Ejercicio Agenda con Cola de Prioridad

import os
import queue


AGENDAR = 1
ATENDER = 2
SALIR = 0


def mostrar_menu():
    os.system("cls")
    print(f"""
    \t MI AGENDA
    {AGENDAR}) Agendar
    {ATENDER}) Atender
    {SALIR}) Salir
    """)


def agendar_evento(ag):
    print("\tAGENDAR EVENTO")
    evento = input("Evento: ")
    ag.put(evento)


def atender_evento(ag):
    print("\t ATENDER EVENTO")
    if ag.empty():
        print("No hay eventos por atender")
    else:
        evento = ag.get()
        print(f"Evento: {evento}")


def main():
    agenda = queue.PriorityQueue()
    continuar = True

    while continuar:
        mostrar_menu()
        opc = int(input("Seleccione una opción: "))
        os.system("cls")

        if opc == AGENDAR:
            agendar_evento(agenda)
        elif opc == ATENDER:
            atender_evento(agenda)
        elif opc == SALIR:
            continuar = False
        else:
            print("Opción no válida ...")
        input("Presione ENTER para continuar ...")

    print("¡Hasta luego!")


if __name__ == '__main__':
    main()
