class BankAccount: # aqui se esta definiendo la plantilla
    def __init__(self, account_holder, balance): # se define el metodo constructor con su parametros account_holder y balance
        self.account_holder = account_holder # almacena el nombre del titular de la cuenta
        self.balance = balance # almacena el saldo inicial de la cuenta
        self.is_active = True # Aqui en esta linea indica que la cuenta esta activa cuando se crea por primera vez

    def deposite(self, amount): # aqui se esta definiedo la funcion deposito, amount es la cantidad de dinero a depositar
        if self.is_active: # aqui se verifica si la cuenta esta activa
            self.balance += amount # incrementa el saldo de la cuenta con el monto depositado ('amount')
            print(f'Se ha depositado el monto actual {amount}. El saldo actual es {self.balance}') # imprime un mensaje indicando el monto depositado y el saldo actual
        
        else:
            print('No se puede depositar el dinero, cuenta inactiva') # si la cuenta no esta activa, imprime un mensaje que no se puede depositar el dinero

    def withdraw(self, amount): # aqui se esta definiendo la funcion retiro de la cuenta, ('amount') la cantidad de dinero a retirar
        if self.is_active: # verifica primero que la cuenta este activa 
            if amount <= self.balance: # comprueba si el monto a retirar es menor o igual al saldo de la ceunta
                self.balance -= amount # decrece el monto del saldo de la cuenta con el monto retirado
                print(f'Se ha retirado el monto de {amount}. El saldo actual es de {self.balance}') # imprime un mensaje indicando el monto retirado y el saldo actual
            else:
                print('Fondos insuficientes') # Imprimira un mensajes cuando el monto retirado sea mayor al del saldo de la cuenta    

    def deactivate_account(self): # se define la desactivacion de la cuenta
        self.is_active = False # Si la cuenta se encuentra activa en esta linea se desactiva la cuenta
        print('La cuenta ha sido desactivada') # Imprime un mensaje de la desactivacion de la cuenta

    def activate_account(self): # se define la función de la activación de la cuenta 
        self.is_active = True # si la cuenta esta desactivada en esta linea se activa la cuenta
        print('La cuenta ha sido activada') # imprime un mensaje que la cuenta ya ha sido activado

account1 = BankAccount('Erick', 500)
account2 =  BankAccount('Alex', 1000)

# Llamada a los metodos
account1.deposite(200)
account2.deposite(100)
account1.deactivate_account()
account1.deposite(50)
account1.activate_account()
account1.deposite(50)
account2.withdraw(1500)