"""
poo_3.py
Script en Python que importe la clase Prenda para después crear dos objetos e imprimir su información en pantalla.
"""
from prenda import Prenda


def main():
    playera = Prenda()

    playera.tipo = 'Cuello de tortuga'
    playera.talla = 'M'

    print(f'Tipo: {playera.tipo}')
    print(f'Talla: {playera.talla}')
    print(playera)


if __name__ == '__main__':
    main()
    