# generador = es una función que produce una secuencia de numeros
# en los cuales podemos iterar

def my_generator(): # Se define la función my_generator 
    yield 1 # Cada yield es como un boton que produce un numero y luego se detiene
    yield 2 # este boton produce otro numero
    yield 3

for values in my_generator():
    print(values) # cuando se hace correr el programa se pide el primer numero osea el 1
                    # de ahi se pide el siguiente que es el numero 2
                    # de ahi se pide el siguiente que es el numero 3
                    # despues ya no hay mas numeros, asi que se cierra el programa