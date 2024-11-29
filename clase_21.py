class Vehicle: # Se define la clase llamada vehiculo, esta clase sirve para crear objetos
    def __init__(self, brand, model, price): # se define el método constructor, bajo los parametros marca, modelo y precio  
        # Encapsulación
        self.brand = brand # Se asigna el parametro brand al atributo brand
        self.model = model # Se asigna el parametro model al atributo model
        self.price = price # Se asigna el parametro price al atributo price
        self.is_available = True # INicializa el atributo is_available como True indicando que el vehiculo esta disponible a la venta

    def sell(self): # definicion de la funcion vender
        if self.is_available: # verifica si el vehiculo esta disponible para la venta
            self.is_available = False # Si el vehiculo esta disponible cambia el valor a False para indicar que ya ha sido vendido
            print(f'El vehiculo {self.brand}. Ha sido vendido') # Imprime un mensaje indicando que ya ha sido vendido
        else: # Si la condición anterior no se cumple
            print(f'El vehiculo {self.brand}. No esta disponible') # Entonce imprimea un mensaje indicando la marca y que ya no esta disponible

    # Abstracción
    def check_available(self): # definicion si el vehiculo esta disponible para la venta
        return self.is_available # retorna el valor del atributo is_available si este es True el vehiculo estara disponible, si es False, no lo esta
    
    def get_price(self): # definicion de obtener el precio del vehiculo
        return self.price # devuelve el valor del atributo
    
    def start_engine(self): # definición del método abstracto para iniciar el motor
        raise NotImplementedError('Este metodo debe ser implementado por la subclase') # Lanza un NotImplementedError indicando que este metodo debe ser implemento por una subclase

    def stop_engine(self): # definición del metodo abstracto para detener el motor
        raise NotImplementedError('Este metodo debe ser implementado por la subclase') # Lanza un NotImplementedError indicando que este metodo debe ser implmentado por una subclase

# Herencia
class Car(Vehicle): # la clase Car hereda de la clase Vehicle, esto quiere decir que Car tiene acceso a todos los metodos y atributos definidos en Vehicle
        # Polimorfismo
        def start_engine(self): # define el inicio del motor del coche
            if not self.is_available: # si no esta disponible, quiere decir que el motor ya esta andando
                return f'El motor del coche {self.brand} está en marcha' # Es por eso que imprime que el motor ya esta en marcha 
            
            else: # Si la condición anterior no se cumple
                return f'El coche {self.brand} no esta disponible' # En este caso caso indica que si el coche esta en en uso no esta disponible

        # Polimorfismo   
        def stop_engine(self): # define la detención del motor
            if self.is_available: # Si el atributo del is_available es True, el coche esta disponible para usarlo
                return f'El motor del coche {self.brand} se ha detenido' # Con esto imprime que el motor se ha detenido y es posible usarlo
            else: # en el caso no se cumpla if
                return f'El coche {self.brand} No esta disponible' # Se asume que el motor ya se ha detenido o no se puede detener indicando que el coche no esta disponible
                    
# Herencia
class Bike(Vehicle): # la clase bike hereda todos los atributos y metodos de Vehicle
        # Polimorfismo
        def start_engine(self): # define que la bicicleta esta en movimiento
            if not self.is_available: # Si la bicicleta no esta disponible, indica que ya esta en uso 
                return f'La bicicleta {self.brand} está en marcha' # Por eso imprime que la bicicleta ya esta en marcha
            
            else: # en caso no se cumpla el if
                return f'La bicicleta {self.brand} no esta disponible' # Indica que la bicicleta esta en uso

        # Polimorfismo  
        def stop_engine(self): # define que la bicicleta esta en movimiento
            if self.is_available: # Si la bicicleta esta dispoble
                return f'La bicicleta {self.brand} se ha detenido' # Indica que la bicicleta se ha detenido, esto quiere decir que esta disponible
            else: # en caso no se cumpla if
                return f'La bicicleta {self.brand} No esta disponible' # Indica que la bicicleta se ha detenido o aun no se ha podido detener por eso no esta disponible

class Truck(Vehicle): # la clase truck hereda todos los atributos y metodo de Vehicle
        def start_engine(self):
            if not self.is_available:
                return f'El moto del camión {self.brand} está en marcha'
            
            else:
                return f'El camión {self.brand} no esta disponible'
            
        def stop_engine(self):
            if self.is_available:
                return f'El motor del camión {self.brand} se ha detenido'
            else:
                return f'El camión {self.brand} No esta disponible'
            
class Customer: # define la clase cliente
        def __init__(self,name): # se usa el metodo constructor con parametro nombre
            self.name = name # Se almacena en name el nombre del cliente
            self.purchased_vehicles = [] # Se almacena en purchased_vehicles la lista de vehiculos comprados por el cliente

        def buy_vehicle(self, vehicle: Vehicle): # Permite comprar un vehiculo al cliente y tiene como parametro al vehicle
            if vehicle.check_available(): # si el vehiculo esta disponible llama al check.available del vehiculo 
                vehicle.sell() # si el vehiculo esta disponible llama al metodo sell y lo añade a la lista 
                self.purchased_vehicles.append(vehicle) # se añade a la lista self.purchased_vehicles 
            else:
                print(f'Los siento.{vehicle.brand} no está disponible')

        def inquire_vehicle(self, vehicle: Vehicle): # se define la función consultar la disponiblidad y precio del vehiculo
            if vehicle.check_available(): # si esta disponible llama al check.available del vehiculo
                availability = 'Disponible' # asigna la disponiblidad del vehiculo
            else: # en caso no se cumpla if 
                availability = 'No disponible' # asigna la indisponibilidad del vehiculo 
            print(f'El {vehicle.brand} esta {availability} y cuesta {vehicle.get_price()}') # aqui imprime la disponiblidad del vehiculo y el precio

class Dearlership: # define la clase consecionaria, modela el concesionario de vehiculos
    def __init__(self): # 
        self.inventory = [] # inventory almacena una lista de objetos de tipo vehicle wue representan los vehiculos disponibles en el concesionario
        self.customers = [] # almacena una lista de objetos de tipo customers que representan a los clientes registrados en el concesionario 

    def add_vehicle(self, vehicle: Vehicle): # Permite agregar un vehiculo al inventario del concesionario
        self.inventory.append(vehicle) # agrega el vehiculo a la lista  de inventario self.inventory utilizando el método append    
        print(f'El {vehicle.brand} ha sido añadido al inventario') # Imprime un mensaje indicando la marca que se ha añadido al inventario

    def register_customers(self, customer: Customer): # Ṕermite registrar a un cliente en el concesionario 
        self.customers.append(customer) # agrega un cliente a la lista lista de clientes self.customers utilizando el método append
        print(f'El cliente {customer.name} ha sido añadido') # Imprime un mensaje indicando el registro del nombre del cliente

    def show_available_vehicle(self): # Permite registrar los vehiculos disponibles en el concesionario
        print(f'Vehiculos disponibles en la tienda') # Imprime un encabezado indicando que se mostraran los vehiculos disponibles en la tienda
        for vehicle in self.inventory: # Itera sobre cada vehiculo en la lista del inventario del concesionario
            if vehicle.check_available(): # verifica si el vehiculo actual esta disponible utilizando el método vehicle.check_available del objeto vehicle
                print(f'-{vehicle.brand} por {vehicle.get_price()}') # Imprime un mensaje indicando la marca del vehiculo y el precio 

car1 = Car('Chagan', 'Unit', 40000) # Crea un objeto car1 con la marca, modelo el precio
bike1 = Bike('Oxford', 'MT-07', 1100) # Crea un objeto bike1 bicicleta con la marca, modelo y precio
truck1 = Truck('Volvo', 'FHT16', 80000) # Crea un objeto truck1 con la marca, modelo y precio 

customer1 = Customer('Luis') # Crea un objeto cliente de nombre Luis

dealership = Dearlership() # Crea un objeto dearlership para representar al concesionario
dealership.add_vehicle(car1) # Agrega un vehiculo car1 a la lista del concesionario
dealership.add_vehicle(bike1) # Agrega un vehiculo bike a la lista del concesionario
dealership.add_vehicle(truck1) # Agrega un vehiculo truck1 a la lista del concesionario

# Mostrar los vehiculos disponible
dealership.show_available_vehicle()

# Cliente consulta los vehiculos
customer1.inquire_vehicle(car1)

# Cliente comprar un vehiculo
customer1.buy_vehicle(car1)

# Mostrar los vehiculos disponibles
dealership.show_available_vehicle()