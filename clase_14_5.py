# Serie de fibonacci
# 0 1 1 2 3 5 8 13 21 34 55 89 144...

def fibonacci(limit): # la funcion fibonacci es una fabrica de numeros => limit: es el numero que queremos alcanzar
    a, b = 0, 1 # a = 0 y b = 1  ; en la serie de fibonacci se empezara como 2 numero a y b, 0 y 1
    while a < limit: # el bucle while va continuar mientras a sea menor que el limite
        yield a # aqui produce el prime numero actual de fibonacci
        a, b = b, a + b # aqui prepara los siguiente dos numeros de la secuencia

for num in fibonacci(250): # el bucle for que esta fuera de la funcion pide numeros de la fabrica
    print(num) # pide uno por uno   