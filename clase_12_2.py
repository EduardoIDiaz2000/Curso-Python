# con varias condicionales
x = 15
y = 20
if x > 10 and y > 15: # and cuando los dos son verdaderos
    print('X es mayor a 10 y Y es mayor a 15')

if x > 20 or y > 18: # or cuando solo uno de ellos son verdaderos
    print('X es menor que 20 y Y es mayor a 18')

if not x > 17: # not cuando no queremos que sea verdadero
    print('X no es mayor que 17')