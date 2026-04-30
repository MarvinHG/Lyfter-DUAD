'''
Ejercicios de Los 4 Pilares de OOP #1

Cree una clase de BankAccount que:
    -Tenga un atributo de balance.
    -Tenga un método para ingresar dinero.
    -Tenga un método para retirar dinero.
Cree otra clase que herede de esta llamada SavingsAccount que:
    -Tenga un atributo de min_balance que se pueda asignar al crearla.
    -Arroje un error si al intentar retirar dinero, el retiro haría que el balance quede debajo del min_balance. 
    -Es decir que sí se pueden hacer retiros siempre y cuando el balance quede arriba del min_balance.
'''

# Create the BankAccount class
class BankAccount:
    # Initialize the balance attribute
    def __init__(self, balance=0):
        self.balance = balance

    # Method to deposit money into the account
    def deposit(self, amount):
        if amount <= 0: # Validation to ensure the deposit amount is positive
            raise ValueError("El monto a depositar debe ser mayor que 0.")
        
        self.balance += amount
        return f"Depósito exitoso: se ingresaron {amount}. Balance actual: {self.balance}"

    # Method to withdraw money from the account
    def withdraw(self, amount):
        if amount <= 0: # Validation to ensure the withdrawal amount is positive
            raise ValueError("El monto a retirar debe ser mayor que 0.")
        
        if amount > self.balance: # Validation to ensure there are sufficient funds for the withdrawal
            raise ValueError("Fondos insuficientes.")
        
        self.balance -= amount
        return f"Retiro exitoso: se retiraron {amount}. Balance actual: {self.balance}"


# Create the SavingsAccount class that inherits from BankAccount
class SavingsAccount(BankAccount):
    # Initialize the balance and min_balance attributes
    def __init__(self, balance=0, min_balance=0):
        super().__init__(balance)
        self.min_balance = min_balance

    # Override the withdraw method to include the min_balance check
    def withdraw(self, amount):
        if self.balance - amount < self.min_balance: # Check if the withdrawal would cause the balance to drop below the minimum balance
            raise ValueError(
                "No puedes retirar esa cantidad porque bajarías del saldo mínimo."
            )
        
        return super().withdraw(amount)
    
# Get user input for withdrawal and deposit amounts
account = SavingsAccount(balance=1000, min_balance=200)
withdrawal_amount = int(input("Ingrese el monto a retirar: "))
deposit_amount = int(input("Ingrese el monto a depositar: "))

# Use try-except blocks to handle potential errors during withdrawal and deposit operations
try:
    withdraw_msg = account.withdraw(withdrawal_amount)
    print(withdraw_msg)

    deposit_msg = account.deposit(deposit_amount)
    print(deposit_msg)

except ValueError as e:
    print(f"Error: {e}")