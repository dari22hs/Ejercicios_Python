"""
enemigo.py
Modelo sencillo de un Enemigo para juego de consola.
Atributos:
    - Tipo -> Tipo de enemigo
    - Ataque -> Ataque que puede realizar el enemigo
    - Energía -> Energía del enemigo
    - Fuerza -> Fuerza con la que puede atacar el enemigo
Comportamientos:
    - Atacar -> Permite realizar el ataque especial al enemigo
"""
MOMIA = 0
ZOMBIE = 1
VAMPIRO = 2
YETI = 3
HOMBRE_LOBO = 4
PIE_GRANDE = 5
CENTAURO = 6
MINOTAURO = 7
RAKE = 8
LA_GORDA = 9

tipos = [MOMIA, ZOMBIE, VAMPIRO, YETI, HOMBRE_LOBO, PIE_GRANDE, CENTAURO, MINOTAURO, RAKE, LA_GORDA]


class Enemigo:
    def __init__(self, tipo='', ataque='', energia=3, fuerza=3):
        self._tipo = tipo
        self._ataque = ataque
        self._energia = energia
        self._fuerza = fuerza

    # Tipo
    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, valor):
        self._tipo = valor

    @tipo.deleter
    def tipo(self):
        del self._tipo

    # Ataque
    @property
    def ataque(self):
        return self._ataque

    @ataque.setter
    def ataque(self, valor):
        self._ataque = valor

    @ataque.deleter
    def ataque(self):
        del self._ataque

    # Energía
    @property
    def energia(self):
        return self._energia

    @energia.setter
    def energia(self, valor):
        self._energia = valor

    @energia.deleter
    def energia(self):
        del self._energia

    # Fuerza
    @property
    def fuerza(self):
        return self._fuerza

    @fuerza.setter
    def fuerza(self, valor):
        self._fuerza = valor

    @fuerza.deleter
    def fuerza(self):
        del self._fuerza

    def atacar(self):
        print(f"{self.tipo} ha atacado con {self.ataque}.")
        print(f"{self.tipo} ha causado {self.fuerza} de daño.")


class Momia(Enemigo):
    def __init__(self):
        super().__init__('Momia', 'Vendaje mortal', 12, 8)


class Zombie(Enemigo):
    def __init__(self):
        super().__init__('Zombie', 'Comecerebro', 16, 10)


class Vampiro(Enemigo):
    def __init__(self):
        super().__init__('Vampiro', 'Chupasangre', 18, 12)
        self._recuperacion = 4

    # Recuperación
    @property
    def recuperacion(self):
        return self._recuperacion

    @recuperacion.setter
    def recuperacion(self, valor):
        self._recuperacion = valor

    @recuperacion.deleter
    def recuperacion(self):
        del self._recuperacion

    def atacar(self):
        super().atacar()
        print(f"{self.tipo} ha recuperado {self.recuperacion} de energía.")
        self.energia += self.recuperacion


class Yeti(Enemigo):
    def __init__(self):
        super().__init__('Yeti', 'Ventisca', 22, 14)


class HombreLobo(Enemigo):
    def __init__(self):
        super().__init__('Hombre Lobo', 'Colmillos Venenosos', 19, 12)
        self._vitalidad = 4

    # Vitalidad
    @property
    def vitalidad(self):
        return self._vitalidad

    @vitalidad.setter
    def vitalidad(self, valor):
        self._vitalidad = valor

    @vitalidad.deleter
    def vitalidad(self):
        del self._vitalidad

    def atacar(self):
        super().atacar()
        print(f"{self.tipo} ha ganado {self.vitalidad} de fuerza.")
        self.fuerza += self.vitalidad


class PieGrande(Enemigo):
    def __init__(self):
        super().__init__('Pie Grande', 'Pisotón', 17, 10)        


class Centauro(Enemigo):
    def __init__(self):
        super().__init__('Centauro', 'Patada Mortal', 20, 16)


class Minotauro(Enemigo):
    def __init__(self):
        super().__init__('Minotauro', 'Cornada Mortal', 21, 13)


class Rake(Enemigo):
    def __init__(self):
        super().__init__('The Rake', 'Desmembramiento', 18, 15)
        self._canibalismo = 4

    # Canibalismo
    @property
    def canibalismo(self):
        return self._canibalismo

    @canibalismo.setter
    def canibalismo(self, valor):
        self._canibalismo = valor

    @canibalismo.deleter
    def canibalismo(self):
        del self._canibalismo

    def atacar(self):
        super().atacar()
        print(f"{self.tipo} ha ganado {self.canibalismo} de energía.")
        self.energia += self.canibalismo


class LaGorda(Enemigo):
    def __init__(self):
        super().__init__('La Gorda', 'Vomitrón', 21, 18)
        self._succion = 6

    # Succión
    @property
    def succion(self):
        return self._succion

    @succion.setter
    def succion(self, valor):
        self._succion = valor

    @succion.deleter
    def succcion(self):
        del self._succion

    def atacar(self):
        super().atacar()
        print(f"{self.tipo} ha ganado {self.succion} de energía.")
        self.energia += self.succion

