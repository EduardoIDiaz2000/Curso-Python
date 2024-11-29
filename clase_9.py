a = [1,2,3,4,5,]
b = a
print(a)
print(b)
del a[0]
print(id(a)) # función id = devuelve un identificador unico para un objeto
print(id(b)) # es numero es unico para cada objeto

c = a[:] # la variable esta copiando solo los elemento de a pero el id de a o su lugar de almacenamiento    
print(id(c))

a.append(6)
print(a)
print(b)
print(c)