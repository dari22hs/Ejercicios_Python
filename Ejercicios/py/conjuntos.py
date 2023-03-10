# No puede tener elementos repetidos
conjunto = set()
# conjunto = {1}
print(type(conjunto))
conjunto.add(2)
conjunto.add(2)
conjunto.add(3)
conjunto.add(4)
print(conjunto)
conjunto.add(5)
conjunto.add(6)
conjunto.add(7)
conjunto.add(1)
conjunto.pop()  # Quita un elemento aleatorio del conjunto
conjunto.remove(4)  # Retorna error si no encuentra el parámetro
conjunto.discard(4)  # NO regresa error si no encuentra el parámetro
print(conjunto)
print(f"Cantidad de elementos en el conjunto: {len(conjunto)}")
print(f"{55 in conjunto}")
