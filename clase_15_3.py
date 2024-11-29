# Replica del ejercicio 3
def add(a, b):
    return a + b

def subtracion(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def calculator():
    while True:
        print('Selección una operación: ')
        print('1. Suma')
        print('2. Resta')
        print('3. Multiplicación')
        print('4. División')
        print('5. Saliendo ')

        option = int(input('Ingrese una elección (1,2,3,4,5): '))

        if option == 5:
            print('Saliendo de la calculadora')

        if option in [1,2,3,4]:
            num1 = float(input('Ingrese el primer numero: '))
            num2 = float(input('Ingrese el segundo numero: '))

            if option == 1:
                print('La suma es: ', add(num1, num2))

            if option == 2:
                print('La resta es: ', subtracion(num1, num2))

            if option == 3:
                print('La multiplicación es: ', multiply(num1, num2))

            if option == 4:
                print('La división es: ', divide(num1, num2))

        else:
            print('La opcion no es válida, reintente otra vez')

calculator()

            