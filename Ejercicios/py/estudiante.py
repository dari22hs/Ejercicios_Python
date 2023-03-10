"""
estudiante.py
Modelo sencillo de un estudiante. Hereda de la clase Persona.
Atributos:
    - Promedio
    - Código de estudiante
Comportamientos:
    - Estudiar una materia
"""
from persona import Persona


class Estudiante(Persona):
    def __init__(self, nombre='', edad=None, promedio=None, codigo=''):
        super().__init__(nombre, edad)
        self._promedio = promedio
        self._codigo = codigo

    # Atributo promedio
    @property
    def promedio(self):
        return self._promedio

    @promedio.setter
    def promedio(self, valor):
        if valor < 0.0:
            self._promedio = None
        else:
            self._promedio = valor

    @promedio.deleter
    def promedio(self):
        del self._promedio

    # Atributo código
    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        self._codigo = valor

    @codigo.deleter
    def codigo(self):
        del self._codigo

    # Comportamiento estudiar
    def estudiar(self, materia):
        print(f'{self.nombre} está estudiando {materia}')

    # Método string
    def __str__(self):
        return f'''{super().__str__()}
Promedio: {self.promedio}
Código: {self.codigo}'''
