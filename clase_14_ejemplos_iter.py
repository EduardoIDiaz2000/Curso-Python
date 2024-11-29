# iteracion sobre una lista
frutas = ['manzana', 'banana', 'cereza']
for fruta in frutas:
    print(fruta)

# iteracion sobre un string
palabra = 'Python'
for letra in palabra:
    print(letra)

# iteracion sobre un range()
for i in range(5):
    print(i)

# Iteracion sobre un diccionario
persona = {'nombre': 'Ana',
           'edad': 15,
           'ciudad': 'Lima'}
for clave, valor in persona.items():
    print(clave, valor)

terma = {'material': 'borosilicato',
         'color': 'negro',
         'longitud': 1.20,
         'origen': 'China',
         'radiación': 'convección'}
for clave, valor in terma.items():
    print(f'{clave}:{valor}')

# Iteracion con enumerate
colores = ['rojo', 'verde', 'azul']
for indice, color in enumerate(colores):
    print(f'Indice {indice}:{color}')

    