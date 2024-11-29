# Crear un iterador para los numeros impares
# Limte

limite = 30 # Se crea hasta donde sera el limite de los numeros impares

# Creando iterador
odd_itter = iter(range(1, limite+1, 2)) # se crea la variable odd_itter, se coloca la funcíón iter en el rango de 1 por es impar, el limite porque es hasta donde debe llegar
                                        # Y 2 por son saltos de 2 en dos

# Usando el iterador 
for num in odd_itter:
    print(num)