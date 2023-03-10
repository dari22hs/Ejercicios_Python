def validar_expresion(expresion):
    pila = []
    for simbolo in expresion:
        if simbolo == '(':
            pila.append('(')
        elif simbolo == ')':
            if len(pila) > 0:
                pila.pop()
            else:
                return False
    return len(pila) == 0


def main():
    print('Bienvenido. Escriba una expresión aritmética')
    e = input("Expresión aritmética: ")
    valida = validar_expresion(e)
    if valida:
        print("La expresión sí está balanceada")
    else:
        print("La expresión no está balanceada")
    print("Chao")


if __name__ == '__main__':
    main()
