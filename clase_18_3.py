def suma_naturales(n):
    if n == 1:
        return 1
    else:
        return (n * (n + 1))/2
    
numero = 25
print(suma_naturales(numero))

def sum_naturales_impares(n):
    if n == 1:
        return 1
    else:
        return 2 * n -1
    
numero_2 = 10
print(sum_naturales_impares(numero_2))

def sum_naturales_pares(n):
    if n == 1:
        return 1
    else:
        return 2 * n
    
numero_3 = 4
print(sum_naturales_pares(numero_3))