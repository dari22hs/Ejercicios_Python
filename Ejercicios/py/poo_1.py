class Figura:
    def __init__(self):
        self._lados = None
        # self._lados = None  # Atributo privado con guión bajo

    @property  # Equivalente a un Getter -> Regresa el valor asociado a la cantidad de datos
    def lados(self):
        return self._lados

    @lados.setter  # Permite asignar valor al atributo lados
    def lados(self, valor):
        if valor <= 2:
            print("El valor debe ser mayor que dos")
            self.lados = None
        else:
            self._lados = valor

    @lados.deleter
    def lados(self):
        del self._lados


def main():
    triangulo = Figura()
    cuadrado = Figura()

    triangulo.lados = 3
    cuadrado.lados = 4
    # del cuadrado.lados  # Eliminar el cuadrado

    print(f"El triángulo tiene {triangulo.lados} lados.")
    print(f"El cuadrado tiene {cuadrado.lados} lados.")


if __name__ == '__main__':
    main()
