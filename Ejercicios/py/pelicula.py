"""
pelicula.py
Modelo de los datos de una película.
Atributos:
    - Título
    - Director
    - Año de estreno
    - Duración
"""


class Pelicula:
    def __init__(self, titulo='', director='', anio=None, duracion=None):
        self._titulo = titulo
        self._director = director
        self._anio = anio
        self._duracion = duracion

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

    # Director
    @property
    def director(self):
        return self._director

    @director.setter
    def director(self, valor):
        self._director = valor

    @director.deleter
    def director(self):
        del self._director

    # Año
    @property
    def anio(self):
        return self._anio

    @anio.setter
    def anio(self, valor):
        self._anio = valor

    @anio.deleter
    def anio(self):
        del self._anio

    # Duración
    @property
    def duracion(self):
        return self._duracion

    @duracion.setter
    def duracion(self, valor):
        self._duracion = valor

    @duracion.deleter
    def duracion(self):
        del self._duracion

    def __str__(self):
        ESPACIOS = 10
        return f'''{"Título:" : <{ESPACIOS}}{self._titulo}
{"Director:" : <{ESPACIOS}}{self._director}
{"Año:" : <{ESPACIOS}}{self._anio}
{"Duración:" : <{ESPACIOS}}{self._duracion} minutos.
'''

    # Sobrecarga de operadores

    def __lt__(self, other):
        return self.duracion < other.duracion

    def __eq__(self, other):
        return self.director == other.director and self.anio == other.anio

    def __le__(self, other):
        return self < other or self == other
