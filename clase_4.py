name = 'Eduardo'
print(name)
print(type(name))

caracter = 'c'
print(caracter)
print(type(name))

name_2 = '''Ignacio
Diaz
Mollocondo''' # Las comillas simples triples son sencibles al salto de linea
print(name_2)
print(type(name_2))

# Ahora en esta parte vamos a ver la posicion de cada letra
print(name_2[0]) # Partiendo desde el 0 hasta el infinito, la lectura se realizara de izquierda a derecha
print(name_2[1])
print(name_2[2])
print(name_2[3])
print(name_2[4])
print(name_2[5])
print(name_2[-1]) # La lectura se realizara de derecha a izquiera y se comenzara en -1
print(name_2[-2])
print(name_2[-3])
print(name_2[-4])
print(name_2[-5])
print(name_2[-6])
print(name_2[-7])


nombre = 'Eduardo Ignacio'
apellido = 'Diaz Mollocondo'

print(nombre)
print(nombre + ' ' + apellido) # concatenación
print(len(nombre)) # función len = permite ver la longitud del texto
print(len(apellido))


print(nombre.lower()) # convierte todo a minuscula
print(nombre.upper()) # convierte todo a mayuscula
print(nombre.capitalize()) # convierte el primer caracter en mayuscula
print(nombre.casefold()) # convertira todo a minusculas
print(nombre.count('o'))# realice el conteo de la letra dentro de las comillas
