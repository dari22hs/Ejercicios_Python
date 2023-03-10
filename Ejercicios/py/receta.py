"""
receta.py
Model sencillo de una receta de cocina
Atributos:
    - Ingredientes -> Lista de ingredientes para la receta
    - Pasos -> Lista de pasos o instrucciones para la receta
Comportamientos:
    - Menú -> Menú de operaciones
    - Agregar ingrediente -> Permite agregar ingredientes a la receta
    - Consultar ingredientes -> Permite consultar los ingredientes
    - Agregar paso -> Permite agregar pasos a la receta
    - Consultar paso -> Permite consultar los pasos para la receta
"""
from ingrediente import Ingrediente
import os


class Receta:
    OPC_AGREGAR_INGREDIENTE = 1
    OPC_CONSULTAR_INGREDIENTES = 2
    OPC_AGREGAR_PASO = 3
    OPC_CONSULTAR_PASOS = 4
    OPC_SALIR = 0

    def __init__(self, nombre=''):
        self._nombre = nombre
        self._ingredientes = []
        self._pasos = []

    def __str__(self):
        s = f'\t\t{self.nombre}\n'
        s += 'Ingredientes: \n'
        for ingrediente in self.ingredientes:
            s += f'{ingrediente}\n'
        s += '\nPasos: \n'
        for i, paso in enumerate(self.pasos):
            s += f'{i+1}. {paso}\n'
        return s

    # Nombre
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @nombre.deleter
    def nombre(self):
        del self._nombre

    # Ingredientes
    @property
    def ingredientes(self):
        return self._ingredientes

    @ingredientes.setter
    def ingredientes(self, valor):
        self._ingredientes = valor

    @ingredientes.deleter
    def ingredientes(self):
        del self._ingredientes

    # Pasos
    @property
    def pasos(self):
        return self._pasos

    @pasos.setter
    def pasos(self, valor):
        self._pasos = valor

    @pasos.deleter
    def pasos(self):
        del self._pasos

    def menu(self):
        continuar = True
        while continuar:
            os.system('cls')
            print(f""""\t\t{self.nombre}
{self.OPC_AGREGAR_INGREDIENTE}) Agregar ingrediente
{self.OPC_CONSULTAR_INGREDIENTES}) Consultar ingredientes
{self.OPC_AGREGAR_PASO}) Agregar paso
{self.OPC_CONSULTAR_PASOS}) Consultar pasos
{self.OPC_SALIR}) Salir""")
            opc = int(input("Seleccione una opción: "))
            if opc == self.OPC_AGREGAR_INGREDIENTE:
                self.agregar_ingrediente()
            elif opc == self.OPC_CONSULTAR_INGREDIENTES:
                self.consultar_ingredientes()
            elif opc == self.OPC_AGREGAR_PASO:
                self.agregar_paso()
            elif opc == self.OPC_CONSULTAR_PASOS:
                self.consultar_pasos()
            elif opc == self.OPC_SALIR:
                continuar = False
            else:
                print("Opción no válida")
            input("Presione ENTER para continuar ...")
        print("¡Hasta la vista!")

    def agregar_ingrediente(self):
        continuar = True
        while continuar:
            os.system('cls')
            print('\t\tAgregar ingrediente')
            nombre = input('Nombre: ')
            cantidad = -1
            while cantidad <= 0:
                cantidad = input('Cantidad: ')
                try:
                    cantidad = float(cantidad)
                except:
                    cantidad = 0
            unidad = input('Unidad de medida: ')
            ingrediente = Ingrediente(nombre, cantidad, unidad)
            self.ingredientes.append(ingrediente)
            respuesta = input('¿Desea agregar otro ingrediente? (S/N) ... ').lower()
            if respuesta != 's':
                continuar = False

    def consultar_ingredientes(self):
        os.system('cls')
        print('\t\tConsultar ingredientes')
        if len(self.ingredientes) == 0:
            print('No hay ingredientes registrados.')
        else:
            for ingrediente in self.ingredientes:
                print(f'{ingrediente}')

    def agregar_paso(self):
        continuar = True
        while continuar:
            os.system('cls')
            print('\t\tAgregar paso')
            paso = input('Paso: ')
            self.pasos.append(paso)
            respuesta = input('¿Desea agregar otro paso? (S/N) ... ').lower()
            if respuesta != 's':
                continuar = False

    def consultar_pasos(self):
        os.system('cls')
        print('\t\tPasos')
        if len(self.pasos) == 0:
            print('No hay pasos registrados.')
        else:
            for i, paso in enumerate(self.pasos):
                print(f'{i+1}. {paso}')
