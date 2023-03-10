"""
persona.py
Modelo sencillo de una Persona con los siguientes atributos:
    - Nombre
    - Edad
Además, tiene los siguiente comportamientos:
    - Hablar (mensaje): mensaje -> el mensaje que dirá la persona.
    - Comer (alimento): alimento -> el alimento que consume la persona.
"""


class Persona:
    def __init__(self, nombre='', edad=None):
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    # Nombre
    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @nombre.deleter
    def nombre(self):
        del self._nombre

    # Edad
    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, valor):
        self._edad = valor

    @edad.deleter
    def edad(self):
        del self._edad

    def hablar(self, mensaje):
        print(f'{self.nombre}: {mensaje}')

    def comer(self, alimento):
        print(f'{self.nombre} está comiendo {alimento}')

    def __str__(self):
        return f'''Nombre: {self.nombre}
Edad: {self.edad}'''
