"""d = {1: 'uno',
     2: 'dos',
     3: 'tres'}

print(d)

x = dict([(1, 'uno'), (2, 'dos'), (3, 'tres')])

x[4] = 'cuatro'
x.setdefault(5, [1, 2, 3, 4, 5])
x[5] = 'cinco'
print(x)

print(x.get(1000, 'No existe la clave XD'))  # Regresa None si no encuentra la clave o se agrega un string en su lugar
print(x.get(1, 'Clave'))
print(x.get(1000))  # Regresa None si no encuentra la clave

x.pop(5)  # Eliminar un elemento, se le pasa la clave
x.popitem()  # Eliminar el último elemento agregado (como si fuera pila)
print(x)

print(x.keys())  # Regresa las claves del diccionario
print(x.values())  # Regresa los valores del diccionario
print(x.items())  # Regresa claves y valores

for k, v in x.items():
    print(f"{k} : {v}")

x.clear()  # Limpiar diccionario
#  x = {}  # Limpiar diccioario

print(x)"""

# Agenda con diccionarios

import os


SALIR = 0
AGREGAR = 1
MOSTRAR = 2
BUSCAR = 3
MODIFICAR = 4
ELIMINAR = 5


def mostrar_menu():
    os.system('cls')
    print(f"""
    \t MI AGENDA
    {AGREGAR}) Agregar contacto
    {MOSTRAR}) Mostrar contactos
    {BUSCAR}) Buscar contactos
    {MODIFICAR}) Modificar contactos
    {ELIMINAR}) Eliminar contacto
    {SALIR}) Salir
    """)


def agregar_contacto(agenda):
    os.system('cls')
    print("\tAGREGAR CONTACTO")
    nombre = input("Nombre: ")
    if agenda.get(nombre):
        print("El contacto ya existe")
    else:
        telefono = input("Teléfono: ")
        email = input("Correo: ")
        agenda.setdefault(nombre, (telefono, email))
        print("Contacto agregado")


def mostrar_contactos(agenda):
    os.system('cls')
    print("\tMIS CONTACTOS")
    if len(agenda) > 0:
        for contacto, datos in agenda.items():
            print(f"Nombre: {contacto}")
            print(f"Teléfono: {datos[0]}")
            print(f"Correo: {datos[1]}")
            print("/"*50)
    else:
        print("No hay contactos")


def buscar_contacto(agenda):
    os.system('cls')
    print("\tBUSCAR CONTACTO")

    if len(agenda) > 0:
        nombre = input("Nombre: ")
        encontrados = 0

        for contacto, datos in agenda.items():
            if nombre in contacto:
                print(f"Nombre: {contacto}")
                print(f"Teléfono: {datos[0]}")
                print(f"Correo: {datos[1]}")
                print("/"*50)
                encontrados += 1

        if encontrados == 0:
            print("No se encontraron resultados")
        else:
            print(f"Resultados encontrados: {encontrados} contacto(s).")

    else:
        print("No hay contactos")


def modificar_contacto(agenda):
    os.system('cls')
    print("\tMODIFICAR CONTACTO")

    if len(agenda) > 0:
        nombre = input("Nombre: ")
        if agenda.get(nombre):
            datos = agenda.get(nombre)
            print("Información actual:")
            print(f"Nombre: {nombre}")
            print(f"Teléfono: {datos[0]}")
            print(f"Correo: {datos[1]}")
            print("/"*50)
            print("Ingresa los nuevos datos:")
            telefono = input("Teléfono: ")
            correo = input("Correo: ")
            agenda[nombre] = (telefono, correo)
            print("Datos actualizados")
        else:
            print("El contacto no existe")

    else:
        print("No hay contactos")


def eliminar_contacto(agenda):
    os.system('cls')
    print("\tELIMINAR CONTACTO")

    if len(agenda) > 0:
        nombre = input("Nombre: ")
        if agenda.get(nombre):
            agenda.pop(nombre)
            print("Contacto eliminado")
        else:
            print("El contacto no existe")
    else:
        print("No hay contactos")


def main():
    continuar = True
    mi_agenda = {}

    while continuar:
        mostrar_menu()
        opc = int(input("Seleccione una opción: "))

        if opc == AGREGAR:
            agregar_contacto(mi_agenda)
        elif opc == MOSTRAR:
            mostrar_contactos(mi_agenda)
        elif opc == BUSCAR:
            buscar_contacto(mi_agenda)
        elif opc == MODIFICAR:
            modificar_contacto(mi_agenda)
        elif opc == ELIMINAR:
            eliminar_contacto(mi_agenda)
        elif opc == SALIR:
            continuar = False
            print("¡Hasta luego!")
        else:
            print("Opción no válida")

        input("Presiona ENTER para continuar ...")


if __name__ == '__main__':
    main()
