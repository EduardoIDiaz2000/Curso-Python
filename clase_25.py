class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name}, {self.age} años'
    
    def __repr__(self):
        return f'Person(name = {self.name}, age = {self.age})'
    
# Crear instancias en pytho de person
person1 = Person('Alice', 30)
person2 = Person('Luis', 14)

# Uso de __str__ # el metodo __str__ devuelve una representacion en cadena del objeto, útil para mensajes de salidas amigables
print(person1)

# Uso de __repr__ # método __repr__  devuelve una representacion más detallas del objeto, útil para la depuración
print(repr(person1))