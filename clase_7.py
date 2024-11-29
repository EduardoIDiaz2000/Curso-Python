# input() =  Para obtener informacion del usuario desde el teclado
name = input('Ingrese su nombre: ')
print(name)
print(type(name))

age = int(input('Ingrese su edad: ')) # Se le coloca int al inicio para que el valor sea un numero entero
print(age)
print(type(age))  # el resultado de ingresar informacion con la función input() siempre va ser string
# se puede cambiar normalmente el tipo de datos que queramos esperamos esperar
# ya se un float, string, int, booleano 