# Encontrar el primer numero divisible por 5 y por 7
for num_divisible in range(1, 200):
    print(num_divisible)
    if num_divisible % 7 == 0 and num_divisible % 5 == 0:
        print('El primer numero divisible entre 5 y 7 es: ', num_divisible)
        break

# Buscar un elemento en la lista
numeros = [4, 6, 7, 1, 8, 3, 6]
buscar = 8
for numero in numeros:
    print(numero)
    if numero == buscar:
        print('Numero encontrado', numero)
        break
    else:
        print('El numero no fue encontrado en la lista', numero)