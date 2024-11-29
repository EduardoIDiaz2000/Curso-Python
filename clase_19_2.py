class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f'Hola, mi nombre es {self.name} y mi edad es {self.age} años')

person1 = Person('Luis', 45)
person2 = Person('Maycol', 82)

person1.greet()
person2.greet()