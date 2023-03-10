import random

'''lista = [i for i in range(11)]
print(lista)

lista2 = [i ** 2 for i in range(11)]
print(lista2)

aleatorio = [random.randint(1, 10) for i in range(20)]
print(aleatorio)'''

# matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(matriz[2][2])  # [Fila] [Columna]
# print(type(matriz))

''' Quiz
lista = ['Python', 'Developers']
result = [i for i in lista if len(i) > 6]
print(*result)


def my_function(a, b, c, d):
    print(a, b, c, d)


my_list = [1, 2, 3, 4], [5, 6], [7, 8], [9, 10]

my_function(*my_list)  # Se usa * para 'desempacar' la lista en cuatro elementos separados y se pueda tomar como cuatro argumentos
'''

N = 3

print(f"Programa que calcula la suma de matrices de tamaño {N} x {N}")

m1 = [[random.randint(1, 50) for j in range(N)] for i in range(N)]
m2 = [[random.randint(1, 50) for j in range(N)] for i in range(N)]
'''resultado = [[0]*N for i in range(N)]

for renglon in range(N):
    for columna in range(N):
        resultado[renglon][columna] = m1[renglon][columna] + m2[renglon][columna]'''

resultado = [[m1[i][j]+m2[i][j] for j in range(N)] for i in range(N)]

'''for i in range(N):
    if i == N//2:
        print(f"{m1[i]} + {m2[i]} = {resultado[i]}")
    else:
        print(f"{m1[i]} + {m2[i]} = {resultado[i]}")'''

for i in range(N):
    print(f"{m1[i]} + {m2[i]} = {resultado[i]}") if i == N//2 else print(f"{m1[i]} + {m2[i]} = {resultado[i]}")
# print(f"La matriz uno es: {m1}")
# print(f"La matriz dos es: {m2}")
# print(f"La suma de las matrices es: {resultado}")

