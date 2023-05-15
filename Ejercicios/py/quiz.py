# Quiz 1
''"""l = list("1234")
print(l)
l[0] = l[1] = 5
print(l)  # Output -> [5, 5, '3', '4']"""

# Quiz 2
'''a = [0, 1, 2, 3]

for a[-1] in a:
    print(a[-1])  # Output -> 0 1 2 2'''

# Quiz 3
'''a = 2*2//2
b = 3//2*3
print(a, b)  # Output -> 2, 3'''

# Quiz 4
'''a = 35
print("%f"%a)  # Output -> 35.000000  Float imprime 6 dígitos por defecto después del punto'''

# Quiz 5
'''dict1 = {"key1": 1, "key2":2}
dict2 = {"key2": 2, "key1":1}
print(dict1 == dict2)  # Output -> True porque los diccionarios no son ordenados'''

# Quiz 6
'''

def f():
    pass


print(type(f()))  # Output -> <class 'NoneType'>'''

# Quiz 7
'''a = '2'
b = '2'
print(a+b)  # Output -> 22  -> Junta las cadenas'''

# Quiz 8


'''def fun():
    return "str" + 'char'


print(fun())  # Output -> strchar -> Junta las cadenas '''

# Quiz 9

'''myList = [3, 2, 1, 4, 5]
result = sorted(myList)[2:]
print(result)  # Output -> [3, 4, 5]'''

# Quiz 10

'''try: print(1)
except: print(2)
finally: print(3)'''

# Output -> 1, 3

# Quiz 11

'''x, y = 5, 3
result = (x ** y) % 4
print(result) # Output -> 1'''

# Quiz 12

'''a = 100
b= 5
print(a//b*a/b) # Output -> 400.0'''

# Quiz 13


def my_fun(n):
    if n == 1:
        return 1
    else:
        return n + my_fun(n - 1)


print(my_fun(5)) # Output -> 15
# def print_pine_tree(n):
#     if n < 4:
#         print("Nope. Make it at least 4.")
#     else:
#         for i in range(n):
#             print(" " * (n - i - 1) + "*" * (2 * i + 1))
#         for i in range(2):
#             print(" " * (n - 2) + "***")
#
#
# print_pine_tree(15)
