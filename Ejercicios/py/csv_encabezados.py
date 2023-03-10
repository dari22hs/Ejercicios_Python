import os
import csv
import pathlib


def registrar_peliculas(nombre_archivo):
    cantidad = int(input("¿Cuántas películas desea registrar?: "))
    campos = ['Título', 'Duración', 'Año']

    if not pathlib.Path(nombre_archivo).exists():
        with open(nombre_archivo, 'w', newline='') as archivo_csv:
            writer = csv.DictWriter(archivo_csv, fieldnames=campos)
            writer.writeheader()

    with open(nombre_archivo, 'a', newline='') as archivo_csv:
        writer = csv.DictWriter(archivo_csv, fieldnames=campos)
        for i in range(cantidad):
            os.system('cls')
            titulo = input("\nTítulo: ")
            duracion = input("Duración: ")
            anio = input("Año: ")
            writer.writerow({'Título': titulo, 'Duración': duracion, 'Año': anio})


def recuperar_peliculas(nombre_archivo):
    os.system('cls')
    print("Películas registradas")
    with open(nombre_archivo, 'r', newline='') as archivo_csv:
        reader = csv.DictReader(archivo_csv)
        for linea in reader:
            for campo, valor in linea.items():
                print(f"{campo}:{valor}")
            print('~'*30)


def main():
    archivo = 'peliculas_encabezado.csv'
    registrar_peliculas(archivo)
    recuperar_peliculas(archivo)


if __name__ == '__main__':
    main()
