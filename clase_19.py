class Person: # class se usa para definir una plantilla, en este caso esta creando la plantilla Person
    def __init__(self, name, age): # def = esta definiendo el metodo constructor # __init__ = es el metodo especial llamado constructor # __ = los doble guiones indican que es un metodo especial  # self = es una regla en nombra el primer parametro asi # name y age = son los parametros
        self.name = name
        self.age = age  # aqui guarda el nombre y la edad

    def greet(self): # define la funcion saludo
        print(f'Hola, mi nombre es {self.name} y mi edad es {self.age}')

person1 = Person('Ana', 30) # esta creando una persona llamada Ana de 30 años
person2 = Person('Luis', 18)

person1.greet() # hace que Ana se presente
person2.greet()