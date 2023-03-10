"""
poo_5.py
Script en Python que utilice el menú de una clase Receta, dentro de la cual, habrá una lista de ingredientes. Cada
Ingrediente tendrá como atributos los siguientes:
    - Nombre
    - Cantidad
    - Unidad de medida
La clase Receta, además de contener un menú y una lista de ingredientes, deberá tener un nombre y una lista de pasos
o instrucciones así como los siguientes comportamientos:
    - Agregar ingrediente
    - Consultar ingrediente
    - Agregar Paso
    - Consultar Paso
"""
from receta import Receta


def main():
    receta = Receta('Pizza')
    receta.menu()
    print(receta)


if __name__ == '__main__':
    main()
