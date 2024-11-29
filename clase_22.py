class Person:
    def __init__(self, name, age):
        self.name = name # atributos
        self.age = age # atributos

    def greet(self):
        print(f'Mi nombre es {self.name} y tengo {self.age} años de edad') # <= Metodo

# Crear una instancia de la clase person

person1 = Person('Luis', 45)

person1.greet()