# Ejercicio de concesionario de vehiculos Chinos
# ------- Elaborado por Eduardo Diaz ----------


class Vehicle: # definicion de la clase vehiculo
    def __init__(self, model, price): # definicion del metodo constructor con parametros como modelo y precio
        self.model = model # asignando el parametro model al atributo self.model
        self.price = price # asignando el paramentro price al atributo self.price
        self.available = True # indicando que esta disponible vehiculo
    
    def sold(self): # definicion que el vehiculo va ser vendido
        if self.available: # verifico si esta disponible
            self.available = False # en este caso el vehiculo se esta vendiendo, y por lo tanto ya no esta disponible
            print(f'El vehiculo {self.model} ha sido vendido') # Imprimo que el vehiculo ha sido vendio

        else: # en caso que el modelo no este disponible imprimira lo siguiente
            print(f'El vehiculo {self.model} no se encuentra disponible') # que el modelo no se encuentra disponible

    def change_price(self, new_price): # definicion del cambio de precio
        self.price = new_price  # atributo price del objeto actual que asigna el valor del nuevo precio a altributo precio
        print(f'El precio del vehiculo {self.model} ha sido actulizado a {self.price}') # despues imprime un mensaje haciendo mencion que el precio del vehiculo ha sido actualizado a otro monto

    def display_info(self): # se define la funcion de mostrar informacion
        if self.available: # verifico si esta disponible
            availability = 'disponible'
        else:
            availability = 'No disponible'
        print(f'El modelo {self.model}, precio {self.price}, se encuentra {availability}')

    def reserve(self): # Se define la funcion reserva del vehiculo
        if self.available: # verifico si esta disponible
            self.available = False
            print(f'El vehiculo {self.model} se encuentra reservado')
        else:
            print(f'El vehiculo {self.model} no se encuentra para reserva')

    def cancel_reservation(self): # se define la cancelacion de la reserva del vehiculo
        if not self.available: # Si el vehiculo no esta disponible
            self.available = True # Cambia su estado a disponible
            print(f'La reserva del vehiculo {self.model} se ha cancelado') # Y imprime un mensaje que la reserva se ha cancelado
        else: # condición
            print(f'El vehiculo {self.model} se encuentra en reserva') # Si el vehiculo esta disponible imprime un mensaje que esta disponible la reserva del vehiculo

model1 = Vehicle('Changan', '22400') # Creando el modelo 1 con su respectivo precio en dolares
model2 = Vehicle('Geely', '22000') # Creando el modelo 2 con su respectivo precio en dolares
model3 = Vehicle('Gac', '27000') # Creando el modelo 3 con su respectivo precio en dolares

model1.display_info() # Se pide la informacion del modelo 1
model2.display_info() # Se pide la información del modelo 2
model3.display_info() # Se pide la informacion del modelo 3

model1.change_price(30000) # Se realiza el cambio del precio en el modelo 1

model2.reserve() # Se realiza la reserva del modelo 2

model2.reserve() # Se pide nuevamente la reserva del modelo 2

