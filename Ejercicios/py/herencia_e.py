"""
herencia_e.py
Script en Python que solicite la información de un objeto de tipo Estudiante y posteriormente imprima en pantalla sus
datos. La clase Estudiante heredará de la clase Persona, es decir, que será un tipo particular de Persona. Un
Estudiante, además de la información y comportamientos de una persona tendrá como atributos un promedio y un código
de estudiante y como comportamiento podrá estudiar una materia. Finalmente, hacer que el Estudiante ejecute el
comportamiento 'estudiar'.
"""
from estudiante import Estudiante


def main():
    nombre = input('Nombre del estudiante: ')
    edad = input('Edad del estudiante: ')
    promedio = float(input('Promedio: '))
    codigo = input('Código: ')

    estudiante = Estudiante(nombre, edad, promedio, codigo)
    print(f'''Los datos del estudiante son:
{estudiante}''')
    print('-'*25)
    estudiante.estudiar('Geografía')
    estudiante.estudiar('Dibujo')


if __name__ == '__main__':
    main()
