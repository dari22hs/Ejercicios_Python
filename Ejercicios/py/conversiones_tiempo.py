import os


SEGUNDOS_POR_MINUTO = 60
MINUTOS_POR_HORA = 60
SEGUNDOS_A_MINUTOS = 1
SEGUNDOS_A_HORAS = 2
MINUTOS_A_SEGUNDOS = 3
MINUTOS_A_HORAS = 4
SALIR = 0


def mostrar_menu():
    print(f"""
    \tConversiones
    {SEGUNDOS_A_MINUTOS}) Segundos a minutos
    {SEGUNDOS_A_HORAS}) Segundos a horas
    {MINUTOS_A_SEGUNDOS}) Minutos a segundos 
    {MINUTOS_A_HORAS}) Minutos a horas 
    {SALIR}) Salir
    """)


def segundos_a_minutos(segundos):
    mins = segundos // SEGUNDOS_POR_MINUTO
    segs = segundos % SEGUNDOS_POR_MINUTO
    return mins, segs


def minutos_a_segundos(minutos, segundos):
    segs = minutos * SEGUNDOS_POR_MINUTO + segundos
    return segs


def minutos_a_horas(minutos, segundos):
    hrs = minutos // MINUTOS_POR_HORA
    mins = minutos % MINUTOS_POR_HORA
    segs = segundos
    return hrs, mins, segs


def segundos_a_horas(segundos):
    mins, segs = segundos_a_minutos(segundos)
    hrs, mins, segs = minutos_a_horas(mins, segs)
    return hrs, mins, segs


def main():
    continuar = True
    while continuar:
        os.system('cls')
        mostrar_menu()
        opc = int(input("Seleccione una opción: "))
        os.system('cls')

        if opc == SEGUNDOS_A_MINUTOS:
            s = -1
            while 0 > s:
                s = int(input("Ingrese los segundos: "))
            mins, segs = segundos_a_minutos(s)
            print(f"El equivalente de {s} segundos es: {mins} minutos con {segs} segundos.")
        elif opc == SEGUNDOS_A_HORAS:
            s = -1
            while 0 > s:
                s = int(input("Ingrese los segundos: "))
            hrs, mins, segs = segundos_a_horas(s)
            print(f"El equivalente de {s} segundos es: {hrs} horas con {mins} minutos y {segs} segundos.")
        elif opc == MINUTOS_A_SEGUNDOS:
            m = -1
            while 0 > m:
                m = int(input("Ingrese los minutos: "))
            s = -1
            while 0 > s or s >= SEGUNDOS_POR_MINUTO:
                s = int(input("Ingrese los segundos: "))
            segs = minutos_a_segundos(m, s)
            print(f"El equivalente de {m} minutos con {s} segundos es: {segs} segundos.")
        elif opc == MINUTOS_A_HORAS:
            m = -1
            while 0 > m:
                m = int(input("Ingrese los minutos: "))
            s = -1
            while 0 > s or s >= SEGUNDOS_POR_MINUTO:
                s = int(input("Ingrese los segundos: "))
            hrs, mins, segs = minutos_a_horas(m, s)
            print(f"El equivalente de {m} minutos con {s} segundos es: {hrs} horas con {mins} minutos y {segs} "
                  f"segundos.")
        elif opc == SALIR:
            print("¡Hasta la vista!")
            continuar = False
        else:
            print("Opción no válida")
        input("Presiona ENTER para continuar ...")


if __name__ == '__main__':
    main()
