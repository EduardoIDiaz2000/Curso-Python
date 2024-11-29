numbers = {1:'uno', 2:'dos', 3:'tres'} # Los diccionarios son mutables, y puede contener diferentes tipos de datos
print(numbers[2])

information = {'nombre': 'Eduardo',
               'apellido': 'Diaz',
               'estatura': 1.65,
               'age': 24}
print(information)
del information['age']
print(information)

# Metodos propios de los diccionarios
claves = information.keys() # función clave o llaves
print(claves)
print(type(claves))

values = information.values() # valor
print(values)
print(type(values))

pair = information.items() # esta funcion extrae los pares de valor osea clave: valor
print(pair)

# vamos hacer una lista de contactos
contacts = {'Eduardo':{'Apellido': 'Diaz',
               'Estatura': 1.65,
               'Age': 24},
               'Lucero':{'Apellido': 'Supo',
               'Estatura': 1.65,
               'Age': 24}}
print(contacts)
print(contacts['Eduardo'])
print(contacts['Lucero'])

# Ejemplito
compras = {'leche': {'cantidad': 430,
                     'marca': 'gloria',
                     'nacionalidad': 'peruana',
                     'precio': 3.80},
                     'mantequilla':{'cantidad': 450,
                                    'marca': 'Dorina',
                                    'precio': 8,
                                    'nacionalidad': 'peruana'}}
print(compras)
print(compras['leche'])
print(compras['mantequilla'])