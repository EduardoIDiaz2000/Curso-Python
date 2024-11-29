class Vehicle():
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True

    def sell(self):
        if self.is_available:
            self.is_available = False
            print(f'El {self.brand} ha sido vendido')
        else:
            print(f'El {self.brand} no esta disponible')

    def check_available(self): # definicion si el vehiculo esta disponible para la venta
        return self.is_available # returna el valor del atributo is_available si es true estara disponible si es false no lo estara
    
    def get_price(self):
        return self.price # returna el valor del atributo
    
    def start_engine(self):
        raise NotImplementedError ('Este método debe ser implementado en la subclase')
    
    def stop_engine(self):
        raise NotImplementedError ('Este método debera ser implementado en la subclase')
    
class Car(Vehicle):
    def start_engine(self):
        if not self.is_available:
            return f'El motor del {self.brand} esta en marcha'
        
        else:
            return f'El coche {self.brand} no esta disponible'
        
    def stop_engine(self):
        if self.is_available:
            return f'El motor del coche {self.brand} se ha detenido' # esto quiere decir que ya esta disponible o que solo se ha detenido
        else:
            return f'El coche {self.brand} no esta disponible'
        
class Bike(Vehicle):
    def start_engine(self):
        if not self.is_available:
            return f'El móvil ya {self.brand} esta en marcha'
        
        else:
            return f'El móvil {self.brand} no esta disponible'
        
    def stop_engine(self):
        if self.is_available:
            return f'El móvil {self.brand} se ha detenido' # esto quiere decir que ya esta disponible o que solo se ha detenido
        else:
            return f'El móvil {self.brand} no esta disponible'
        
class Truck(Vehicle):
    def start_engine(self):
        if not self.is_available:
            return f'El motor del {self.brand} esta en marcha'
        
        else:
            return f'El coche {self.brand} no esta disponible'
        
    def stop_engine(self):
        if self.is_available:
            return f'El motor del coche {self.brand} se ha detenido' # esto quiere decir que ya esta disponible o que solo se ha detenido
        else:
            return f'El coche {self.brand} no esta disponible'
        
class Customer: # esta clase define la clase cliente
    def __init__(self, name):
        self.name = name
        self.purchased_vehicles = []

    def buy_vehicles(self, vehicle: Vehicle): # permite comprar un vehiculo al cliente y tiene como parametro el vehiculo
        if vehicle.check_available(): # Si esta disponible para la venta llama al metodo check.available
            vehicle.sell() # si el vehiculo se encuentra disponible entonces llama al metodo vender
            self.purchased_vehicles.append(vehicle) # el vehiculo es añadida a la lista self.purchased_vehicles

        else: # en caso if no se cumpla osea que no este disponible
            print(f'Lo siento, {vehicle.brand} no se encuentra disponible')

    def inquire_vehicle(self, vehicle: Vehicle):
        if vehicle.check_available(): # verifica si esta disponible
            availability = 'Disponible' # Asigna un mensaje que esta disponible
        else: # en caso no se cumpla if
            availability = 'No disponible'
            print(f'El {vehicle.brand} esta {availability} y cuesta {vehicle.get_price()}') # se imprime la disponiblidad del vehiculo y el precio

class Dearlership: # se define la clase consecionaria
    def __init__(self):
        self.inventory = []
        self.customers = []

    def add_vehicle(self, vehicle: Vehicle):
        self.inventory.append(vehicle)
        print(f'El {vehicle.brand} ha sido añadido al consecionario de vehiculos')

    def register_customer(self, customer: Customer):
        self.customers.append(customer)
        print(f'El cliente {customer.name} ha sido añadido')

    def show_available_vehicle(self): # permite registrar los vehiculos en el concesionario
        print(f'Vehiculos disponibles en la tienda')
        for vehicle in self.inventory:
            if vehicle.check_available():
                print(f'- {vehicle.brand} por {vehicle.get_price()}')

# Creacion de los objetos de los vehiculos
car1 = Car('Toyota', 'Hilux 4x4', 35000)
bike1 = Bike('Oxford', 'MT-07', 1500)
Truck1 = Truck('Volvo', 'FHT16', 80000)

# Creación del objeto cliente
customer1 = Customer('Luis')

dearlership = Dearlership()
dearlership.add_vehicle(car1)
dearlership.add_vehicle(bike1)
dearlership.add_vehicle(Truck1)

# Mostra los vehiculos disponibles
dearlership.show_available_vehicle()

customer1.inquire_vehicle(car1)

customer1.buy_vehicles(car1)

