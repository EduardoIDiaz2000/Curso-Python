print('Nunca pares de aprender')

print('Nunca', 'pares', 'de', 'aprender') # el uso de coma en Python añade automaticamente los espacios

print('Nunca' + 'pares' + 'de' + 'aprender')

# para agregar espacio el uso de comilla ' '
print('Nunca' + ' ' + 'pares' + ' ' + 'de' + ' ' + 'aprender')

# uso de sep
print('Nunca', 'pares', 'de', 'aprender', sep=',') # sep separa los elementos con una coma. se puede usar cualquier otro caracter

# uso de end
print('Nunca', end=' ')
print('pares de aprender') # end permite que al imprimir se realice en una sola linea

# Impresión de las variables
frase = 'Nunca pares de aprender'
Author = 'Platzi'

print('Frase:', frase, 'Author:', Author)

# Formato de f-string
frase = 'Nunca pares de aprender'
author = 'platzi'

print(f'frase:{frase}, Author:{author}')

# Uso de formato Format
frase = 'Nunca pares de aprender'
author = 'platzi'

print('Frase:{}, Author:{}'.format(frase, author))


# Formato especifico
valor = 3.14159
print('Valor:{:.2f}'.format(valor)) # :.2f indica la cantida de cifras significativas que se imprima

# Saltos de lineas y caracteres especiales
print('Hola \nmundo ') # Salto de linea


