"""
poo_8.py
Script en Python que tenga una lista de objetos tipo Película. La lista deberá ser ordenada según el nombre de las
películas, una vez ordenada, se mostrará la lista, además del menor y mayor objeto dentro de la colección.
"""
from pelicula import Pelicula


def main():
    peliculas = []
    peliculas.append(Pelicula('The Godfather', 'Francis Ford', 1972, 175))
    peliculas.append(Pelicula('Pulp Fiction', 'Quentin Tarantino', 1998, 162))
    peliculas.append(Pelicula('Casino', 'Martin Scorsese', 1985, 134))
    peliculas.append(Pelicula('Heat', 'Michael Mann', 1989, 155))
    peliculas.append(Pelicula('Hateful Eight', 'Quentin Tarantino', 2014, 125))

    peliculas.sort()
    # peliculas[0] == peliculas[1]

    for pelicula in peliculas:
        print(pelicula)
        print('-'*30)

    print(f'Menor película en la colección:\n {min(peliculas)}')
    print(f'Mayor película en la colección:\n {max(peliculas)}')


if __name__ == '__main__':
    main()
