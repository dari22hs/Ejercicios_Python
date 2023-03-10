"""
poo_4.py
Script en Python que cree y asigne valor a los atributos de un objeto tipo Ingrediente. Los ingredientes serán
modelados dentro de una clase en un módulo separado y tendrán los siguientes atributos:
- Nombre
- Cantidad
- Unidad de medida
Además, la clase Ingrediente podrá recibir como argumentos los valores iniciales para sus atributos a través del
método constructor.
"""
from ingrediente import Ingrediente


def main():
    ingrediente = Ingrediente('Fresa', 2, 'kg.')
    print(ingrediente)


if __name__ == '__main__':
    main()
