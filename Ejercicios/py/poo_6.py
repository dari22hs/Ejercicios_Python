"""
poo_6.py
Script en Python que cree e imprima la información de un objeto de tipo Persona y de otro tipo Deportista.
La clase Deportista heredará de la clase Persona, es decir, que será un tipo particular de persona.
"""
from persona import Persona
from deportista import Deportista


def main():
    per_1 = Persona('Juan Tomás', 50)
    deportista = Deportista('Ankara Messi', 35, 'Fulbo')

    print(f'Datos de la persona:')
    print(f'{per_1}')
    print('-'*25)
    print('Datos del deportista:')
    print(f'{deportista}')

    deportista.entrenar()
    deportista.hablar('"Bobo"')


if __name__ == '__main__':
    main()
