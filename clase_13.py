numbers = [1 ,2, 3, 4, 5, 6] # iterar = significa recorrer o procesar los elementos
for i in numbers:
    print('Aqui i es igua a: ', i) # los valores de la lista se guardan en i

for i in range(3, 10): # range(3, 10) va iniciar desde el numero 3 hasta el numero 9, llegara hasta el 9 porque esa es la posición 10
    print(i)


fruits = ['manzana', 'pera', 'Uva', 'naranja', 'tomate']
for fruta in fruits: # aqui esta iterando todos los elementos de fruits en la variable fruta
    print(fruta)
    if fruta == 'naranja': # al iterar cuando llegue a naranja, ahi es cuando imprimira naranja encontrada
        print('Naranja encontrada')

x = 0
while x < 5:
    print(x)
    x += 1 # explicación = aqui le estamos diciendo que x es menor que 5
            # Por ende entrara al bucle while se imprimira el 0, de ahi se le sumara 1
            # Nuevamente ingresara al bucle se imprimira el 1 y nuevamente se le sumara 1
            # Entonces x seria 2 ingresaria de nuevo, y nuevamente ingresa y se le suma y se volveria 3
            # Y se detednra hasta que se cumpla la condición que x < 5

x = 0
while x < 5:
    if x == 3:
        break # se le pone la condición cuando llegue a 3 con la función break que pare el continuo
    print(x)    # si no cumple esa condición entonces que siga iterando hasta que cumpla la condición de while
    x += 1 

numbers = [1 ,2, 3, 4, 5, 6] 
for i in numbers:
    if i == 3: # aqui se le pone la condición cuando llegue a tres que lo omita y pase de frente al siguiente
        continue # osea ya no lo incluye al 3 sino pasa defrente al 4
    print('Aqui i es igua a: ', i)