"""
poo_7.py
Script en Python que simule un personaje y un grupo de enemigos que podrán atacar al personaje principal de forma
especial según su naturaleza. Los enemigos serán modelados con clases y se hará uso de polimorfismo para permitirles
atacar de manera personalizada.
"""
import enemigo
import os
import random


def main():
    enemigos = []

    for i in range(5):
        tipo_enemigo = random.randint(0, len(enemigo.tipos)-1)
        if tipo_enemigo == enemigo.MOMIA:
            enemigos.append(enemigo.Momia())

        elif tipo_enemigo == enemigo.ZOMBIE:
            enemigos.append(enemigo.Zombie())

        elif tipo_enemigo == enemigo.YETI:
            enemigos.append(enemigo.Yeti())

        elif tipo_enemigo == enemigo.HOMBRE_LOBO:
            enemigos.append(enemigo.HombreLobo())

        elif tipo_enemigo == enemigo.PIE_GRANDE:
            enemigos.append(enemigo.PieGrande())

        elif tipo_enemigo == enemigo.CENTAURO:
            enemigos.append(enemigo.Centauro())

        elif tipo_enemigo == enemigo.MINOTAURO:
            enemigos.append(enemigo.Minotauro())

        elif tipo_enemigo == enemigo.RAKE:
            enemigos.append(enemigo.Rake())

        elif tipo_enemigo == enemigo.LA_GORDA:
            enemigos.append(enemigo.LaGorda())

        else:
            enemigos.append(enemigo.Vampiro())

    # for e in enemigos:
    #     # os.system('cls')
    #     e.atacar()
    #     input('\nPresione ENTER para continuar ...')

    personaje = {'energia': 50, 'fuerza': 40}
    GANANCIA_DE_ENERGIA = 5
    INCREMENTO_FUERZA = 3

    while personaje['energia'] > 0 and len(enemigos) > 0:
        while personaje['energia'] > 0 and enemigos[0].energia > 0:
            os.system('cls')
            print(f"Energía: {personaje['energia']}.   {enemigos[0].tipo}:{enemigos[0].energia}")
            enemigos[0].atacar()
            personaje['energia'] -= enemigos[0].fuerza
            if personaje['energia'] > 0:
                print(f"Has atacado a {enemigos[0].tipo} y causaste {personaje['fuerza']} de daño.")
                enemigos[0].energia -= personaje['fuerza']
                input("Continuar batalla ...")
        if personaje['energia'] > 0:
            os.system('cls')
            print(f"Energía: {personaje['energia']}.   {enemigos[0].tipo}:{enemigos[0].energia}")
            print(f"Has derrotado a {enemigos[0].tipo}")
            print(f"Has recuperado {GANANCIA_DE_ENERGIA} de energía")
            print(f"Tu fuerza ha aumentado {INCREMENTO_FUERZA} puntos.")
            personaje['energia'] += GANANCIA_DE_ENERGIA
            personaje['fuerza'] += INCREMENTO_FUERZA
            enemigos.pop(0)
            input('Continuar aventura ...')

    if personaje['energia'] > 0:
        print('¡Has vencido a todos tus rivales!')
    else:
        print('Has sido derrotado. Pillaste.')


if __name__ == '__main__':
    main()
