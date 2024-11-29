def add(a, b): # aqui se esta definiendo la suma 
    return a + b

def subtracion(a, b): # definineod la resta
    return a - b

def multiply(a, b): # definiendo la multiplicacion
    return a * b

def divide(a, b): # definiendo la división
    return a/b

def calculator(): # definiendo la funcion calculadora
    while True: # Si es verdadero que imprima lo siguiente
        print('Seleccione una operación')
        print('1. Suma')
        print('2. Resta')
        print('3. Multiplicación')
        print('4. División')
        print('5. Salir')

        option = int(input('Ingrese una selección (1,2,3,4,5): ')) # la variables opcion es igual al imput este es un entero 

        if option == 5:
            print('Estas saliendo de la calculadora')
            break

        if option in [1,2,3,4]:
            num1 = float(input('Ingrese el primer numero: '))
            num2 = float(input('Ingrese el segundo numero: '))

            if option == 1:
                print('La suma es: ', add(num1, num2))

            elif option == 2:
                print('La resta es;', subtracion(num1, num2))

            elif option == 3:
                print('La multiplicación es: ', multiply(num1, num2))

            elif option == 4:
                print('La division es: ', divide(num1, num2))
        
        else:
            print('Opcion no valida, intente de nuevo')

calculator()
