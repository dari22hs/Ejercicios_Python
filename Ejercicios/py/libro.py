"""
libro.py
Modelo sencillo de un libro.
Atributos:
    - ISBN ---> ISBN del libro
    - Título -> Título del libro
    - Autor --> Autor del libro
"""
import json


class Libro:
    def __init__(self, isbn='', titulo='', autor=''):
        self._isbn = isbn
        self._titulo = titulo
        self._autor = autor

    # ISBN
    @property
    def isbn(self):
        return self._isbn

    @isbn.setter
    def isbn(self, valor):
        self._isbn = valor

    @isbn.deleter
    def isbn(self):
        del self._isbn

    # Título
    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, valor):
        self._titulo = valor

    @titulo.deleter
    def titulo(self):
        del self._titulo

    # Autor
    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, valor):
        self._autor = valor

    @autor.deleter
    def autor(self):
        del self._autor

    def __str__(self):
        ESPACIOS = 8
        return f'''{"ISBN: " : <{ESPACIOS}}{self.isbn}
{"Título: " : <{ESPACIOS}}{self.titulo}
{"Autor: " : <{ESPACIOS}}{self.autor}'''


class LibroEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Libro):
            return {'isbn': obj.isbn, 'titulo': obj.titulo, 'autor': obj.autor}
        return json.JSONEncoder.default(self, obj)


def desde_json(diccionario):
    return Libro(diccionario['isbn'], diccionario['titulo'], diccionario['autor'])
