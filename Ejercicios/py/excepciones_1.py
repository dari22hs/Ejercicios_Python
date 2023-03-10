import os

MAGO = 1
GUERRERO = 2
SACERDOTISA = 3
SALIR = 0


def mostrar_menu():
    os.system('cls')
    print(f"""
    {MAGO}) Mago
    {GUERRERO}) Guerrero
    {SACERDOTISA}) Sacerdotisa
    {SALIR}) Salir""")


def main():
    continuar = True

    '''try:
        with open('saved_game.txt', 'r') as archivo:
            pass
    except:
        with open ('saved_game.txt', 'w') as archivo:
            pass'''

    while continuar:
        mostrar_menu()
        opc = input("Selecciona a tu personaje: ")
        try:
            opc = int(opc)
        except ValueError as error:
            opc = -1
            print(f"Error: {error}")

        os.system('cls')

        if opc == MAGO:
            print("\tMAGO")
            print("Fuerza: 35")
            print("Energía: 46")
            print("Habilidad: 41")
        elif opc == GUERRERO:
            print("\tGUERRERO")
            print("Fuerza: 48")
            print("Energía: 39")
            print("Habilidad: 38")
        elif opc == SACERDOTISA:
            print("\tSACERDOTISA")
            print("Fuerza: 33")
            print("Energía: 48")
            print("Habilidad: 44")
        elif opc == SALIR:
            continuar = False
        else:
            print("Opción no válida")
        input("Presiona ENTER para continuar ...")

    print("¡Hasta luego!")


if __name__ == '__main__':
    main()
