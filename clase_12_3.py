is_member = True
age = 15
if is_member:
    if age >= 15:
        print('Tienes acceso ya que eres miembro y tu edad es igual o mayor que 15 años') # es cuando cumple con ambas conficiones
    else:
        print('No tienes acceso ya que eres miembro pero tu edad es menor a 15 años') # no tiene acceso porque no cumple con edad requerida
else:
    print('No eres miembro y NO TIENES ACCESO') # No es miembro y no tiene acceso porque no cumple ninguna de las condiciones
    
    