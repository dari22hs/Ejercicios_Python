"""
biblioteca.py
Modelo sencillo de una biblioteca.
Atributos:
    - Libros -> Colección de libros de la biblioteca
Métodos:
    - recuperar_libros(ruta) -> Recupera los libros desde el archivo indicado por ruta.
    - almacenar_libros(ruta) -> Almacena los libros en el archivo indicado por ruta.
    - agregar_libro ----------> Agrega un libro en la colección de libros.
    - consultar_libros -------> Consulta los libros de la biblioteca.
    - menú -------------------> Menú para la biblioteca.
"""
import json
from libro import *
import os
import pathlib


class Biblioteca:
    AGREGAR_LIBRO = 1
    CONSULTAR_LIBROS = 2
    SALIR = 0

    def __init__(self):
        self._libros = []
        self.recuperar_libros('libros.json')

    # Destructor de clase
    def __del__(self):
        self.almacenar_libros('libros.json')

    @property
    def libros(self):
        return self._libros

    @libros.setter
    def libros(self, valor):
        self._libros = valor

    @libros.deleter
    def libros(self):
        del self._libros

    def recuperar_libros(self, ruta):
        if pathlib.Path(ruta).exists():
            with open(ruta, 'r') as archivo:
                datos = json.load(archivo)
            for lib in datos['libros']:
                self.libros.append(desde_json(lib))

    def almacenar_libros(self, ruta):
        with open(ruta, 'w') as archivo:
            json.dump({'libros': self.libros}, archivo, cls=LibroEncoder, indent=4)

    def agregar_libro(self):
        os.system('cls')
        print('\tAgregar libro')
        isbn = input("ISBN: ")
        titulo = input("Título: ")
        autor = input("Autor: ")
        self.libros.append(Libro(isbn, titulo, autor))

    def consultar_libro(self):
        os.system('cls')
        print("\tConsultar libros")
        if len(self.libros) == 0:
            print("No hay libros registrados")
        else:
            for lib in self.libros:
                print(f"{lib}")
                print("-" * 30)

    def menu(self):
        continuar = True
        while continuar:
            os.system('cls')
            print(f"""\tBIBLIOTECA
{Biblioteca.AGREGAR_LIBRO}) Agregar libro
{Biblioteca.CONSULTAR_LIBROS}) Consultar libro
{Biblioteca.SALIR}) Salir""")
            opc = input("Seleccione una opción del menú: ")
            try:
                opc = int(opc)
            except ValueError:
                opc = -1
            if opc == Biblioteca.AGREGAR_LIBRO:
                self.agregar_libro()
            elif opc == Biblioteca.CONSULTAR_LIBROS:
                self.consultar_libro()
            elif opc == Biblioteca.SALIR:
                continuar = False
            else:
                os.system('cls')
                print("Opción no válida")
            input("Presione ENTER para continuar ...")
        input("Presione ENTER para salir ...")
