"""
poo_2.py
Script en Python que implemente una clase Persona con las siguientes propiedades:
- Nombre
- Edad
Además, se deberán agregar los siguiente comportamientos:
- Hablar (mensaje): mensaje -> el mensaje que dirá la persona.
- Comer (alimento): alimento -> el alimento que consume la persona.
"""


class Persona:
    def __init__(self, nombre='', edad=None):
        self._nombre = ''
        self._edad = None

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @nombre.deleter
    def nombre(self):
        del self._nombre

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


def main():
    persona_1 = Persona()
    persona_2 = Persona()

    persona_1.nombre = 'Pedrou Pascal'
    persona_1.edad = 38

    persona_2.nombre = 'Don Pidro'
    persona_2.edad = 58

    print('Datos de la primera persona: ')
    print(f'Nombre: {persona_1.nombre}')
    print(f'Edad: {persona_1.edad}')

    print('Datos de la segunda persona: ')
    print(f'Nombre: {persona_2.nombre}')
    print(f'Edad: {persona_2.edad}')

    persona_1.hablar(f'Hola, {persona_2.nombre}. ¿Qué haces?')
    persona_2.hablar(f'Hola, {persona_1.nombre}. Nada, me estoy haciendo bobo.')
    persona_1.hablar(f'Entonces ... GO TO THE FUCKING GYM, GO TO THE FUCKING GYM.')

    persona_1.comer(f'Tostilocos con mostaza.')
    persona_2.comer(f'arroz con popote.')


if __name__ == '__main__':
    main()
