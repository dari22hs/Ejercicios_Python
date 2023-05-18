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


'''def my_fun(n):
    if n == 1:
        return 1
    else:
        return n + my_fun(n - 1)


print(my_fun(5)) # Output -> 15'''

# Quiz 14
'''a = [1, 2, 3]
b = a.copy()
print(a == b, a is b) # Output -> True False'''

# Quiz 15
'''x = 10
y = 3
result = x // y + x % y
print(result) # Output -> 4'''

# Quiz 16
'''aTuple = 1, 2, 3
a, b, c = aTuple
print(a) # Output -> 1'''

# Quiz 17
'''a = 4/5
b = 5//4
print(a * b) # Output -> 0.8'''

# Quiz 18
'''for i in range(1, 5):
    for j in range(i):
        if i % j == 0:
            break
        else:
            print(i, end="")'''
# Output -> ZeroDivisionError: integer division or modulo by zero

# Quiz 19
'''x = 10
y = 3
result = x / y
print(result) # Output -> 3.3333333333333335'''

# Quiz 20
'''a = "python"
b = "hub"
print(a[1:] + b[1:]) # Output -> "ythonub"'''

# Quiz 21
'''x = 0
while x < 3:
    x += 1
else:
    print(x) # Output -> 3'''

# Quiz 22
'''num = 6
while num >= 0:
    print(num, end="")
    num -= 2 if num % 3 == 0 else 1'''
    # Output -> 64310

# Quiz 23
'''num = 7
while num > 0:
    print(num, end="")
    num //= 2'''
    # Output -> 731

# Quiz 24


'''def f(x, y):
    x = y + 2
    return x + y


print(f(2, 3)) # Output -> 8'''

# Quiz 25
'''x = 5
while x > 0:
    x -= 1
    if x == 2:
        continue
    print(x) # Output 4 3 1 0'''

# Quiz 26
'''myList = [1, 2, 3, 4, 5]
for i in range(len(myList)):
    myList[i] += 1
print(myList) # Output -> [2, 3, 4, 5, 6]'''

# Quiz 27
'''for num in range(10):
    if num < 5:
        continue
    elif num > 8:
        break
    print(num, end=" ") # Output 5 6 7 8'''

# Quiz 28
'''numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        continue
    print(num ** 2, end=" ") # Output -> 1 9 25'''

# Quiz 29
'''i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i, end=" ") # Output -> 1 2 4 5'''

# Quiz 30
numbers = [1, 2, 3, 4, 5]
result = [n for n in numbers if n % 2 == 0]
print(result) # Output -> [2, 4]

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
