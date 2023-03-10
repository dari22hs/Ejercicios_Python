"""
formato_json_1.py
Script en Python que permite el registro y consulta de libros dentro de una biblioteca. Los libros serán modelados
dentro de una clase y podrán ser almacenados en un archivo con formato json y recuperados desde este mismo.
La biblioteca será modelada dentro de una clase que podrá administrar a los objetos de tipo libro.
"""
from biblioteca import Biblioteca


def main():
    bib = Biblioteca()
    bib.menu()


if __name__ == '__main__':
    main()
