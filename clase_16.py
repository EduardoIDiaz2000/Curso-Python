add = lambda a, b: a + b
print(add(10, 5))

multiply = lambda a, b: a * b
print(multiply(2, 5))

# Cuadrado de un numero
numbers = range(11)
square_numbers = list(map(lambda x: x ** 2, numbers))
print('Numeros al cuadrado',square_numbers)

# numeros pares
even_numbers = list(filter(lambda x: x % 2 == 0, numbers)) # de la lista de numbers de los 11 numeros, solo filtrara los numeros pares
print('Numeros pares: ', even_numbers)

# numeros impares
even_numbers2 = list(filter(lambda x: x % 2, numbers)) # de la lista de numbers de los 11 numeros, solo filtrara los numeros impares
print('Numeros impares', even_numbers2)