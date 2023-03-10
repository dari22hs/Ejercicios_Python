# Una tupla es inmutable

"""tupla = (1,)
tupla += (2, 3, 4)

tupla += ([10, 11],)
print(f"Versión 1 de la tupla: {tupla}")
tupla[4][0] = 1000  # Agregar un elemento mutable a la tupla
print(f"Cantidad de elementos en la tupla: {len(tupla)}")
print(f"El número 4 aparece {tupla.count(4)} veces")
print(f"El número 3 está en el índice: {tupla.index(3)}")
print(f"Versión 2 de la tupla: {tupla}")"""

# Ejercicio registro de mascotas

import os


REGISTRAR = 1
CONSULTAR = 2
SALIR = 0


def mostrar_menu():
    os.system("cls")
    print(f"""
    \t AGENDA DE MASCOTAS
    {REGISTRAR}) Registrar
    {CONSULTAR}) Consultar
    {SALIR}) Salir
    """)


def registrar_mascota(mascotas):
    os.system("cls")
    print("\tREGISTRAR MASCOTA")
    nombre = input("Nombre de la mascota: ")
    edad = int(input("Edad de la mascota: "))
    peso = float(input("Peso de la mascota: "))
    tipo = input("Tipo de mascota: ")
    mascotas.append((nombre, edad, peso, tipo))


def consultar_mascotas(mascotas):
    os.system("cls")
    print("\tMIS MASCOTAS")
    if len(mascotas) == 0:
        print("No hay mascotas registradas")
    else:
        for mascota in mascotas:
            nombre, edad, peso, tipo = mascota
            print(f"Nombre: {nombre}")
            print(f"Edad: {edad}")
            print(f"Peso: {peso}")
            print(f"Tipo: {tipo}")
            print("[^_^]"*5+"\n")


def main():
    mis_mascotas = []
    continuar = True

    while continuar:
        mostrar_menu()
        opc = int(input("Seleccione una opción: "))

        if opc == REGISTRAR:
            registrar_mascota(mis_mascotas)
        elif opc == CONSULTAR:
            consultar_mascotas(mis_mascotas)
        elif opc == SALIR:
            continuar = False
        else:
            print("Opción no válida")

        input("Presione ENTER para continuar ...")

    input("¡Hasta luego!")


if __name__ == '__main__':
    main()
