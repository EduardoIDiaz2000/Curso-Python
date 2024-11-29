# try =   # codigo que puede generar un exepción

# Except = # código que maneja la excepción

valor = int(input('Ingresa un numero: '))
resultado = 10 / valor
print(f'El resultado es {resultado}')


################################################################
# Manejo de ValueError
try: # Se define un bloque de código donde se anticipa el error
    edad = int(input('Introduce tu edad:'))
    print(f'Tu edad es: {edad}')

except ValueError: # aqui es donde se maneja el error
    print('Error: debes introducir un numero')

#################################################################
# Manejo de multiples excepciones
try:
    divisor = int(input('Ingrese un numero divisor: '))
    resultado = 100/divisor
    print(f'El resultado es {resultado}')

except ValueError:
    print('Debe introducir un numero valido')

except ZeroDivisionError:
    print('Cero no es numero valido, reintente otra vez: ')

#################################################################
 # Manejo general de excepciones
try:
    nombre = input('Introduce tu nombre: ')
    print(f'Tu nombre es: {nombre}!')

except Exception as e:
    print(f'Ha ocurrido un error: {e}')


