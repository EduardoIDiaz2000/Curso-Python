# numeros pares

def num_pares(limit):
    numero = 0
    while numero < limit:
        yield numero
        numero += 2

for pares in num_pares(25):
    print(pares)

def num_impares(limit):
    numero = 1
    while numero < limit:
        yield numero
        numero += 2

for impares in num_impares(25):
    print(impares)