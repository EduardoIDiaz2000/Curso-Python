class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f'Hola, mi nombre es {self.name} y tengo {self.age} años')

person1 = Person('Anita', 21)
person2 = Person('Luis', 30)

person1.greet()
person2.greet()