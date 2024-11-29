class BanckAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True

    def deposite(self, amount):
        if self.is_active:
            self.balance += amount
            print(f'Se ha depositado {amount}. Y el saldo actual es {self.balance}')

        else:
            print('No se puede depositar, cuenta no esta activa')

    def withdraw(self, amount):
        if self.is_active:
            if amount <= self.balance:
                self.balance -= amount
                print(f'Se ha retirado {amount}.El saldo actual es de {self.balance}')

            else:
                print('No se puede retira, saldo insuficiente')

    def desactivate_account(self):
        self.is_active = False
        print('La cuenta ha sido desactivada')

    def activate_account(self):
        self.is_active = True
        print('La cuenta ha sido activada')

account1 = BanckAccount('Adriana', 500)
account2 = BanckAccount('Nestor', 1000)

account1.deposite(500)
account2.deposite(250)
account1.desactivate_account()
account1.deposite(50)
account1.activate_account()
account1.deposite(50)