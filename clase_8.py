to_do = ['Dirigirnos al hotel',
         'Ir a almorzar',
         'Visitar el museo',
         'Volver al hotel']

print(to_do)

#ahora entiendo que son los arrays - jonathan
number = [1, 2, 3, 4, 4, 'seis']
print(number)
print(type(number))

mix = ['uno', 2, 3, 4, 3.14, True, [1, 2, 3]] # puede contener diferentes tipos de datos
print(mix)
print(type(mix))

print(len(mix)) # la función len es para saber la logitud de la lista
print('primer elemento', mix[0]) # la indexación = permite acceder a los elementos individuales partiendo del 0
print('segundo elemento', mix[1])
print('tercer elemento', mix[2])
print('cuarto elemento', mix[3])
print('quinto elemento', mix[4])
print('Ultimo elemento', mix[-1]) # de derecha a izquierda se empieza con el -1, y asi sucvesivamente


string = 'Hola mundo' # A los string tambien se le conocen como cadenas 
print('primer elemento', string[0])
print('segundo elemento', string[1])
print('tercero elemento', string[2])
print('cuarto elemento', string[3])

# slicing = [incio: final]el incio es donde se quiere empezarar a tener los datos, eso se indica para sacar el grupo que se quiere de la lista
print(mix[0:2])
print(mix[1:4]) # la posicion final va al final pero restandole -1


# metodos
print(mix)
mix.append(False) # append = agrega elementos a la lista
print(mix)
mix.insert(1, ['a', 'b']) # inser = agrega elementos en una posición especifica
print(mix)

print(mix.index(False)) # index permite saber la posicion del elemento False

number = [1, 2, 3, 4.18, 93, 115, 4, 4]
print(number)
print('Elemento mayor: ', max(number)) # maximo valor de la lista
print('Elemento menor: ', min(number)) # minimo valor de la lista

del number[-1] # esta acción elimina un elemento de la posición -1
print(number)

del number[:2] # elimina una porcion de elemento del 0 al 2
print(number)

del number # esta acción elimina toda la lista
print(number)