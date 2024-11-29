class LivingBeing: # es la clase base que inicializa con el atributo name
    def __init__(self, name):
        self.name = name

class Person(LivingBeing): # person es una subclase de LivingBeing que inicializa name a traves __init__ (name)
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

class Student(Person): # student es una subclase de person que inicializa (name, age) a traves de __init__ (name, age, student_id)
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        print(f"Hi, I'm {self.name}, {self.age} years old, and my ID is:{self.student_id}")

# Cracion de instancia
student = Student('Marco', 23, 'S1234')
student.introduce()