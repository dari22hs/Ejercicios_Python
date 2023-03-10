# r -> read
# w -> write
# a -> append
# r+ -> read + write
# b -> binary

"""archivo = open('mi_archivo.txt', 'r')
# archivo.write('Buenas noches')
archivo.read()
archivo.close()

with open('mi_archivo.txt', 'w') as archivo:
    for i in range(11):
        archivo.write(f"{i}\n")

with open('mi_archivo.txt', 'r') as archivo:
    for linea in archivo:
        print(linea, end="")"""

# Listar todos los archivos de la carpeta actual

'''import pathlib


ruta = pathlib.Path('.')

for archivo in ruta.iterdir():
    print(archivo)'''

# Listar todos los archivos de una carpeta y que contengan una extensión determinada

'''import pathlib

ruta = pathlib.Path('.')

for archivo in ruta.glob('*.txt'):
    print(archivo)'''

# Buscar un archivo en una carpeta, buscar si existe o no. En caso de existir, mostrará su tamaño.

'''import pathlib

ruta = pathlib.Path('.')

print("Buscar un arhivo dentro de la carpeta")
archivo = input("Nombre del archivo: ")

archivo = ruta / archivo

if archivo.exists():
    print(f"El archivo existe y mide {archivo.stat().st_size} bytes.")
else:
    print("El archivo no existe.")'''

# Mostrar todas las extensiones únicas de archivos existentes en carpetas

'''import pathlib


def main():
    ruta = pathlib.Path('.')

    extensiones = {archivo.suffix for archivo in ruta.iterdir()}
    print(f"Extensiones: {extensiones}")


if __name__ == '__main__':
    main()'''

# Generar un diccionario con las llaves siendo las extensiones únicas de los archivos encontrados en una carpeta y
# los valores una lista de los nombres de cada uno de dichos archivos

'''import pathlib


def main():
    ruta = pathlib.Path('.')

    diccionario = {k: [v.name for v in ruta.glob(f"*{k}")]
                   for k in {archivo.suffix for archivo in ruta.iterdir()}}

    for extension, archivos in diccionario.items():
        print(f"Extensión: {extension}")
        print(f"Archivos: {archivos}")


if __name__ == '__main__':
    main()'''

# Organizar el contenido de la carpeta actual. Generar una carpeta para cada tipo de archivo y todos los archivos del
# tipo correspondiente deberán ser movidos a la carpeta según su tipo

'''import pathlib


def main():
    ruta = pathlib.Path('.')

    diccionario = {k: [v for v in ruta.glob(f"*{k}")]
                   for k in {archivo.suffix for archivo in ruta.iterdir()}}

    for extension, archivos in diccionario.items():
        carpeta = ruta / extension[1:]
        carpeta.mkdir()
        for archivo in archivos:
            archivo.replace(carpeta / archivo.name)


if __name__ == '__main__':
    main()'''

import os
import shutil

# Write the name of the directory here,
# that needs to get sorted
path = 'C:/Users/DARIO/PycharmProjects/pptEjercicios/Ejercicios'

# This will create a properly organized
# list with all the filename that is
# there in the directory
list_ = os.listdir(path)

# This will go through each and every file
for file_ in list_:
    name, ext = os.path.splitext(file_)

    # This is going to store the extension type
    ext = ext[1:]

    # This forces the next iteration,
    # if it is the directory
    if ext == '':
        continue

    # This will move the file to the directory
    # where the name 'ext' already exists
    if os.path.exists(path + '/' + ext):
        shutil.move(path + '/' + file_, path + '/' + ext + '/' + file_)

    # This will create a new directory,
    # if the directory does not already exist
    else:
        os.makedirs(path + '/' + ext)
        shutil.move(path + '/' + file_, path + '/' + ext + '/' + file_)
