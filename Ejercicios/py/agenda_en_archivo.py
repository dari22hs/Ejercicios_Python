import pathlib
import os


SALIR = 0
AGREGAR = 1
MOSTRAR = 2
BUSCAR = 3


def mostrar_menu():
    os.system('cls')
    print(f"""
    \tMI AGENDA
    {AGREGAR}) Agregar contacto
    {MOSTRAR}) Mostrar contactos
    {BUSCAR}) Buscar contactos
    {SALIR}) Salir
    """)


def cargar_agenda(agenda, nombre_archivo):
    if pathlib.Path(nombre_archivo).exists():
        with open(nombre_archivo, 'r') as archivo:
            for linea in archivo:
                contacto, telefono, email = linea.strip().split(',')
                agenda.setdefault(contacto, (telefono, email))
    else:
        with open(nombre_archivo, 'w') as archivo:
            pass


def agregar_contacto(agenda, nombre_archivo):
    os.system('cls')
    print("\tAGREGAR CONTACTO")

    nombre = input("Nombre: ")
    if agenda.get(nombre):
        print("El contacto ya existe.")
    else:
        telefono = input("Teléfono: ")
        email = input("Correo electrónico: ")
        agenda.setdefault(nombre, (telefono, email))
        with open(nombre_archivo, 'a') as archivo:
            archivo.write(f"{nombre}, {telefono}, {email}\n")
        print("Contacto agregado con éxito.")


def mostrar_contactos(agenda):
    os.system('cls')
    print("\tMIS CONTACTOS")

    if len(agenda) > 0:
        for contacto, datos in agenda.items():
            print(f"Nombre: {contacto}")
            print(f"Teléfono: {datos[0]}")
            print(f"Correo: {datos[1]}")
            print("*" * 50)
    else:
        print("No hay contactos")


def buscar_contacto(agenda):
    os.system('cls')
    print("\tBUSCAR CONTACTO")

    if len(agenda) > 0:
        nombre = input("Nombre: ")
        print("*" * 25)
        coincidencias = 0

        for contacto, datos in agenda.items():
            if nombre in contacto:
                print(f"Nombre: {contacto}")
                print(f"Teléfono: {datos[0]}")
                print(f"Correo: {datos[1]}")
                coincidencias += 1
                print("*" * 50)

        if coincidencias == 0:
            print("No se encontró el contacto")
        else:
            print(f"Resultado(s) para '{nombre}': {coincidencias} contacto(s).")

    else:
        print("No hay contactos")


def main():
    continuar = True
    agenda = {}
    nombre_archivo = 'agenda.txt'

    cargar_agenda(agenda, nombre_archivo)

    while continuar:
        mostrar_menu()
        opc = int(input("Selecciona una opción: "))

        if opc == AGREGAR:
            agregar_contacto(agenda, nombre_archivo)
        elif opc == MOSTRAR:
            mostrar_contactos(agenda)
        elif opc == BUSCAR:
            buscar_contacto(agenda)
        elif opc == SALIR:
            continuar = False
        else:
            print("Opción no válida")
        input("Presiona ENTER para continuar ...")

    print("¡Hasta luego!")


if __name__ == '__main__':
    main()
