"""x = ',-,'.join(['nombre', 'apellido'])
print(x)

cadena = "Qué mira bobo, qué mira bobo?"
cadena = cadena[:4] + 'M' + cadena[5:]
print(cadena)"""

# Hangman game
import random
import os

MAX_FALLOS = 5
paises = ['Alemania', 'Argentina', 'Bahamas', 'Belice', 'Canadá', 'Croacia', 'España', 'Francia', 'Guatemala', 'Bolivia', 'Brasil', 'Chile', 'Colombia',
          'Costa Rica', 'Cuba', 'Ecuador', 'Estados Unidos', 'México', 'Marruecos', 'Países Bajos', 'Polonia']
paises.sort()


def crear_cadena():
    pais = random.choice(paises)
    secreto = '_' * len(pais)
    return pais, secreto


def reemplazar_simbolo(original, secreto, simbolo):
    cantidad = original.count(simbolo)
    inicio = 0
    for i in range(cantidad):
        pos = original.find(simbolo, inicio)
        secreto = secreto[:pos] + simbolo + secreto[pos+1:]
        inicio = pos + 1
    return secreto


def ahorcado():
    original, secreto = crear_cadena()
    fallos = 0

    print(paises)

    print("\tEL JUEGO DEL AHORCADO")
    print(f"Adivina el nombre del país. Tiene {len(original)} letras y puedes fallar hasta {MAX_FALLOS} veces.")
    print("* Ten cuidado con acentos, espacios y mayúsculas *")
    input("Presiona ENTER para comenzar ...")

    while secreto != original and fallos < MAX_FALLOS:
        os.system('cls')
        print(f"Palabra: {secreto}")
        entrada = input("Ingresa una letra: ")

        if entrada in original:
            secreto = reemplazar_simbolo(original, secreto, entrada)
            print("¡BIEN!")
        else:
            print("¡FALLASTE!")
            fallos += 1
            print(f"Te quedan {MAX_FALLOS-fallos} intentos ...")
        input("Presiona ENTER para continuar ...")

    os.system('cls')
    if secreto == original:
        print(f"¡SOS UN CRACK! Has acertado, el país es {secreto}.")
    else:
        print(f"¡ANDÁ PA' SHA, BOBO! Perdiste, el país era {original}.")

    print("¡Hasta la próxima!")


def main():
    ahorcado()


if __name__ == '__main__':
    main()


# secreto = reemplazar_simbolo('crayola', '_______', 'a')
# print(secreto)
# original, secreto = crear_cadena()
# print(original)
# print(f"El país tiene {len(original)} letras")
# print(secreto)
