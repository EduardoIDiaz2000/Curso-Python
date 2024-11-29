class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self): # la clase person define un método greet() que imprime un saludo generico
        print('Hello! I am a person.')

class Student(Person): # es una subclase de la class person
    def __init__(self, name, age, student_id):
        super().__init__(name, age) # utiliza super().__init(name, age) para llamar al constructor  de la superclase Person y luego sobreescirbir el metodo greet() psra agregar información especfica 
        self.student_id = student_id

    def greet(self):
        super().greet()
        print(f"Hi, I'm {self.name} and I'm a student with ID:{self.student_id}")

student = Student('Raúl' ,23 ,'s1502')
student.greet()